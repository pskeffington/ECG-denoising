# Status and Roadmap

## Current status

**Early-stage methods development.**

This repository supports an ECG denoising and signal-quality benchmark direction aligned with open medical data and reproducible biomedical AI evaluation. It should remain a methods-development workspace until the dataset, noise taxonomy, benchmark baselines, and clinical morphology metrics are selected.

## Public-facing status language

Use the following wording in CV, portfolio, and public research-status outputs:

> ECG denoising and signal-quality benchmark scaffold aligned with open medical data and reproducible biomedical AI evaluation; dataset, noise classes, methods, and results tables remain pending.

## Near-term roadmap

1. Select a public ECG dataset and record source terms.
2. Define noise classes and stress-test conditions.
3. Choose baseline denoising methods.
4. Define morphology-preservation metrics, including QRS and ST-segment checks where feasible.
5. Create method-comparison and morphology-preservation result-table templates.
6. Add a minimal reproducible benchmark script.

## Validation gates

- Do not claim clinical performance until benchmark results are generated and reviewed.
- Keep signal-quality and morphology-preservation claims separate from diagnostic claims.
- Maintain dataset provenance and license constraints.

## Roadmap priority

Medium priority as a biomedical AI evaluation proof packet after higher-priority journal review and infrastructure-risk work are stabilized.
