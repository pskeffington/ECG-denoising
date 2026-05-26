# ECG Denoising

Reproducible review and benchmark of ECG noise-reduction methods using open PhysioNet datasets.

**Maintainer:** Paul Skeffington, MS, MPH  
**Repository status:** active benchmark scaffold; no method comparison should be treated as final until dataset access, preprocessing, and metric-validation checks are documented.  
**Last documentation refresh:** 2026-05-26

## Focus

This repository evaluates ECG denoising methods for baseline wander, muscle artifact, electrode-motion artifact, and powerline interference. The review emphasizes both signal-quality improvement and preservation of clinically relevant ECG morphology.

## Core Question

Among open ECG datasets, how do classical filtering, wavelet/time-frequency methods, and lightweight deep-learning denoisers compare in reducing common ECG noise while preserving clinically relevant waveform morphology?

## Current update — 2026-05-26

The repository remains in v0.1.0 foundation mode. The current documentation priority is to keep the dataset inventory, noise taxonomy, method matrix, benchmark protocol, and morphology-preservation metrics explicit before adding comparative results or manuscript claims.

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

## Repository Structure

```text
.
├── docs/
├── data_manifest/
├── manuscript/
├── notebooks/
├── results/
└── src/
```

## Current Stage

v0.1.0 foundation: scope, dataset inventory, noise taxonomy, method matrix, benchmark protocol, and morphology-preservation metric planning. Documentation refreshed on 2026-05-26.
