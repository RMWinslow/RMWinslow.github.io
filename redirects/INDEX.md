---
nav_exclude: true
search_exclude: true
---

<!-- claude-generated -->

# Redirect Index

## How the redirects work

When a page moves from this repo to another subsite (e.g. the `notes` repo),
we place a small redirect stub in this `redirects/` folder. Each stub has only
two lines of frontmatter:

```yaml
---
permalink: /old/path
redirect_to: /new/path
---
```

Jekyll + `jekyll-redirect-from` generates a lightweight HTML page at the old
URL containing a JavaScript `location` redirect, an instant `<meta refresh>`,
a `<link rel="canonical">` pointing to the new URL, and
`<meta name="robots" content="noindex">`. GitHub Pages serves this as a static
200 response — the redirect happens client-side. Google treats instant meta
refresh as a permanent redirect (confirmed in our 2026-03-19 test; see
CLAUDE.md for the full narrative).

The `redirects/` folder uses no underscore prefix so Jekyll processes it
without needing an `include` directive in `_config.yml`.

## How to validate redirects

Run through this checklist after creating or updating redirect stubs:

1. **Push the changes** to both repos and wait for GitHub Pages builds to
   complete (usually 1-2 minutes).
2. **Curl each old URL** and verify the response contains a redirect to the
   expected target:
   ```
   curl -s https://www.rmwinslow.com/OLD/PATH | grep 'location='
   ```
3. **Curl each new URL** and verify the target page renders correctly:
   ```
   curl -s https://www.rmwinslow.com/notes/NEW/PATH | grep '<title>'
   ```
4. **Check for single hop** — the redirect should go directly from the old URL
   to the new one with no intermediate step. If the target itself redirects,
   that's a chain and should be fixed.
5. **Update this index** — mark each entry as validated with a date.

## How to handle post-migration moves

If a page is renamed or reorganized after migration:

1. Add a new location entry to the page's record in this index.
2. Update the redirect stub's `redirect_to` value to point to the new URL.
3. If the page had a `redirect_from` in its frontmatter (e.g.
   `twoperiod-endowment.md`), make sure those old paths are still covered —
   either by the notes repo's own `redirect_from` or by additional stubs here.
4. Re-validate using the procedure above.

---

## Migration inventory

Each page's location history is listed chronologically. The entry tagged
`[pre-migration]` is the URL that needs a redirect stub in this repo. The
entry tagged `[current]` is where the page lives now. After migration, update
`[current]` tags accordingly.

Pages are grouped by their nav hierarchy. Assets (images, YML configs,
Highcharts HTML, PDFs) move with their parent pages and don't need individual
redirect stubs since they aren't in the Jekyll nav or search index.

Files starting with `_` (underscore) are excluded from Jekyll's build by
default — they never generate URLs and don't need redirect stubs. They're
tracked here for completeness but grouped separately.

### Top-level nav page

#### Notes
- [ ] `RMWinslow.github.io/notes.md` → `/notes` (original)
- [ ] `RMWinslow.github.io/notes_temp.md` → `/notes_temp` (renamed for redirect test) `[pre-migration]`
- [ ] `notes/index.md` → `/notes/` `[current]`
- Redirect stub: probably not needed — the notes repo deploys at `/notes/`,
  so the old `/notes` URL will be served by the new repo directly. The main
  repo's `notes_temp.md` just needs to be deleted. Verify during migration
  that `/notes` resolves correctly without a stub.

### Parent pages (second level in notes repo)

#### Intermediate Macro Notes
- [ ] `RMWinslow.github.io/3102/topic-overview.md` → `/3102/topic-overview` `[pre-migration]`
- [ ] `notes/3102/topic-overview.md` → `/notes/3102/topic-overview` `[current]`
- Redirect stub: `redirects/3102-topic-overview.md`
- has_children: true

### Content pages

#### Bank Runs (Diamond-Dybvig)
- [ ] `RMWinslow.github.io/3102/diamond.md` → `/3102/diamond` `[pre-migration]`
- [ ] `notes/3102/diamond.md` → `/notes/3102/diamond` `[current]`
- Redirect stub: `redirects/3102-diamond.md`

#### McCall Job Search
- [ ] `RMWinslow.github.io/3102/jobsearch.md` → `/3102/jobsearch` `[pre-migration]`
- [ ] `notes/3102/jobsearch.md` → `/notes/3102/jobsearch` `[current]`
- Redirect stub: `redirects/3102-jobsearch.md`

#### Constrained Optimization
- [ ] `RMWinslow.github.io/3102/math-lagrangian.md` → `/3102/math-lagrangian` `[pre-migration]`
- [ ] `notes/3102/math-lagrangian.md` → `/notes/3102/math-lagrangian` `[current]`
- Redirect stub: `redirects/3102-math-lagrangian.md`

#### Business Cycles
- [ ] `RMWinslow.github.io/3102/measurement-cylical.md` → `/3102/measurement-cylical` `[pre-migration]`
- [ ] `notes/3102/measurement-cylical.md` → `/notes/3102/measurement-cylical` `[current]`
- Redirect stub: `redirects/3102-measurement-cylical.md`

#### Gross Domestic Product
- [ ] `RMWinslow.github.io/3102/measurement-gdp.md` → `/3102/measurement-gdp` `[pre-migration]`
- [ ] `notes/3102/measurement-gdp.md` → `/notes/3102/measurement-gdp` `[current]`
- Redirect stub: `redirects/3102-measurement-gdp.md`

#### Labor Aggregates
- [ ] `RMWinslow.github.io/3102/measurement-labor.md` → `/3102/measurement-labor` `[pre-migration]`
- [ ] `notes/3102/measurement-labor.md` → `/notes/3102/measurement-labor` `[current]`
- Redirect stub: `redirects/3102-measurement-labor.md`

#### Money Concepts
- [ ] `RMWinslow.github.io/3102/measurement-money.md` → `/3102/measurement-money` `[pre-migration]`
- [ ] `notes/3102/measurement-money.md` → `/notes/3102/measurement-money` `[current]`
- Redirect stub: `redirects/3102-measurement-money.md`

#### Prices
- [ ] `RMWinslow.github.io/3102/measurement-prices.md` → `/3102/measurement-prices` `[pre-migration]`
- [ ] `notes/3102/measurement-prices.md` → `/notes/3102/measurement-prices` `[current]`
- Redirect stub: `redirects/3102-measurement-prices.md`

#### National Savings
- [ ] `RMWinslow.github.io/3102/measurement-savings.md` → `/3102/measurement-savings` `[pre-migration]`
- [ ] `notes/3102/measurement-savings.md` → `/notes/3102/measurement-savings` `[current]`
- Redirect stub: `redirects/3102-measurement-savings.md`

#### Representative Consumer
- [ ] `RMWinslow.github.io/3102/oneperiod-consumer.md` → `/3102/oneperiod-consumer` `[pre-migration]`
- [ ] `notes/3102/oneperiod-consumer.md` → `/notes/3102/oneperiod-consumer` `[current]`
- Redirect stub: `redirects/3102-oneperiod-consumer.md`

#### One Period Equilibrium
- [ ] `RMWinslow.github.io/3102/oneperiod-equilibrium.md` → `/3102/oneperiod-equilibrium` `[pre-migration]`
- [ ] `notes/3102/oneperiod-equilibrium.md` → `/notes/3102/oneperiod-equilibrium` `[current]`
- Redirect stub: `redirects/3102-oneperiod-equilibrium.md`

#### Representative Producer
- [ ] `RMWinslow.github.io/3102/oneperiod-producer.md` → `/3102/oneperiod-producer` `[pre-migration]`
- [ ] `notes/3102/oneperiod-producer.md` → `/notes/3102/oneperiod-producer` `[current]`
- Redirect stub: `redirects/3102-oneperiod-producer.md`

#### Two Period Agents with Production
- [ ] `RMWinslow.github.io/3102/twoperiod-agents.md` → `/3102/twoperiod-agents` `[pre-migration]`
- [ ] `notes/3102/twoperiod-agents.md` → `/notes/3102/twoperiod-agents` `[current]`
- Redirect stub: `redirects/3102-twoperiod-agents.md`

#### Credit Market Imperfections
- [ ] `RMWinslow.github.io/3102/twoperiod-creditfrictions.md` → `/3102/twoperiod-creditfrictions` `[pre-migration]`
- [ ] `notes/3102/twoperiod-creditfrictions.md` → `/notes/3102/twoperiod-creditfrictions` `[current]`
- Redirect stub: `redirects/3102-twoperiod-creditfrictions.md`

#### Two-Period Endowment Economy
- [ ] `RMWinslow.github.io/3102/twoperiod-endowment.md` → `/3102/twoperiod-endowment` `[pre-migration]`
- [ ] `notes/3102/twoperiod-endowment.md` → `/notes/3102/twoperiod-endowment` `[current]`
- Redirect stub: `redirects/3102-twoperiod-endowment.md`
- **Pre-existing redirects:** This page has `redirect_from` in its frontmatter
  covering three legacy URLs: `/twoperiod-consumer/`, `/3102/twoperiod-consumer/`,
  and `/twoperiod-consumer`. These need to be preserved — either keep them in
  the notes repo's frontmatter (to redirect within the notes site) or add
  stubs here for each. Since the old URLs are on the main domain, stubs here
  are needed:
  - `redirects/twoperiod-consumer.md` (permalink: `/twoperiod-consumer` → `/notes/3102/twoperiod-endowment`)
  - `redirects/3102-twoperiod-consumer.md` (permalink: `/3102/twoperiod-consumer` → `/notes/3102/twoperiod-endowment`)

#### Two Period Equilibrium
- [ ] `RMWinslow.github.io/3102/twoperiod-equilibrium.md` → `/3102/twoperiod-equilibrium` `[pre-migration]`
- [ ] `notes/3102/twoperiod-equilibrium.md` → `/notes/3102/twoperiod-equilibrium` `[current]`
- Redirect stub: `redirects/3102-twoperiod-equilibrium.md`

#### Exchange Rates
- [ ] `RMWinslow.github.io/3102/twoperiod-exchangerates.md` → `/3102/twoperiod-exchangerates` `[pre-migration]`
- [ ] `notes/3102/twoperiod-exchangerates.md` → `/notes/3102/twoperiod-exchangerates` `[current]`
- Redirect stub: `redirects/3102-twoperiod-exchangerates.md`

#### Social Security
- [ ] `RMWinslow.github.io/3102/twoperiod-socialsecurity.md` → `/3102/twoperiod-socialsecurity` `[pre-migration]`
- [ ] `notes/3102/twoperiod-socialsecurity.md` → `/notes/3102/twoperiod-socialsecurity` `[current]`
- Redirect stub: `redirects/3102-twoperiod-socialsecurity.md`

#### Small Open Economy
- [ ] `RMWinslow.github.io/3102/twoperiod-soe.md` → `/3102/twoperiod-soe` `[pre-migration]`
- [ ] `notes/3102/twoperiod-soe.md` → `/notes/3102/twoperiod-soe` `[current]`
- Redirect stub: `redirects/3102-twoperiod-soe.md`

#### Money and Business Cycles
- [ ] `RMWinslow.github.io/3102/twoperiod-stickyprices.md` → `/3102/twoperiod-stickyprices` `[pre-migration]`
- [ ] `notes/3102/twoperiod-stickyprices.md` → `/notes/3102/twoperiod-stickyprices` `[current]`
- Redirect stub: `redirects/3102-twoperiod-stickyprices.md`

### Nav-hidden pages

These are excluded from the nav tree but still served. They need redirect
stubs if anyone has bookmarked or linked to them.

#### 3102 Graphs (kgjs)
- [ ] `RMWinslow.github.io/3102/graphs.md` → `/3102/graphs` `[pre-migration]`
- [ ] `notes/3102/graphs.md` → `/notes/3102/graphs` `[current]`
- Redirect stub: `redirects/3102-graphs.md`
- nav_exclude: true

#### 3102 Graphs (Highcharts, old)
- [ ] `RMWinslow.github.io/3102/graphs2.md` → `/3102/graphs2` `[pre-migration]`
- [ ] `notes/3102/graphs2.md` → `/notes/3102/graphs2` `[current]`
- Redirect stub: `redirects/3102-graphs2.md`
- nav_exclude: true

#### Money Slides
- [ ] `RMWinslow.github.io/3102/measurement-money-slides.md` → `/3102/measurement-money-slides` `[pre-migration]`
- [ ] `notes/3102/measurement-money-slides.md` → `/notes/3102/measurement-money-slides` `[current]`
- Redirect stub: `redirects/3102-measurement-money-slides.md`
- nav_exclude: true, uses remark_slides layout

### Pages not migrating to notes

#### Econ Electives
- [ ] `RMWinslow.github.io/econ/UMNelectives.md` → `/econ/UMNelectives`
- nav_exclude: true. Robert is no longer at UMN. This page stays in the main
  repo, hidden from nav. No redirect needed.

### Underscore-prefixed files (excluded from Jekyll build, no redirect stubs)

Jekyll ignores files starting with `_` by default — they are never built into
pages, so they have no URLs to redirect from. These are tracked here for
migration completeness. In the notes repo, they can be renamed (dropping the
underscore) once they're ready to be published as real pages.

#### Competitive Equilibrium (`_equilibrium.md`)
- [ ] `RMWinslow.github.io/3102/_equilibrium.md` — not built `[pre-migration]`
- [ ] `notes/3102/_equilibrium.md` — not built `[current]`
- has_children: true (phantom — children to be wired up post-migration)

#### Aggregate Measurement (`_measurement.md`)
- [ ] `RMWinslow.github.io/3102/_measurement.md` — not built `[pre-migration]`
- [ ] `notes/3102/_measurement.md` — not built `[current]`
- has_children: true (phantom — children to be wired up post-migration)

#### Balance of Payment (`_bop.md`)
- [ ] `RMWinslow.github.io/3102/_bop.md` — not built `[pre-migration]`
- [ ] `notes/3102/_bop.md` — not built `[current]`

#### Money (`_money.md`)
- [ ] `RMWinslow.github.io/3102/_money.md` — not built `[pre-migration]`
- [ ] `notes/3102/_money.md` — not built `[current]`

#### _solow.md
- [ ] `RMWinslow.github.io/3102/_solow.md` — not built `[pre-migration]`
- [ ] `notes/3102/_solow.md` — not built `[current]`
- No YAML frontmatter at all — just a raw link dump.

### Asset directories (move with content, no redirect stubs needed)

These directories contain images, data files, and interactive HTML that are
referenced by the pages above. They move to the notes repo alongside the
markdown files.

- `3102/graphs/` — 10 YML config files for kgjs interactive graphs
- `3102/highcharts/` — 9 HTML files + 4 images for Highcharts graphs
- `3102/img-money/` — 17 images for the money concepts page
- `3102/img-*.png`, `3102/img-*.svg`, `3102/img-*.webp` — loose images
- `3102/python graphs/` — CSV data and Python scripts for generating figures
- `3102/Ponzi.pdf` — PDF referenced by one of the pages

---

## Summary counts

- **Total redirect stubs to create:** 26
  - 20 content pages
  - 1 parent page (topic-overview)
  - 3 nav-hidden pages (graphs, graphs2, money slides)
  - 2 legacy alias stubs (twoperiod-consumer variants)
- **Underscore-prefixed files (no stubs):** 5 (not built by Jekyll)
- **Pages staying in main repo:** 1 (UMN Electives)
- **Notes top-level:** 1 (likely no stub needed — verify during migration)
- **Asset files moving with content:** 72 (no stubs needed)
