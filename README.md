# Kiran Upadhyay portfolio

A responsive static portfolio for AI, Agentic AI, and Python engineering opportunities.

## Preview and validation

```powershell
python scripts/build.py
node --check assets/js/theme.js
node --check assets/js/main.js
python -m http.server 4173 --bind 127.0.0.1
```

Open http://127.0.0.1:4173/. The build validates local links, IDs, metadata and JSON-LD, then copies the static entry point and assets to ignored `dist/`. There are no runtime dependencies, remote fonts, analytics, cookies or backend services. Theme preference is stored locally when available.

## GitHub Pages

The existing Pages configuration publishes `main` from `/` with the legacy Jekyll build. `_config.yaml` is retained unchanged. `index.html` is a static entry point without front matter and is copied by Jekyll alongside `assets/`. The build script is for local verification; `dist/` is not the Pages publishing source. No deployment workflow is added.

Review branch: `portfolio/ai-engineering-refresh`. Merging into `main` will trigger the existing Pages publication: merge only after owner approval.

## Content maintenance

Personal details and the unchanged downloadable PDF use the supplied Intel resume. Certifications are retained from the previous portfolio at the owner's request. Project claims are limited to the evidence described in [docs/CONTENT_SOURCES.md](docs/CONTENT_SOURCES.md). Keep benchmark scope and research limitations when updating metrics. Update dated PR statuses when reviewing contributions.

See [docs/REVIEW.md](docs/REVIEW.md) for design choices and validation results.
