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

## Pre-migration checklist

Things to do during the migration itself, beyond just moving files and
creating stubs:

- [x] **Rewrite frontmatter hierarchy.** Done 2026-03-19. `topic-overview.md`
  is now a top-level parent (no `parent: Notes`), content pages dropped
  `grand_parent: Notes`, and the phantom parents (`_equilibrium.md`,
  `_measurement.md`) now have `parent: Intermediate Macro Notes`.
- [x] **Remove `redirect_from` from `twoperiod-endowment.md`.** Done
  2026-03-19. The three legacy URLs are handled by redirect stubs in this repo.
- [x] **Create `notes/index.md`.** Done 2026-03-19.
- [x] **Delete `notes.md`** from the main repo. Done 2026-03-19.
- [x] **Update link in `teaching/3102.md`.** Done 2026-03-19. Changed to
  `/notes/302/topic-overview`.
- [x] **Fix hardcoded URL in `measurement-money-slides.md`.** Done 2026-03-19.
  Changed to a relative path (`img-money-snails.webp`).
- [ ] **Fix placeholder in `measurement-gdp.md`** — contains `IMAGEURLHERE`
  as a broken image reference (noted in `claude_audits.md`).
- [ ] **Verify `math: mathjax`** works for all pages. The notes repo config
  sets this site-wide. The graphs pages load KaTeX explicitly — check for
  conflicts post-migration.

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
- [ ] `RMWinslow.github.io/notes_temp.md` → `/notes_temp` (temporary rename for redirect test, 2026-03-19)
- [ ] `RMWinslow.github.io/notes.md` → `/notes` (renamed back, 2026-03-19) `[pre-migration]`
- [ ] `notes/index.md` → `/notes/` `[current]`
- **Not migrated — replaced.** The notes repo deploys at `/notes/` and its own
  `index.md` takes over this URL. During migration, delete `notes.md` from
  the main repo. No redirect stub needed — verify that `/notes` resolves
  correctly once the notes repo is deployed.
- **Content to carry over:** The current `notes.md` says "Here you can find my
  notes on teaching or other economic subjects." The notes repo's `index.md`
  should incorporate this (or an updated version) as its landing page content.

### Parent pages (second level in notes repo)

#### Intermediate Macro Notes
- [ ] `RMWinslow.github.io/3102/topic-overview.md` → `/3102/topic-overview` `[pre-migration]`
- [ ] `notes/302/topic-overview.md` → `/notes/302/topic-overview` `[current]`
- Redirect stub: `redirects/3102-topic-overview.md`
- has_children: true

### Content pages

#### Bank Runs (Diamond-Dybvig)
- [ ] `RMWinslow.github.io/3102/diamond.md` → `/3102/diamond` `[pre-migration]`
- [ ] `notes/302/diamond.md` → `/notes/302/diamond` `[current]`
- Redirect stub: `redirects/3102-diamond.md`

#### McCall Job Search
- [ ] `RMWinslow.github.io/3102/jobsearch.md` → `/3102/jobsearch` `[pre-migration]`
- [ ] `notes/302/jobsearch.md` → `/notes/302/jobsearch` `[current]`
- Redirect stub: `redirects/3102-jobsearch.md`

#### Constrained Optimization
- [ ] `RMWinslow.github.io/3102/math-lagrangian.md` → `/3102/math-lagrangian` `[pre-migration]`
- [ ] `notes/302/math-lagrangian.md` → `/notes/302/math-lagrangian` `[current]`
- Redirect stub: `redirects/3102-math-lagrangian.md`

#### Business Cycles
- [ ] `RMWinslow.github.io/3102/measurement-cylical.md` → `/3102/measurement-cylical` `[pre-migration]`
- [ ] `notes/302/measurement-cylical.md` → `/notes/302/measurement-cylical` `[current]`
- Redirect stub: `redirects/3102-measurement-cylical.md`

#### Gross Domestic Product
- [ ] `RMWinslow.github.io/3102/measurement-gdp.md` → `/3102/measurement-gdp` `[pre-migration]`
- [ ] `notes/302/measurement-gdp.md` → `/notes/302/measurement-gdp` `[current]`
- Redirect stub: `redirects/3102-measurement-gdp.md`

#### Labor Aggregates
- [ ] `RMWinslow.github.io/3102/measurement-labor.md` → `/3102/measurement-labor` `[pre-migration]`
- [ ] `notes/302/measurement-labor.md` → `/notes/302/measurement-labor` `[current]`
- Redirect stub: `redirects/3102-measurement-labor.md`

#### Money Concepts
- [ ] `RMWinslow.github.io/3102/measurement-money.md` → `/3102/measurement-money` `[pre-migration]`
- [ ] `notes/302/measurement-money.md` → `/notes/302/measurement-money` `[current]`
- Redirect stub: `redirects/3102-measurement-money.md`

#### Prices
- [ ] `RMWinslow.github.io/3102/measurement-prices.md` → `/3102/measurement-prices` `[pre-migration]`
- [ ] `notes/302/measurement-prices.md` → `/notes/302/measurement-prices` `[current]`
- Redirect stub: `redirects/3102-measurement-prices.md`

#### National Savings
- [ ] `RMWinslow.github.io/3102/measurement-savings.md` → `/3102/measurement-savings` `[pre-migration]`
- [ ] `notes/302/measurement-savings.md` → `/notes/302/measurement-savings` `[current]`
- Redirect stub: `redirects/3102-measurement-savings.md`

#### Representative Consumer
- [ ] `RMWinslow.github.io/3102/oneperiod-consumer.md` → `/3102/oneperiod-consumer` `[pre-migration]`
- [ ] `notes/302/oneperiod-consumer.md` → `/notes/302/oneperiod-consumer` `[current]`
- Redirect stub: `redirects/3102-oneperiod-consumer.md`

#### One Period Equilibrium
- [ ] `RMWinslow.github.io/3102/oneperiod-equilibrium.md` → `/3102/oneperiod-equilibrium` `[pre-migration]`
- [ ] `notes/302/oneperiod-equilibrium.md` → `/notes/302/oneperiod-equilibrium` `[current]`
- Redirect stub: `redirects/3102-oneperiod-equilibrium.md`

#### Representative Producer
- [ ] `RMWinslow.github.io/3102/oneperiod-producer.md` → `/3102/oneperiod-producer` `[pre-migration]`
- [ ] `notes/302/oneperiod-producer.md` → `/notes/302/oneperiod-producer` `[current]`
- Redirect stub: `redirects/3102-oneperiod-producer.md`

#### Two Period Agents with Production
- [ ] `RMWinslow.github.io/3102/twoperiod-agents.md` → `/3102/twoperiod-agents` `[pre-migration]`
- [ ] `notes/302/twoperiod-agents.md` → `/notes/302/twoperiod-agents` `[current]`
- Redirect stub: `redirects/3102-twoperiod-agents.md`

#### Credit Market Imperfections
- [ ] `RMWinslow.github.io/3102/twoperiod-creditfrictions.md` → `/3102/twoperiod-creditfrictions` `[pre-migration]`
- [ ] `notes/302/twoperiod-creditfrictions.md` → `/notes/302/twoperiod-creditfrictions` `[current]`
- Redirect stub: `redirects/3102-twoperiod-creditfrictions.md`

#### Two-Period Endowment Economy
- [ ] `RMWinslow.github.io/3102/twoperiod-endowment.md` → `/3102/twoperiod-endowment` `[pre-migration]`
- [ ] `notes/302/twoperiod-endowment.md` → `/notes/302/twoperiod-endowment` `[current]`
- Redirect stub: `redirects/3102-twoperiod-endowment.md`
- **Pre-existing redirects:** This page has `redirect_from` in its frontmatter
  covering three legacy URLs: `/twoperiod-consumer/`, `/3102/twoperiod-consumer/`,
  and `/twoperiod-consumer`. These need to be preserved — either keep them in
  the notes repo's frontmatter (to redirect within the notes site) or add
  stubs here for each. Since the old URLs are on the main domain, stubs here
  are needed:
  - `redirects/twoperiod-consumer.md` (permalink: `/twoperiod-consumer` → `/notes/302/twoperiod-endowment`)
  - `redirects/3102-twoperiod-consumer.md` (permalink: `/3102/twoperiod-consumer` → `/notes/302/twoperiod-endowment`)

#### Two Period Equilibrium
- [ ] `RMWinslow.github.io/3102/twoperiod-equilibrium.md` → `/3102/twoperiod-equilibrium` `[pre-migration]`
- [ ] `notes/302/twoperiod-equilibrium.md` → `/notes/302/twoperiod-equilibrium` `[current]`
- Redirect stub: `redirects/3102-twoperiod-equilibrium.md`

#### Exchange Rates
- [ ] `RMWinslow.github.io/3102/twoperiod-exchangerates.md` → `/3102/twoperiod-exchangerates` `[pre-migration]`
- [ ] `notes/302/twoperiod-exchangerates.md` → `/notes/302/twoperiod-exchangerates` `[current]`
- Redirect stub: `redirects/3102-twoperiod-exchangerates.md`

#### Social Security
- [ ] `RMWinslow.github.io/3102/twoperiod-socialsecurity.md` → `/3102/twoperiod-socialsecurity` `[pre-migration]`
- [ ] `notes/302/twoperiod-socialsecurity.md` → `/notes/302/twoperiod-socialsecurity` `[current]`
- Redirect stub: `redirects/3102-twoperiod-socialsecurity.md`

#### Small Open Economy
- [ ] `RMWinslow.github.io/3102/twoperiod-soe.md` → `/3102/twoperiod-soe` `[pre-migration]`
- [ ] `notes/302/twoperiod-soe.md` → `/notes/302/twoperiod-soe` `[current]`
- Redirect stub: `redirects/3102-twoperiod-soe.md`

#### Money and Business Cycles
- [ ] `RMWinslow.github.io/3102/twoperiod-stickyprices.md` → `/3102/twoperiod-stickyprices` `[pre-migration]`
- [ ] `notes/302/twoperiod-stickyprices.md` → `/notes/302/twoperiod-stickyprices` `[current]`
- Redirect stub: `redirects/3102-twoperiod-stickyprices.md`

### Nav-hidden pages

These are excluded from the nav tree but still served. They need redirect
stubs if anyone has bookmarked or linked to them.

#### 302 Graphs (kgjs)
- [ ] `RMWinslow.github.io/3102/graphs.md` → `/3102/graphs` `[pre-migration]`
- [ ] `notes/302/graphs.md` → `/notes/302/graphs` `[current]`
- Redirect stub: `redirects/3102-graphs.md`
- nav_exclude: true

#### 302 Graphs (Highcharts, old)
- [ ] `RMWinslow.github.io/3102/graphs2.md` → `/3102/graphs2` `[pre-migration]`
- [ ] `notes/302/graphs2.md` → `/notes/302/graphs2` `[current]`
- Redirect stub: `redirects/3102-graphs2.md`
- nav_exclude: true

#### Money Slides
- [ ] `RMWinslow.github.io/3102/measurement-money-slides.md` → `/3102/measurement-money-slides` `[pre-migration]`
- [ ] `notes/302/measurement-money-slides.md` → `/notes/302/measurement-money-slides` `[current]`
- Redirect stub: `redirects/3102-measurement-money-slides.md`
- nav_exclude: true, uses remark_slides layout
- **Post-migration fix needed:** Contains one hardcoded absolute URL
  (`https://www.rmwinslow.com/3102/img-money-snails.webp`) that will need
  updating to a relative path or the new `/notes/` prefix.

### Pages migrated on 2026-03-20

#### The Costs of Inflation
- [ ] `RMWinslow.github.io/202/inflation-costs.md` → `/202/inflation-costs` `[pre-migration]`
- [ ] `notes/202/inflation-costs.md` → `/notes/202/inflation-costs` `[current]`
- Redirect stub: `redirects/202-inflation-costs.md`
- The only content page from the 202 (Principles of Macro) section.

### Pending: full `econ/` migration to notes repo

All files below will move to the notes repo. Redirect stubs will be created
for every HTML and MD content file. Assets (images, SVGs, LyX files, Excel
files) move with their parent pages but don't need individual redirect stubs.

#### `econ/UMNelectives.md`
- `/econ/UMNelectives` → redirect stub needed
- Jekyll markdown page, nav_exclude: true.

#### `econ/teaching/typesetting/` (3 HTML + 5 PNG)
- `/econ/teaching/typesetting/latexMath.html` → redirect stub needed
- `/econ/teaching/typesetting/lyxTutorial.html` → redirect stub needed
- `/econ/teaching/typesetting/typesettingSoftware.html` → redirect stub needed
- Assets: 5 PNGs (MSWordEqn, MSWordMathMode, lyxEnvironments, lyxEqn, lyxMathMode)
- Note: `econ/teaching/3102/typesetting/` also has copies of the same 5 PNGs;
  those are orphaned now that the duplicate HTML files have been deleted.

#### `econ/teaching/3012.html`
- `/econ/teaching/3012.html` → redirect stub needed
- Likely a typo for 3102. Single standalone file.

#### `econ/teaching/3102/equilibrium/` (5 HTML + 2 PNG)
- `/econ/teaching/3102/equilibrium/consumer.html` → redirect stub needed
- `/econ/teaching/3102/equilibrium/consumerInteractive.html` → redirect stub needed
- `/econ/teaching/3102/equilibrium/equilibrium.html` → redirect stub needed
- `/econ/teaching/3102/equilibrium/firm.html` → redirect stub needed
- `/econ/teaching/3102/equilibrium/solving.html` → redirect stub needed
- Assets: bigE.png, star.png

#### `econ/teaching/3102/interactive/` (10 HTML + 4 PNG)
- `/econ/teaching/3102/interactive/ConsumerAndProducerInteractive.html` → redirect stub needed
- `/econ/teaching/3102/interactive/OnePeriodEquilibiriumInteractive.html` → redirect stub needed
- `/econ/teaching/3102/interactive/consumerInteractive.html` → redirect stub needed
- `/econ/teaching/3102/interactive/exampleInteractive.html` → redirect stub needed
- `/econ/teaching/3102/interactive/interactivegraphs.html` → redirect stub needed
- `/econ/teaching/3102/interactive/producerInteractive.html` → redirect stub needed
- `/econ/teaching/3102/interactive/solowInteractive.html` → redirect stub needed
- `/econ/teaching/3102/interactive/twoPeriodEndowment.html` → redirect stub needed
- `/econ/teaching/3102/interactive/twoPeriodEndowmentWithBorrowingLimits.html` → redirect stub needed
- `/econ/teaching/3102/interactive/twoPeriodEndowmentWithDifferentRates.html` → redirect stub needed
- Assets: bigE.png, smallE.png, star.png, star2.png

#### `econ/teaching/3102/intertemporal/` (6 HTML + 8 SVG + 1 PNG + 1 PY)
- `/econ/teaching/3102/intertemporal/consumerProblemWithLabor.html` → redirect stub needed
- `/econ/teaching/3102/intertemporal/creditFrictions.html` → redirect stub needed
- `/econ/teaching/3102/intertemporal/firmProblem.html` → redirect stub needed
- `/econ/teaching/3102/intertemporal/intertemporalCE_Definiton.html` → redirect stub needed
- `/econ/teaching/3102/intertemporal/shifterExamples.html` → redirect stub needed
- `/econ/teaching/3102/intertemporal/twoPeriodEndowment.html` → redirect stub needed
- Assets: images/ (8 SVGs), bigE.png, star.png, pythonhLaborCurveGenerator.py

#### `econ/teaching/3102/test/` (4 HTML + 2 PNG)
- `/econ/teaching/3102/test/CEInteractive.html` → redirect stub needed
- `/econ/teaching/3102/test/consumerInteractive.html` → redirect stub needed
- `/econ/teaching/3102/test/exampleInteractive.html` → redirect stub needed
- `/econ/teaching/3102/test/producerInteractive.html` → redirect stub needed
- Assets: bigE.png, star.png

#### `econ/teaching/3102psets/` (6 HTML + many SVG + 2 XLSX)
- `/econ/teaching/3102psets/HW1_dataGraphs.html` → redirect stub needed
- `/econ/teaching/3102psets/HW2_dataGraphs.html` → redirect stub needed
- `/econ/teaching/3102psets/HWBCycles_old/dataResultsFlippedPercentDiff.html` → redirect stub needed
- `/econ/teaching/3102psets/HWBCycles_old/dataResultsOG.html` → redirect stub needed
- `/econ/teaching/3102psets/HWBCycles_old/dataResultsOnlyImages.html` → redirect stub needed
- `/econ/teaching/3102psets/HWBCycles_old/week9solutions.html` → redirect stub needed
- Assets: HW1_GrowthGraphs/ (60 SVGs), HW2_BCycleGraphs/ (60 SVGs),
  HWBCycles_old/ (72 SVGs + 2 XLSX)

#### `econ/macroprelim/` (12 HTML + 11 PNG)
- `/econ/macroprelim/prelimindex.html` → redirect stub needed
- `/econ/macroprelim/roadmapTODO.html` → redirect stub needed
- `/econ/macroprelim/Chari/privatemoney.html` → redirect stub needed
- `/econ/macroprelim/Chari/productionrisk.html` → redirect stub needed
- `/econ/macroprelim/Chari/sustainabledebt.html` → redirect stub needed
- `/econ/macroprelim/Concepts/envelope.html` → redirect stub needed
- `/econ/macroprelim/Concepts/flowchartkey/FlowChartKey.html` → redirect stub needed
- `/econ/macroprelim/Jones/HumanCapital.html` → redirect stub needed
- `/econ/macroprelim/Jones/dynamicprogramming.html` → redirect stub needed
- `/econ/macroprelim/Kehoe/Search.html` → redirect stub needed
- `/econ/macroprelim/Kehoe/crossingProof.html` → redirect stub needed
- `/econ/macroprelim/Kehoe/dp.html` → redirect stub needed
- Assets: Chari/FriedmanRule.png, Concepts/flowchartkey/ (6 PNGs),
  Kehoe/ (KehoeSearchLabels.png, laser1-3.png)

#### `econ/tradeprelim/` (15 HTML + 3 LyX + 3 LyX~)
- `/econ/tradeprelim/prelimindex.html` → redirect stub needed
- `/econ/tradeprelim/amador/multipleborrowers.html` → redirect stub needed
- `/econ/tradeprelim/fitzgerald/armingtongravity.html` → redirect stub needed
- `/econ/tradeprelim/fitzgerald/melitzottaviano.html` → redirect stub needed
- `/econ/tradeprelim/fitzgerald/melitzottaviano/melitzottaviano.html` → redirect stub needed
- `/econ/tradeprelim/fitzgerald/melitzottaviano_problem.html` → redirect stub needed
- `/econ/tradeprelim/fitzgerald/melitzottaviano_solution.html` → redirect stub needed
- `/econ/tradeprelim/kehoe/LBD/LBDconcepts.html` → redirect stub needed
- `/econ/tradeprelim/kehoe/LBD/LBDprelim.html` → redirect stub needed
- `/econ/tradeprelim/kehoe/LBD/LBDprelimSolutionA.html` → redirect stub needed
- `/econ/tradeprelim/kehoe/hecksherohlin.html` → redirect stub needed
- `/econ/tradeprelim/kehoe/learningbydoing.html` → redirect stub needed
- `/econ/tradeprelim/kehoe/monopolisticcompetition.html` → redirect stub needed
- `/econ/tradeprelim/kehoe/self-fulfillingdebt.html` → redirect stub needed
- Note: `econ/tradeprelim/kehoe/LBD/` was listed as 3 HTML in the earlier
  exploration but there are actually 3 HTML files plus LyX working files.
- Assets: LyX files (amador/EatonG notes.lyx, fitzgerald/mellitz work.lyx,
  kehoe/debtcrisiswork.lyx, kehoe/hecksherwork.lyx) and LyX backup files

#### `econ/nonsense/mathsymbols.html`
- `/econ/nonsense/mathsymbols.html` → redirect stub needed

#### `econ/presentations/` (2 HTML + many SVG/PNG)
- `/econ/presentations/biglisthtml.html` → redirect stub needed
- `/econ/presentations/percolationSlides.html` → redirect stub needed
- Assets: ~40 SVGs and PNGs (graph theory diagrams for the percolation talk)

---

**Redirect stub count for `econ/` migration:** 66 stubs total
- 1 MD file (UMNelectives)
- 65 HTML files

### Underscore-prefixed files (excluded from Jekyll build, no redirect stubs)

Jekyll ignores files starting with `_` by default — they are never built into
pages, so they have no URLs to redirect from. These are tracked here for
migration completeness. In the notes repo, they can be renamed (dropping the
underscore) once they're ready to be published as real pages.

#### Competitive Equilibrium (`_equilibrium.md`)
- [ ] `RMWinslow.github.io/3102/_equilibrium.md` — not built `[pre-migration]`
- [ ] `notes/302/_equilibrium.md` — not built `[current]`
- has_children: true (phantom — children to be wired up post-migration)

#### Aggregate Measurement (`_measurement.md`)
- [ ] `RMWinslow.github.io/3102/_measurement.md` — not built `[pre-migration]`
- [ ] `notes/302/_measurement.md` — not built `[current]`
- has_children: true (phantom — children to be wired up post-migration)

#### Balance of Payment (`_bop.md`)
- [ ] `RMWinslow.github.io/3102/_bop.md` — not built `[pre-migration]`
- [ ] `notes/302/_bop.md` — not built `[current]`

#### Money (`_money.md`)
- [ ] `RMWinslow.github.io/3102/_money.md` — not built `[pre-migration]`
- [ ] `notes/302/_money.md` — not built `[current]`

#### _solow.md
- [ ] `RMWinslow.github.io/3102/_solow.md` — not built `[pre-migration]`
- [ ] `notes/302/_solow.md` — not built `[current]`
- No YAML frontmatter at all — just a raw link dump.

### Asset directories (move with content, no redirect stubs needed)

These directories contain images, data files, and interactive HTML that are
referenced by the pages above. They move to the notes repo alongside the
markdown files.

- `302/graphs/` — 10 YML config files for kgjs interactive graphs
- `302/highcharts/` — 9 HTML files + 4 images for Highcharts graphs
- `302/img-money/` — 17 images for the money concepts page
- `302/img-*.png`, `302/img-*.svg`, `302/img-*.webp` — loose images
- `302/python graphs/` — CSV data and Python scripts for generating figures
- `302/Ponzi.pdf` — PDF referenced by one of the pages

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
