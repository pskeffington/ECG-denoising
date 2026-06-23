# Prioritized Roadmap

**Project:** ECG denoising review-benchmark  
**Maintainer:** Paul Skeffington, MS, MPH  
**Status date:** 2026-06-23  
**Current stage:** v0.1.0 foundation to v0.2.0 executable baseline  
**Project classification:** non-operational academic/research scaffold

## Priority Order

### P0 — Research governance and exposure guardrails

This repository should remain clearly separated from operational systems. The current roadmap treats it as an academic/research benchmark scaffold for open ECG denoising methods, not as an operational medical, diagnostic, monitoring, surveillance, or deployment system.

**Actions**

- Keep the project framed as a reproducible review-benchmark, not an operational pipeline.
- Do not include clinical deployment instructions, live-monitoring claims, patient-specific decision logic, or production integration details.
- Keep raw PhysioNet data out of git.
- Keep local paths, credentials, API keys, and credentialed-data notes in ignored local configuration only.
- Keep filenames and object names plain Latin characters.
- Reassess repository visibility only if the scope changes toward unpublished sensitive methods, credentialed-data handling, or operational deployment.

**Exit criteria**

- Repository classification is explicit: non-operational academic/research scaffold.
- Public visibility is intentional only while the repository contains non-sensitive documentation, reproducible benchmark scaffolding, and no raw or credentialed data.
- No raw waveform data or local credentials are committed.
- `.gitignore` continues to block local environment files, data caches, build artifacts, and temporary output.

### P1 — Close foundation documentation gaps

The project scope, dataset inventory, noise taxonomy, method matrix seed, and benchmark protocol exist. The next action is to make the dataset and protocol documentation audit-ready.

**Actions**

- Update `docs/01_dataset_inventory.md` with citation/source fields for each dataset.
- Mark credentialed datasets clearly as Phase 2.
- Add acquisition notes without storing raw data.
- Confirm NSTDB as the first Phase 1 benchmark anchor.
- Recheck `docs/02_noise_taxonomy.md` for source, mechanism, clinical risk, and benchmark handling consistency.
- Recheck `docs/04_benchmark_protocol.md` against fixed SNR levels and morphology-preservation metrics.

**Exit criteria**

- Issue 002 acceptance criteria are fully satisfied.
- Issues 001, 003, and 005 can be closed after final review.

### P2 — Build executable benchmark skeleton

Move from documentation scaffold to reproducible code scaffold without committing raw data. Keep the implementation limited to offline benchmarking, synthetic/noise-injection experiments, and reproducible metric calculation.

**Proposed source layout**

```text
src/ecg_denoising/
├── __init__.py
├── cfg.py
├── data/
│   ├── __init__.py
│   ├── manifest.py
│   └── physionet.py
├── noise/
│   ├── __init__.py
│   ├── inject.py
│   └── synth.py
├── methods/
│   ├── __init__.py
│   ├── classical.py
│   └── wavelet.py
├── metrics/
│   ├── __init__.py
│   ├── signal_quality.py
│   └── morphology.py
└── bench/
    ├── __init__.py
    └── run.py
```

**Actions**

- Add `pyproject.toml` with minimal dependencies.
- Add typed configuration object for local data paths and output paths.
- Add manifest loader that reads metadata only.
- Add deterministic noise-injection utilities.
- Add baseline filters: high-pass, bandpass, notch, and bandpass-plus-notch.
- Add metric stubs for SNR improvement, RMSE, PRD, Pearson correlation, R-peak timing error, QRS distortion, and ST-segment preservation.
- Add tests for shape preservation, deterministic seeds, and no raw-data writes.

**Exit criteria**

- A clean environment can install the package.
- Tests run without requiring raw PhysioNet data.
- Benchmark code can operate on synthetic placeholder ECG arrays.
- No runtime path implies live clinical use or operational monitoring.

### P3 — Complete the method review matrix

The method matrix is seeded but not literature-complete.

**Actions**

- Index at least 25 ECG denoising studies.
- Classify each by method family, noise target, dataset, metric, reproducibility status, clinical-preservation measurement, and limitation.
- Separate generic signal-quality metrics from morphology-preservation claims.
- Flag papers that lack reproducible data or code.

**Exit criteria**

- Issue 004 acceptance criteria are satisfied.
- Matrix can support manuscript background and method selection.

### P4 — Produce baseline benchmark outputs

After the executable scaffold exists, run the first Phase 1 benchmark on open datasets or synthetic placeholders where dataset download is not available.

**Actions**

- Generate `results/baseline_signal_quality.csv`.
- Generate `results/morphology_preservation.csv`.
- Generate clean/noisy/denoised ECG overlay figures.
- Version output parameters and random seeds.
- Document preprocessing parameters.

**Exit criteria**

- Results are reproducible from a single offline command.
- Output tables match `docs/04_benchmark_protocol.md`.
- Figures are traceable to method, noise type, SNR level, and dataset source.
- Results are not represented as clinical validation or deployment evidence.

### P5 — Manuscript integration

Only after baseline outputs are reproducible, begin claims suitable for manuscript drafting.

**Actions**

- Draft Methods from the benchmark protocol.
- Draft Results only from reproducible tables and figures.
- Draft Limitations emphasizing open-data constraints, morphology validation limits, and dataset generalizability.
- Keep deep-learning claims conservative until a training and validation protocol exists.

**Exit criteria**

- Manuscript claims trace to repo artifacts.
- No method comparison is presented as final without documented preprocessing and metric validation.
- No claim implies operational readiness, diagnostic authority, or patient-care deployment.

## Immediate Action Queue

1. Keep repository classification explicit as non-operational research scaffold.
2. Update `docs/01_dataset_inventory.md` with source/citation fields.
3. Review and close issues 001, 003, and 005 if their acceptance criteria are met.
4. Keep issue 004 open until 25 studies are indexed.
5. Add `pyproject.toml` and the `src/ecg_denoising/` package skeleton.
6. Add tests for deterministic noise injection and signal-shape preservation.
7. Implement classical filters before wavelet methods.
8. Implement metric functions before producing comparative results.
9. Generate placeholder benchmark outputs using synthetic ECG-like arrays.
10. Replace placeholders with PhysioNet-backed runs only after dataset acquisition notes are complete.

## Recommended Next Milestone

**v0.2.0 executable baseline** should include explicit non-operational research classification, finalized Phase 1 dataset documentation, installable Python package scaffold, deterministic synthetic benchmark run, and passing tests that do not require raw external data.
