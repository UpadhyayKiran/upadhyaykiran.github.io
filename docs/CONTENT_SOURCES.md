# Content sources and accuracy boundaries

Reviewed 13 October 2026.

## Resume

Source: owner-specified `D:\Kiran_Resume\Kiran_Upadhyay_Intel.pdf`. The file is copied unchanged to `assets/docs/Kiran_Upadhyay_Intel.pdf`; both pages were visually inspected. Personal experience, education, skills, achievements, contact details, paper title and identifier follow this resume. The older existing README supplied certifications, explicitly retained by the owner. No individual credential URLs were supplied; the site links to the verified resume's LinkedIn profile without claiming independent credential verification.

ML ranks are identified as resume-listed achievements, without invented competition sponsors, dates, or public leaderboard evidence.

## GraphFix

Repository: https://github.com/UpadhyayKiran/GraphFix

Inspected commit: `e8f171561582722e26b3edb89b60d2d7dd52606a`.

Sources: `README.md`, `pyproject.toml`, `.github/workflows/ci.yml`, `src/graphfix/`, `results/phase1_evaluation_summary/full560_method_comparison.csv`, `results/adaptive_fixed_full560/full560_summary.json`, `docs/PHASE1_FINAL_RESULTS.md`.

The frozen 560-issue Loc-Bench V1 cohort reports BM25 file Hit@1 0.3000 and MRR 0.4152267574; Adaptive Fixed reports Hit@1 0.3946428571 and MRR 0.5019883787 (display rounded to 39.46% and 0.5020). Rankings use pre-fix snapshots with patch-derived gold evaluated post hoc. Bounded prompted graph navigation is validated by a deterministic environment; this is localization, not patch generation or an autonomous multi-agent platform. Neo4j export is optional and is not described as a core dependency.

## Biomedical RAG

Repository: https://github.com/UpadhyayKiran/Biomedical-RAG-Research-Assistant

Inspected commit: `be3fa194d8099355e928e90519d748f8106ec61c`.

Sources: `README.md`, `docs/ARCHITECTURE.md`, `docs/EVALUATION.md`, `data/corpus_manifest.csv`, and `biomedical_rag/` source.

152 processed documents, 2,267 chunks and 175 instruction examples are reported inspected local artifact counts. Manifest has 152 article entries. Full corpus/index/model assets are intentionally omitted from the public release, so the website attributes these counts to inspected local artifacts rather than independently recomputed public files. No performance accuracy, clinical reliability, calibrated confidence or autonomous multi-agent claim is published. Planning is rule-based and the final implementation uses fixed Python stages, not LangChain orchestration. Response validation checks formatting and patterns rather than medical factuality.

## Budget-Aware AutoLLM

Exact repository discovered through the user's GitHub repository list: https://github.com/UpadhyayKiran/Budget-Aware-AutoLLM

Inspected commit: `77aaf1b037bdf48fdec26385220279418e737809`.

Sources: `README.md`, `CITATION.cff`, `.github/workflows/ci.yml`, `src/budget_autollm/` strategy/routing contracts.

Five implemented reasoning strategies and four routing policies are component counts. Public release validation reports 27 successful executions, with three examples per dataset run. These are small integration checks. No estimator-based savings are presented as measured efficiency, no local estimated monetary cost is described as a billed charge, and no public full-benchmark result is inferred from these runs.

## Research paper

Owner-provided URL: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7544241

Title, sole authorship, SSRN preprint status, October 2026 and DOI follow the Intel PDF. The local final SSRN submission metadata and preprint abstract agree on 2,400 routed and 4,000 exhaustive executions across four benchmarks. Low-to-high budget-tier violation comparisons are explicitly distinguished from improvement over a baseline. The abstract also states conservative routing is not uniformly beneficial. This study is distinct from AutoLLM's public software release validation. SSRN returned 403 to automated requests, preventing independent public-page verification; no acceptance, peer review or conference publication is claimed.

## Open source

GitHub API verified these statuses on 13 October 2026:

- https://github.com/flet-dev/flet/pull/6770 — merged.
- https://github.com/statsmodels/statsmodels/pull/10326 — open.
- https://github.com/huggingface/optimum/pull/2502 — open.
- https://github.com/huggingface/huggingface_hub/pull/4963 — open.

Descriptions follow resume and PR metadata. Open work is never labeled merged.

## Links and privacy

GitHub, LinkedIn, Hugging Face, email and phone match the supplied PDF and its embedded links. LinkedIn returned 999 to automated requests; this is recorded as blocked verification, not a successful availability check. The downloadable PDF intentionally includes the public contact details requested by the owner. No form service, tracking script, credential, inference API, or uploaded model artifact is used.

## Final skills refinement - 14 October 2026

At the owner's explicit direction, MLOps, Docker, Kubernetes, AWS and CI/CD are listed under **Academic hands-on experience**. This is an academic experience qualification, not a production operations claim. The supplied Intel PDF remains unchanged; its replacement is deferred. Verified project descriptions and benchmark metrics are unchanged.
