<!-- claude-generated -->

# Migration Note for `econ/research/`

This directory contains early research working files — Python simulations, LyX
drafts, presentation materials, and exploratory HTML writeups — that predate the
current organization of Robert's repos. The files were actively committed between
roughly January and October 2020, but have not been meaningfully edited since.

The full commit history for this directory is available at:
https://github.com/RMWinslow/RMWinslow.github.io/commits/master/econ/research

## What's here

- **`ContagionThing/`** — The largest subdirectory (~80 files). Contains Python
  SIR simulations, LyX math writeups, oral prelim presentation drafts, gradient
  plotter visualizations, and 28 unlabeled `pasted*.png` screenshots. This is
  the early-stage working directory for what became the contagion/network
  epidemics research project.

- **`farmingToy/`** — A toy trade model exploring autarky and specialization.
  Contains a LyX draft, a Python equilibrium calculator, and two HTML writeups
  that work through the math with emoji variable names.

- **`arrowroot/`** — Notes on Arrow-Debreu / root-related incentive problems.
  Three HTML pages and a PDF.

- **`FIFA/`** — A short auction idea writeup and two versions of a draft PDF.

- **Loose files** — `halfbakedideas.html`, `readingnotes.html`,
  `talkNotes.html` (research notes and talk prep), an IO pricing PDF, and an
  `img/` folder with house doodles for a rent control example.

## Where it's going

These files are being moved to the `papersdrafts` repo. The contagion-related
material belongs alongside the existing `contagion/` directory there, which
contains the more recent and organized versions of that research. The other
files can be sorted into `_mini_projects/` or `_ideas/` as appropriate.

This directory does not contain teaching notes and should not be included in the
`notes` repo migration.
