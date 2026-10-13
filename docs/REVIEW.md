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
- Existing `_config.yaml` unchanged; no deployment workflow, hosting identity or Pages settings modified. The local copy build verifies static assets, not a complete local Jekyll execution. Actual Pages publication is intentionally deferred until approval.

Machine-readable results are in [validation/](validation/). Browser tests use an isolated QA directory outside the website checkout; no browser testing dependencies are shipped to visitors. Lighthouse values are local lab measurements, not production field data. Existing Pages caching headers are outside the static site's control.

- Final local mobile Lighthouse: Performance 100, Accessibility 100, Best Practices 100, SEO 100. FCP 1.1 s; LCP 1.2 s; TBT 0 ms; CLS 0.001; initial transfer approximately 37 KiB. The additional label/name mismatch audit passes after correcting the logo accessible name.
