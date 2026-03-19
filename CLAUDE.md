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
- [ ] Clean up duplicate directory trees in the legacy `econ/` area.
  `econ/teaching/3102/typesetting/` and `econ/teaching/typesetting/` contain
  identical files. `econ/teaching/3102/intertemporal/intertemporal/` is a
  duplicated subdirectory inside itself, complete with duplicate SVG images.
  One copy of each should be deleted.
- [ ] Remove Windows copy-paste artifacts from the repo: files named things
  like `consumerInteractive (2).html`, `LBDconcepts - Copy (2).html`,
  `LBDconcepts - Copy (3).html`, `twoPeriodEndowment (2).html`,
  `sakura copy.css`, `sakuraPink - Copy.css`. These are accidental duplicates
  that add clutter.
- [ ] Add `.lyx~`, `.lyx.emergency`, and `__pycache__/` to `.gitignore`, then
  remove the ones already committed. There are dozens of LyX backup files in
  `econ/research/` and `econ/tradeprelim/`, plus a Python bytecode cache in
  `econ/research/ContagionThing/__pycache__/`.
- [ ] Clean up or reorganize `econ/research/ContagionThing/`. This is the
  messiest single directory — 80+ files including Python scripts, LyX drafts,
  backup files, simulation output images, 28 `pasted*.png` screenshots with
  no clear labels, and a `.graphml` file. It reads like a working directory
  that was committed wholesale. Worth deciding what to keep vs archive.
- [ ] Clean up the `styles/` directory — most of these files are dead weight.

  Audited 2026-03-18. Of the 22 CSS/SCSS files in `styles/`, only 6 are
  actually referenced by any HTML page in the repo. All of them are used
  exclusively by the legacy pre-Jekyll HTML files; the Jekyll site itself
  uses the JTD-RMW theme CSS and doesn't touch any of these.

  **Actively used:**

  | File | Pages | Notes |
  |------|-------|-------|
  | `sakura.css` | ~60 | The main workhorse — used by legacy HTML across `econ/` |
  | `basic.css` | 1 | Only `index.html` |
  | `basic_sakura.css` | ~8 | Trade prelim pages in `econ/tradeprelim/` |
  | `sakuraBlue.css` | 3 | Jones macro prelim pages |
  | `sakuraGreen.css` | 2 | Chari macro prelim pages |
  | `sakuraPink.css` | 3 | Kehoe macro prelim pages |

  The color variants are a fun detail — they're professor-specific theming
  for the macro prelim study notes. Chari gets green, Kehoe gets pink,
  Jones gets blue.

  **Effectively dead (1):** `everythingbagel.css` is linked from
  `_layouts/default_basic.html`, but no page in the repo uses that layout.

  **Completely unreferenced — safe to delete (15):**
  `TODOsakuraSolar.css`, `classless.css`, `everythingbagel-JTD.css`,
  `everythingbagel-lists.css`, `main.scss`, `panfried.css`,
  `sakura copy.css`, `sakura solarized test 2.css`,
  `sakura-earthly.scss.txt`, `sakura-paper.scss`, `sakuraPink - Copy.css`,
  `sakuraUMN.css`, `sakura_basic.css`, `style.css`, `sakura.css.map`.
  Also `assets/css/extrabits.css` is unreferenced.
- [ ] Rename or remove `font/sdfsdfds.ttf` — it's a keyboard-mash test font
  filename that got committed. Either give it a real name or delete it if
  it's not used.

## Project Context — Research

The job market paper ("How much did Bonus Unemployment Insurance Payments
During the COVID Pandemic Depress Aggregate Employment?") is currently under
review as of March 2026. Listed at `research/jmp.md`.

Robert is no longer at UMN — the Econ Electives page (`econ/UMNelectives.md`)
has been hidden from nav accordingly.

## Observations

There are two generations of interactive economics graphs in the repo, both
nav-hidden but actively served:

- **`3102/graphs.md`** is the current version, using kgjs (KineticGraphs).
  It loads YML config files from `3102/graphs/*.yml` and renders them
  client-side with `kg3d.0.2.6.js`. These support click-and-drag interaction.

- **`3102/graphs2.md`** is the older version, using Highcharts. It embeds
  the 9 HTML files in `3102/highcharts/` via iframes and provides standalone
  links to each. These files are self-contained (no external CSS, no sakura)
  and still functional. They're not orphaned legacy — they're intentionally
  kept as a working fallback.

The legacy `econ/` HTML files that use `sakura.css` are a separate matter
entirely — those are pre-Jekyll study notes that aren't linked from anywhere
in the current nav tree.
