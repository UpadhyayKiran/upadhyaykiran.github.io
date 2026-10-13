# Portfolio review

## Proposed design

An editorial portfolio with warm ivory, ink blue and teal, large type, an illustrated engineering-focus diagram, and a project-first reading order. System fonts eliminate font downloads. Dark mode follows system preference until the visitor explicitly chooses a theme. Short entrance and hover animations respect reduced-motion preferences.

Sections: introduction, three featured projects with evidence and architecture, SSRN research, experience, open-source PRs, technical skills, education, retained certifications, resume-listed achievements, contact and resume download.

## Deployment boundary

Original base: `86c304a` on `main`. Pages API confirmed legacy build, `main` branch, `/` source, HTTPS enabled, no custom domain, no Actions workflows. `_config.yaml` is unchanged. The review branch cannot publish through the existing branch-based Pages setup. No merge or deployment has been performed.

## Validation

Final results are recorded here after checks complete. Automated accessibility results complement visual and keyboard checks; they do not certify complete accessibility compliance.

### Design previews

[Desktop light](preview/1440-light.png) · [Desktop dark](preview/1440-dark.png) · [Mobile light](preview/390-light.png) · [Mobile dark](preview/390-dark.png)

### Completed checks

- Static build: `python scripts/build.py`; all local navigation targets, assets, metadata, JSON-LD and unique IDs pass. Generated `dist/` served successfully. JavaScript syntax passes `node --check` for both files.
- Chrome/Playwright: 320, 390, 768 and 1440 CSS pixels, light and dark. No horizontal overflow or page errors. axe WCAG 2 A/AA and 2.1 AA checks: zero violations in all eight combinations.
- Keyboard: first Tab reaches the skip link; activation transfers focus to main. Focus indicators and navigation inspected. Resume download returns the correct filename. Theme selection survives reload.
- Resilience: system light/dark preferences, disabled JavaScript, unavailable localStorage, reduced motion, and a 640 CSS pixel viewport pass. No-JS content and navigation remain available; theme control hides gracefully.
- Visual: desktop light/dark, mobile sections and both pages of the supplied PDF inspected. PDF is unchanged, verified SHA-256 `076862abb1208958b62dd420833990d1cc5a4df9814232d35bf8f4e5fc315367`.
- Links: all 11 unique GitHub URLs, Hugging Face profile, and canonical site return 200. SSRN returns 403 and LinkedIn 999 to automated clients. Both use resume-verified URLs; automated public-page availability remains unverified. Email/phone match the supplied PDF; no test email or phone call was sent.
- Gitleaks 8.30.1: working directory and all four original commits scanned with zero findings. Its Windows download checksum matched the official release checksums. Extracted resume text also checked for common credential patterns with no matches. Personal contact data is intentionally included.
- Existing `_config.yaml` unchanged; no deployment workflow, hosting identity or Pages settings modified. The initial review used a static copy build; the final refinement below also verifies a complete local Jekyll build. Actual Pages publication is intentionally deferred until approval.

Machine-readable results are in [validation/](validation/). Browser tests use an isolated QA directory outside the website checkout; no browser testing dependencies are shipped to visitors. Lighthouse values are local lab measurements, not production field data. Existing Pages caching headers are outside the static site's control.

- Final local mobile Lighthouse: Performance 100, Accessibility 100, Best Practices 100, SEO 100. FCP 1.1 s; LCP 1.2 s; TBT 0 ms; CLS 0.001; initial transfer approximately 37 KiB. The additional label/name mismatch audit passes after correcting the logo accessible name.


## Final refinements - 14 October 2026

Added MLOps, Docker, Kubernetes, AWS and CI/CD under an explicit **Academic hands-on experience** label in the existing technical skills section. The design, verified project descriptions and benchmark metrics remain unchanged. The Intel PDF remains byte-identical to the previous commit and the owner-specified file; a general-purpose replacement is deferred.

Validation rerun after the skills edit:

- Static build, all local links/assets, IDs, metadata and JSON-LD pass.
- Both JavaScript files pass syntax checks; `git diff --check` passes.
- Chrome/axe at 320, 390, 768 and 1440 pixels in light/dark: zero tagged WCAG A/AA violations, horizontal overflow or page errors. Keyboard skip focus, theme persistence and PDF download pass.
- Skills section visually inspected at desktop and mobile widths.
- Gitleaks working-tree scan: zero findings.
- Automated comparison confirms project, research, experience and contribution content unchanged. PDF SHA-256 remains `076862abb1208958b62dd420833990d1cc5a4df9814232d35bf8f4e5fc315367`.
- Pages API still reports legacy Jekyll publication from `main` at `/`; configuration is unchanged. No merge or deployment performed.

Lighthouse scores above are from the initial review, not a fresh audit for this text-only refinement.

### Jekyll compatibility verified

Docker was available although native Ruby/Jekyll were absent. An isolated official `ruby:3.3` container installed `github-pages` 232, then successfully ran Jekyll 3.10.0 with the existing configuration:

```sh
jekyll build --source /src --destination /tmp/portfolio-site --config /src/_config.yaml
```

The checkout was mounted read-only and output remained temporary inside the container. Build completed successfully in 0.656 seconds. `cmp` verified that the generated `index.html` and downloadable Intel PDF were byte-identical to their source files. No Gemfile, dependency lockfile, theme, configuration or deployment workflow change was required. This is a local compatibility check, not a live Pages deployment.
