# Querying University of South Dakota Course Sections Without Login

> **AI-generated and not independently verified:** This document was generated
> by OpenAI Codex on August 12, 2026. Robert Winslow has not reviewed or verified
> its contents. Independently check the described endpoints, parameters,
> examples, and code before relying on them.

Last tested by OpenAI Codex: **August 11–12 and 19, 2026**

This document explains how to download public University of South Dakota (USD)
course-section listings from the South Dakota Board of Regents (SDBOR) Ellucian
Banner Registration Self-Service application. The interface is public and does
not require a student, faculty, or portal login.

The data includes course and section identifiers, CRNs, instructors, meeting
dates, days, times, buildings, and rooms. The response also contains public
aggregate enrollment and seat counts. It does **not** expose student rosters.
Discard fields you do not intend to publish.

The official browser entry point is:

<https://registration.sdbor.edu/StudentRegistrationSsb/ssb/term/termSelection?mepCode=BOR&mode=search>

USD itself links to this service and says that anyone may browse its current
searchable course database:

<https://www.usd.edu/Academics/USD-Online/Online-Courses-and-Registration>

## Essential facts

- The useful JSON endpoint is part of the web application's private-in-practice
  interface, not a separately documented public API. It can change if SDBOR
  upgrades or reconfigures Banner.
- No authentication is required, but a cookie-backed anonymous session is.
- Select a term in that session before querying its sections.
- `txt_campus=U` means **University of South Dakota**, not merely the Vermillion
  physical campus. It includes USD's Vermillion, Sioux Falls, online, clinical,
  internship, and other USD offerings.
- `txt_session` is the separate physical-location/delivery filter. Omit it to
  retain every USD offering.
- Banner retains search state. The safest automation uses a fresh session for
  each term/filter combination. To reuse a session with different criteria,
  reset it first.
- Results are paginated. `pageOffset` is a row offset, not a page number.
- Multi-value filters are comma-separated: `txt_subject=ACCT,ECON`. Do not
  repeat the same parameter as `txt_subject=ACCT&txt_subject=ECON`.
- The results endpoint always returns its fixed row schema. A tested `fields=`
  projection parameter was ignored.
- Request gzip compression; it reduced a tested 500-row page from about 2.10 MB
  to 0.21 MB on the wire.

## Base URLs

```text
ROOT = https://registration.sdbor.edu
APP  = https://registration.sdbor.edu/StudentRegistrationSsb/ssb
```

Important routes:

```text
GET  /term/termSelection?mepCode=BOR&mode=search
GET  /classSearch/getTerms
POST /term/search?mode=search
GET  /classSearch/classSearch
GET  /searchResults/searchResults
POST /classSearch/resetDataForm
```

Lookup routes:

```text
GET /classSearch/get_campus
GET /classSearch/get_session
GET /classSearch/get_subject
GET /classSearch/get_subjectcoursecombo
GET /classSearch/get_instructor
GET /classSearch/get_level
GET /classSearch/get_attribute
GET /classSearch/get_partOfTerm
```

All paths above are relative to `APP`.

## Companion Worker API used by the website

The repository also contains a deliberately narrow Cloudflare Worker wrapper
at:

```text
usd/_cloudflare-worker-source/usd-beacom-catalog-api/
```

Its deployed base URL is:

```text
https://usd-beacom-catalog-api.rmwinslow.workers.dev
```

The browser-facing routes are:

```text
GET /api/terms
GET /api/semester?term=202680
GET /api/instructor?term=202680&name=Carr
```

- The `terms` query returns a list of semester codes available in the database.
- The `semester` query tries to grab all the "Beacom" courses. (See below for the heuristic it uses.)
- And the `instructor` query finds all matches for an instructor name, regardless of subject.

`/api/terms` returns Banner's term lookup array. `/api/semester` first queries
the Beacom seed subjects `ACCT,BADM,BLAW,DSCI,ECON,EMBA,ENTR,FIN,HRM,HSAD,MGMT,MKTG`,
collects the returned instructors' session-specific `bannerId` values, resets
the sticky Banner search state by reselecting the same term, and then returns
all USD sections for those instructors without a subject filter. It then
reselects the term, queries every section physically scheduled in Beacom Hall
with `txt_building=UB`, and returns the term-and-CRN-deduplicated union of the
instructor and building results.
The point of this approach is to try to grab all the courses taught by Beacom Faculty,
without exceeding the 500-response limit for a Banner query for each semester.
This can still fail to capture a non-Beacom-Hall section for an instructor who
does not teach any seed subject in the same semester.
(The instructor query below ignores subjects, 
so at least this failure mode won't arise when looking for a particular person.)

`/api/instructor` uses Banner's instructor-name lookup in the selected term,
then queries all USD subjects for the matching session-specific instructor
IDs. Banner controls the lookup's partial or fuzzy name-matching behavior.

Both course routes request at most 500 rows per Banner results query and add
`limitExceeded: true` when Banner reports more than 500 course results. For the
semester route, that flag covers the seed, instructor, and building queries;
its `totalCount` is the number of deduplicated union rows returned. The
instructor route also adds
`instructorMatchCount` and `instructorLookupLimitExceeded`; the latter means
the lookup itself produced more than the Worker's 500-instructor safety cap.
The remaining course-result fields retain Banner's normal shape. Ordinary
JavaScript JSON consumers ignore these extra fields unless they deliberately
enforce a strict schema.

The website's `Other (EMBA, UHON, etc.)` subject checkbox dynamically includes
every subject prefix in the returned union that lacks its own named checkbox.
It therefore continues to work when a newly encountered subject appears.

A client that calls both course routes should merge their `data` arrays and
deduplicate sections by term plus `courseReferenceNumber`. The full Worker
contract, caching rules, origin policy, and request counts are documented in
`usd/_cloudflare-worker-source/usd-beacom-catalog-api/README.md`.

## Complete anonymous-session workflow

### 1. Start an anonymous session

Create an HTTP client that retains cookies, then request the term-selection
page:

```http
GET /StudentRegistrationSsb/ssb/term/termSelection?mepCode=BOR&mode=search
```

The response normally sets cookies including `JSESSIONID`. Keep those cookies
for every subsequent request in the workflow.

### 2. Discover available terms

In the same session, request:

```http
GET /StudentRegistrationSsb/ssb/classSearch/getTerms?searchTerm=&offset=1&max=50
```

The response is a JSON array:

```json
[
  {"code": "202710", "description": "2027 Spring"},
  {"code": "202680", "description": "2026 Fall"},
  {"code": "202650", "description": "2026 Summer (View Only)"}
]
```

`(View Only)` means registration is closed. It does not prevent public catalog
queries. Historical terms were successfully queried as far back as the oldest
term then advertised, Summer 2019 (`201950`).

The live term list on August 11, 2026 was:

| Term code | Description |
|---|---|
| `202710` | 2027 Spring |
| `202680` | 2026 Fall |
| `202650` | 2026 Summer (View Only) |
| `202610` | 2026 Spring (View Only) |
| `202580` | 2025 Fall (View Only) |
| `202550` | 2025 Summer (View Only) |
| `202510` | 2025 Spring (View Only) |
| `202480` | 2024 Fall (View Only) |
| `202450` | 2024 Summer (View Only) |
| `202410` | 2024 Spring (View Only) |
| `202380` | 2023 Fall (View Only) |
| `202350` | 2023 Summer (View Only) |
| `202310` | 2023 Spring (View Only) |
| `202280` | 2022 Fall (View Only) |
| `202250` | 2022 Summer (View Only) |
| `202210` | 2022 Spring (View Only) |
| `202180` | 2021 Fall (View Only) |
| `202150` | 2021 Summer (View Only) |
| `202110` | 2021 Spring (View Only) |
| `202080` | 2020 Fall (View Only) |
| `202050` | 2020 Summer (View Only) |
| `202010` | 2020 Spring (View Only) |
| `201980` | 2019 Fall (View Only) |
| `201950` | 2019 Summer (View Only) |

Always rediscover terms rather than hard-coding this snapshot.

### 3. Select the term

POST the desired Banner term code in the same session:

```http
POST /StudentRegistrationSsb/ssb/term/search?mode=search
Content-Type: application/x-www-form-urlencoded
X-Requested-With: XMLHttpRequest

term=202680
```

The JSON response looks like:

```json
{
  "fwdURL": "/StudentRegistrationSsb/ssb/classSearch/classSearch"
}
```

Follow `fwdURL` with a GET in the same session. This initializes the class
search page for the selected term.

### 4. Query USD sections

Request the results endpoint:

```http
GET /StudentRegistrationSsb/ssb/searchResults/searchResults
    ?txt_term=202680
    &txt_campus=U
    &pageOffset=0
    &pageMaxSize=500
    &sortColumn=subjectDescription
    &sortDirection=asc
X-Requested-With: XMLHttpRequest
Accept-Encoding: gzip
```

The required conceptual filters are:

```text
txt_term=202680
txt_campus=U
```

The other parameters provide predictable sorting and pagination. Omitting
`txt_session` is deliberate: that keeps every USD physical site, online
section, internship, clinical placement, and section lacking a recognized
session/location code.

### 5. Paginate

The response includes:

```json
{
  "success": true,
  "totalCount": 2528,
  "data": ["...section objects..."],
  "pageOffset": 0,
  "pageMaxSize": 500
}
```

After processing a page, increment the offset by the number of rows actually
returned:

```python
offset += len(response["data"])
```

Stop when `offset >= totalCount`. Do not rely on `sectionsFetchedCount` as the
page length; use `len(data)`.

## Confirmed search filters

All filters below are supplied to `/searchResults/searchResults` after the term
has been selected in the session.

| Parameter | Meaning | Example |
|---|---|---|
| `txt_term` | Banner term code | `202680` |
| `txt_campus` | SDBOR university code | `U` |
| `txt_session` | Location/delivery code | `U,F,I` |
| `txt_subject` | Subject prefix | `ACCT` |
| `txt_courseNumber` | Course number | `210` |
| `txt_subjectcoursecombo` | Combined subject and course | `ACCT210` |
| `txt_instructor` | Session-specific instructor lookup code | `18202` |
| `txt_level` | Academic level | `UG`, `GR`, `LA`, `MD` |
| `txt_attribute` | Course/section attribute | `HON`, `HSDC` |
| `txt_partOfTerm` | Part-of-term code | `U1`, `U2` |
| `txt_course_number_range` | Minimum course number | `300` |
| `txt_course_number_range_to` | Maximum course number | `499` |
| `txt_credithourlow` | Minimum credit hours | `3` |
| `txt_credithourhigh` | Maximum credit hours | `4` |

Different filter fields combine as AND. Comma-separated values inside one
field combine as OR. For example:

```text
txt_term=202680
txt_campus=U
txt_subject=ACCT,ECON,DSCI
txt_level=UG,GR
txt_session=U,F,I
```

This means: sections belonging to USD, whose subject is ACCT or ECON or DSCI,
whose level is undergraduate or graduate, and whose delivery/location is
Vermillion or official USD–Sioux Falls or online.

Prefer omitting `txt_session` for a complete USD archive.

## Lookup endpoints and codes

Lookup endpoints should be called after term selection and with the same
session cookies. A typical lookup query is:

```text
?searchTerm=&term=202680&offset=1&max=100
```

Paged lookup fields such as subjects and instructors may need repeated calls
when `max` is small. The UI uses ten results at a time.

### Universities (`txt_campus`)

```http
GET /StudentRegistrationSsb/ssb/classSearch/get_campus
    ?searchTerm=&term=202680&offset=1&max=100
```

Verified codes:

| Code | University |
|---|---|
| `B` | BHSU Black Hills State University |
| `D` | DSU Dakota State University |
| `N` | NSU Northern State University |
| `M` | South Dakota Mines |
| `S` | SDSU South Dakota State University |
| `U` | USD University of South Dakota |

Again, `txt_campus=U` is the correct filter for **all USD sections**.

### Locations/delivery (`txt_session`)

```http
GET /StudentRegistrationSsb/ssb/classSearch/get_session
    ?searchTerm=&term=202680&offset=1&max=100
```

Verified advertised codes:

| Code | Description |
|---|---|
| `I` | Online/Internet |
| `Q` | Virtual |
| `B` | BHSU Spearfish Main Campus |
| `D` | DSU Madison Main Campus |
| `N` | NSU Aberdeen Main Campus |
| `M` | South Dakota Mines Rapid City Main Campus |
| `S` | SDSU Brookings Main Campus |
| `U` | USD Vermillion Main Campus |
| `F` | USD Sioux Falls Campus |
| `J` | Ellsworth Air Force Base |
| `4` | Huron |
| `Z` | Off-Campus Internship |
| `P` | Pierre Capital University Center |
| `Y` | Rapid City (Not Main Campus) |
| `R` | Rapid City University Center |
| `X` | Sioux Falls (Not USD SF) |
| `W` | Watertown |

For Fall 2026 with `txt_campus=U`, the separately queried nonzero session
counts were:

| Code | USD sections |
|---|---:|
| `U` | 1,526 |
| `I` | 447 |
| `X` | 158 |
| `F` | 120 |
| `Z` | 61 |
| `Y` | 37 |

The complete USD query returned 2,528 sections, while these advertised nonzero
session values summed to 2,349. Therefore, 179 sections did not match any
advertised `txt_session` value. This is another reason to omit the location
filter when building a complete archive.

`F` and `X` are distinct:

- `F` is the formal USD–Sioux Falls campus. Examples use buildings such as the
  Science & Technology Building (`FSC1`) and section numbers like `UF1`.
- `X` is Sioux Falls but not administratively designated USD–Sioux Falls. It
  includes sites such as the GEAR Building (`FGER`), clinical locations, and
  host/receive-site courses.

`Y` Rapid City sections in Fall 2026 were largely medical clinical rotations.
Many were marked face-to-face but had no building, room, day, or time in Banner.

### Subjects (`txt_subject`)

```http
GET /StudentRegistrationSsb/ssb/classSearch/get_subject
    ?searchTerm=Accounting&term=202680&offset=1&max=20
```

Example response:

```json
[
  {"code": "ACCT", "description": "Accounting"}
]
```

Pass the returned code to the results query:

```text
txt_subject=ACCT
```

Multiple subjects work as a comma-separated union:

```text
txt_subject=ACCT,ECON
```

### Combined subject/course (`txt_subjectcoursecombo`)

```http
GET /StudentRegistrationSsb/ssb/classSearch/get_subjectcoursecombo
    ?searchTerm=ACCT%20210&term=202680&offset=1&max=20
```

Example response:

```json
[
  {"code": "ACCT210", "description": "ACCT210 Accounting"}
]
```

### Instructors (`txt_instructor`)

Instructor filtering is a two-step operation. Search by name:

```http
GET /StudentRegistrationSsb/ssb/classSearch/get_instructor
    ?searchTerm=Franken&term=202580&offset=1&max=20
```

Example response:

```json
[
  {"code": "18202", "description": "Derek Scott Franken"}
]
```

Then, without changing sessions, query:

```text
txt_instructor=18202
```

The lookup code was observed to change between anonymous sessions. Treat it as
session-specific: look it up and consume it using the same cookie jar.

If the goal is merely to obtain all instructors who teach a subject, it is
simpler and more reliable to query `txt_subject=ACCT`, then deduplicate the
`faculty` arrays in the returned sections.

### Levels (`txt_level`)

```http
GET /StudentRegistrationSsb/ssb/classSearch/get_level
    ?searchTerm=&term=202680&offset=1&max=50
```

Verified codes:

| Code | Level |
|---|---|
| `UG` | Undergraduate |
| `GR` | Graduate |
| `LA` | Law |
| `MD` | Medical |

### Attributes (`txt_attribute`)

```http
GET /StudentRegistrationSsb/ssb/classSearch/get_attribute
    ?searchTerm=&term=202680&offset=1&max=100
```

Observed examples include:

| Code | Attribute |
|---|---|
| `HSDC` | High School Dual Credit Course |
| `HON` | Honors |
| `GEAH` | Gen Ed Arts & Humanities |
| `GECV` | Gen Ed Civics |
| `GEMT` | Gen Ed Mathematics |
| `GESC` | Gen Ed Natural Sciences |
| `GESP` | Gen Ed Oral Communication |
| `GESS` | Gen Ed Social Sciences |
| `GEWC` | Gen Ed Written Communication |

Available attributes can change by term, so use the lookup endpoint.

### Parts of term (`txt_partOfTerm`)

```http
GET /StudentRegistrationSsb/ssb/classSearch/get_partOfTerm
    ?searchTerm=&term=202580&offset=1&max=100
```

Examples for Fall 2025 included:

```text
U1  USD First 8 Weeks
U2  USD Second 8 Weeks
```

Descriptions include actual start and end dates. Discover them per term.

## Result structure

A section object from `data` has fields similar to:

```json
{
  "term": "202680",
  "termDesc": "2026 Fall",
  "courseReferenceNumber": "73367",
  "partOfTerm": "UF",
  "courseNumber": "210",
  "courseDisplay": "210",
  "subject": "ACCT",
  "subjectDescription": "Accounting",
  "sequenceNumber": "U15",
  "campusDescription": "USD University of South Dakota",
  "scheduleTypeDescription": "Face-to-Face",
  "courseTitle": "Principles of Accounting I",
  "creditHours": 3,
  "faculty": [
    {
      "bannerId": "00000",
      "displayName": "Fake J Name",
      "emailAddress": "fake.name@usd.edu",
      "primaryIndicator": true
    }
  ],
  "meetingsFaculty": [
    {
      "faculty": [],
      "meetingTime": {
        "beginTime": "1400",
        "endTime": "1450",
        "startDate": "08/24/2026",
        "endDate": "12/16/2026",
        "monday": true,
        "tuesday": false,
        "wednesday": true,
        "thursday": false,
        "friday": true,
        "saturday": false,
        "sunday": false,
        "building": "UB",
        "buildingDescription": "Beacom Hall",
        "room": "244",
        "campus": "U",
        "campusDescription": "USD University of South Dakota"
      }
    }
  ],
  "sectionAttributes": [],
  "instructionalMethod": "R",
  "instructionalMethodDescription": "Lecture"
}
```

Useful field mapping:

| Desired information | JSON field |
|---|---|
| CRN | `courseReferenceNumber` |
| Subject | `subject` |
| Course number | `courseNumber` or `courseDisplay` |
| Section number | `sequenceNumber` |
| Title | `courseTitle` |
| Credits | `creditHours`, or `creditHourLow`/`creditHourHigh` |
| Instructor name | `faculty[].displayName` |
| Instructor email | `faculty[].emailAddress` |
| Primary instructor | `faculty[].primaryIndicator` |
| Delivery style | `scheduleTypeDescription` |
| Instructional method | `instructionalMethodDescription` |
| Meeting rows | `meetingsFaculty[]` |
| Start/end time | `meetingsFaculty[].meetingTime.beginTime/endTime` |
| Start/end date | `meetingsFaculty[].meetingTime.startDate/endDate` |
| Days | Boolean weekday fields inside `meetingTime` |
| Building code/name | `meetingTime.building/buildingDescription` |
| Room | `meetingTime.room` |

Do not assume every section has an instructor or meeting details. Online,
independent study, internship, and clinical sections often contain empty or
partial meeting records. A section can also have multiple instructors and
multiple meetings.

The raw object also contains aggregate fields such as:

```text
maximumEnrollment
enrollment
seatsAvailable
waitCapacity
waitCount
waitAvailable
crossListCapacity
crossListCount
crossListAvailable
```

These are aggregate section statistics, not personally identifiable student
records. Omit them from a public static payload if they are outside the intended
scope.

## Complete Python downloader

This example uses `requests`, which handles cookies and gzip automatically.
Install it with `python -m pip install requests` if needed.

```python
from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import urljoin

import requests


ROOT = "https://registration.sdbor.edu"
APP = ROOT + "/StudentRegistrationSsb/ssb"


def new_session() -> requests.Session:
    session = requests.Session()
    session.headers.update({
        "User-Agent": "USD-course-catalog-downloader/1.0",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip",
        "X-Requested-With": "XMLHttpRequest",
    })
    response = session.get(
        APP + "/term/termSelection",
        params={"mepCode": "BOR", "mode": "search"},
        timeout=60,
    )
    response.raise_for_status()
    return session


def get_terms() -> list[dict]:
    session = new_session()
    response = session.get(
        APP + "/classSearch/getTerms",
        params={"searchTerm": "", "offset": 1, "max": 100},
        timeout=60,
    )
    response.raise_for_status()
    return response.json()


def select_term(session: requests.Session, term: str) -> str:
    response = session.post(
        APP + "/term/search",
        params={"mode": "search"},
        data={"term": term},
        timeout=60,
    )
    response.raise_for_status()
    class_search_url = urljoin(ROOT, response.json()["fwdURL"])

    response = session.get(class_search_url, timeout=60)
    response.raise_for_status()
    return class_search_url


def get_sections(
    term: str,
    *,
    campus: str = "U",
    page_size: int = 500,
    **filters,
) -> list[dict]:
    # Use a fresh session for each term/filter combination because Banner keeps
    # search criteria in anonymous session state.
    session = new_session()
    referer = select_term(session, term)

    query = {
        "txt_term": term,
        "txt_campus": campus,
        "pageOffset": 0,
        "pageMaxSize": page_size,
        "sortColumn": "subjectDescription",
        "sortDirection": "asc",
        **filters,
    }

    rows = []
    total = None

    while total is None or query["pageOffset"] < total:
        response = session.get(
            APP + "/searchResults/searchResults",
            params=query,
            headers={"Referer": referer},
            timeout=120,
        )
        response.raise_for_status()
        payload = response.json()

        if not payload.get("success"):
            raise RuntimeError(f"Banner search failed: {payload!r}")

        total = int(payload["totalCount"])
        batch = payload.get("data") or []

        if not batch and query["pageOffset"] < total:
            raise RuntimeError(
                f"Unexpected empty page at offset {query['pageOffset']} of {total}"
            )

        rows.extend(batch)
        query["pageOffset"] += len(batch)
        print(f"Downloaded {len(rows)}/{total}")

    return rows


if __name__ == "__main__":
    print(json.dumps(get_terms(), indent=2))

    # Complete USD Fall 2026 archive, including every USD location/delivery.
    all_usd = get_sections("202680")
    Path("usd-202680-raw.json").write_text(
        json.dumps(all_usd, ensure_ascii=False),
        encoding="utf-8",
    )

    # A narrower example: undergraduate ACCT or ECON in Vermillion,
    # official USD-Sioux Falls, or online.
    business_subset = get_sections(
        "202680",
        txt_subject="ACCT,ECON",
        txt_level="UG",
        txt_session="U,F,I",
    )
    Path("usd-202680-business-subset.json").write_text(
        json.dumps(business_subset, ensure_ascii=False),
        encoding="utf-8",
    )
```

A compact-schema downloader created during the original endpoint investigation
is also saved beside this guide as `download_sdbor_usd_catalog.py`. It emits the
schema consumed by <https://www.rmwinslow.com/usd/catalog> rather than retaining
the complete Banner response.

## Curl outline

The same sequence can be performed with curl. `-c` writes cookies and `-b`
reads them:

```bash
curl -c cookies.txt -b cookies.txt \
  'https://registration.sdbor.edu/StudentRegistrationSsb/ssb/term/termSelection?mepCode=BOR&mode=search'

curl -c cookies.txt -b cookies.txt \
  'https://registration.sdbor.edu/StudentRegistrationSsb/ssb/classSearch/getTerms?searchTerm=&offset=1&max=50'

curl -c cookies.txt -b cookies.txt \
  -H 'X-Requested-With: XMLHttpRequest' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  --data 'term=202680' \
  'https://registration.sdbor.edu/StudentRegistrationSsb/ssb/term/search?mode=search'

curl -c cookies.txt -b cookies.txt \
  'https://registration.sdbor.edu/StudentRegistrationSsb/ssb/classSearch/classSearch'

curl --compressed -c cookies.txt -b cookies.txt \
  -H 'X-Requested-With: XMLHttpRequest' \
  'https://registration.sdbor.edu/StudentRegistrationSsb/ssb/searchResults/searchResults?txt_term=202680&txt_campus=U&pageOffset=0&pageMaxSize=500&sortColumn=subjectDescription&sortDirection=asc'
```

Use a temporary cookie file and delete it when finished. Although the session is
anonymous, treating cookie files as temporary avoids confusing later runs with
stale Banner state.

## Resetting or isolating search state

Banner can retain the first search criteria used in a session. A later query in
the same session may unexpectedly reuse the earlier criteria.

Preferred approach:

```text
Create one fresh session per term/filter combination.
```

Alternative when reusing a session:

```http
POST /StudentRegistrationSsb/ssb/classSearch/resetDataForm
X-Requested-With: XMLHttpRequest
```

Then issue the new search. For bulk independent queries, fresh sessions are
easier to reason about.

## Bandwidth and storage

### Response-field projection is not supported

The endpoint ignored this tested parameter:

```text
fields=courseReferenceNumber,subject
```

It returned the same fixed fields and the same response size. Strip unwanted
fields locally after downloading.

### Use gzip

Send:

```http
Accept-Encoding: gzip
```

In one Fall 2026 test, a 500-row page was:

```text
Uncompressed: 2,100,132 bytes
Gzip:           210,371 bytes
```

Python `requests` normally advertises and decodes gzip automatically. Curl does
so with `--compressed`.

### Filter server-side where useful

`txt_campus=U` is the most important bandwidth-saving filter because it avoids
downloading other SDBOR universities. Subject, level, and other known filters
can reduce the response further when a complete USD archive is unnecessary.

## Less obvious and unsupported capabilities

### Building search parameter

Banner accepts `txt_building` even though the live form does not expose a
building lookup. A live Fall 2026 (`202680`) test on August 19, 2026 returned
135 rows for `txt_campus=U&txt_building=UB`, compared with 2,519 total USD
rows without the building filter. Every returned row listed `UB` in its meeting
data. The Worker uses this filter to retrieve Beacom Hall sections.

Code that consumes these results can still validate or post-filter them using:

```text
meetingsFaculty[].meetingTime.building
meetingsFaculty[].meetingTime.buildingDescription
meetingsFaculty[].meetingTime.room
```

### No useful college/department course filter

The live class-search page exposes no configured academic-college or department
filter. Calls to plausible `get_college` and `get_department` lookup routes
returned empty arrays when tested.

The `College` label in `/searchResults/getSectionCatalogDetails` is misleading
for this purpose. It returned classification values such as `Common Course 1C`
and `Unique Course 1U`, not organizational values such as Beacom School of
Business or College of Arts & Sciences.

For a college filter, maintain a local subject-prefix mapping. For example, USD
business documentation identifies these prefixes with the Beacom School of
Business:

```text
ACCT BADM BLAW DSCI ECON EMBA ENTR FIN HRM HSAD MGMT MKTG
```

Mappings for interdisciplinary subjects may need multiple affiliations or an
explicit policy decision.

## Faculty and staff directory enrichment

This is a separate system from Banner course search. USD's public directory is:

<https://www.usd.edu/research-and-faculty/faculty-and-staff/>

The directory is Coveo-backed and supports URL-fragment filters for college,
department, and profile type. It does not directly understand Banner subject
prefixes.

Example: everyone associated with Accounting and Finance:

```text
https://www.usd.edu/research-and-faculty/faculty-and-staff/#sort=%40facultyz32xmemberz32xlastz32xname%20ascending&f:facultydepartments=[Accounting%20and%20Finance]
```

Restrict that directory query to profiles classified as Faculty:

```text
https://www.usd.edu/research-and-faculty/faculty-and-staff/#sort=%40facultyz32xmemberz32xlastz32xname%20ascending&f:profiletype=[Faculty]&f:facultydepartments=[Accounting%20and%20Finance]
```

This answers “who is organizationally associated with the department?” Banner
answers a different question: “who is assigned to teach this subject in this
term?” For the latter, query `txt_subject=ACCT` and deduplicate faculty:

```python
instructors = {
    (faculty["displayName"], faculty.get("emailAddress"))
    for section in sections
    for faculty in section.get("faculty", [])
}
```

Union that result across historical terms to build a “has taught ACCT” roster.

Banner also has a faculty contact-card endpoint:

```text
GET /contactCard/retrieveData?bannerId=<faculty.bannerId>&termCode=202680
```

Its schema can contain `personData.title` and
`personData.deptAndCollegeInformation`, but both were `null` for the tested USD
instructors across ACCT, BME, ECON, ENGL, LAW, FAMP, PSYC, and NURS. The USD
directory is therefore the more useful source for organizational enrichment.

## Validation checks for a downloader

A production refresh should verify at least the following:

1. Term discovery returns a JSON list containing the requested term.
2. Term selection returns an `fwdURL`.
3. Every results response has `success: true`.
4. Every returned row has the requested `term`.
5. Every row returned for `txt_campus=U` has
   `campusDescription == "USD University of South Dakota"`.
6. Pagination produces exactly `totalCount` rows with no empty intermediate
   page.
7. CRNs are deduplicated per term unless duplicate handling is explicitly
   intended.
8. Missing faculty and meeting records are accepted rather than treated as
   fatal errors.
9. Stored output excludes any raw fields the application does not intend to
   publish.

Record the retrieval timestamp, term code, filter set, returned `totalCount`,
and tool version in generated artifacts. Those values make later changes and
discrepancies auditable.

## Verified snapshot notes

These counts are observations, not invariants; course schedules change:

- Fall 2026 (`202680`), all SDBOR institutions: 8,717 sections during the later
  verification request.
- Fall 2026 (`202680`), `txt_campus=U`: 2,528 USD sections.
- Fall 2025 (`202580`), `txt_campus=U`: 2,605 USD sections.
- Spring 2020 (`202010`), `txt_campus=U`: 3,162 USD sections.
- Summer 2019 (`201950`), `txt_campus=U`: 524 USD sections.

The existing static catalog payload at
<https://www.rmwinslow.com/usd/catalog/fall-2026-usd-web-payload.json> recorded
2,529 USD Fall 2026 sections when fetched June 11, 2026. The one-row difference
from the August verification demonstrates why fresh downloads and retrieval
timestamps matter.

## Troubleshooting

### Results contain every SDBOR school

Ensure the first results request in the fresh session contains:

```text
txt_campus=U
```

Do not interpret meeting-level `campus` as the institutional filter; use the
top-level search parameter.

### Sioux Falls or online courses are missing

Remove `txt_session`. `txt_campus=U` already restricts results to USD while
retaining all USD delivery locations.

### A changed filter appears to be ignored

Banner probably retained earlier search state. Start a new anonymous session or
POST to `/classSearch/resetDataForm` before issuing the changed query.

### Instructor filtering causes an error or returns nothing

Re-run `get_instructor` and use its returned code within that same session. Do
not cache instructor lookup codes across sessions.

### Historical term is labeled View Only

Proceed normally. The label prevents registration, not browsing. Select the
term, follow `fwdURL`, and query results exactly as for an active term.

### Large responses are slow

Use `Accept-Encoding: gzip`, retain `txt_campus=U`, and consider a smaller
`pageMaxSize` if proxies or client timeouts interrupt 500-row pages. Add bounded
retry logic for transient network errors, but do not silently skip a failed
page.
