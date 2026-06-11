#!/usr/bin/env python3
"""ChatGPT-generated utility for building USD course catalog payloads.

This combines the public SDBOR Banner scraper and the condenser used for
the USD course browser. It fetches full term results in memory and writes
only the condensed JSON catalog payload, not the raw page responses.
"""

from __future__ import annotations

import argparse
import html
import json
import re
from collections import defaultdict
from datetime import datetime
from http.cookiejar import CookieJar
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import HTTPCookieProcessor, Request, build_opener


BASE_URL = "https://registration.sdbor.edu"
REGISTRATION_URL = f"{BASE_URL}/StudentRegistrationSsb/ssb/registration?mepCode=BOR"
TERM_SELECTION_URL = f"{BASE_URL}/StudentRegistrationSsb/ssb/term/termSelection?mode=search"
SAVE_TERM_URL = f"{BASE_URL}/StudentRegistrationSsb/ssb/term/saveTerm?mode=search"
TERM_SEARCH_URL = f"{BASE_URL}/StudentRegistrationSsb/ssb/term/search?mode=search"
SEARCH_URL = f"{BASE_URL}/StudentRegistrationSsb/ssb/searchResults/searchResults"

DEFAULT_INSTITUTION = "USD University of South Dakota"
DEFAULT_TERMS = [
    ("202680", "Fall 2026"),
    ("202710", "Spring 2027"),
]
PAGE_SIZE = 500

DAY_FIELDS = [
    ("M", "monday"),
    ("T", "tuesday"),
    ("W", "wednesday"),
    ("R", "thursday"),
    ("F", "friday"),
    ("S", "saturday"),
    ("U", "sunday"),
]


def clean(value):
    if value is None:
        return None
    if isinstance(value, str):
        value = value.strip()
        for _ in range(2):
            unescaped = html.unescape(value)
            if unescaped == value:
                break
            value = unescaped
        return value or None
    return value


def compact_dict(data):
    return {key: value for key, value in data.items() if value not in (None, "", [])}


def slug(value):
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    return value or "term"


def json_inline(value):
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"))


def json_map_lines(data):
    if not data:
        return "{}"
    return "{\n" + ",\n".join(
        f"{json_inline(key)}:{json_inline(value)}" for key, value in data.items()
    ) + "\n}"


def json_schema(schema):
    return "{\n" + ",\n".join(
        [
            f"{json_inline('course')}:{json_map_lines(schema['course'])}",
            f"{json_inline('meeting')}:{json_map_lines(schema['meeting'])}",
        ]
    ) + "\n}"


def json_lookups(lookups):
    return "{\n" + ",\n".join(
        [
            f"{json_inline('institutions')}:{json_inline(lookups['institutions'])}",
            f"{json_inline('meeting_campuses')}:{json_map_lines(lookups['meeting_campuses'])}",
            f"{json_inline('ambiguous_meeting_campuses')}:{json_map_lines(lookups['ambiguous_meeting_campuses'])}",
            f"{json_inline('subjects')}:{json_map_lines(lookups['subjects'])}",
            f"{json_inline('buildings')}:{json_map_lines(lookups['buildings'])}",
            f"{json_inline('ambiguous_buildings')}:{json_map_lines(lookups['ambiguous_buildings'])}",
        ]
    ) + "\n}"


def json_courses(courses):
    if not courses:
        return "[]"
    return "[\n" + ",\n".join(json_inline(course) for course in courses) + "\n]"


def json_payload(payload):
    return "{\n" + ",\n".join(
        [
            f"{json_inline('term')}:{json_map_lines(payload['term'])}",
            f"{json_inline('source')}:{json_map_lines(payload['source'])}",
            f"{json_inline('scope')}:{json_map_lines(payload['scope'])}",
            f"{json_inline('schema')}:{json_schema(payload['schema'])}",
            f"{json_inline('lookups')}:{json_lookups(payload['lookups'])}",
            f"{json_inline('count')}:{json_inline(payload['count'])}",
            f"{json_inline('courses')}:{json_courses(payload['courses'])}",
        ]
    ) + "\n}\n"


def request_json(opener, url, params):
    request = Request(
        f"{url}?{urlencode(params)}",
        headers={
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "User-Agent": "Mozilla/5.0",
            "X-Requested-With": "XMLHttpRequest",
        },
    )
    with opener.open(request, timeout=60) as response:
        return json.loads(response.read().decode("utf-8"))


def request_raw_json(opener, url, params):
    request = Request(
        f"{url}?{urlencode(params)}",
        headers={
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "User-Agent": "Mozilla/5.0",
            "X-Requested-With": "XMLHttpRequest",
        },
    )
    with opener.open(request, timeout=60) as response:
        body = response.read()
    return body, json.loads(body.decode("utf-8"))


def post_form_json(opener, url, data):
    request = Request(
        url,
        data=urlencode(data).encode("utf-8"),
        headers={
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "User-Agent": "Mozilla/5.0",
            "X-Requested-With": "XMLHttpRequest",
        },
        method="POST",
    )
    with opener.open(request, timeout=60) as response:
        return json.loads(response.read().decode("utf-8"))


def initialize_session(term):
    opener = build_opener(HTTPCookieProcessor(CookieJar()))
    opener.addheaders = [("User-Agent", "Mozilla/5.0")]
    with opener.open(REGISTRATION_URL, timeout=60) as response:
        response.read()
    with opener.open(TERM_SELECTION_URL, timeout=60) as response:
        response.read()
    request_json(opener, SAVE_TERM_URL, {"term": term})
    post_form_json(
        opener,
        TERM_SEARCH_URL,
        {
            "term": term,
            "studyPath": "",
            "studyPathText": "",
            "student": "",
            "altPin": "",
            "stu_pin": "",
            "holdPassword": "",
            "startDatepicker": "",
            "endDatepicker": "",
        },
    )
    return opener


def fetch_sections(term, term_title, page_size):
    opener = initialize_session(term)
    fetched_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sections = []
    pages = []
    offset = 0
    page_number = 1
    total_count = None
    total_bytes = 0

    while total_count is None or offset < total_count:
        params = {
            "txt_term": term,
            "pageOffset": str(offset),
            "pageMaxSize": str(page_size),
            "sortColumn": "subjectDescription",
            "sortDirection": "asc",
        }
        body, page = request_raw_json(opener, SEARCH_URL, params)
        rows = page.get("data") or []
        total_count = int(page.get("totalCount") or 0)
        sections.extend(rows)
        total_bytes += len(body)
        pages.append(
            {
                "page": page_number,
                "offset": offset,
                "rowCount": len(rows),
                "totalCount": total_count,
                "bytes": len(body),
            }
        )
        if not rows:
            break
        offset += len(rows)
        page_number += 1

    manifest = {
        "term": term,
        "termTitle": term_title,
        "fetchedAt": fetched_at,
        "source": "SDBOR public Registration Self-Service",
        "searchUrl": SEARCH_URL,
        "pageSize": page_size,
        "pageCount": len(pages),
        "totalRowsFetched": len(sections),
        "reportedTotalCount": total_count,
        "totalBytes": total_bytes,
        "totalMiB": round(total_bytes / 1024 / 1024, 2),
    }
    return sections, manifest


def weekly_days(meeting):
    return "".join(label for label, key in DAY_FIELDS if meeting.get(key)) or None


def institution_matches(section, institution):
    description = clean(section.get("campusDescription"))
    if not institution:
        return True
    if not description:
        return False
    needle = institution.casefold()
    haystack = description.casefold()
    return needle == haystack or needle in haystack


def build_lookups(sections):
    building_descriptions = defaultdict(set)
    campus_descriptions = defaultdict(set)
    subject_descriptions = defaultdict(set)
    institution_ids = {}
    institutions = []

    for section in sections:
        institution = clean(section.get("campusDescription"))
        if institution and institution not in institution_ids:
            institution_ids[institution] = len(institutions)
            institutions.append(institution)

        subject = clean(section.get("subject"))
        subject_description = clean(section.get("subjectDescription"))
        if subject and subject_description:
            subject_descriptions[subject].add(subject_description)

        for meeting_faculty in section.get("meetingsFaculty") or []:
            meeting = meeting_faculty.get("meetingTime") or {}
            building = clean(meeting.get("building"))
            building_description = clean(meeting.get("buildingDescription"))
            campus = clean(meeting.get("campus"))
            campus_description = clean(meeting.get("campusDescription"))
            if building and building_description:
                building_descriptions[building].add(building_description)
            if campus and campus_description:
                campus_descriptions[campus].add(campus_description)

    building_map = {}
    ambiguous_buildings = {}
    for building, descriptions in sorted(building_descriptions.items()):
        values = sorted(descriptions)
        if len(values) == 1:
            building_map[building] = values[0]
        else:
            ambiguous_buildings[building] = values

    campus_map = {}
    ambiguous_campuses = {}
    for campus, descriptions in sorted(campus_descriptions.items()):
        values = sorted(descriptions)
        if len(values) == 1:
            campus_map[campus] = values[0]
        else:
            ambiguous_campuses[campus] = values

    subject_map = {
        subject: sorted(descriptions)[0]
        for subject, descriptions in sorted(subject_descriptions.items())
        if descriptions
    }

    return {
        "institution_ids": institution_ids,
        "institutions": institutions,
        "subject_map": subject_map,
        "building_map": building_map,
        "ambiguous_buildings": ambiguous_buildings,
        "campus_map": campus_map,
        "ambiguous_campuses": ambiguous_campuses,
    }


def faculty_names(section):
    names = []
    for faculty in section.get("faculty") or []:
        name = clean(faculty.get("displayName"))
        if name:
            names.append(name)
    return names


def meeting_row(meeting_faculty, ambiguous_buildings):
    meeting = meeting_faculty.get("meetingTime") or {}
    building = clean(meeting.get("building"))
    row = compact_dict(
        {
            "d": weekly_days(meeting),
            "bt": clean(meeting.get("beginTime")),
            "et": clean(meeting.get("endTime")),
            "b": building,
            "r": clean(meeting.get("room")),
        }
    )
    if building in ambiguous_buildings:
        row["bd"] = clean(meeting.get("buildingDescription"))
    return row


def course_row(section, lookups):
    institution = clean(section.get("campusDescription"))
    return compact_dict(
        {
            "crn": clean(section.get("courseReferenceNumber")),
            "inst": lookups["institution_ids"].get(institution),
            "subj": clean(section.get("subject")),
            "num": clean(section.get("courseNumber")),
            "sec": clean(section.get("sequenceNumber")),
            "title": clean(section.get("courseTitle")),
            "fac": faculty_names(section),
            "mtg": [
                meeting_row(meeting_faculty, lookups["ambiguous_buildings"])
                for meeting_faculty in section.get("meetingsFaculty") or []
            ],
        }
    )


def condense_sections(all_sections, manifest, institution, all_institutions):
    if all_institutions:
        sections = all_sections
        scope_description = "all Board of Regents institutions"
    else:
        sections = [
            section
            for section in all_sections
            if institution_matches(section, institution)
        ]
        scope_description = institution

    lookups = build_lookups(sections)
    seen_crns = set()
    courses = []
    for section in sections:
        crn = clean(section.get("courseReferenceNumber"))
        if not crn or crn in seen_crns:
            continue
        seen_crns.add(crn)
        courses.append(course_row(section, lookups))

    return {
        "term": {
            "code": manifest.get("term"),
            "description": manifest.get("termTitle"),
        },
        "source": {
            "name": manifest.get("source"),
            "search_url": manifest.get("searchUrl"),
            "fetched_at": manifest.get("fetchedAt"),
            "page_count": manifest.get("pageCount"),
            "page_size": manifest.get("pageSize"),
            "reported_total_count": manifest.get("reportedTotalCount"),
            "total_rows_fetched": manifest.get("totalRowsFetched"),
        },
        "scope": {
            "institution": None if all_institutions else institution,
            "description": scope_description,
            "input_rows": len(all_sections),
            "selected_rows": len(sections),
        },
        "schema": {
            "course": {
                "crn": "course_reference_number",
                "inst": "institutions index from section campusDescription",
                "subj": "subject",
                "num": "course_number",
                "sec": "sequence_number",
                "title": "course_title",
                "fac": "faculty_names",
                "mtg": "meetings",
            },
            "meeting": {
                "d": "weekly_days",
                "bt": "begin_time",
                "et": "end_time",
                "b": "building code",
                "r": "room",
                "bd": "building_description, only when code is ambiguous",
            },
        },
        "lookups": {
            "institutions": lookups["institutions"],
            "meeting_campuses": lookups["campus_map"],
            "ambiguous_meeting_campuses": lookups["ambiguous_campuses"],
            "subjects": lookups["subject_map"],
            "buildings": lookups["building_map"],
            "ambiguous_buildings": lookups["ambiguous_buildings"],
        },
        "count": len(courses),
        "courses": courses,
    }


def default_output_path(output_dir, term_title, institution, all_institutions):
    if all_institutions:
        suffix = "bor"
    elif institution == DEFAULT_INSTITUTION:
        suffix = "usd"
    else:
        suffix = slug(institution)
    return output_dir / f"{slug(term_title)}-{suffix}-web-payload.json"


def parse_terms(args):
    if not args.term:
        return DEFAULT_TERMS
    titles = args.term_title or []
    if titles and len(titles) != len(args.term):
        raise SystemExit("--term-title must be repeated once for each --term")
    return [
        (term, titles[index] if titles else term)
        for index, term in enumerate(args.term)
    ]


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--term", action="append", help="Banner term code; repeat for multiple terms.")
    parser.add_argument("--term-title", action="append", help="Term title matching each --term.")
    parser.add_argument("--page-size", type=int, default=PAGE_SIZE)
    parser.add_argument(
        "--institution",
        default=DEFAULT_INSTITUTION,
        help="Filter to an owning institution/campusDescription. Substrings are accepted.",
    )
    parser.add_argument(
        "--all-institutions",
        action="store_true",
        help="Include all Board of Regents institutions.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(__file__).parent,
    )
    return parser.parse_args()


def main():
    args = parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    for term, term_title in parse_terms(args):
        sections, manifest = fetch_sections(term, term_title, args.page_size)
        payload = condense_sections(
            sections,
            manifest,
            institution=args.institution,
            all_institutions=args.all_institutions,
        )
        output_path = default_output_path(
            args.output_dir,
            term_title,
            args.institution,
            args.all_institutions,
        )
        output_path.write_text(json_payload(payload), encoding="utf-8")
        print(
            f"{term_title}: fetched {len(sections)} rows, "
            f"wrote {payload['count']} records to {output_path}"
        )


if __name__ == "__main__":
    main()
