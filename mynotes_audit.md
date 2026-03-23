---
nav_exclude: true
search_exclude: true
---

# mynotes Repo Audit (2026-03-22)

Audit of the `mynotes` repository at `C:\Users\RMW\Documents\GitHub\mynotes`.

## Deployment

- **Live URL:** <https://www.rmwinslow.com/mynotes/> (confirmed live)
- **`_config.yml` claims:** `url: https://www.robertmwinslow.com`,
  `baseurl: /notes` — but `robertmwinslow.com` does not resolve. The site is
  actually served at `rmwinslow.com/mynotes/` via GitHub Pages' default
  subdirectory deployment (repo name = `mynotes`, GitHub user = `RMWinslow`).
- **No CNAME file** in the repo.
- **Remote:** `https://github.com/RMWinslow/mynotes.git`
- **Branch:** master

## Theme and Dependencies

- **Theme:** minimal-mistakes (remote theme: `mmistakes/minimal-mistakes`)
- **Skin:** "dirt"
- **Math rendering:** KaTeX via CDN (in `_includes/head.html`)
- **Search:** jekyll-algolia
- **Plugins:** jekyll-paginate, jekyll-sitemap, jekyll-gist, jekyll-feed,
  jemoji, jekyll-include-cache, jekyll-algolia

## Site Description

Title is "Robbie's Notes." The about page describes it as "very sloppy notes
on things I've read or watched" — a searchable personal note-taking system
rather than a blog. Content is primarily economics research notes, workshop
notes, academic paper readings, and general educational material from
Robert's time at UMN (2020–2021).

## Directory Structure

```
mynotes/
├── _config.yml
├── Gemfile
├── README.md
├── index.html              (minimal-mistakes home layout)
├── goodness.md             (page about writing good papers)
├── goodness (2).md         (accidental duplicate)
├── _data/
│   └── navigation.yml
├── _includes/
│   ├── head.html           (KaTeX setup)
│   ├── footer.html
│   └── navigation.yml      (unused?)
├── _hidden/
│   └── 2020-10-16-latour-tuberculosis.md
├── _examples/              (9 template files from minimal-mistakes, not active)
├── _pages/
│   ├── 404.md
│   ├── about.md
│   ├── category-archive.md
│   ├── goodness.md         (third copy?)
│   ├── tag-archive.md
│   └── year-archive.md
├── _posts/                 (91 files across 7 subdirectories)
│   ├── class/     (15)
│   ├── journal/   (10)
│   ├── mynotes/    (7)
│   ├── online/    (42)
│   ├── talk/      (10)
│   ├── textbook/   (4)
│   └── youtube/    (3)
└── img/                    (11 files, including orphan "New Text Document.txt")
```

## Navigation

From `_data/navigation.yml`:
- Posts (`/posts/`)
- Categories (`/categories/`)
- Tags (`/tags/`)
- About (`/about/`)

## Content Inventory: _posts/ (91 files)

Posts are organized by category, which reflects the source type (lecture notes,
journal paper readings, online article notes, etc.). Each post uses the date
in the filename for chronological ordering.

### class/ (15 posts) — Lecture and workshop notes

| File | Title | Tags |
|------|-------|------|
| `2020-09-28-fatih.md` | Econ 8192 | machine learning, econ 8192 |
| `2020-10-20-micro-theory-workshop.md` | rahman | micro, theory |
| `2021-2-1-cristianels.md` | Cristian ELS estimators | workshop, els, stats |
| `2021-2-1-fatih-feb.md` | ELS february notes | fatih, money, learning |
| `2021-2-15-mahdi-ai.md` | Mahdi Data Economy | AI, business |
| `2021-2-16-pickens-unions-.md` | pickens unions talk | micro theory workshop, labor |
| `2021-2-22-fatih-feb-.md` | Bassler Structural Transformation Subsaharan Africa | growth, population, agriculture |
| `2021-2-8-fatih-skewness.md` | Fatih Rene Leon Skewness | macro workshop, learning |
| `2021-3-1-fatih-mar.md` | Automation and Jobs class | ai, automation |
| `2021-3-12-paper-ideas.md` | rahman advice | *(none)* |
| `2021-3-22-fatihwalmart.md` | Walmart expansion | *(none)* |
| `2021-3-8-tomasrosefatih.md` | Credit and Labor market frictions | labor market frictions |
| `2021-4-19-fatih-optimization.md` | Fatih Lecture 5 Optimization | workshop, computation, optimization |
| `2021-4-26-fapr.md` | fatihapril26 | class |
| `2021-5-3-moser-fatih.md` | Sean Bassler and Rene Leon presentations | workshop |

### journal/ (10 posts) — Academic paper reading notes

| File | Title | Tags |
|------|-------|------|
| `2020-09-23-vnm-aumann.md` | Von Neumann-Morgenstern Solutions to Cooperative Games Without Side Payments | Aumann, Peleg, game theory |
| `2020-09-24-gul-dissapointment.md` | A Theory of Disappointment Aversion | Gul, preferences, risk |
| `2020-09-25-superspreading-variation.md` | Superspreading and the effect of individual variation on disease emergence | disease, risk, contagion, superspreading |
| `2020-09-28-network-sars.md` | Network theory and SARS: predicting outbreak diversity | disease, contagion, networks |
| `2020-09-29-social-mixing-disease.md` | Social Contacts and Mixing Patterns Relevant to the Spread of Infectious Diseases | disease, contagion, population |
| `2020-09-29-variation-herdimmunity.md` | Individual variation in susceptibility or exposure to SARS-CoV-2 lowers the herd immunity threshold | disease, contagion |
| `2020-10-18-voluntary-testing-isolation.md` | A Theory of Voluntary Testing and Self-isolation in an Ongoing Pandemic | disease, contagion, behavior |
| `2021-3-11-fertilitymortalitymigration.md` | Fertility, mortality, migration | demographics, forecasting, health |
| `2021-3-19-coolsmart.md` | Cool to be smart smart to be cool | decision theory, signalling |
| `2021-3-25-kremeraids.md` | *(title not captured)* | *(tags not captured)* |

### mynotes/ (7 posts) — Personal research notes and projects

| File | Title | Tags |
|------|-------|------|
| `2020-10-23-infection-distribution.md` | *(not captured)* | *(not captured)* |
| `2021-2-21-poisson-games.md` | *(not captured)* | *(not captured)* |
| `2021-4-20-regbugs.md` | *(not captured)* | *(not captured)* |
| `2021-6-7-naturalmagic.md` | *(not captured)* | *(not captured)* |
| `2021-7-19-onion.md` | *(not captured)* | *(not captured)* |
| `2021-7-20-mapcopy.md` | *(not captured)* | *(not captured)* |
| *(1 additional file)* | | |

### online/ (42 posts) — Notes from online articles and resources

| File | Title | Tags |
|------|-------|------|
| `2020-09-25-cochrane-writing-tips.md` | Cochrane writing tips | writing, research |
| `2020-09-27-branching-problem.md` | *(not captured)* | |
| `2020-10-06-remembering.md` | *(not captured)* | |
| `2020-10-10-phdstudent.md` | *(not captured)* | |
| `2020-10-15-common-metals.md` | *(not captured)* | |
| `2020-10-16-atlantic-k.md` | *(not captured)* | |
| `2020-10-16-cdc-terms.md` | *(not captured)* | |
| `2020-10-23-gradhacker-productivity.md` | *(not captured)* | |
| `2020-10-23-townsend-ledgers-article.md` | *(not captured)* | |
| `2020-10-28-p-addic.md` | *(not captured)* | |
| `2020-11-1-bea-2020-q3-gdp.md` | *(not captured)* | |
| `2020-11-12-ceres.md` | *(not captured)* | |
| `2020-11-4-how-read-paper.md` | *(not captured)* | |
| `2020-11-4-reading-scientific-papers.md` | *(not captured)* | |
| `2020-12-15-hotplate.md` | *(not captured)* | |
| `2020-12-19-trade-and-textbook.md` | *(not captured)* | |
| `2020-12-9-water.md` | *(not captured)* | |
| `2021-01-05-vaccination.md` | *(not captured)* | |
| `2021-2-12-colors.md` | *(not captured)* | |
| `2021-2-13-color-names.md` | *(not captured)* | |
| `2021-2-14-egypt-soul.md` | *(not captured)* | |
| `2021-2-19-cie-uv.md` | *(not captured)* | |
| `2021-2-22-how-to-give-seminar-talk.md` | *(not captured)* | teaching, advice |
| `2021-2-23-griddy.md` | *(not captured)* | |
| `2021-2-28-malaria.md` | *(not captured)* | |
| `2021-2-9-speech-selection.md` | *(not captured)* | |
| `2021-3-14-inkscape-qgis.md` | *(not captured)* | |
| `2021-3-23-notes-from-reading-about-farming-collectives-on-wikipedia.md` | *(not captured)* | |
| `2021-3-6-hurricane.md` | *(not captured)* | |
| `2021-3-7-uncertainty.md` | *(not captured)* | |
| `2021-4-19-nuclear-flop.md` | Why has nuclear power been a flop | energy, environment, nuclear |
| `2021-4-22-peqmas.md` | Thanksgiving and the Pequot massacre | history |
| `2021-4-24-umnlinux.md` | UMN banned from Linux kernel | computer, ethics, code |
| `2021-5-10-publicdomain.md` | Public Domain years | copyright, images, resources |
| `2021-5-12-asset-madoff.md` | Civil Asset Forfeiture and Madoff | police, money, ponzi |
| `2021-5-5-palstic.md` | plastic waste | plastic, environment |
| `2021-8-4-pandoc.md` | pandoc command reference | reference, pandoc, pdf |
| *(~5 additional files)* | | |

### talk/ (10 posts) — Seminar and conference talk notes

| File | Title | Tags |
|------|-------|------|
| `2020-09-01-archive.md` | Old Talk notes from the previous repo | health, math, risk |
| `2020-10-01-ConorRyan-cost-sharing.md` | Conor Ryan Insurance Competition and Health Consumption | medicare, insurance, health |
| `2021-01-13-marriage.md` | Davide Alonzo on migration and marriage | marriage, migration, inequality |
| `2021-09-07-bankruns.md` | Javier Bianchi - Bank runs, fragility, and credit easing | finance, banking |
| `2021-1-19-rahmanintro.md` | Spr 2021 Rahman Martingales' shadow prices | micro, workshop |
| `2021-1-25-fatih-.md` | Fatih trends 2021 | advice, trends, labor |
| `2021-11-23-kodjoml.md` | Kodjo ML | machine learning, workshop |
| `2021-2-4-quant-theory.md` | Two illustrations of the Quantity theory of money | money, macro |
| `2021-3-18-class-intl-inclusive.md` | Strats for making class participation inclusive | teaching, advice |
| `2021-3-31-rdcs.md` | Federal Statistical Research Data Centers | data, research |

### textbook/ (4 posts) — Textbook chapter notes

| File | Title | Tags |
|------|-------|------|
| `2020-10-10-ELS-14.3.md` | ELS 14.3 - Cluster Analysis | Machine Learning, Econ 8791 |
| `2020-10-12-MLAPP-11-24.md` | EM for GMMs and Clustering | Machine Learning, Econ 8791 |
| `2021-2-12-lasso.md` | LASSO | machine learning, statistics |
| `2021-3-16-plantfamilies.md` | Economically Important Plant Families | plants, phylogeny, food |

### youtube/ (3 posts) — Video notes

| File | Title | Tags |
|------|-------|------|
| `2020-09-23-microsoft-how-to-write-paper.md` | How to Write a Great Research Paper | paper writing, advice |
| `2020-10-04-unconventional-jekyll.md` | Unconventional Use Cases For Jekyll | computers, website, github |
| `2020-10-10-plague.md` | Medieval Misconceptions: THE BLACK DEATH | disease, history |

## Other Content Files

| File | Title | Notes |
|------|-------|-------|
| `goodness.md` (root) | What makes a paper good? | Page about writing quality |
| `goodness (2).md` (root) | *(duplicate)* | Windows copy-paste artifact |
| `_pages/goodness.md` | What makes a paper good? | Possible third copy |
| `_hidden/2020-10-16-latour-tuberculosis.md` | Existing and Nonexisting Objects Bruno Latour | Hidden from nav (underscore prefix) |

## Assets

**Images in `img/` (11 files):**
- `bio-photo.jpg` — Author avatar
- `ELS-14.3-normalization.PNG` — Cluster analysis figure
- `ryan-insuranceModel.png`, `ryan-primaryCopays.png`,
  `ryan-specialistCopays.png` — From the Conor Ryan talk notes
- `vectorizediconLinesSMOL.png` — Site logo
- `water-crops.png`, `water-indices.png`, `water-map.png`,
  `water-sources.png`, `water.png` — From the water article notes
- `New Text Document.txt` — Orphaned empty file (should be deleted)

## Issues and Cleanup Candidates

1. **`goodness (2).md`** at the repo root is a Windows copy-paste duplicate.
   Should be deleted.
2. **`New Text Document.txt`** in `img/` is an orphaned empty file. Should be
   deleted.
3. **`_config.yml` URL mismatch** — Claims `url: https://www.robertmwinslow.com`
   but the domain doesn't resolve. The site actually lives at
   `https://www.rmwinslow.com/mynotes/`.
4. **`_examples/` directory** contains 9 template files from the
   minimal-mistakes starter. These are not active content and could be removed.
5. **`_includes/navigation.yml`** appears to be a misplaced copy of the data
   file — `_data/navigation.yml` is the one Jekyll actually reads.
6. **Inconsistent title formatting** — Many post titles are raw shorthand
   (e.g., "fatihapril26", "rahman", "pickens unions talk") rather than
   descriptive titles.
7. **Typo in filename** — `2021-5-5-palstic.md` (should be "plastic").

## Migration Considerations

If this repo is consolidated into the `notes` repo (which uses JTD-RMW):

- **Theme change:** minimal-mistakes → JTD-RMW. Layouts, frontmatter keys,
  and navigation structure will all need to change.
- **Category system:** The current category-based organization (class, journal,
  online, talk, textbook, youtube, mynotes) would need to map to JTD-RMW's
  parent/child nav hierarchy or become `nav_exclude: true` pages with a
  different discovery mechanism.
- **KaTeX → MathJax:** The notes repo uses MathJax; this repo uses KaTeX.
  Any math-heavy posts will need syntax verification (they're mostly
  compatible but not identical).
- **91 posts** is a significant volume. Many are rough notes that may not be
  worth migrating in their current state. A completeness audit would help
  prioritize which posts are worth polishing vs. archiving.
- **Images** would need to move to the notes repo's asset structure.
- **URL preservation** — The current URLs at `rmwinslow.com/mynotes/...`
  would need redirect stubs if anyone has linked to them.
