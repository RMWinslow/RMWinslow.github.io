---
nav_exclude: true
search_exclude: true
---

# Annotated Directory Listing

Quick-reference map of every file in the repo, annotated by role.

**Legend:**
- `[NAV]` — appears in the site's navigation sidebar
- `[NAV-HIDDEN]` — has `nav_exclude: true` or `search_exclude: true`
- `[LEGACY]` — an HTML file with no frontmatter, not in the nav tree
- `[DRAFT]` — underscore-prefixed or clearly a draft/scratch file
- `[CONFIG]` — site config files
- `[ASSET]` — images, CSS, JS, fonts, PDFs, data files, etc.
- `[META]` — repo meta files

Generated 2026-03-18 from the navigation hierarchy audit in `claude_audits.md`.

```
RMWinslow.github.io/
│
├── .gitignore                                      [CONFIG]
├── _config.yml                                     [CONFIG]
├── CNAME                                           [CONFIG] www.rmwinslow.com
├── favicon.ico                                     [ASSET]
├── CLAUDE.md                                       [META]
├── README.md                                       [META]
├── claude_audits.md                                [META]
├── claude_directory.md                             [META] (this file)
│
├── index.html                                      [LEGACY] custom landing page (no frontmatter)
├── 404.html                                        [LEGACY] custom 404 page (no frontmatter)
│
├── _layouts/
│   └── default_basic.html                          [CONFIG] custom layout override
│
├── cv.md                                           [NAV] "CV" (nav_order: 0)
├── research.md                                     [NAV] "Research" (parent, nav_order: 10)
├── teaching.md                                     [NAV] "Teaching" (parent, nav_order: 20)
├── notes.md                                        [NAV] "Notes" (parent, nav_order: 30)
│
│
│── ── RESEARCH ──────────────────────────────────────────
│
├── research/
│   ├── contagion.md                                [NAV] "Branching Processes and Behavioral Choice"
│   ├── jmp.md                                      [NAV] "Job Market Paper"
│   ├── mebdi22.md                                  [NAV] "Predicting Unemployment Status"
│   ├── reu.md                                      [NAV] "Graph Two-Rankings"
│   └── pdf/
│       ├── MEDBI22_metrics_comparison.pdf          [ASSET]
│       ├── WinslowMebdi22Summary.pdf               [ASSET]
│       ├── contagion_draft_2021-09-26.pdf          [ASSET]
│       ├── jmp.pdf                                 [ASSET]
│       └── networks_conference_2024.pdf            [ASSET]
│
│
│── ── TEACHING ──────────────────────────────────────────
│
├── teaching/
│   ├── 3102.md                                     [NAV] "Econ 3102 (UMN)" child of Teaching
│   ├── 330.md                                      [NAV] "Econ 330" child of Teaching
│   └── calendar_creator.html                       [LEGACY] standalone calendar tool
│
│
│── ── NOTES: INTERMEDIATE MACRO (3102) ──────────────────
│
├── 3102/
│   ├── topic-overview.md                           [NAV] "Intermediate Macro Notes" parent page
│   │
│   │   ── Children of Intermediate Macro Notes ──
│   ├── math-lagrangian.md                          [NAV] "Constrained Optimization"
│   ├── measurement-gdp.md                          [NAV] "Gross Domestic Product"
│   ├── measurement-prices.md                       [NAV] "Prices"
│   ├── measurement-savings.md                      [NAV] "National Savings"
│   ├── measurement-labor.md                        [NAV] "Labor Aggregates"
│   ├── measurement-cylical.md                      [NAV] "Business Cycles"
│   ├── measurement-money.md                        [NAV] "Money Concepts"
│   ├── oneperiod-consumer.md                       [NAV] "Representative Consumer"
│   ├── oneperiod-producer.md                       [NAV] "Representative Producer"
│   ├── oneperiod-equilibrium.md                    [NAV] "One Period Equilibrium"
│   ├── jobsearch.md                                [NAV] "McCall Job Search"
│   ├── twoperiod-endowment.md                     [NAV] "Two-Period Endowment Economy"
│   ├── twoperiod-creditfrictions.md                [NAV] "Credit Market Imperfections"
│   ├── twoperiod-socialsecurity.md                 [NAV] "Social Security"
│   ├── twoperiod-agents.md                         [NAV] "Two Period Agents with Production"
│   ├── twoperiod-equilibrium.md                    [NAV] "Two Period Equilibrium"
│   ├── twoperiod-stickyprices.md                   [NAV] "Money and Business Cycles"
│   ├── twoperiod-soe.md                            [NAV] "Small Open Economy"
│   ├── twoperiod-exchangerates.md                  [NAV] "Exchange Rates"
│   ├── diamond.md                                  [NAV] "Bank Runs"
│   ├── _bop.md                                     [NAV] "Balance of Payment" (child of Intermediate Macro Notes)
│   ├── _money.md                                   [NAV] "Money" (child of Intermediate Macro Notes)
│   │
│   │   ── Hidden nav pages ──
│   ├── graphs.md                                   [NAV-HIDDEN] "3102 Graphs" (kgjs, nav_exclude)
│   ├── graphs2.md                                  [NAV-HIDDEN] "3102 Graphs (Highcharts, old)" (nav_exclude)
│   ├── measurement-money-slides.md                 [NAV-HIDDEN] "Money Slides" (remark_slides, nav_exclude)
│   │
│   │   ── Phantom parents (has_children: true but no children) ──
│   ├── _equilibrium.md                             [NAV] "Competitive Equilibrium" phantom parent
│   ├── _measurement.md                             [NAV] "Aggregate Measurement" phantom parent (no layout)
│   │
│   │   ── Draft ──
│   ├── _solow.md                                   [DRAFT] no frontmatter, Solow model links
│   │
│   │   ── Assets ──
│   ├── Ponzi.pdf                                   [ASSET]
│   ├── img-CE-endogenous-doodle.png                [ASSET]
│   ├── img-gdp-three-ways.png                      [ASSET]
│   ├── img-jobsearch-McCall-flowchart.png          [ASSET]
│   ├── img-jobsearch-McCall-flowchart.svg          [ASSET]
│   ├── img-jobsearch-lakes.png                     [ASSET]
│   ├── img-jobsearch-lakes.svg                     [ASSET]
│   ├── img-money-coinhoard.webp                    [ASSET]
│   ├── img-money-lydia.webp                        [ASSET]
│   ├── img-money-scrip.webp                        [ASSET]
│   ├── img-money-snails.webp                       [ASSET]
│   ├── img-socialsecurity_olg.png                  [ASSET]
│   ├── img-socialsecurity_olg.svg                  [ASSET]
│   ├── img-socialsecurity_olg_fullyfunded.png      [ASSET]
│   ├── img-socialsecurity_olg_payasyougo.png       [ASSET]
│   ├── img-socialsecurity_olg_v2.png               [ASSET]
│   ├── img-socialsecurity_olg_v2.svg               [ASSET]
│   ├── img-socialsecurity_olg_v2.webp              [ASSET]
│   ├── img-twoperiod_shifter_blank.png             [ASSET]
│   ├── img-twoperiod_shifter_coordination.png      [ASSET]
│   ├── img-twoperiod_shifter_keynes_fix.png        [ASSET]
│   ├── img-twoperiod_shifter_keynes_lowr.png       [ASSET]
│   ├── img-twoperiod_shifter_rbc_G.png             [ASSET]
│   ├── img-twoperiod_shifter_rbc_M.png             [ASSET]
│   ├── img-twoperiod_shifter_rbc_z.png             [ASSET]
│   ├── img-twoperiod_shifter_rbc_zboth.png         [ASSET]
│   ├── img-twoperiod_shifter_rbc_zprime.png        [ASSET]
│   ├── img-money/ — 18 image files (png)           [ASSET]
│   ├── graphs/
│   │   ├── onePeriodBothAgents.yml                 [ASSET]
│   │   ├── onePeriodConsumer.yml                   [ASSET]
│   │   ├── onePeriodLaborMarket.yml                [ASSET]
│   │   ├── onePeriodProducer.yml                   [ASSET]
│   │   ├── test.yml                                [ASSET]
│   │   ├── twoPeriodCollateralConstraint.yml       [ASSET]
│   │   ├── twoPeriodEndowment.yml                  [ASSET]
│   │   ├── twoPeriodEquilibrium.yml                [ASSET]
│   │   └── twoPeriodInterestRateSpread.yml         [ASSET]
│   ├── python graphs/
│   │   ├── C-CPI-U.csv                            [ASSET]
│   │   ├── CCPIU_by_type.py                        [ASSET]
│   │   ├── GDPpie.py                               [ASSET]
│   │   └── PCE_by_type.py                          [ASSET]
│   │
│   └── highcharts/
│       ├── data_CCPIU.html                         [LEGACY]
│       ├── onePeriodBothAgents.html                [LEGACY]
│       ├── onePeriodConsumer.html                  [LEGACY]
│       ├── onePeriodEquilibrium.html               [LEGACY]
│       ├── onePeriodProducer.html                  [LEGACY]
│       ├── solowSteadyState.html                   [LEGACY]
│       ├── twoPeriodEndowment.html                 [LEGACY]
│       ├── twoPeriodEndowmentWithBorrowingLimits.html [LEGACY]
│       ├── twoPeriodEndowmentWithDifferentRates.html [LEGACY]
│       ├── bigE.png                                [ASSET]
│       ├── smallE.png                              [ASSET]
│       ├── star.png                                [ASSET]
│       └── star2.png                               [ASSET]
│
│
│── ── NOTES: PRINCIPLES OF MACRO (202) ──────────────────
│
├── 202/
│   ├── topic-overview.md                           [NAV] "Principles of Macro" parent page
│   ├── trade-accounts.md                           [NAV] "Balance of Payments"
│   ├── adas.md                                     [NAV] "The AD-AS Model"
│   ├── inflation-costs.md                          [NAV] "The Costs of Inflation"
│   │
│   ├── graphs/
│   │   ├── 3102 Graphs - Robert Winslow.html       [LEGACY] kgjs graph page
│   │   ├── AD_AS, The Labor Market, and the Phillips Curve - EconGraphs.html [LEGACY]
│   │   ├── adas_labor_phillips.yml                 [ASSET]
│   │   └── graphs/
│   │       └── onePeriodConsumer.yml               [ASSET]
│   │
│   └── handouts/
│       ├── 202 Ch 17 - Quantity Theory of Money.lyx    [ASSET]
│       ├── 202 Ch 17 - Quantity Theory of Money.pdf    [ASSET]
│       ├── 202 Ch 18 - Exchange Rates.lyx              [ASSET]
│       ├── 202 Ch 18 - Imports Exports and Capital Flows.lyx  [ASSET]
│       ├── 202 Ch 19 - Examples.lyx                    [ASSET]
│       ├── 202 Ch 19 - Examples.pdf                    [ASSET]
│       ├── 202 Ch 19 - Open Economy Equilibrium.lyx    [ASSET]
│       ├── 202 Ch 19 - Open Economy Equilibrium.pdf    [ASSET]
│       ├── 202 Ch 20 - AD-AS.lyx                       [ASSET]
│       ├── 202 Ch 20 - AD-AS.pdf                       [ASSET]
│       ├── Figure 32-3.png                             [ASSET]
│       ├── Figure 32-5.png                             [ASSET]
│       ├── img_blank_ch19_model.png                    [ASSET]
│       ├── img_blank_ch19_model_more_whitespace.png    [ASSET]
│       ├── img_blank_ch20_ASAD.png                     [ASSET]
│       └── img_blank_supply_and_demand.png             [ASSET]
│
│
│── ── NOTES: PRINCIPLES OF MICRO (101) ──────────────────
│
├── 101/
│   ├── topic-overview.md                           [NAV-HIDDEN] "Principles of Micro" (nav_exclude: true)
│   ├── equilibrium.md                              [NAV] "Market Equilibrium" child of Principles of Micro
│   └── graphs/
│       ├── equilibriumShocks.yml                   [ASSET]
│       └── onePeriodConsumer.yml                   [ASSET]
│
│
│── ── NOTES: ECON ELECTIVES ─────────────────────────────
│
├── econ/
│   ├── UMNelectives.md                             [NAV] "Econ Electives" child of Notes
│   └── subsite map.txt                             [ASSET]
│
│
│── ── NOTES: MONEY AND BANKING (330) ────────────────────
│
├── 330/
│   ├── index.md                                    [NAV] "Money and Banking" parent (has_children)
│   │
│   └── hw/
│       ├── hw1.md                                  [NAV-HIDDEN] "Econ 330 HW1" (nav_exclude)
│       ├── hw2.md                                  [NAV-HIDDEN] "Econ 330 HW2" (nav_exclude)
│       ├── hw3.md                                  [NAV-HIDDEN] "Econ 330 HW3" (nav_exclude)
│       ├── hw4.md                                  [NAV-HIDDEN] "Econ 330 HW4" (nav_exclude)
│       ├── hw5.md                                  [NAV-HIDDEN] "Econ 330 HW5" (nav_exclude)
│       │
│       ├── hw1-inflation/
│       │   ├── 330hw1q2_filtered_freddata.xlsx     [ASSET]
│       │   ├── 330hw1q3_freddata.csv               [ASSET]
│       │   ├── BEA2.8.4.csv                        [ASSET]
│       │   ├── HW1_Q1_PCE_pct_change.png           [ASSET]
│       │   ├── HW1_Q1_annualized_core_inflation.png     [ASSET]
│       │   ├── HW1_Q1_annualized_core_inflation_excel.png  [ASSET]
│       │   ├── HW1_Q4_PCE_components_pct_change.png     [ASSET]
│       │   └── hw1-inflation.py                    [ASSET]
│       │
│       ├── hw4/
│       │   ├── answers.md                          [NAV-HIDDEN] "Econ 330 HW4" solutions (nav_exclude)
│       │   ├── hw4q5.png                           [ASSET]
│       │   ├── Econ 330 HW 4 solutions.lyx         [ASSET]
│       │   ├── Econ 330 HW 4 solutions.pdf         [ASSET]
│       │   └── solutions.lyx~                      [ASSET] backup file
│       │
│       └── hw5/
│           ├── Econ 330 HW 5.lyx                   [ASSET]
│           ├── Econ 330 HW 5.pdf                   [ASSET]
│           └── Econ 330 HW 5.html.LyXconv/
│               ├── Econ_330_HW_5.html              [LEGACY] LyX-converted homework
│               └── Econ_330_HW_5.css               [ASSET]
│
│
│── ── SLIDES ────────────────────────────────────────────
│
├── slides/
│   ├── index.md                                    [NAV-HIDDEN] "Slide Deck Index" (nav_exclude)
│   ├── remark_formattest.md                        [NAV-HIDDEN] "Remark Formatting Test" (nav_exclude)
│   ├── defense.pdf                                 [ASSET]
│   ├── jmp-usd.pdf                                 [ASSET]
│   ├── m22.pdf                                     [ASSET]
│   ├── mpbc.pdf                                    [ASSET]
│   └── nsf.pdf                                     [ASSET]
│
│
│── ── LEGACY ECON (pre-Jekyll HTML pages) ───────────────
│
├── econ/
│   │
│   ├── macroprelim/
│   │   ├── prelimindex.html                        [LEGACY]
│   │   ├── roadmapTODO.html                        [LEGACY]
│   │   ├── Chari/
│   │   │   ├── privatemoney.html                   [LEGACY]
│   │   │   ├── productionrisk.html                 [LEGACY]
│   │   │   ├── sustainabledebt.html                [LEGACY]
│   │   │   └── FriedmanRule.png                    [ASSET]
│   │   ├── Concepts/
│   │   │   ├── envelope.html                       [LEGACY]
│   │   │   └── flowchartkey/
│   │   │       ├── FlowChartKey.html               [LEGACY]
│   │   │       ├── FCchance.png                    [ASSET]
│   │   │       ├── FCchoice.png                    [ASSET]
│   │   │       ├── FCincome.png                    [ASSET]
│   │   │       ├── FClabel.png                     [ASSET]
│   │   │       ├── FCprocess.png                   [ASSET]
│   │   │       └── FCtime.png                      [ASSET]
│   │   ├── Jones/
│   │   │   ├── HumanCapital.html                   [LEGACY]
│   │   │   ├── dynamicprogramming.html             [LEGACY]
│   │   │   └── questions.txt                       [ASSET]
│   │   └── Kehoe/
│   │       ├── Search.html                         [LEGACY]
│   │       ├── crossingProof.html                  [LEGACY]
│   │       ├── dp.html                             [LEGACY]
│   │       ├── KehoeSearchLabels.png               [ASSET]
│   │       ├── laser1.png                          [ASSET]
│   │       ├── laser2.png                          [ASSET]
│   │       └── laser3.png                          [ASSET]
│   │
│   ├── tradeprelim/
│   │   ├── prelimindex.html                        [LEGACY]
│   │   ├── amador/
│   │   │   ├── multipleborrowers.html              [LEGACY]
│   │   │   ├── EatonG notes.lyx                    [ASSET]
│   │   │   └── EatonG notes.lyx~                   [ASSET]
│   │   ├── fitzgerald/
│   │   │   ├── armingtongravity.html               [LEGACY]
│   │   │   ├── melitzottaviano.html                [LEGACY]
│   │   │   ├── melitzottaviano_problem.html        [LEGACY]
│   │   │   ├── melitzottaviano_solution.html       [LEGACY]
│   │   │   ├── mellitz work.lyx                    [ASSET]
│   │   │   ├── mellitz work.lyx~                   [ASSET]
│   │   │   └── melitzottaviano/
│   │   │       └── melitzottaviano.html            [LEGACY]
│   │   └── kehoe/
│   │       ├── hecksherohlin.html                  [LEGACY]
│   │       ├── learningbydoing.html                [LEGACY]
│   │       ├── monopolisticcompetition.html        [LEGACY]
│   │       ├── self-fulfillingdebt.html            [LEGACY]
│   │       ├── debtcrisiswork.lyx                  [ASSET]
│   │       ├── hecksherwork.lyx                    [ASSET]
│   │       ├── hecksherwork.lyx~                   [ASSET]
│   │       └── LBD/
│   │           ├── LBDconcepts - Copy (2).html     [LEGACY]
│   │           ├── LBDconcepts - Copy (3).html     [LEGACY]
│   │           ├── LBDconcepts.html                [LEGACY]
│   │           ├── LBDprelim.html                  [LEGACY]
│   │           ├── LBDprelimSolutionA.html         [LEGACY]
│   │           └── learningbydoingConcepts - Copy.html [LEGACY]
│   │
│   ├── research/
│   │   ├── halfbakedideas.html                     [LEGACY]
│   │   ├── readingnotes.html                       [LEGACY]
│   │   ├── talkNotes.html                          [LEGACY]
│   │   ├── IO - Optimal lower than optimal pricing.pdf [ASSET]
│   │   ├── img/
│   │   │   ├── housedoodle1.png                    [ASSET]
│   │   │   ├── housedoodle3.png                    [ASSET]
│   │   │   └── sillyhousedoodle.svg                [ASSET]
│   │   ├── arrowroot/
│   │   │   ├── arrownotes.html                     [LEGACY]
│   │   │   ├── arrowrootnotes.html                 [LEGACY]
│   │   │   ├── rootnotes.html                      [LEGACY]
│   │   │   ├── Root - Incentive Stuff.pdf          [ASSET]
│   │   │   └── debug.log                           [ASSET]
│   │   ├── farmingToy/
│   │   │   ├── farmingToy.html                     [LEGACY]
│   │   │   ├── farmingToyExperimentalFormat.html   [LEGACY]
│   │   │   ├── eqCalculator.py                     [ASSET]
│   │   │   ├── farming notes.lyx                   [ASSET]
│   │   │   ├── farming notes.lyx.emergency         [ASSET]
│   │   │   ├── farming notes.lyx~                  [ASSET]
│   │   │   ├── farmingNotesRedo-lyxformat-508.lyx~ [ASSET]
│   │   │   ├── farmingNotesRedo.lyx                [ASSET]
│   │   │   ├── trade.lyx                           [ASSET]
│   │   │   ├── trade.lyx~                          [ASSET]
│   │   │   └── trade.tex                           [ASSET]
│   │   ├── FIFA/
│   │   │   ├── FIFA auction idea.txt               [ASSET]
│   │   │   ├── Fifa draft.lyx                      [ASSET]
│   │   │   ├── Fifa draft.pdf                      [ASSET]
│   │   │   └── Fifa-draft.pdf                      [ASSET]
│   │   └── ContagionThing/
│   │       ├── notes about where to go.html        [LEGACY]
│   │       ├── notes about where to go.txt         [ASSET]
│   │       ├── Presentation Planning Notes.txt     [ASSET]
│   │       ├── example.svg                         [ASSET]
│   │       ├── k5.graphml                          [ASSET]
│   │       ├── graphtransmission1.png              [ASSET]
│   │       ├── fisherapprox.png                    [ASSET]
│   │       ├── *.py — 13 Python simulation scripts [ASSET]
│   │       ├── *.lyx / *.lyx~ — 14 LyX files      [ASSET]
│   │       ├── pasted*.png — 28 pasted images      [ASSET]
│   │       ├── *.png — 12 other result images      [ASSET]
│   │       ├── __pycache__/
│   │       │   └── yed.cpython-36.pyc              [ASSET]
│   │       ├── img/ — 21 simulation result PNGs    [ASSET]
│   │       ├── gradientPlotter/
│   │       │   ├── adjustForN.html                 [LEGACY]
│   │       │   ├── blank.html                      [LEGACY]
│   │       │   ├── blank2.html                     [LEGACY]
│   │       │   ├── gradient.png                    [ASSET]
│   │       │   └── gradient2.png                   [ASSET]
│   │       ├── friday presentation/
│   │       │   ├── *.lyx / *.lyx~ — 9 LyX files   [ASSET]
│   │       │   └── outline2.pdf                    [ASSET]
│   │       └── septPresentation/
│   │           ├── outline.md                      [DRAFT] no frontmatter, presentation outline
│   │           ├── outlineCode.html                [LEGACY]
│   │           └── septWkspPresentOutline.lyx      [ASSET]
│   │
│   ├── teaching/
│   │   ├── 3012.html                               [LEGACY] (likely typo for 3102)
│   │   │
│   │   ├── 3102/
│   │   │   ├── equilibrium/
│   │   │   │   ├── consumer.html                   [LEGACY]
│   │   │   │   ├── consumerInteractive (2).html    [LEGACY]
│   │   │   │   ├── consumerInteractive.html        [LEGACY]
│   │   │   │   ├── equilibrium.html                [LEGACY]
│   │   │   │   ├── firm.html                       [LEGACY]
│   │   │   │   ├── solving.html                    [LEGACY]
│   │   │   │   ├── bigE.png                        [ASSET]
│   │   │   │   └── star.png                        [ASSET]
│   │   │   ├── interactive/
│   │   │   │   ├── ConsumerAndProducerInteractive.html    [LEGACY]
│   │   │   │   ├── OnePeriodEquilibiriumInteractive.html  [LEGACY]
│   │   │   │   ├── consumerInteractive.html        [LEGACY]
│   │   │   │   ├── exampleInteractive.html         [LEGACY]
│   │   │   │   ├── interactivegraphs.html          [LEGACY]
│   │   │   │   ├── producerInteractive.html        [LEGACY]
│   │   │   │   ├── solowInteractive.html           [LEGACY]
│   │   │   │   ├── twoPeriodEndowment.html         [LEGACY]
│   │   │   │   ├── twoPeriodEndowmentWithBorrowingLimits.html  [LEGACY]
│   │   │   │   ├── twoPeriodEndowmentWithDifferentRates.html   [LEGACY]
│   │   │   │   ├── change notes for format.txt     [ASSET]
│   │   │   │   ├── bigE.png                        [ASSET]
│   │   │   │   ├── smallE.png                      [ASSET]
│   │   │   │   ├── star.png                        [ASSET]
│   │   │   │   └── star2.png                       [ASSET]
│   │   │   ├── intertemporal/
│   │   │   │   ├── consumerProblemWithLabor.html   [LEGACY]
│   │   │   │   ├── creditFrictions.html            [LEGACY]
│   │   │   │   ├── firmProblem.html                [LEGACY]
│   │   │   │   ├── intertemporalCE_Definiton.html  [LEGACY]
│   │   │   │   ├── shifterExamples.html            [LEGACY]
│   │   │   │   ├── twoPeriodEndowment.html         [LEGACY]
│   │   │   │   ├── twoPeriodEndowment (2).html     [LEGACY]
│   │   │   │   ├── pythonhLaborCurveGenerator.py   [ASSET]
│   │   │   │   ├── bigE.png                        [ASSET]
│   │   │   │   ├── star.png                        [ASSET]
│   │   │   │   ├── images/ — 8 SVG diagram files   [ASSET]
│   │   │   │   └── intertemporal/
│   │   │   │       ├── equilibirumDefinition.html  [LEGACY]
│   │   │   │       ├── shifterExamples.html        [LEGACY]
│   │   │   │       └── images/ — 8 SVG files (duplicates of parent) [ASSET]
│   │   │   ├── test/
│   │   │   │   ├── CEInteractive.html              [LEGACY]
│   │   │   │   ├── consumerInteractive.html        [LEGACY]
│   │   │   │   ├── exampleInteractive.html         [LEGACY]
│   │   │   │   ├── producerInteractive.html        [LEGACY]
│   │   │   │   ├── bigE.png                        [ASSET]
│   │   │   │   └── star.png                        [ASSET]
│   │   │   └── typesetting/
│   │   │       ├── latexMath.html                  [LEGACY]
│   │   │       ├── lyxTutorial.html                [LEGACY]
│   │   │       ├── typesettingSoftware.html        [LEGACY]
│   │   │       ├── MSWordEqn.png                   [ASSET]
│   │   │       ├── MSWordMathMode.png              [ASSET]
│   │   │       ├── lyxEnvironments.png             [ASSET]
│   │   │       ├── lyxEqn.png                      [ASSET]
│   │   │       └── lyxMathMode.png                 [ASSET]
│   │   │
│   │   ├── typesetting/                            (duplicate of 3102/typesetting/)
│   │   │   ├── latexMath.html                      [LEGACY]
│   │   │   ├── lyxTutorial.html                    [LEGACY]
│   │   │   ├── typesettingSoftware.html            [LEGACY]
│   │   │   ├── MSWordEqn.png                       [ASSET]
│   │   │   ├── MSWordMathMode.png                  [ASSET]
│   │   │   ├── lyxEnvironments.png                 [ASSET]
│   │   │   ├── lyxEqn.png                          [ASSET]
│   │   │   └── lyxMathMode.png                     [ASSET]
│   │   │
│   │   └── 3102psets/
│   │       ├── HW1_dataGraphs.html                 [LEGACY]
│   │       ├── HW2_dataGraphs.html                 [LEGACY]
│   │       ├── HW1_GrowthGraphs/ — 60 country-specific SVG growth graphs  [ASSET]
│   │       ├── HW2_BCycleGraphs/ — 60 country-specific SVG business cycle graphs  [ASSET]
│   │       └── HWBCycles_old/
│   │           ├── dataResultsFlippedPercentDiff.html   [LEGACY]
│   │           ├── dataResultsOG.html              [LEGACY]
│   │           ├── dataResultsOnlyImages.html      [LEGACY]
│   │           ├── week9solutions.html             [LEGACY]
│   │           ├── SwedenNominal.xlsx              [ASSET]
│   │           ├── SwedenReal.xlsx                 [ASSET]
│   │           └── 60 country SVG graphs           [ASSET]
│   │
│   ├── nonsense/
│   │   └── mathsymbols.html                        [LEGACY]
│   │
│   └── presentations/
│       ├── biglisthtml.html                        [LEGACY]
│       ├── percolationSlides.html                  [LEGACY] Reveal.js slides
│       ├── bern/ — 10 SVG graph theory diagrams    [ASSET]
│       ├── breadth/ — 10 SVG graph theory diagrams [ASSET]
│       ├── 1D lattice.svg                          [ASSET]
│       ├── 2D lattice.svg                          [ASSET]
│       ├── 2DDual.svg                              [ASSET]
│       ├── Rado_graph.svg                          [ASSET]
│       ├── bipartite33.svg                         [ASSET]
│       ├── complete6.svg                           [ASSET]
│       ├── cycle6.svg                              [ASSET]
│       ├── examplenums.png                         [ASSET]
│       ├── numberLine.svg                          [ASSET]
│       ├── star6.svg                               [ASSET]
│       ├── star6v2.svg                             [ASSET]
│       ├── testGraphConnectedComponents.svg        [ASSET]
│       ├── testGraphE.svg                          [ASSET]
│       ├── testGraphElabel.svg                     [ASSET]
│       ├── testGraphNeighbor5.svg                  [ASSET]
│       ├── testGraphNeighborDegree.svg             [ASSET]
│       ├── testGraphNoPath.svg                     [ASSET]
│       ├── testGraphPath.svg                       [ASSET]
│       ├── testGraphRandom.svg                     [ASSET]
│       ├── testGraphV.svg                          [ASSET]
│       ├── testGraphVlabel.svg                     [ASSET]
│       ├── testgraph.png                           [ASSET]
│       ├── testgraph.svg                           [ASSET]
│       ├── testgraphE.png                          [ASSET]
│       ├── testgraphElabel.png                     [ASSET]
│       ├── testgraphV.png                          [ASSET]
│       ├── testgraphVlabel.png                     [ASSET]
│       ├── testvector.svg                          [ASSET]
│       ├── transmissionnetworks.png                [ASSET]
│       ├── vectorDoodles.svg                       [ASSET]
│       ├── worldgraphElectricity.svg               [ASSET]
│       ├── worldgraphGerm.svg                      [ASSET]
│       ├── worldgraphNerves.svg                    [ASSET]
│       ├── worldgraphRoads.svg                     [ASSET]
│       ├── worldgraphRumor.svg                     [ASSET]
│       └── worldgraphSocial.svg                    [ASSET]
│
│
│── ── STATIC ASSETS ─────────────────────────────────────
│
├── assets/
│   └── css/
│       └── extrabits.css                           [ASSET]
│
├── styles/ — 22 CSS/SCSS files                     [ASSET]
│   ├── main.scss                                   Sakura CSS variant
│   ├── sakura.css
│   ├── sakura.css.map
│   ├── sakuraBlue.css
│   ├── sakuraGreen.css
│   ├── sakuraPink.css
│   ├── sakuraPink - Copy.css
│   ├── sakuraUMN.css
│   ├── sakura_basic.css
│   ├── sakura copy.css
│   ├── sakura solarized test 2.css
│   ├── sakura-earthly.scss.txt
│   ├── sakura-paper.scss
│   ├── basic.css
│   ├── basic_sakura.css
│   ├── classless.css
│   ├── everythingbagel.css
│   ├── everythingbagel-JTD.css
│   ├── everythingbagel-lists.css
│   ├── panfried.css
│   ├── style.css
│   └── TODOsakuraSolar.css
│
├── font/ — 6 font files                           [ASSET]
│   ├── Catrinity.otf
│   ├── Catrinity.ttf
│   ├── codes.txt
│   ├── sdfsdfds.ttf
│   ├── strippedCards.ttf
│   └── strippedCards2.ttf
│
├── portraits/ — 9 headshot/portrait images         [ASSET]
│   ├── Marketing_PublicWebsite.jpeg
│   ├── headshot.webp
│   ├── headshot_bee_cropped - Copy.webp
│   ├── headshot_bee_cropped.webp
│   ├── headshot_bee_cropped3.webp
│   ├── headshotcircle.webp
│   ├── headshotsquare.webp
│   ├── suiteddie.webp
│   └── suiteddie2.webp
│
├── files/ — 6 downloadable documents               [ASSET]
│   ├── CV Robert Winslow.pdf
│   ├── CV - Robert Winslow - Jan 2025.docx
│   ├── CV Robert Winslow - Job Market.pdf
│   ├── 3102_s22_syllabus_compact.pdf
│   ├── 3102_s22_syllabus_comprehensive.pdf
│   └── ECON 330 Syllabus 2025 Fall.pdf
│
├── js/
│   └── katex/
│       ├── README.md                               [NAV-HIDDEN] KaTeX readme (nav_exclude + search_exclude)
│       ├── katexTest.html                          [LEGACY] KaTeX test page
│       ├── katex.css                               [ASSET]
│       ├── katex.min.css                           [ASSET]
│       ├── katex.js                                [ASSET]
│       ├── katex.min.js                            [ASSET]
│       ├── katex.mjs                               [ASSET]
│       ├── contrib/ — 17 JS/CSS files              [ASSET]
│       │   (auto-render, copy-tex, mathtex-script-type, mhchem, render-a11y-string)
│       └── fonts/ — 60 font files (ttf, woff, woff2)  [ASSET]
│
│
│── ── SUMMARY ───────────────────────────────────────────
│
│   NAV pages:              35
│   NAV-HIDDEN pages:       13
│   DRAFT files:             2
│   LEGACY HTML:           ~104
│   CONFIG files:            4
│   META files:              4  (+ this file)
│   ASSET files:           ~450+
│
│   Total files:           ~610  (excluding .git/)
```
