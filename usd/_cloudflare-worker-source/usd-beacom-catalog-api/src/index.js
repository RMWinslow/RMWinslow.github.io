const SDBOR_ROOT = "https://registration.sdbor.edu";
const SDBOR_APP = `${SDBOR_ROOT}/StudentRegistrationSsb/ssb`;
const BEACOM_SUBJECTS = [
  "ACCT",
  "BADM",
  "BLAW",
  "DSCI",
  "ECON",
  "ENTR",
  "FIN",
  "HRM",
  "HSAD",
  "MGMT",
  "MKTG"
].join(",");
const MAX_SECTIONS = 500;
const CACHE_SECONDS = 15 * 60;
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

function cacheKey(request, resource, term = "") {
  const url = new URL(request.url);
  url.pathname = `/__cache/${resource}`;
  url.search = term ? `?term=${encodeURIComponent(term)}` : "";
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
  const key = cacheKey(request, "semester", term);
  const cached = await cache.match(key);
  if (cached) {
    return cached;
  }

  const cookieJar = new Map();
  await beginBannerSession(cookieJar);
  await selectTerm(term, cookieJar);

  const parameters = new URLSearchParams({
    txt_term: term,
    txt_campus: "U",
    txt_subject: BEACOM_SUBJECTS,
    pageOffset: "0",
    pageMaxSize: String(MAX_SECTIONS),
    sortColumn: "subjectDescription",
    sortDirection: "asc"
  });
  const upstream = await bannerFetch(
    `/searchResults/searchResults?${parameters}`,
    cookieJar
  );
  const response = cacheableUpstreamResponse(upstream);
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

      return jsonResponse(
        {
          name: "USD Beacom catalog API",
          endpoints: [
            "/api/terms",
            "/api/semester?term=202680"
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
