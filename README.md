# ECG Denoising

Reproducible review and benchmark of ECG noise-reduction methods using open PhysioNet datasets.

**Maintainer:** Paul Skeffington, MS, MPH  
**Repository status:** non-operational academic/research benchmark scaffold; no method comparison should be treated as final until dataset access, preprocessing, and metric-validation checks are documented.  
**Last documentation refresh:** 2026-06-23

## Focus

This repository evaluates ECG denoising methods for baseline wander, muscle artifact, electrode-motion artifact, and powerline interference. The review emphasizes both signal-quality improvement and preservation of clinically relevant ECG morphology.

## Core Question

Among open ECG datasets, how do classical filtering, wavelet/time-frequency methods, and lightweight deep-learning denoisers compare in reducing common ECG noise while preserving clinically relevant waveform morphology?

## Current update — 2026-06-23

The repository is moving from v0.1.0 foundation mode toward a v0.2.0 executable benchmark scaffold. The current code supports synthetic placeholder tests and the first real-data NSTDB benchmark path through `wfdb`. Raw PhysioNet waveform data remain outside git.

## Primary Contribution

The project contributes a reproducible review-benchmark framework that separates general signal-quality improvement from clinically relevant ECG morphology preservation.

## Phase 1 Datasets

- MIT-BIH Noise Stress Test Database
- MIT-BIH Arrhythmia Database
- PTB-XL
- PTB-XL+

## Phase 2 Datasets

- MIMIC-IV-ECG
- MIMIC-III Waveform Database

## Method Families

- Classical filters
- Adaptive filters
- Wavelet and time-frequency methods
- Lightweight deep-learning denoisers

## Primary Metrics

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

Run the first real-data NSTDB benchmark by streaming public records through WFDB. Use `--sampto` for a short smoke run before running full records:

```bash
python scripts/run_nstdb_real_benchmark.py --sampto 5000 --output results/baseline_signal_quality.csv
```

Optionally cache Phase 1 files outside git:

```bash
python scripts/fetch_phase1_data.py --data-root ../ecg_data
```

Then run from the local cache:

```bash
python scripts/run_nstdb_real_benchmark.py --data-root ../ecg_data --sampto 5000 --output results/baseline_signal_quality.csv
```

## Repository Structure

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

## Current Stage

v0.2.0 scaffold in progress: non-operational research classification, Phase 1 dataset inventory, installable Python package scaffold, synthetic tests, and first real-data NSTDB benchmark path through PhysioNet/WFDB.
