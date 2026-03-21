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

## Do Not Fabricate

Never invent details about how something works when you don't actually know.
If you haven't read the code or verified the mechanism, say "I don't know how
this works" rather than confecting a plausible-sounding explanation. Making
things up poisons the project's documentation and memory — a confident
falsehood in a comment or note will mislead future sessions (and humans) who
trust it at face value. State what you've observed, flag what you're unsure
about, and leave blanks rather than filling them with fiction. This applies to
comments in code, notes in this file, commit messages, and any other written
output.

## Writing Conventions for Claude

Do not drop articles ("a", "an", "the") from commit messages, prose, or any
other written text. Write in complete, natural English rather than telegraphic
shorthand. Dropping articles makes text read like a telegram and is especially
noticeable in commit messages, which become part of the permanent project
history. Before finalizing any commit message or written output, re-read it and
check that every noun phrase that needs an article has one. Pay special
attention to commit subject lines, where there's a temptation to compress —
"Clean up redirect test" should be "Clean up the redirect test."

Commit messages should explain reasoning and motivation ("why"), not restate
the diff ("what"). A good commit message reads like a short note to a future
reader explaining the decision, not a changelog entry listing which files
changed.

When migrating or reorganizing files, separate the mechanical move from any
edits to the moved files. First commit the files with their original content
and structure preserved exactly, then commit the modifications (frontmatter
rewrites, link fixes, etc.) as a separate change. This makes each commit
independently reviewable and keeps the move diffable.

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
`bib` (bibliography), `games` (game rules), `circe` (literary text), and
`notes` (economics teaching notes, deployed at `/notes/`). A detailed audit
of all these sites lives in `claude_audits.md` in this repo.

## TODOs

- [x] *(Resolves with notes migration)* Fix 3 phantom parents in this repo:
  "Competitive Equilibrium" and "Aggregate Measurement" have
  `has_children: true` but no child pages reference them. **Done 2026-03-19.**
  These files moved to the notes repo, where `_equilibrium.md` and
  `_measurement.md` now have `parent: Intermediate Macro Notes` and can have
  children wired beneath them once they're ready to publish. "Money and
  Banking" was a false positive (`teaching/330.md` already has
  `has_children: false`).
- [x] Review the broken internal links identified in `claude_audits.md` for
  this site. **Done 2026-03-20.** All 31 broken links from the audit were in
  files that have since moved to the notes repo (`econ/`, `3102/`, `202/`) or
  been deleted (`js/katex/`). The only links the audit flagged in files still
  here are the three cross-repo links in `index.html` (`/art`, `/games`,
  `/posts`), which aren't actually broken — they resolve correctly at the
  domain level because those repos deploy as subdirectories of
  `www.rmwinslow.com`. The broken-link items that are now the notes repo's
  responsibility have been transferred to its `CLAUDE.md`.
- [ ] Consider adding `search_exclude: true` to legacy HTML files that lack
  frontmatter, to keep them out of the search index. Most of these have now
  moved to the notes repo — check what remains in the main repo.
- [ ] Create markdown-based posts for research projects instead of just hosting
  PDFs. The idea is to write shorter, more approachable descriptions of each
  research project in natural language — something a visitor can actually read
  on the site — while still including nice images, key figures, and links to
  the full papers. Think of these as accessible summaries rather than formal
  abstracts.
- [x] Split the notes section out into its own subsite. **Done 2026-03-19.**
  The `3102/` directory and `notes.md` have been moved to the `notes` repo,
  which deploys at `www.rmwinslow.com/notes/`. The directory was subsequently
  renamed from `3102/` to `302/` on 2026-03-20, so the notes now live at
  `notes/302/` and are served at `/notes/302/...`. The 26 redirect stubs in
  `redirects/` cover all the old URLs (21 content pages, 3 nav-hidden pages,
  2 legacy twoperiod-consumer aliases), and the notes repo pages also have
  `redirect_from` entries covering the intermediate `/notes/3102/...` URLs.
  The nav hierarchy was restructured so that `topic-overview.md` is a
  top-level parent with room for a third level. See `redirects/INDEX.md` for
  the full inventory and validation procedure.

  The redirect strategy uses site-relative paths (e.g.
  `redirect_to: /notes/302/topic-overview`) and `jekyll-redirect-from`
  generates single-hop client-side redirects with `noindex` and `canonical`
  tags. The test from 2026-03-19 confirmed this works end-to-end.

  **Still TODO:** Consolidate the `mynotes` repo (currently on the
  `minimal-mistakes` theme at a separate URL) into the notes repo.
- [x] Migrate the entire `econ/` directory to the notes repo. **Done
  2026-03-20.** The entire `econ/` directory (~345 tracked files) was copied
  to the notes repo and removed from the main repo. 65 redirect stubs were
  created in `redirects/` (1 MD + 64 HTML) to preserve all existing URLs.
  The orphaned PNGs in `econ/teaching/3102/typesetting/` were deleted before
  the move (the duplicate HTML files had already been removed). The duplicate
  `intertemporal/intertemporal/` directory and `3102/typesetting/` HTML files
  were already cleaned up in prior commits. The `.lyx~` backup files were
  already untracked via `.gitignore`. A `.gitignore` was added to the notes
  repo to keep LyX backup files out of tracking there as well. The CSS
  references in these HTML files use root-relative paths (`/assets/css/...`)
  which continue to work under the shared domain.
- [x] Move the CSS files in `styles/` into `assets/css/` and update all
  references. **Done 2026-03-20.** All 7 stylesheets moved to `assets/css/`.
  All 65 HTML files under `econ/` were updated to use root-relative paths
  (`/assets/css/...`), which also fixes the ~15 broken relative paths
  identified in the audit. `index.html` and `_layouts/default_basic.html`
  were updated as well. No subsites successfully referenced these stylesheets
  — the two cross-repo references in the `games` repo
  (`cardImages.html` → `sakura.css`, `randomWords.html` → `everythingbagel.css`)
  were already broken and remain so (they point at a `styles/` directory that
  doesn't exist in that repo). The `econ/presentations/percolationSlides.html`
  Reveal.js references (`styles/reveal/`) were already broken (no such
  directory ever existed) and are unrelated to these stylesheets.
- [ ] *(Best done after notes migration)* Add a link back to the main site
  (www.rmwinslow.com) in each subsite's navigation. The subsites (`posts`,
  `games`, `bib`, `circe`, and the future `notes`) don't currently have an
  obvious way to get back to the root site. JTD-RMW supports
  `nav_external_links` in `_config.yml` — the main site already uses this for
  the Blog link. Makes sense to do this when setting up the notes repo's
  config anyway.
- [ ] Move the `font/` directory into `assets/font/` and update all references.
  The `font/` directory at the repo root contains custom webfonts (e.g.
  `strippedCards2.ttf`). It should live under `assets/` for consistency with
  the CSS move to `assets/css/`. References in `sakura.css` and any HTML files
  that load these fonts will need updating.
- [ ] Fix metadata on the CV files in `files/`. The PDFs there (e.g.
  "CV Robert Winslow - Job Market.pdf", "CV Robert Winslow.pdf",
  "CV - Robert Winslow - Jan 2025.docx") could use updated document properties
  (title, author, dates) so they present cleanly when shared or indexed.
- [ ] Revisit the organization of the `bib` repo. It worked well with a small
  number of papers but didn't scale — the result is a mess. The publicly
  indexed nature of it is nice (a browsable bibliography), but the current
  structure needs rethinking. Some ideas:
  - Use an AI-assisted workflow to standardize the file format across entries,
    validate and clean up metadata, and identify natural groupings.
  - Reorganize around research strains/topics as visible nav-level collections,
    while making individual paper pages `nav_exclude: true` (so they exist and
    are searchable, but don't clutter the sidebar).
  - Investigate Zotero integration — can entries be round-tripped between the
    bib repo and a Zotero library? Import from Zotero to generate pages, export
    annotations back? This would let Zotero handle the bibliographic metadata
    while the repo handles the public-facing presentation and personal notes.
  - Whatever the new structure is, it should still allow for Robert's own
    reading notes and annotations on each paper.
- [x] Update the main site README to index the subsites. **Done 2026-03-20.**
  The README now lists all active subsites (posts, notes, bib, games, circe)
  with repo links, live URLs, and descriptions, plus the unconsolidated older
  repos (tones, mynotes, macronotes). It also describes what's in this repo
  and how the pieces fit together.
- [ ] In the `posts` repo, replace the orphaned-parent hack for hiding pages
  with proper `nav_exclude: true`. Four pages ("Games Free with Amazon Prime",
  "Novels", "NES A-Z", "Web Fiction") use a nonexistent parent value like
  `"hidden"` or `"_Media"` to keep themselves out of the sidebar. That works
  but is fragile and unclear — `nav_exclude: true` is the intended mechanism.
- [x] Clean up duplicate directory trees in the legacy `econ/teaching/` area.
  **Done 2026-03-19 through 2026-03-20.** The duplicate HTML files in
  `econ/teaching/3102/typesetting/` were removed in 79fc635 (deduplication
  step). The orphaned PNGs left behind were deleted in f934c65 (pre-migration
  cleanup). The duplicate `intertemporal/intertemporal/` directory was also
  removed in 79fc635. The surviving copies at `econ/teaching/typesetting/`
  and `econ/teaching/3102/intertemporal/` now live in the notes repo.
- [x] Remove Windows copy-paste artifacts from the repo: files named things
  like `consumerInteractive (2).html`, `LBDconcepts - Copy (2).html`,
  `LBDconcepts - Copy (3).html`, `twoPeriodEndowment (2).html`,
  `sakura copy.css`, `sakuraPink - Copy.css`. These are accidental duplicates
  that add clutter. **Done 2026-03-19.** Also removed two "- Copy" PNGs from
  `ContagionThing/img/`. The mirrored headshot in `portraits/` was kept
  intentionally.
- [x] Add `.lyx~`, `.lyx.emergency`, and `__pycache__/` to `.gitignore`, then
  remove the ones already committed. **Done 2026-03-19.** Added
  `*.lyx.emergency` and `__pycache__/` to `.gitignore` (the `*.lyx~` rule was
  already there). Untracked 19 `.lyx~` files, 1 `.lyx.emergency` file, and
  1 `__pycache__/` directory using `git rm --cached`.
- [x] Migrate `econ/research/` to the `papersdrafts` repo. **Done 2026-03-19.**
  The entire `econ/research/` directory (ContagionThing, farmingToy, arrowroot,
  FIFA, and loose files) was moved to `papersdrafts/research/`. These were
  pre-git and 2020-era research working files, not teaching notes. A migration
  note with the original commit history link is included in the destination.
- [x] Clean up the `styles/` directory — most of these files are dead weight.
  **Done 2026-03-19.** Deleted 15 unreferenced CSS/SCSS files. The 6 actively
  used stylesheets and `everythingbagel.css` (layout dependency) are retained.

  **Correction:** `assets/css/extrabits.css` was originally flagged as
  unreferenced, but it is actually imported by the JTD-RMW theme's main CSS
  file at build time. It does not appear in any HTML `<link>` tag in this
  repo, which is why the audit missed it. It should not be deleted.

  These 7 files were subsequently moved from `styles/` to `assets/css/` on
  2026-03-20. The color variants are professor-specific theming for the
  macro prelim study notes (Chari gets green, Kehoe gets pink, Jones gets
  blue).
- [x] Rename or remove `font/sdfsdfds.ttf`. **Done 2026-03-19.** Deleted. Based
  on the git history, it appears to have been an intermediate build of the
  strippedCards font from the 2019 Samsung emoji workaround — it was added in
  the same commit as updates to `strippedCards2.ttf` and `cardImages.html`,
  and is nearly identical in file size (70,360 vs 70,396 bytes).

## Redirect Strategy Test (2026-03-19)

As part of the plan to split the economics notes into their own repo, we needed
to verify that the proposed redirect strategy actually works before committing
to a full migration. The idea is simple: when the notes move to a new `notes`
repo deployed at `www.rmwinslow.com/notes/`, redirect stubs in the main repo
should seamlessly send visitors from the old URLs to the new ones. But "should
work" and "does work" are different things, especially with GitHub Pages, Jekyll
theme interactions, and `baseurl` pathing all in the mix. So we ran a minimum
viable test.

We created a small `notes` repo with `baseurl: /notes` in its `_config.yml`,
a bare-bones `index.md` landing page, and a `test.md` page whose only purpose
was to exist at `www.rmwinslow.com/notes/test` as a redirect target. On the
main repo side, we created `redirects/test-redirect.md` — a file with nothing
but `permalink: /test-redirect` and `redirect_to: /notes/test` in its
frontmatter. The `redirects/` folder (no underscore prefix) was chosen so Jekyll
would process it without needing any `include` directive in `_config.yml`. We
then pushed both repos and waited for the GitHub Pages builds to complete.

The results confirmed everything works as intended. Curling the redirect stub
at `www.rmwinslow.com/test-redirect` returned a lightweight HTML page generated
by `jekyll-redirect-from` with three redirect mechanisms: a JavaScript
`location` assignment, an instant `<meta http-equiv="refresh">`, and a
`<link rel="canonical">` pointing to the target. The page also included
`<meta name="robots" content="noindex">` to keep the stub out of search
indexes. GitHub Pages served this as a normal 200 response (not a 301 or 302),
which is expected — GitHub Pages only serves static files, so the redirect
happens client-side. Google treats instant meta refresh redirects as permanent
redirects according to their own documentation, so this is fine for SEO
purposes.

Curling the target at `www.rmwinslow.com/notes/test` returned a fully rendered
JTD-RMW themed page with all assets (CSS, JS, fonts) correctly resolving under
the `/notes/` base path. The nav sidebar showed up, the search bar was present,
MathJax loaded — the whole theme came through cleanly. The `baseurl: /notes`
setting worked exactly as expected, and the notes repo is properly deployed as a
subdirectory of the main domain rather than a subdomain.

One detail worth noting: the `redirect_to` value was a relative path
(`/notes/test`) rather than an absolute URL, and `jekyll-redirect-from`
correctly expanded it to the full `https://www.rmwinslow.com/notes/test` URL in
the generated redirect page. This means the redirect stubs can use site-relative
paths, which is cleaner and more portable than hardcoding the full domain.

The redirect is a single hop — there is no intermediate redirect or chain. A
visitor hitting `/test-redirect` goes straight to `/notes/test` in one step.
This was a key requirement to avoid redirect chains that slow down page loads
and can confuse search engine crawlers.

After verifying everything, we deleted the test files from both repos. The test
confirmed that the redirect strategy described in the TODOs section above is
sound and ready for the full migration whenever we're ready to move the
content over.

The SEO research supporting the subdirectory deployment choice (over a subdomain)
is documented in `claude_audits.md` at the end of the file.

## Project Context — Research

The job market paper ("How much did Bonus Unemployment Insurance Payments
During the COVID Pandemic Depress Aggregate Employment?") is currently under
review as of March 2026. Listed at `research/jmp.md`.

Robert is no longer at UMN — the Econ Electives page (now at
`notes/econ/UMNelectives.md`) has been hidden from nav accordingly.

The `101/` directory (Principles of Micro) has been deleted — it was just
placeholders. The `202/` directory (Principles of Macro) has been moved to the
private Teaching-Notes repo at `202/_legacy website draft notes (incorporate
later)`. Only `inflation-costs.md` had real content; the other two pages were
placeholders with extensive research notes hidden in HTML comments. This
reduces the notes migration scope and eliminates two redirect stubs.

## Observations

There are two generations of interactive economics graphs in the repo, both
nav-hidden but actively served:

- **`302/graphs.md`** (in the notes repo) is the current version, using kgjs
  (KineticGraphs). It loads YML config files from `302/graphs/*.yml` and
  renders them client-side with `kg3d.0.2.6.js`. These support click-and-drag
  interaction.

- **`302/graphs2.md`** (in the notes repo) is the older version, using
  Highcharts. It embeds the 9 HTML files in `302/highcharts/` via iframes and
  provides standalone links to each. These files are self-contained (no
  external CSS, no sakura) and still functional. They're not orphaned legacy —
  they're intentionally kept as a working fallback.

The legacy `econ/` HTML files that use `sakura.css` now live in the notes repo
(at `notes/econ/`). They're pre-Jekyll study notes that aren't linked from
anywhere in the current nav tree but are still actively served via redirect
stubs in the main repo.
