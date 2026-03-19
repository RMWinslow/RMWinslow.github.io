---
nav_exclude: true
search_exclude: true
---

# Claude Notes

This file serves as Claude's working memory for the RMWinslow.github.io project.
Rather than relying on the separate `.claude/` memory system, store observations,
context, and notes here so they stay visible in the repo and are easy to review.

## Writing Style

When taking notes in this file, use natural flowing language rather than terse
bullet fragments. Write as though explaining things to a colleague — complete
sentences, clear reasoning, enough context that the note makes sense on its own
months later. Bullet points are fine for lists of items, but each bullet should
still read as a coherent thought.

## How to Use This File

- **Memories go here.** Any context, observations, or learned details about the
  project that would be useful across conversations should be written directly
  into this file rather than (or in addition to) the `.claude/` memory directory.
  This keeps everything version-controlled and human-readable.
- **TODOs go here.** Track outstanding tasks, ideas, and next steps in the TODOs
  section below. Check items off as they're completed. If a TODO grows complex
  enough to need its own tracking, note that here and point to where the detail
  lives.
- **Update regularly.** When you learn something new about the project, finish a
  task, or notice something worth remembering, update this file in the same
  conversation rather than waiting.

## Project Context

This is Robert Winslow's personal academic website, built with Jekyll and hosted
on GitHub Pages. It uses the custom `RMWinslow/JTD-RMW` theme (a fork of
Just the Docs). The site contains teaching materials, research pages, and notes
primarily related to economics.

There are several sibling repos that share the same theme: `posts` (blog),
`bib` (bibliography), `games` (game rules), and `circe` (literary text). A
detailed audit of all these sites lives in `claude_audits.md` in this repo.

## TODOs

- [ ] Fix 3 phantom parents in this repo: "Competitive Equilibrium",
  "Aggregate Measurement", and "Money and Banking" all have `has_children: true`
  but no child pages reference them.
- [ ] Review the 31 broken internal links identified in `claude_audits.md` for
  this site (mostly legacy HTML files with wrong relative paths to `sakura.css`).
- [ ] Consider adding `search_exclude: true` to the 104 legacy HTML files that
  lack frontmatter, to keep them out of the search index.
- [ ] Create markdown-based posts for research projects instead of just hosting
  PDFs. The idea is to write shorter, more approachable descriptions of each
  research project in natural language — something a visitor can actually read
  on the site — while still including nice images, key figures, and links to
  the full papers. Think of these as accessible summaries rather than formal
  abstracts.
- [ ] Consider splitting the notes section out into its own subsite (a separate
  repo with its own GitHub Pages deployment, like `posts`, `games`, etc.).
  The notes are already a fairly self-contained collection under their own nav
  parent, so they might be a natural candidate for separation. Worth weighing
  whether the added repo overhead is justified by the organizational clarity.
- [ ] Fix metadata on the CV files in `files/`. The PDFs there (e.g.
  "CV Robert Winslow - Job Market.pdf", "CV Robert Winslow.pdf",
  "CV - Robert Winslow - Jan 2025.docx") could use updated document properties
  (title, author, dates) so they present cleanly when shared or indexed.
- [ ] In the `posts` repo, replace the orphaned-parent hack for hiding pages
  with proper `nav_exclude: true`. Four pages ("Games Free with Amazon Prime",
  "Novels", "NES A-Z", "Web Fiction") use a nonexistent parent value like
  `"hidden"` or `"_Media"` to keep themselves out of the sidebar. That works
  but is fragile and unclear — `nav_exclude: true` is the intended mechanism.

## Observations

Nothing yet — add notes here as work progresses.
