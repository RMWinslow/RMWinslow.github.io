---
nav_exclude: true
search_exclude: true
---

# Search Index Audit (2026-03-22)

Audit of which pages appear in the main site's search index
(`/assets/js/search-data.json`) and whether each entry is appropriate.

## Current search index entries

| URL path | Source file | Appropriate? | Notes |
|---|---|---|---|
| `/teaching.html` | `teaching.md` | Yes | Parent nav page |
| `/teaching/3102.html` | `teaching/3102.md` | Yes | Course page |
| `/teaching/330.html` | `teaching/330.md` | Yes | Course page |
| `/research.html` | `research.md` | Yes | Parent nav page |
| `/research/jmp.html` | `research/jmp.md` | Yes | Job market paper |
| `/research/mebdi22.html` | `research/mebdi22.md` | Yes | Research project |
| `/research/contagion.html` | `research/contagion.md` | Yes | Research project |
| `/research/reu.html` | `research/reu.md` | Yes | Research project |
| `/cv.html` | `cv.md` | Yes | CV page |
| `/slides/` | `slides/index.md` | Debatable | Has `nav_exclude: true` but no `search_exclude`. Lists PDF slide decks. |
| `/slides/remark_formattest.html` | `slides/remark_formattest.md` | **No** | Test page with 10 heading sub-entries polluting the index. Has `nav_exclude: true` but no `search_exclude`. |

## Pages with `nav_exclude: true` but missing `search_exclude: true`

These files are hidden from the sidebar but still appear in search results:

- **`slides/remark_formattest.md`** — A formatting test page for Remark
  slides. Generates 10+ sub-entries in the search index from its headings
  ("Slide with a Footnote", "alt footnote test", "katex gdefs", etc.). This
  is clearly not something a visitor should find via search. Should add
  `search_exclude: true`.

- **`slides/index.md`** — The slide deck index page. It's nav-hidden, which
  suggests it's not meant for primary discovery, but someone searching for
  "slides" or "defense" might reasonably want to find it. Could go either
  way.

## HTML files without frontmatter (not in search index)

These are static HTML files served by Jekyll but not processed through the
theme. They don't appear in the search index because they lack frontmatter,
which is correct behavior:

- `index.html` — Site landing page (custom HTML, not themed)
- `404.html` — Error page
- `teaching/calendar_creator.html` — Interactive calendar tool

## Redirect stubs (not in search index)

The `redirects/` directory contains 93 stub files (26 for the 3102 migration,
2 for 202, 1 for econ-UMN electives, 64 for the econ/ migration). These have
minimal frontmatter (`permalink` + `redirect_to`) and do **not** explicitly
set `search_exclude: true`. However, `jekyll-redirect-from` generates pages
with `<meta name="robots" content="noindex">` and no real content, so they
don't produce search index entries. None appear in the live search data.

## Internal/documentation files (correctly excluded)

These files have both `nav_exclude: true` and `search_exclude: true`:

- `CLAUDE.md` — Claude's working memory
- `claude_audits.md` — Audit notes
- `claude_directory.md` — Directory listing
- `redirects/INDEX.md` — Redirect inventory

## Recommended actions

1. **Add `search_exclude: true` to `slides/remark_formattest.md`** — This is
   the clearest win. A test page shouldn't appear in search at all, let alone
   with 10 sub-entries.

2. **Decide on `slides/index.md`** — Either add `search_exclude: true` for
   consistency with its nav-hidden status, or remove `nav_exclude: true` if
   it's actually useful for visitors to find via both search and nav.
