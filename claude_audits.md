---
nav_exclude: true
search_exclude: true
---

## Audit Results

### Layout usage (2026-03-16)

Counted across all five locally pulled JTD-RMW sites. The `layout: true/false` hits in the raw grep are false positives from Remark slide content (where `layout` is a Remark keyword inside the slide markdown, not Jekyll frontmatter).

**Totals (excluding false positives):**

| Layout | Count | Notes |
|--------|-------|-------|
| `post` | 147 | The workhorse layout, used across all five sites. |
| `game` | 42 | A custom layout defined in the `games` repo's own `_layouts/game.html`. Extends `default`, similar to `post` but adds game-specific metadata (players, equipment) and hides the date line. Also checks `modified` but not the `modified` alias. |
| `remark_slides` | 2 | Both in `RMWinslow.github.io`. |
| `default` | 1 | A single page in `games`. |
| `null` | 1 | A single page in `posts`. |
| `page` / `home` / `about` | 0 | None of the three identical passthrough layouts are used by any consuming site. |

**Per-site breakdown:**

| Site | `post` | `game` | `remark_slides` | `default` | `null` |
|------|--------|--------|-----------------|-----------|--------|
| posts | 74 | — | — | — | 1 |
| RMWinslow.github.io | 48 | — | 2 | — | — |
| bib | 4 | — | — | — | — |
| games | 7 | 42 | — | 1 | — |
| circe | 14 | — | — | — | — |

### Pages without frontmatter (2026-03-16)

Markdown files that don't start with a `---` frontmatter block. Jekyll will still process these, but they'll have no title, no layout, and no metadata — they just get rendered through the default layout as anonymous pages.

| Site | Count | Notes |
|------|-------|-------|
| posts | 33 | Mostly raw data files (BIRDUPraw markdown sources, alphabet book word lists, a LICENSE file). Not intended as pages. |
| RMWinslow.github.io | 2 | A draft Solow model page and a presentation outline. |
| bib | 0 | — |
| games | 1 | A draft (`_drafts/GluestickCombat.md`). |
| circe | 0 | — |

These are mostly data files and drafts, so the lack of frontmatter is not a problem in practice. The raw data markdown files in `posts` could potentially be excluded from the Jekyll build if they're not meant to be served as pages.

### Pages with frontmatter but no layout (2026-03-16)

These pages have a YAML frontmatter block but don't specify a `layout`. Jekyll falls back to `default` for these, which means they get the sidebar and footer chrome but no title header, date line, or TOC.

| Site | Total | `search_exclude` | `nav_exclude` | Both |
|------|-------|-------------------|---------------|------|
| posts | 34 | 3 | 10 | 3 |
| RMWinslow.github.io | 4 | 0 | 1 | 0 |
| bib | 230 | 0 | 0 | 0 |
| games | 23 | 0 | 3 | 0 |
| circe | 1 | 1 | 1 | 1 |

The 230 in `bib` are the bulk of the bibliography — each is a minimal page with just `parent: Other` (or similar) and no explicit layout. They render through `default`, which is fine for their purpose — they're short notes that don't need the `post` layout's title/date header.

In `posts`, 24 of the 34 no-layout pages are neither search-excluded nor nav-excluded, meaning they show up in search and navigation as layout-less pages. These may warrant a closer look.

In `games`, the 23 no-layout pages are likely category index pages (parents) that rely on the `default` layout's automatic child TOC.

**Observations [claude's suggestions]:**
- The `game` layout in the `games` repo is essentially a fork of `post` with added `players`/`equipment` fields and a hidden date line. It could potentially be folded back into JTD-RMW as an official layout, or the `post` layout could be made flexible enough to support the extra fields.
- `page`, `home`, and `about` are never used anywhere. They could be removed from the theme without breaking anything.
- The `game` layout checks for `page.last_modified_date` but not the `modified` alias, matching the same inconsistency as the footer.

### Navigation hierarchy audit (2026-03-16)

Full sitemaps of all five active JTD-RMW sites. Pages marked `[hidden]` have `nav_exclude: true`. Issues marked with a warning.

**posts (blog.rmwinslow.com)**

```
├── Art and Culture
│   ├── Binomial Color Names
│   ├── Isomorphic Keyboards
│   ├── Jianpu
│   │   ├── Christmas Songs
│   │   ├── Jianpu ASCII Font
│   │   ├── Jianpu Key Signatures
│   │   ├── Some Simple Melodies [hidden]
│   │   ├── Stephen Foster's Music
│   │   ├── Tom Lehrer's Songs
│   │   └── Video Game Music [hidden]
│   └── Media Recommendations
│       ├── Discworld Ranking
│       ├── Movies [hidden]
│       ├── SNES Top 100 [hidden]
│       ├── Visual Artists [hidden]  ⚠️ missing grand_parent
│       ├── X in the ABCs  ⚠️ missing grand_parent
│       └── YouTube Channels
├── Econ
│   ├── Childcare Time Use
│   ├── Commuting Correlations [hidden]
│   ├── Econ News Sources [hidden]
│   ├── GDP and Gold Prices [hidden]
│   ├── Government Purchases by Purpose
│   ├── Interesting Examples [hidden]
│   ├── LLMs and Teaching [hidden]
│   ├── Partial UI Thresholds
│   ├── That's Economics (song)
│   ├── Time Use After Covid
│   ├── Working from Home (surgevsdiscounts.md)  ⚠️ DUPLICATE TITLE
│   └── Working from Home (workfromhome.md)  ⚠️ DUPLICATE TITLE
├── Food and Health
│   ├── Baby Tips
│   ├── Fish to Eat When Pregnant
│   └── Lead in Dark Chocolate
├── Language
│   ├── Chinese Characters
│   │   ├── Chinese Element Names
│   │   └── List of Basic Chinese Terms
│   ├── Doctors and Lords
│   ├── Interesting Etymologies
│   ├── Open-source Emojis
│   ├── Patterns in Consonants
│   ├── Prefix-suffix Bicliques
│   ├── Remade Scattergories Dice
│   ├── Unicode Characters [hidden]  ⚠️ HC:true but no children
│   ├── Word Shapes
│   └── Wordle Solutions
├── Links
│   ├── Encabulators
│   ├── Misc Links
│   │   ├── Links - Spring 2017 [hidden]
│   │   ├── Links - September 2017 [hidden]
│   │   ├── Links - October 2017 [hidden]
│   │   ├── Links - Spring 2018 [hidden]
│   │   ├── Links - September 2018 [hidden]
│   │   ├── Links - 2019 [hidden]
│   │   ├── Links - 2020 [hidden]
│   │   ├── Links - 2023 and 2022
│   │   ├── Links - June 2024
│   │   ├── Links - November 2024
│   │   ├── Links - December 2024
│   │   ├── Links - January 2025
│   │   └── Links - April 2025
│   ├── Online Data Sources
│   ├── Sites with Manual html
│   └── Useful Links
├── Maps
│   ├── GIS Maps
│   ├── Maps I Like
│   └── Sister States [hidden]
├── Numbers
│   ├── Every Holiday is Wrong.
│   ├── Horizon Distances
│   ├── Human Energy Units
│   ├── Syllabic Quinary
│   └── Why the Mile is Weird
├── Science and Nature
│   ├── Astro Symbols
│   │   ├── Astro Fonts
│   │   └── Notes on Astro Symbols
│   ├── Calling a Whale a Fish
│   ├── Dual Scale Solar System
│   ├── Element Names
│   ├── New State Birds
│   │   ├── Bird Scores - Informedness
│   │   ├── Bird Scores - Markedness
│   │   ├── Bird Scores - Phi
│   │   ├── Bird Scores - Prevalence
│   │   ├── Bird Scores - Weighted Phi
│   │   └── Photo Credits
│   ├── Notes on Plastics
│   ├── Plant Ranking
│   └── XYX Compounds
├── News [hidden]
├── Home [hidden]
├── Markdown Kitchen Sink [hidden]
├── Christmas Wishlist [hidden]
├── Munsell Test [hidden]
│
│   ⚠️ ORPHANED (parent doesn't match any title):
├── Games Free with Amazon Prime  (parent: "hidden")
├── Novels  (parent: "hidden")
├── NES A-Z  (parent: "Media")
└── Web Fiction  (parent: "_Media")
```

**RMWinslow.github.io (www.rmwinslow.com)**

```
├── CV
├── Research
│   ├── Branching Processes and Behavioral Choice
│   ├── Graph Two-Rankings
│   ├── Job Market Paper
│   └── Predicting Unemployment Status
├── Teaching
│   ├── Econ 3102 (UMN)
│   └── Econ 330
├── Notes
│   ├── Aggregate Measurement  ⚠️ PHANTOM (HC:true, no children)
│   ├── Competitive Equilibrium  ⚠️ PHANTOM (HC:true, no children)
│   ├── Econ Electives
│   ├── Intermediate Macro Notes
│   │   ├── Constrained Optimization
│   │   ├── Gross Domestic Product
│   │   ├── Prices
│   │   ├── National Savings
│   │   ├── Labor Aggregates
│   │   ├── Business Cycles
│   │   ├── Money Concepts
│   │   ├── Representative Consumer
│   │   ├── Representative Producer
│   │   ├── One Period Equilibrium
│   │   ├── McCall Job Search
│   │   ├── Two-Period Endowment Economy
│   │   ├── Credit Market Imperfections
│   │   ├── Social Security
│   │   ├── Two Period Agents with Production
│   │   ├── Two Period Equilibrium
│   │   ├── Money and Business Cycles
│   │   ├── Small Open Economy
│   │   ├── Exchange Rates
│   │   ├── Bank Runs
│   │   ├── Balance of Payment
│   │   ├── Money
│   │   ├── 3102 Graphs [hidden]
│   │   └── 3102 Graphs (Highcharts, old) [hidden]
│   ├── Money and Banking  ⚠️ PHANTOM (HC:true, no children)
│   ├── Principles of Macro
│   │   ├── Balance of Payments
│   │   ├── The AD-AS Model
│   │   └── The Costs of Inflation
│   └── Principles of Micro [hidden]
│       └── Market Equilibrium
├── Econ 330 HW1–HW5 [hidden]
├── Money Slides [hidden]
├── Remark Formatting Test [hidden]
└── Slide Deck Index [hidden]
```

**bib (www.rmwinslow.com/bib)**

```
├── Books (~6 entries, mostly untitled)
├── Collections (1 entry)
├── Other (~15 entries)
│   └── BLS CEX
│       └── Data Dictionary for the BLS CEX
└── Papers (~190 entries, mostly untitled)
(no site index page in nav)
```

**games (www.rmwinslow.com/games)**

```
├── Abstract Games
│   ├── Ayu [hidden]
│   ├── Bug
│   ├── Checkers Etc.
│   ├── Five in a Row
│   ├── Go (Weiqi)
│   ├── Hex / Slither
│   ├── Homeworlds
│   ├── Symple
│   └── Zendo
├── Boardgames
│   ├── Boardgame Collection
│   └── Rules References
│       ├── Cthulhu Wars
│       ├── Gaslands [hidden]
│       └── KTANE
├── Climbing Games
│   ├── Do Dizhu
│   ├── Haggish [hidden]
│   └── Kickball
├── Mahjong Set Games
│   ├── Mahjong Poker
│   ├── Mahjong Solitaire
│   ├── Phase Shí [hidden]
│   └── Simple Mahjong
├── Micro RPGs
│   ├── Honey Heist [hidden]
│   ├── Lasers & Feelings  ⚠️ HC:false but has 3 children
│   │   ├── Scrolls & Swords
│   │   ├── Truth & Daring
│   │   └── Wits & Chivalry
│   ├── Pool Wagering [hidden]
│   └── Roll for Shoes [hidden]
├── Other Card Games
│   ├── 6-Card Golf
│   ├── GoPS
│   ├── Kings Corners
│   ├── Literature [hidden]
│   ├── No Merci!
│   ├── Regicide
│   ├── Reno
│   ├── Skull & Roses
│   ├── Superjack [hidden]
│   ├── Vizzini's Battle of Wits
│   └── Win, Lose, Banana
├── Party Games
│   ├── Fishbowl
│   ├── Telephone Pictionary
│   └── These People Are Lying
├── Poker Hand Games
│   ├── Lamarckian Poker
│   ├── Ocean's Eleven
│   ├── Pyramid Poker
│   └── Ricochet Poker
├── Tools
│   ├── Links to Games
│   ├── Mysterium Park Layout Generator
│   ├── Random Wiki Articles
│   └── Random Word Generator
├── Trick-taking Games
│   ├── Devil's Poker
│   ├── Diamonds [hidden]
│   ├── Fox in the Forest [hidden]
│   ├── Hearts
│   ├── Oh Hell!
│   ├── Ship's Crew
│   │   ├── Mission List
│   │   └── Player Count Variants
│   └── Spades
└── Home [hidden]
```

**circe (www.rmwinslow.com/circe)**

```
├── The Circe (index)
├── Dialogue I. Oister and Mole
├── Dialogue II. The Snake
├── Dialogue III. The Hare
├── Dialogue IV. The Goat
├── Dialogue V. The Hind
├── Dialogue VI. The Lyon
├── Dialogue VII. The Horse
├── Dialogue VIII. The Dog
├── Dialogue IX. The Bullock
├── Dialogue X. The Elephant
├── La Circe — Complete Text [hidden]
├── The Argument [hidden]
├── Title Page [hidden]
└── To the Reader [hidden]
```

**Issues found:**

| # | Site | Issue | Details |
|---|------|-------|---------|
| 1 | posts | Orphaned parent | "Games Free with Amazon Prime" → parent `"hidden"` doesn't exist |
| 2 | posts | Orphaned parent | "Novels" → parent `"hidden"` doesn't exist |
| 3 | posts | Orphaned parent | "NES A-Z" → parent `"Media"` (should be `"Media Recommendations"`) |
| 4 | posts | Orphaned parent | "Web Fiction" → parent `"_Media"` doesn't exist |
| 5 | posts | Duplicate title | Two pages titled "Working from Home" under Econ (`surgevsdiscounts.md` and `workfromhome.md`) |
| 6 | posts | Missing grand_parent | "X in the ABCs" and "Visual Artists" under Media Recommendations lack `grand_parent: Art and Culture` that their siblings have |
| 7 | posts | Phantom parent | "Unicode Characters" has `has_children: true` but no children reference it |
| 8 | RMWinslow.github.io | Phantom parent | "Competitive Equilibrium" has `has_children: true` but no children reference it |
| 9 | RMWinslow.github.io | Phantom parent | "Aggregate Measurement" has `has_children: true` but no children reference it |
| 10 | RMWinslow.github.io | Phantom parent | "Money and Banking" has `has_children: true` but no children reference it |
| 11 | games | Missing HC flag | "Lasers & Feelings" has `has_children: false` but 3 pages reference it as parent |

### Broken internal links audit (2026-03-16)

**circe** — Clean. No broken internal links.

**posts** — 11 broken links:

| Source file | Link target | Issue |
|---|---|---|
| `econ/workfromhome.md` | `wfhimg/plotMinWFH_WFH.png` | File not found; actual file is `plotMinWFH_WFH1.png` (missing "1") |
| `econ/workfromhome.md` | `wfhimg/plotMinWorkWFH.png` | File not found; actual file is `plotMinWorkWFH1.png` (missing "1") |
| `nature/astronotes.md` | `elementasociationtierlist.png` | File not found in `nature/` |
| `nature/astronotes.md` | `elementhex.svg` | File not found in `nature/` |
| `nature/astronotes.md` | `elementhex2.png` | File not found in `nature/` |
| `nature/astronotes.md` | `elementhexplus.png` | File not found in `nature/` |
| `nature/astrosymbols.md` | Same 4 element images | Same missing files as astronotes.md |
| `nature/birdup.md` | `birdup/weightedphi.html` | Resolves to `nature/birdup/birdup/weightedphi.html` — double-nested path |
| `nature/birdup/prevalance.md` | Several `prevalence_*` links | Spelling mismatch (file uses "prevalance", links use "prevalence") + targets are CSVs not pages |
| `media/film.md` | `tt4849438` | Incomplete IMDB link (missing `https://www.imdb.com/title/` prefix) |
| `language/wordshapes/dolph/README.md` | `r` | Broken/placeholder link |

**bib** — 4 broken links:

| Source file | Link target | Issue |
|---|---|---|
| `book/hastie2009elements.md` | `../../img/ELS-14.3-normalization.PNG` | Path goes above repo root |
| `paper/mccall1996unemployment.md` | `JSTOR link` | Reversed markdown syntax `[url](JSTOR link)` |
| `paper/restrepo2020effect.md` | `/restrepo2022work` | Absolute path; file is at `paper/restrepo2022work.md` |
| `zotero/lou2013accurate.md` | `nori2019interpretml` | Resolves to `zotero/`; file is in `paper/` |

**games** — 3 broken links (excluding 2 `.html`→`.md` links that work in practice via Jekyll):

| Source file | Link target | Issue |
|---|---|---|
| `rules/category-party.md` | `./links` | Resolves to `rules/links` but the file is in `tools/links.md` |
| `rules/cardImages.html` | `../../styles/sakura.css` | Path goes above repo root |
| `tools/randomWords.html` | `../styles/everythingbagel.css` | No `styles/` directory in this repo |

**RMWinslow.github.io** — 31 broken links (the largest number, mostly in older HTML files):

| Source file | Link target | Issue |
|---|---|---|
| `index.html` | `/art` | Separate GitHub Pages repo, not a subdirectory of this site |
| `index.html` | `/games` | Same — points to the `games` repo |
| `index.html` | `/posts` | Same — points to the `posts` repo |
| `3102/measurement-gdp.md` | `IMAGEURLHERE` | Placeholder, not a real path |
| `3102/topic-overview.md` | `twoperiod-consumer` | File not found in `3102/` |
| `202/graphs/3102 Graphs - Robert Winslow.html` | `./graphs/onePeriodBothAgents.yml` | Double-nested: resolves to `202/graphs/graphs/...` — not found |
| `202/graphs/3102 Graphs - Robert Winslow.html` | `./graphs/onePeriodProducer.yml` | Same double-nesting issue |
| `202/graphs/3102 Graphs - Robert Winslow.html` | `./graphs/twoPeriodCollateralConstraint.yml` | Same |
| `202/graphs/3102 Graphs - Robert Winslow.html` | `./graphs/twoPeriodEndowment.yml` | Same |
| `202/graphs/3102 Graphs - Robert Winslow.html` | `./graphs/twoPeriodEquilibrium.yml` | Same |
| `202/graphs/3102 Graphs - Robert Winslow.html` | `./graphs/twoPeriodInterestRateSpread.yml` | Same |
| `202/graphs/3102 Graphs - Robert Winslow.html` | `graphs2` | Not found |
| `econ/macroprelim/prelimindex.html` | `../styles/sakura.css` | Wrong relative depth; `styles/sakura.css` exists at site root |
| `econ/macroprelim/Jones/HumanCapital.html` | `../styles/sakura.css` | Same sakura.css issue |
| `econ/macroprelim/Jones/HumanCapital.html` | `../FlowChartKey.html` | Not found; file is in `Concepts/flowchartkey/` |
| `econ/macroprelim/Jones/HumanCapital.html` | `KehoeSearchLabels.png` | Not found in `Jones/` |
| `econ/macroprelim/Jones/HumanCapital.html` | `crossingProof.html` | Not found in `Jones/` |
| `econ/macroprelim/Jones/dynamicprogramming.html` | `../styles/sakura.css` | Same sakura.css issue |
| `econ/macroprelim/Jones/dynamicprogramming.html` | `../FlowChartKey.html` | Same FlowChartKey issue |
| `econ/macroprelim/Jones/dynamicprogramming.html` | `KehoeSearchLabels.png` | Same missing image |
| `econ/macroprelim/Jones/dynamicprogramming.html` | `crossingProof.html` | Same missing file |
| `econ/macroprelim/Kehoe/Search.html` | `../FlowChartKey.html` | Same FlowChartKey issue |
| `econ/macroprelim/Kehoe/dp.html` | `../FlowChartKey.html` | Same |
| `econ/macroprelim/Concepts/flowchartkey/FlowChartKey.html` | `../../styles/sakura.css` | Same sakura.css issue |
| `econ/macroprelim/arrowroot/arrownotes.html` | `../styles/sakura.css` | Same |
| `econ/macroprelim/arrowroot/rootnotes.html` | `../styles/sakura.css` | Same |
| `econ/research/readingnotes.html` | `../styles/sakura.css` | Same |
| `econ/teaching/3012.html` | `../styles/sakura.css` | Same |
| `econ/teaching/3102/intertemporal/*.html` | `../../styles/sakura.css` | Same (multiple files) |
| `econ/teaching/3102psets/HWBCycles_old/*.html` | `../../styles/sakura.css` | Same (multiple files) |
| `econ/teaching/3102psets/HW1_dataGraphs.html` | `HW1_GrowthGraphs/https://code.highcharts.com/highcharts.js` | Malformed: local path prefix before an external URL |
| `econ/teaching/3102psets/HW2_dataGraphs.html` | `HW2_BCycleGraphs/https://code.highcharts.com/highcharts.js` | Same malformed pattern |
| `econ/nonsense/mathsymbols.html` | `../../../styles/sakuraBlue.css` | Wrong relative depth to `sakuraBlue.css` |
| `econ/tradeprelim/kehoe/learningbydoing.html` | `../../styles/sakura.css` | Same sakura.css issue |
| `econ/tradeprelim/kehoe/LBD/learningbydoingConcepts - Copy.html` | `google.com` | Missing `https://` prefix |
| `econ/tradeprelim/kehoe/LBD/learningbydoingConcepts - Copy.html` | `link` | Placeholder |
| `econ/presentations/percolationSlides.html` | `../../styles/reveal/css/reveal.css` | No `reveal/` directory under `styles/` |
| `econ/presentations/percolationSlides.html` | `../../styles/reveal/css/theme/white.css` | Same |
| `econ/presentations/percolationSlides.html` | `../../styles/reveal/js/reveal.js` | Same |
| `js/katex/README.md` | `CONTRIBUTING.md` | Not found in `js/katex/` |

Most of these are older standalone HTML files that predate the Jekyll site structure. The `sakura.css` relative path issue affects ~15 files and could be fixed with a find-and-replace to use absolute paths from the site root.

### Files not in the navigation trees (2026-03-16)

Files (`.md` and `.html`) that exist in each repo but do not appear in the navigation hierarchy sitemaps above. Excludes `_`-prefixed directories (`_drafts/`, `_layouts/`, `_includes/`, etc.), config files, READMEs, and root index pages.

**circe** — Clean. Every content file is in the navigation tree.

**bib** — 1 orphan:

| File | Title | Parent | Issue |
|------|-------|--------|-------|
| `zotero/lou2013accurate.md` | (no title) | `papers` (lowercase) | Case mismatch — should be `Papers`. Duplicate of `paper/lou2013accurate.md` which has the correct parent. |

**games** — 8 files, all frontmatter-less HTML:

| File | Notes |
|------|-------|
| `codenames/pinyinCodenames.html` | Pinyin codenames word generator |
| `codenames/pinyinCodenames2.html` | Pinyin codenames word generator (v2) |
| `ref/mycitycards.html` | My City card reference |
| `rules/cardImages.html` | Card image display page |
| `scythe/automountie.html` | Scythe automa tool |
| `tools/mysterium.html` | Raw HTML companion to `tools/mysterium.md` (which is in the tree) |
| `tools/randomWikipedia.html` | Raw HTML companion to `tools/randomwiki.md` (which is in the tree) |
| `tools/randomWords.html` | Raw HTML companion to `tools/randomwords.md` (which is in the tree) |

The last three are standalone HTML tools embedded/linked by their `.md` counterparts. The first five are independent standalone pages with no Jekyll chrome.

**posts** — 35 files:

*Data/source files with no frontmatter (30 files):*

| File | Notes |
|------|-------|
| `nature/BIRDUPraw/Informedness_genus_markdownsource.md` | Raw markdown table for BIRDUP analysis |
| `nature/BIRDUPraw/Informedness_species_markdownsource.md` | " |
| `nature/BIRDUPraw/Markedness_genus_markdownsource.md` | " |
| `nature/BIRDUPraw/Markedness_species_markdownsource.md` | " |
| `nature/BIRDUPraw/WeightedInfoMark_genus_markdownsource.md` | " |
| `nature/BIRDUPraw/WeightedInfoMark_species_markdownsource.md` | " |
| `nature/BIRDUPraw/YulePhi_genus_markdownsource.md` | " |
| `nature/BIRDUPraw/YulePhi_species_markdownsource.md` | " |
| `nature/BIRDUPraw/agreement_genus_markdownsource.md` | " |
| `nature/BIRDUPraw/agreement_species_markdownsource.md` | " |
| `nature/BIRDUPraw/basicbirdup_genus_markdownsource.md` | " |
| `nature/BIRDUPraw/basicbirdup_species_markdownsource.md` | " |
| `nature/BIRDUPraw/birdupplusprevalence_genus_markdownsource.md` | " |
| `nature/BIRDUPraw/birdupplusprevalence_species_markdownsource.md` | " |
| `nature/BIRDUPraw/cohenkappa_genus_markdownsource.md` | " |
| `nature/BIRDUPraw/cohenkappa_species_markdownsource.md` | " |
| `nature/BIRDUPraw/fowlkesmallows_genus_markdownsource.md` | " |
| `nature/BIRDUPraw/fowlkesmallows_species_markdownsource.md` | " |
| `nature/BIRDUPraw/jaccard_genus_markdownsource.md` | " |
| `nature/BIRDUPraw/jaccard_species_markdownsource.md` | " |
| `nature/BIRDUPraw/normalizedTPR_genus_markdownsource.md` | " |
| `nature/BIRDUPraw/normalizedTPR_species_markdownsource.md` | " |
| `nature/BIRDUPraw/prevalance_genus_markdownsource.md` | " |
| `nature/BIRDUPraw/prevalance_species_markdownsource.md` | " |
| `media/alphabet_books/x words from wikipedia corpus - filtered by grok V2.md` | Word list data |
| `media/alphabet_books/x words from wikipedia corpus - filtered.md` | Word list data |
| `media/alphabet_books/x words from wikipedia corpus.md` | Word list data |
| `nature/astrosymbols/dualscalesolarsystem_PeterGift_figues.md` | Notes/figures, no frontmatter |
| `art/Lehrer/LICENSE.md` | License file for Lehrer content |
| `maps/sisterstates/index.html` | Standalone HTML inside the Sister States page directory |

*Draft/scratch files (3 files):*

| File | Notes |
|------|-------|
| `econ/_texaslawsuit.md` | No frontmatter; underscore-prefixed filename (likely a draft) |
| `language/_tengwartest.html` | No frontmatter; underscore-prefixed filename |
| `art/colors/tabletest.html` | No frontmatter; test file |

*Files with frontmatter but outside the tree (2 files):*

| File | Title | Layout | Parent | Notes |
|------|-------|--------|--------|-------|
| `art/colors/colors.html` | (no title) | null | — | Embedded HTML artifact, probably for the Binomial Color Names page |
| `nature/_everyanimal.md` | A List of Every Animal | post | Science and Nature | Underscore prefix may cause Jekyll to skip it, or it's a work in progress. Has no `nav_exclude` set. |

**RMWinslow.github.io** — 110 files:

*Files with frontmatter (6 — individual homework pages, all `nav_exclude: true`):*

| File | Title | Layout |
|------|-------|--------|
| `330/hw/hw1.md` | Econ 330 HW1 | post |
| `330/hw/hw2.md` | Econ 330 HW2 | post |
| `330/hw/hw3.md` | Econ 330 HW3 | post |
| `330/hw/hw4.md` | Econ 330 HW4 | post |
| `330/hw/hw4/answers.md` | Econ 330 HW4 | post |
| `330/hw/hw5.md` | Econ 330 HW5 | post |

The nav tree has a single combined "Econ 330 HW1–HW5" entry. These individual pages are intentionally hidden.

*Files without frontmatter (104 — all legacy pre-Jekyll HTML except 2 markdown files):*

Legacy Highcharts graphs (`3102/highcharts/`, 9 files):

| File |
|------|
| `3102/highcharts/data_CCPIU.html` |
| `3102/highcharts/onePeriodBothAgents.html` |
| `3102/highcharts/onePeriodConsumer.html` |
| `3102/highcharts/onePeriodEquilibrium.html` |
| `3102/highcharts/onePeriodProducer.html` |
| `3102/highcharts/solowSteadyState.html` |
| `3102/highcharts/twoPeriodEndowment.html` |
| `3102/highcharts/twoPeriodEndowmentWithBorrowingLimits.html` |
| `3102/highcharts/twoPeriodEndowmentWithDifferentRates.html` |

Teaching interactives and notes (`econ/teaching/3102/`, 28 files):

| File |
|------|
| `econ/teaching/3102/equilibrium/consumer.html` |
| `econ/teaching/3102/equilibrium/consumerInteractive (2).html` |
| `econ/teaching/3102/equilibrium/consumerInteractive.html` |
| `econ/teaching/3102/equilibrium/equilibrium.html` |
| `econ/teaching/3102/equilibrium/firm.html` |
| `econ/teaching/3102/equilibrium/solving.html` |
| `econ/teaching/3102/interactive/ConsumerAndProducerInteractive.html` |
| `econ/teaching/3102/interactive/OnePeriodEquilibiriumInteractive.html` |
| `econ/teaching/3102/interactive/consumerInteractive.html` |
| `econ/teaching/3102/interactive/exampleInteractive.html` |
| `econ/teaching/3102/interactive/interactivegraphs.html` |
| `econ/teaching/3102/interactive/producerInteractive.html` |
| `econ/teaching/3102/interactive/solowInteractive.html` |
| `econ/teaching/3102/interactive/twoPeriodEndowment.html` |
| `econ/teaching/3102/interactive/twoPeriodEndowmentWithBorrowingLimits.html` |
| `econ/teaching/3102/interactive/twoPeriodEndowmentWithDifferentRates.html` |
| `econ/teaching/3102/intertemporal/consumerProblemWithLabor.html` |
| `econ/teaching/3102/intertemporal/creditFrictions.html` |
| `econ/teaching/3102/intertemporal/firmProblem.html` |
| `econ/teaching/3102/intertemporal/intertemporal/equilibirumDefinition.html` |
| `econ/teaching/3102/intertemporal/intertemporal/shifterExamples.html` |
| `econ/teaching/3102/intertemporal/intertemporalCE_Definiton.html` |
| `econ/teaching/3102/intertemporal/shifterExamples.html` |
| `econ/teaching/3102/intertemporal/twoPeriodEndowment (2).html` |
| `econ/teaching/3102/intertemporal/twoPeriodEndowment.html` |
| `econ/teaching/3102/test/CEInteractive.html` |
| `econ/teaching/3102/test/consumerInteractive.html` |
| `econ/teaching/3102/test/exampleInteractive.html` |
| `econ/teaching/3102/test/producerInteractive.html` |

Typesetting guides (6 files, duplicated in two locations):

| File |
|------|
| `econ/teaching/3102/typesetting/latexMath.html` |
| `econ/teaching/3102/typesetting/lyxTutorial.html` |
| `econ/teaching/3102/typesetting/typesettingSoftware.html` |
| `econ/teaching/typesetting/latexMath.html` |
| `econ/teaching/typesetting/lyxTutorial.html` |
| `econ/teaching/typesetting/typesettingSoftware.html` |

Problem set data/graphs (6 files):

| File |
|------|
| `econ/teaching/3102psets/HW1_dataGraphs.html` |
| `econ/teaching/3102psets/HW2_dataGraphs.html` |
| `econ/teaching/3102psets/HWBCycles_old/dataResultsFlippedPercentDiff.html` |
| `econ/teaching/3102psets/HWBCycles_old/dataResultsOG.html` |
| `econ/teaching/3102psets/HWBCycles_old/dataResultsOnlyImages.html` |
| `econ/teaching/3102psets/HWBCycles_old/week9solutions.html` |

Macro prelim notes (`econ/macroprelim/`, 12 files):

| File |
|------|
| `econ/macroprelim/Chari/privatemoney.html` |
| `econ/macroprelim/Chari/productionrisk.html` |
| `econ/macroprelim/Chari/sustainabledebt.html` |
| `econ/macroprelim/Concepts/envelope.html` |
| `econ/macroprelim/Concepts/flowchartkey/FlowChartKey.html` |
| `econ/macroprelim/Jones/HumanCapital.html` |
| `econ/macroprelim/Jones/dynamicprogramming.html` |
| `econ/macroprelim/Kehoe/Search.html` |
| `econ/macroprelim/Kehoe/crossingProof.html` |
| `econ/macroprelim/Kehoe/dp.html` |
| `econ/macroprelim/prelimindex.html` |
| `econ/macroprelim/roadmapTODO.html` |

Trade prelim notes (`econ/tradeprelim/`, 17 files):

| File |
|------|
| `econ/tradeprelim/amador/multipleborrowers.html` |
| `econ/tradeprelim/fitzgerald/armingtongravity.html` |
| `econ/tradeprelim/fitzgerald/melitzottaviano.html` |
| `econ/tradeprelim/fitzgerald/melitzottaviano/melitzottaviano.html` |
| `econ/tradeprelim/fitzgerald/melitzottaviano_problem.html` |
| `econ/tradeprelim/fitzgerald/melitzottaviano_solution.html` |
| `econ/tradeprelim/kehoe/LBD/LBDconcepts - Copy (2).html` |
| `econ/tradeprelim/kehoe/LBD/LBDconcepts - Copy (3).html` |
| `econ/tradeprelim/kehoe/LBD/LBDconcepts.html` |
| `econ/tradeprelim/kehoe/LBD/LBDprelim.html` |
| `econ/tradeprelim/kehoe/LBD/LBDprelimSolutionA.html` |
| `econ/tradeprelim/kehoe/LBD/learningbydoingConcepts - Copy.html` |
| `econ/tradeprelim/kehoe/hecksherohlin.html` |
| `econ/tradeprelim/kehoe/learningbydoing.html` |
| `econ/tradeprelim/kehoe/monopolisticcompetition.html` |
| `econ/tradeprelim/kehoe/self-fulfillingdebt.html` |
| `econ/tradeprelim/prelimindex.html` |

Research notes (`econ/research/`, 14 files):

| File |
|------|
| `econ/research/ContagionThing/gradientPlotter/adjustForN.html` |
| `econ/research/ContagionThing/gradientPlotter/blank.html` |
| `econ/research/ContagionThing/gradientPlotter/blank2.html` |
| `econ/research/ContagionThing/notes about where to go.html` |
| `econ/research/ContagionThing/septPresentation/outline.md` |
| `econ/research/ContagionThing/septPresentation/outlineCode.html` |
| `econ/research/arrowroot/arrownotes.html` |
| `econ/research/arrowroot/arrowrootnotes.html` |
| `econ/research/arrowroot/rootnotes.html` |
| `econ/research/farmingToy/farmingToy.html` |
| `econ/research/farmingToy/farmingToyExperimentalFormat.html` |
| `econ/research/halfbakedideas.html` |
| `econ/research/readingnotes.html` |
| `econ/research/talkNotes.html` |

Other standalone files (11 files):

| File | Notes |
|------|-------|
| `202/graphs/3102 Graphs - Robert Winslow.html` | Legacy kgjs graph page |
| `202/graphs/AD_AS, The Labor Market, and the Phillips Curve - EconGraphs.html` | Saved EconGraphs page |
| `3102/_solow.md` | No frontmatter; underscore-prefixed (draft) |
| `330/hw/hw5/Econ 330 HW 5.html.LyXconv/Econ_330_HW_5.html` | LyX-converted homework |
| `404.html` | Custom 404 page |
| `econ/nonsense/mathsymbols.html` | Math symbols reference |
| `econ/presentations/biglisthtml.html` | Presentation list |
| `econ/presentations/percolationSlides.html` | Reveal.js slides |
| `econ/teaching/3012.html` | Likely a typo for 3102 |
| `js/katex/katexTest.html` | KaTeX test page |
| `teaching/calendar_creator.html` | Calendar tool |

## TODOs

- [x] Index the websites that consume this theme as a remote theme. (Done — see the inventory below.)
- [ ] Clean up or archive obsolete repos (e.g. `jtd-test-style`, `latexpagetest`, `just-the-docs-tweaked`, and any other repos that are no longer actively used).
- [x] ~~Add `url: "https://www.rmwinslow.com"` to the **bib** site's `_config.yml`.~~ Verified 2026-03-18: canonical and og:url now correctly use `https://www.rmwinslow.com/bib/`.
- [x] ~~Add `author: Robert Winslow` to the **bib** site's `_config.yml`.~~ Verified 2026-03-18: author meta tag now reads "Robert Winslow".
- [ ] Audit the other consuming sites (`games`, `RMWinslow.github.io`) for the same `url`/`author` gaps.
- [ ] Fix the 11 navigation hierarchy issues found in the sitemap audit:
  - **posts**: Fix 4 orphaned parent refs (`"hidden"` x2, `"Media"`, `"_Media"`), rename one of the duplicate "Working from Home" pages, add missing `grand_parent` to "X in the ABCs" and "Visual Artists", remove or populate phantom parent "Unicode Characters".
  - **RMWinslow.github.io**: Remove or populate 3 phantom parents ("Competitive Equilibrium", "Aggregate Measurement", "Money and Banking") — these have `has_children: true` but no children.
  - **games**: Set `has_children: true` on "Lasers & Feelings" (currently `false` but has 3 children).

## Consuming Sites Inventory

Indexed 2026-03-16 from https://github.com/RMWinslow?tab=repositories.

### Sites using `RMWinslow/JTD-RMW`

| Repo | Title | Notes |
|------|-------|-------|
| **posts** | RMW's Blogalike | Main blog. Has `CLAUDE.md` excluded from build. |
| **RMWinslow.github.io** | Robert Winslow | Root personal site. Uses MathJax. |
| **bib** | Bibliography | Minimal config. |
| **games** | Game Rules | Includes webfont directory reference. |
| **circe** | La Circe | Uses `_config.yaml` (not `.yml`). Missing `url` and `author`. Pulled locally. |
| **jtd-test-style** | JTD test | Test/sandbox site for the theme — candidate for archival. |

### Sites using a different theme

| Repo | Title | Theme | Notes |
|------|-------|-------|-------|
| **macronotes** | Macro Notes | `pmarsceill/just-the-docs` (original unmodified JTD) | Solarized color scheme. Could potentially migrate to JTD-RMW. |
| **3102old** | 3102 Instructor Notes | `RMWinslow/just-the-docs-tweaked` | Older fork, not JTD-RMW. |
| **tones** | Pure Tones | `RMWinslow/just-the-docs-tweaked` | Older fork, not JTD-RMW. Search disabled. |
| **mynotes** | Robbie's Notes | `minimal-mistakes` | Completely different theme. UMN email, kramdown, pagination. |
| **cv** | (CV) | `davewhipp` style | Simple markdown-to-CV theme. |
| **latexpagetest** | Testing a Theme | `Hammie217/LatexJekyll` | Had JTD-RMW commented out — candidate for archival. |
| **lists** | Lists of Links | No remote theme (default GitHub Pages) | Just markdown files of links. |
| **retlab** | — | Ben Balter config | Appears to be a fork, not an original RMW site. |

### Repos with no GitHub Pages config found

ytrss, scrapetest, webfonts, umn-git-thesis-demo, kgjs, emojitwo, twemoji-colr-tweaked, doodads, code, pui-data-repository, ModernSlides

(Checked for both `_config.yml` and `_config.yaml` on both `main` and `master` branches. None found.)

## Audit Ideas [claude's suggestions]

These are potential audits that could be run across the theme and consuming sites to improve consistency, cleanliness, and maintainability.

### Frontmatter hygiene (per-page, across all sites) — PARTIALLY DONE (layout usage, no-frontmatter, no-layout counts)

- **Missing titles.** Pages without a `title` produce a broken `<title>` tag (` - Site Title`) and are invisible to navigation and search. Scan for any untitled pages that aren't intentionally using `layout: null`.
- **Orphaned `parent` references.** Pages whose `parent` value doesn't match any existing page's `title` will silently fail to nest in the sidebar. This is easy to break when renaming a parent page.
- **Phantom `has_children`.** Pages marked `has_children: true` that don't actually have any children referencing them (empty nav groups), or the reverse — pages that have children pointing at them but aren't marked `has_children: true` (children won't render as a collapsible group).
- **`modified` vs `last_modified_date` usage.** Pages using the `modified` shorthand won't get the footer timestamp. Scan for pages using `modified` and flag them, since `last_modified_date` is the more complete option.
- **Stale dates.** Pages whose `last_modified_date` is older than their most recent git commit — the date may have been forgotten after an edit.
- **Missing `description`.** Pages that are likely to be shared (top-level, high-traffic) but have no `description` for social previews and SEO.
- **Unnecessary math loading.** Pages that don't contain any math notation but still load KaTeX (the default). Adding `math: none` to pages or sections that don't need it could reduce page weight, especially on sites like `games` where math is probably never used.
- **Double KaTeX conflict.** Some pages load interactive graphs via a third-party library (kgjs) that bundles its own KaTeX. When the theme also loads KaTeX, the page stutters and locks up because two instances of KaTeX are fighting over the same DOM. This needs to be fixed — likely by setting `math: none` on those pages, or by making the theme's KaTeX loading smarter about detecting an existing instance.

### Navigation structure — DONE (full sitemaps built, 11 issues found)

- **Depth consistency.** Check whether any site uses more than three levels of nesting, and whether the breadcrumb limitation (only two levels) causes confusion for deeply nested pages.
- **Single-child parents.** Parent pages with only one child — the grouping may not be adding value and could be flattened.
- **Nav ordering gaps.** Pages using `nav_order` with large gaps or inconsistent numbering that makes future insertions awkward.

### Cross-site consistency — PARTIALLY DONE (site config fields audited, SEO meta tags compared)

- **Plugin standardization.** The sites use different plugin sets (some have `jekyll-sitemap`, some don't; some have `jekyll-redirect-from`, some don't). Consider whether all sites should have a standard plugin baseline.
- **`page_excerpts: true`** is set on some sites but the theme never reads it. Either remove it everywhere or add support for it in the theme.
- **`webfontdirectory`** is set on `posts` and `games` but not on `bib`, `circe`, or `RMWinslow.github.io`. If some pages on those sites reference web fonts, they may be loading from the wrong path.
- **`gh_edit_link: false`** is set inconsistently — present on most sites but missing from `bib`. Harmless in practice (the footer guards against incomplete config) but inconsistent.
- **`last_edit_timestamp: true`** is only set on `posts`. The other sites don't show "Page last modified" in the footer even when pages have `last_modified_date` set.

### Link and content integrity — PARTIALLY DONE (internal broken links scanned; external link rot, images, redirects not yet checked)

- **Internal broken links.** Links between pages within a site that point to pages that have been moved, renamed, or deleted.
- **External link rot.** Links to external resources that have gone stale (404s, domain changes). Particularly relevant for `bib` which is full of paper references.
- **Missing or broken images.** Image references that don't resolve, especially in older posts.
- **Redirect chains.** Sites using `jekyll-redirect-from` may have accumulated stale redirects that could be cleaned up.

### Performance

- **Search index size.** On large sites like `posts`, the Lunr search index (`search-data.json`) can get very large. Pages that don't need to be searchable could use `search_exclude: true` to trim it.

Theme-level cleanup, accessibility, and performance items related to the theme's own code have been moved to the JTD-RMW repo's `CLAUDE.md`.

---

## Subdomain vs. Subdirectory: SEO Research Report

**Decision (2026-03-19):** Deploy the notes repo at `www.rmwinslow.com/notes/`
(subdirectory) rather than `notes.rmwinslow.com` (subdomain). The research
below informed this decision.

### Google Search Central — Redirects and URL Canonicalization

**Source:** https://developers.google.com/search/docs/crawling-indexing/301-redirects

> "Googlebot follows the redirect, and the indexing pipeline uses the redirect
> as a **strong** signal that the redirect target should be canonical."

> "Google Search interprets instant `meta refresh` redirects as permanent
> redirects."

> "One of the URLs will be the canonical; which one, depends on signals such as
> whether the redirect was temporary or permanent. The other URL becomes an
> _alternate name_ of the canonical URL."

This confirms that `jekyll-redirect-from`'s instant meta refresh is treated as
a permanent redirect by Google, and that the canonical URL consolidation will
happen over time.

### Semrush — Subdomain vs. Subdirectory

**Source:** https://www.semrush.com/blog/subdomain-vs-subdirectory/

> "Google treats subdomains as distinct websites. Which means they crawl and
> index subdomains separately."

> "Subdirectories are seen as part of the main domain."

> "All the hard work you put into building backlinks is more likely to benefit
> every piece of content under that main domain, including those in
> subdirectories."

> "Subdomains may not fully benefit from the backlinks the main domain has
> garnered over the years."

### Carnegie Mellon University — Web Best Practices

**Source:** https://www.cmu.edu/web/best-practices/search-engine-optimization/subdomains-vs-subdirectories.html

> "For net-new external-facing websites, subdirectories will provide the best
> and fastest SEO authority."

> "Subdirectories...carry the same weight and authority as the rest of
> www.cmu.edu."

> "Google often treats them as separate sites — SEO equity from cmu.edu may
> not transfer."

> "The SEO best-practice recommendation is to use subdirectories in most
> instances."

Particularly relevant: this is guidance from a major university about their own
academic web properties — the same kind of site as Robert's.

### Cloudflare Blog — Subdomains vs. Subdirectories Best Practices

**Source:** https://blog.cloudflare.com/subdomains-vs-subdirectories-best-practices-workers-part-1/

> "The subdirectory strategy concentrates your keywords onto a single domain
> while the subdomain strategy spreads your keywords across multiple distinct
> domains."

> "Keywords are diluted across subdomains. Each additional subdomain decreases
> the likelihood that any particular domain ranks in a given search."

> "In a word, the subdirectory strategy results in better root domain authority.
> Higher domain authority leads to better search rankings."

### Search Engine Journal — John Mueller (Google) Quotes

**Source:** https://www.searchenginejournal.com/google-treats-subdomains-subdirectories-john-mueller-says/254687/

> "In general, we see these the same." — John Mueller, Google

> "I would personally try to keep things together as much as possible." — John
> Mueller, Google

> "If you're like 'well I don't care either way' then I would just keep it
> within the same site." — John Mueller, Google

Google's official position is neutrality, but Mueller's personal recommendation
leans toward subdirectories.

### SE Ranking — 20,000 Keyword Study

**Source:** https://seranking.com/blog/subdomains-vs-subdirectories-research/

> "Subdomains account for just 3% of domain structures in SERPs and are only
> prevalent in top positions in multilingual markets."

> "Subdirectories are often considered the best option for international brands
> targeting multiple locales. Our research reflects that assumption, with
> subdirectories accounting for over 20% of the top three ranking positions."

> "Ultimately, whichever option you choose can be successful if your site is
> well optimised."

### Summary

| Factor | Subdirectory | Subdomain |
|--------|-------------|-----------|
| Domain authority inheritance | Automatic | Not guaranteed |
| Backlink consolidation | All links benefit root domain | Links may not transfer |
| Google's stated position | Treated the same | Treated the same |
| Practical SERP evidence | Dominant in top positions | ~3% of top positions |
| Recommended default | Yes (Mueller, CMU, Cloudflare, Semrush) | Only when technically necessary |
