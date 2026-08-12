const SDBOR_ROOT = "https://registration.sdbor.edu";
const SDBOR_APP = `${SDBOR_ROOT}/StudentRegistrationSsb/ssb`;
const BEACOM_SUBJECTS = [
  "ACCT",
  "BADM",
  "BLAW",
  "DSCI",
  "ECON",
  "EMBA",
  "ENTR",
  "FIN",
  "HRM",
  "HSAD",
  "MGMT",
  "MKTG"
].join(",");
const MAX_SECTIONS = 500;
const MAX_INSTRUCTOR_MATCHES = 500;
const MAX_INSTRUCTOR_NAME_LENGTH = 100;
const CACHE_SECONDS = 15 * 60;
const CACHE_VERSION = "v2";
const TERM_PATTERN = /^\d{6}$/;

const ALLOWED_ORIGINS = new Set([
  "https://rmwinslow.github.io",
  "null",
  "http://127.0.0.1:8000",
  "http://localhost:8000",
  "http://127.0.0.1:8765",
  "http://localhost:8765"
]);

function requestOrigin(request) {
  return request.headers.get("Origin") || "";
}

function originIsAllowed(origin) {
  if (!origin || ALLOWED_ORIGINS.has(origin)) {
    return true;
  }

  try {
    const url = new URL(origin);
    return (
      url.protocol === "https:" &&
      (url.hostname === "rmwinslow.com" || url.hostname.endsWith(".rmwinslow.com"))
    );
  } catch (error) {
    return false;
  }
}

function addBrowserHeaders(response, origin) {
  const headers = new Headers(response.headers);
  headers.delete("Set-Cookie");
  headers.delete("Content-Length");
  headers.set("X-Content-Type-Options", "nosniff");
  if (origin && originIsAllowed(origin)) {
    headers.set("Access-Control-Allow-Origin", origin);
    headers.append("Vary", "Origin");
  }
  return new Response(response.body, {
    status: response.status,
    statusText: response.statusText,
    headers
  });
}

function jsonResponse(payload, status, origin) {
  return addBrowserHeaders(
    new Response(JSON.stringify(payload), {
      status,
      headers: {
        "Content-Type": "application/json; charset=utf-8",
        "Cache-Control": "no-store"
      }
    }),
    origin
  );
}

function cacheableJsonResponse(payload) {
  return new Response(JSON.stringify(payload), {
    status: 200,
    headers: {
      "Content-Type": "application/json; charset=utf-8",
      "Cache-Control": `public, max-age=${CACHE_SECONDS}`
    }
  });
}

function cookieValues(headers) {
  if (typeof headers.getSetCookie === "function") {
    return headers.getSetCookie();
  }
  const singleValue = headers.get("Set-Cookie");
  return singleValue ? [singleValue] : [];
}

function absorbCookies(response, cookieJar) {
  for (const setCookie of cookieValues(response.headers)) {
    const pair = setCookie.split(";", 1)[0];
    const equals = pair.indexOf("=");
    if (equals > 0) {
      cookieJar.set(pair.slice(0, equals), pair);
    }
  }
}

async function bannerFetch(path, cookieJar, init = {}) {
  const headers = new Headers(init.headers || {});
  headers.set("Accept", "application/json, text/javascript, */*; q=0.01");
  headers.set("X-Requested-With", "XMLHttpRequest");
  if (cookieJar.size) {
    headers.set("Cookie", Array.from(cookieJar.values()).join("; "));
  }

  const response = await fetch(`${SDBOR_APP}${path}`, {
    ...init,
    headers,
    redirect: "manual"
  });
  absorbCookies(response, cookieJar);

  if (!response.ok) {
    await response.arrayBuffer();
    throw new Error(`SDBOR returned HTTP ${response.status}.`);
  }
  return response;
}

async function beginBannerSession(cookieJar) {
  const response = await bannerFetch(
    "/term/termSelection?mepCode=BOR&mode=search",
    cookieJar
  );
  await response.arrayBuffer();
}

async function selectTerm(term, cookieJar) {
  const response = await bannerFetch("/term/search?mode=search", cookieJar, {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
    },
    body: new URLSearchParams({ term }).toString()
  });
  await response.arrayBuffer();
}

function cacheKey(request, resource, parameters = {}) {
  const url = new URL(request.url);
  url.pathname = `/__cache/${CACHE_VERSION}/${resource}`;
  url.search = "";
  for (const [name, value] of Object.entries(parameters)) {
    url.searchParams.set(name, value);
  }
  return new Request(url.toString(), { method: "GET" });
}

function cacheableUpstreamResponse(upstream) {
  const headers = new Headers(upstream.headers);
  headers.delete("Set-Cookie");
  headers.delete("Content-Length");
  headers.set("Cache-Control", `public, max-age=${CACHE_SECONDS}`);
  return new Response(upstream.body, {
    status: upstream.status,
    statusText: upstream.statusText,
    headers
  });
}

function sectionLimitExceeded(payload) {
  const totalCount = Number(payload && payload.totalCount);
  return Number.isFinite(totalCount) && totalCount > MAX_SECTIONS;
}

async function parseSectionPayload(response) {
  const payload = await response.json();
  if (
    !payload ||
    typeof payload !== "object" ||
    payload.success !== true ||
    !Array.isArray(payload.data)
  ) {
    throw new Error("SDBOR returned an unexpected course-results response.");
  }
  return payload;
}

async function fetchSections(term, cookieJar, filters = {}) {
  const parameters = new URLSearchParams({
    txt_term: term,
    txt_campus: "U",
    ...filters,
    pageOffset: "0",
    pageMaxSize: String(MAX_SECTIONS),
    sortColumn: "subjectDescription",
    sortDirection: "asc"
  });
  const response = await bannerFetch(
    `/searchResults/searchResults?${parameters}`,
    cookieJar
  );
  return parseSectionPayload(response);
}

function instructorIdsFromSections(payload) {
  const ids = new Set();
  for (const section of payload.data) {
    for (const faculty of Array.isArray(section.faculty) ? section.faculty : []) {
      if (faculty && faculty.bannerId) {
        ids.add(String(faculty.bannerId));
      }
    }
  }
  return Array.from(ids);
}

async function fetchInstructorMatches(term, name, cookieJar) {
  const parameters = new URLSearchParams({
    searchTerm: name,
    term,
    offset: "1",
    max: String(MAX_INSTRUCTOR_MATCHES + 1)
  });
  const response = await bannerFetch(
    `/classSearch/get_instructor?${parameters}`,
    cookieJar
  );
  const payload = await response.json();
  if (!Array.isArray(payload)) {
    throw new Error("SDBOR returned an unexpected instructor-search response.");
  }
  return payload;
}

async function termsResponse(request, context) {
  const cache = caches.default;
  const key = cacheKey(request, "terms");
  const cached = await cache.match(key);
  if (cached) {
    return cached;
  }

  const cookieJar = new Map();
  await beginBannerSession(cookieJar);
  const upstream = await bannerFetch(
    "/classSearch/getTerms?searchTerm=&offset=1&max=100",
    cookieJar
  );
  const response = cacheableUpstreamResponse(upstream);
  context.waitUntil(cache.put(key, response.clone()));
  return response;
}

async function semesterResponse(request, term, context) {
  const cache = caches.default;
  const key = cacheKey(request, "semester", { term });
  const cached = await cache.match(key);
  if (cached) {
    return cached;
  }

  const cookieJar = new Map();
  await beginBannerSession(cookieJar);
  await selectTerm(term, cookieJar);

  const beacomPayload = await fetchSections(term, cookieJar, {
    txt_subject: BEACOM_SUBJECTS
  });
  const instructorIds = instructorIdsFromSections(beacomPayload);
  let resultPayload = beacomPayload;

  if (instructorIds.length) {
    // Banner retains the previous subject filter. Reselecting the term clears
    // that state while preserving the session-specific instructor IDs.
    await selectTerm(term, cookieJar);
    resultPayload = await fetchSections(term, cookieJar, {
      txt_instructor: instructorIds.join(",")
    });
  }

  const response = cacheableJsonResponse({
    ...resultPayload,
    limitExceeded:
      sectionLimitExceeded(beacomPayload) || sectionLimitExceeded(resultPayload)
  });
  context.waitUntil(cache.put(key, response.clone()));
  return response;
}

async function instructorResponse(request, term, name, context) {
  const cache = caches.default;
  const key = cacheKey(request, "instructor", {
    term,
    name: name.toLowerCase()
  });
  const cached = await cache.match(key);
  if (cached) {
    return cached;
  }

  const cookieJar = new Map();
  await beginBannerSession(cookieJar);
  await selectTerm(term, cookieJar);

  const matches = await fetchInstructorMatches(term, name, cookieJar);
  const instructorLookupLimitExceeded =
    matches.length > MAX_INSTRUCTOR_MATCHES;
  const instructorIds = Array.from(
    new Set(
      matches
        .slice(0, MAX_INSTRUCTOR_MATCHES)
        .map((match) => match && match.code)
        .filter(Boolean)
        .map(String)
    )
  );

  let resultPayload = { success: true, totalCount: 0, data: [] };
  if (instructorIds.length) {
    resultPayload = await fetchSections(term, cookieJar, {
      txt_instructor: instructorIds.join(",")
    });
  }

  const response = cacheableJsonResponse({
    ...resultPayload,
    limitExceeded: sectionLimitExceeded(resultPayload),
    instructorMatchCount: instructorIds.length,
    instructorLookupLimitExceeded
  });
  context.waitUntil(cache.put(key, response.clone()));
  return response;
}

export default {
  async fetch(request, environment, context) {
    const origin = requestOrigin(request);

    if (!originIsAllowed(origin)) {
      return jsonResponse({ error: "Origin not allowed." }, 403, "");
    }

    if (request.method === "OPTIONS") {
      if (!origin) {
        return new Response(null, { status: 204 });
      }
      return new Response(null, {
        status: 204,
        headers: {
          "Access-Control-Allow-Origin": origin,
          "Access-Control-Allow-Methods": "GET, OPTIONS",
          "Access-Control-Allow-Headers": "Content-Type",
          "Access-Control-Max-Age": "86400",
          "Vary": "Origin"
        }
      });
    }

    if (request.method !== "GET") {
      return jsonResponse({ error: "Method not allowed." }, 405, origin);
    }

    const url = new URL(request.url);

    try {
      if (url.pathname === "/api/terms") {
        return addBrowserHeaders(await termsResponse(request, context), origin);
      }

      if (url.pathname === "/api/semester") {
        const term = url.searchParams.get("term") || "";
        if (!TERM_PATTERN.test(term)) {
          return jsonResponse(
            { error: "A six-digit Banner term code is required." },
            400,
            origin
          );
        }
        return addBrowserHeaders(
          await semesterResponse(request, term, context),
          origin
        );
      }

      if (url.pathname === "/api/instructor") {
        const term = url.searchParams.get("term") || "";
        const name = (url.searchParams.get("name") || "").trim();
        if (!TERM_PATTERN.test(term)) {
          return jsonResponse(
            { error: "A six-digit Banner term code is required." },
            400,
            origin
          );
        }
        if (!name) {
          return jsonResponse(
            { error: "A nonblank instructor name is required." },
            400,
            origin
          );
        }
        if (name.length > MAX_INSTRUCTOR_NAME_LENGTH) {
          return jsonResponse(
            {
              error: `Instructor names are limited to ${MAX_INSTRUCTOR_NAME_LENGTH} characters.`
            },
            400,
            origin
          );
        }
        return addBrowserHeaders(
          await instructorResponse(request, term, name, context),
          origin
        );
      }

      return jsonResponse(
        {
          name: "USD Beacom catalog API",
          endpoints: [
            "/api/terms",
            "/api/semester?term=202680",
            "/api/instructor?term=202680&name=Carr"
          ]
        },
        200,
        origin
      );
    } catch (error) {
      return jsonResponse(
        { error: error instanceof Error ? error.message : "Unexpected error." },
        502,
        origin
      );
    }
  }
};
