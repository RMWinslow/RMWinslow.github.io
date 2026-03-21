# RMWinslow.github.io

Robert Winslow's personal academic website, deployed at
[www.rmwinslow.com](https://www.rmwinslow.com).

The homepage is a standalone HTML page (`index.html`). Everything else uses
[JTD-RMW](https://github.com/RMWinslow/JTD-RMW), a fork of the Just the Docs
Jekyll theme, which generates a navigation sidebar with collapsible nested
links.

## What's in this repo

- **`research/`** — Research project pages (job market paper, contagion model,
  etc.) and PDFs.
- **`teaching/`** — Teaching pages (Econ 3102, Econ 330 with homework).
- **`redirects/`** — Redirect stubs for content that has moved to other repos.
  See `redirects/INDEX.md` for the full inventory.
- **`assets/css/`** — Shared stylesheets (sakura variants, etc.) used by both
  this repo and the legacy HTML files in the notes repo.
- **`_layouts/`** — A single custom layout (`default_basic.html`).
- **`files/`** — Downloadable files (CV PDFs).

## Subsites

The full website is split across several repos, all served as subdirectories
of `www.rmwinslow.com` and sharing the JTD-RMW theme:

| Repo | URL | Description |
|------|-----|-------------|
| [**posts**](https://github.com/RMWinslow/posts) | [/posts](https://www.rmwinslow.com/posts) | Blog — a wide variety of posts on economics, language, science, games, and miscellany. |
| [**notes**](https://github.com/RMWinslow/notes) | [/notes](https://www.rmwinslow.com/notes) | Economics teaching notes, interactive graphs, prelim study notes, and legacy course materials. |
| [**bib**](https://github.com/RMWinslow/bib) | [/bib](https://www.rmwinslow.com/bib) | Bibliography — reading notes and paper references. |
| [**games**](https://github.com/RMWinslow/games) | [/games](https://www.rmwinslow.com/games) | Card and board game rules, plus interactive tools. |
| [**circe**](https://github.com/RMWinslow/circe) | [/circe](https://www.rmwinslow.com/circe) | An annotated edition of Giovanni Battista Gelli's *La Circe*. |

There are also a few older repos on different themes
that haven't been consolidated:

| Repo | Description |
|------|-------------|
| [**tones**](https://github.com/RMWinslow/tones) | A piano widget (uses an older JTD fork). |
| [**mynotes**](https://github.com/RMWinslow/mynotes) | Older economics notes (Minimal Mistakes theme). Planned for consolidation into the notes repo. |
| [**macronotes**](https://github.com/RMWinslow/macronotes) | Macro notes (original unmodified JTD). |

