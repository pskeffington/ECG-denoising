# ECG Denoising

Author: Paul Skeffington, MS, MPH  
GitHub: `@pskeffington-github`  
Public contact: `paulskeffington@gmail.com`  
Repository status: non-operational academic/research benchmark scaffold  
Last documentation refresh: 2026-06-25

## Purpose

This repository is a reproducible review and benchmark scaffold for ECG noise-reduction methods using open PhysioNet datasets.

This repository contributes the **Resilient Sensing** lane of the broader portfolio evidence chain.

## Portfolio role

```text
Portfolio pillar: Resilient Sensing
Primary object: benchmark_result
Candidate ML task: benchmark_result_outlier_detection
Current maturity: established synthetic benchmark-result evidence
```

The repository supports signal-integrity review, noise taxonomy, benchmark governance, and non-clinical morphology-preservation framing. It does not claim clinical validity, diagnostic utility, patient-level interpretation, denoising superiority, biomedical deployment readiness, or model performance.

## Focus

This repository evaluates ECG denoising methods for baseline wander, muscle artifact, electrode-motion artifact, and powerline interference. The review emphasizes both signal-quality improvement and preservation of clinically relevant ECG morphology while keeping all claims non-clinical and research-bounded.

## Core question

Among open ECG datasets, how do classical filtering, wavelet/time-frequency methods, and lightweight deep-learning denoisers compare in reducing common ECG noise while preserving waveform morphology under bounded, non-clinical benchmark conditions?

## Evidence chain

```text
benchmark_result
  -> schema
  -> synthetic fixture
  -> benchmark readiness matrix
  -> benchmark validation report
  -> benchmark outlier detection task card
  -> feature registry representation in Portfolio
  -> synthetic feature dataset row in Portfolio
  -> generated validation result in Portfolio
  -> HSE alignment proof packet
```

## Current update — 2026-06-25

The repository is moving from v0.1.0 foundation mode toward a v0.2.0 executable benchmark scaffold. The current code supports synthetic tests and the first real-data NSTDB benchmark path through `wfdb`. Raw PhysioNet waveform data remain outside git.

## Primary contribution

The project contributes a reproducible review-benchmark framework that separates general signal-quality improvement from morphology-preservation review. The intended contribution is benchmark governance and signal-integrity framing, not clinical validation.

## Phase 1 datasets

- MIT-BIH Noise Stress Test Database
- MIT-BIH Arrhythmia Database
- PTB-XL
- PTB-XL+

## Phase 2 datasets

- MIMIC-IV-ECG
- MIMIC-III Waveform Database

## Method families

- Classical filters
- Adaptive filters
- Wavelet and time-frequency methods
- Lightweight deep-learning denoisers

## Primary metrics

- SNR improvement
- RMSE
- PRD
- Pearson correlation
- R-peak timing error
- QRS distortion
- ST-segment preservation

## Real-data benchmark path

Install the package locally:

```bash
python -m pip install -e ".[dev]"
```

Run the full baseline signal-quality table by streaming public records through WFDB. Use `--sampto` for a short smoke run before running full records:

```bash
python scripts/run_nstdb_real_benchmark.py --methods all --sampto 5000 --output results/baseline_signal_quality.csv
```

Run a subset of methods:

```bash
python scripts/run_nstdb_real_benchmark.py --methods bandpass,bandpass_notch --sampto 5000 --output results/baseline_signal_quality.csv
```

Optionally cache Phase 1 files outside git:

```bash
python scripts/fetch_phase1_data.py --data-root ../ecg_data
```

Then run from the local cache:

```bash
python scripts/run_nstdb_real_benchmark.py --data-root ../ecg_data --methods all --sampto 5000 --output results/baseline_signal_quality.csv
```

## Repository structure

```text
.
├── docs/
├── data_manifest/
├── manuscript/
├── notebooks/
├── results/
├── scripts/
├── src/
└── tests/
```

## Supported contribution

```text
A resilient-sensing benchmark pathway for synthetic outlier-review planning, noise-taxonomy review, and morphology-preservation governance.
```

## Unsupported contribution

```text
No clinical validity, diagnostic utility, patient-level interpretation, denoising superiority, method endorsement, biomedical deployment readiness, or model-performance claim is made.
```

## Next targeted progression

```text
1. Refresh benchmark_result proof packet.
2. Add public-safe benchmark summary for Portfolio alignment.
3. Keep all claims non-clinical and benchmark-governance oriented.
4. Mirror any validated benchmark feature updates into Portfolio feature-registry artifacts.
```

## Current stage

v0.2.0 scaffold in progress: non-operational research classification, Phase 1 dataset inventory, installable Python package scaffold, synthetic tests, validated classical baseline filters, and first real-data NSTDB benchmark table path through PhysioNet/WFDB.
