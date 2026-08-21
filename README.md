# ECG Denoising

Author: Paul Skeffington, MS, MPH  
GitHub: `@pskeffington-github`  
Public contact: `paulskeffington@gmail.com`  
Repository status: executable non-clinical academic/research benchmark with a defined public freeze protocol  
Last documentation refresh: 2026-08-19

## Purpose

This repository is a reproducible review and benchmark framework for ECG noise-reduction methods using open PhysioNet datasets.

This repository contributes the **Biomedical Signal Evaluation** lane of the broader portfolio evidence chain.

## Public-Interest Research Boundary

This repository is maintained for biomedical engineering scholarship, open-data benchmark development, signal-quality documentation, and reproducible analysis. It supports non-clinical morphology-preservation review, benchmark governance, noise taxonomy, and human-reviewed research outputs.

It does not provide clinical advice, diagnostic interpretation, patient-level findings, device claims, biomedical deployment readiness, regulatory conclusions, or clinical-superiority claims. Outputs are intended to support documentation, quality review, and further research.

## Current Research Status

The repository now contains an executable Phase 1 NSTDB benchmark path through `wfdb`, synthetic benchmark-object validation artifacts, and a formal public benchmark freeze protocol. The first public freeze is bounded to 12 MIT-BIH Noise Stress Test Database electrode-motion records and four deterministic classical baselines, for an expected one-channel result cardinality of 48 rows before any documented exclusions.

A comparative public result is **not** claimed merely because the executable path or freeze protocol exists. Public comparative language remains gated on a completed freeze packet, reproducibility metadata, row-count reconciliation, result hashing, rerun agreement, and morphology-preservation review.

Raw PhysioNet waveform data remain outside git; only derived metrics, metadata, schemas, documentation, and reproducible code are appropriate for the public repository.

### Current Stage

- Stage: executable Phase 1 benchmark pathway with public freeze protocol
- Evidence status: schema/synthetic validation, executable real-data path, and freeze protocol present; reviewed comparative freeze pending
- Data status: versioned public PhysioNet data accessed through documented tooling; raw waveform data excluded from git
- Primary limitation: a reviewed full-record freeze packet and morphology-preservation gate are still required before comparative method claims

### Recent Progress

- Defined the public benchmark freeze contract for the Phase 1 NSTDB benchmark.
- Aligned the biomedical proof packet and terminology with the non-clinical research boundary.
- Reconciled the executable real-data path with public CV evidence language without promoting unsupported comparative claims.
- Preserved explicit separation between signal-quality benchmark execution and clinical or diagnostic validity.

### Next Actions

1. Execute and review the full Phase 1 benchmark configuration.
2. Record repository SHA, environment, dataset versions, command, parameters, row count, and result digest in a freeze metadata artifact.
3. Reconcile the expected 48-row one-channel benchmark cardinality with actual output and document any exclusions.
4. Re-run the frozen configuration and document numerical reproducibility tolerance.
5. Complete the morphology-preservation gate for R-peak timing, QRS distortion, and ST-segment handling before any comparative morphology claim.
6. Promote only reviewed, bounded evidence into the Portfolio evidence envelope and public CV surfaces.

## Portfolio Role

```text
Portfolio pillar: Biomedical Signal Evaluation
Primary object: benchmark_result
Candidate ML task: benchmark_result_outlier_detection
Current maturity: executable benchmark pathway; comparative public result freeze pending
```

The repository supports signal-integrity review, noise taxonomy, benchmark governance, and non-clinical morphology-preservation framing. It does not claim clinical validity, diagnostic utility, patient-level interpretation, denoising superiority, biomedical deployment readiness, or generalized model performance.

## Focus

This repository evaluates ECG denoising methods for baseline wander, muscle artifact, electrode-motion artifact, and powerline interference. The review emphasizes both signal-quality improvement and preservation of ECG morphology while keeping all claims non-clinical and research-bounded.

## Core Question

Among open ECG datasets, how do classical filtering, wavelet/time-frequency methods, and lightweight deep-learning denoisers compare in reducing common ECG noise while preserving waveform morphology under bounded, non-clinical benchmark conditions?

## Evidence Chain

```text
benchmark_result
  -> schema
  -> synthetic fixture
  -> benchmark readiness matrix
  -> benchmark validation report
  -> executable NSTDB benchmark path
  -> public benchmark freeze protocol
  -> reviewed freeze packet
  -> portfolio evidence envelope
  -> public-safe CV evidence
```

## Primary Contribution

The project contributes a reproducible review-benchmark framework that separates benchmark execution, signal-quality measurement, morphology-preservation review, and any later comparative interpretation. The intended contribution is benchmark governance and signal-integrity framing, not clinical validation.

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

## Real-Data Benchmark Path

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

The requirements for promoting a real-data result are defined in `docs/BENCHMARK_FREEZE_PROTOCOL.md`.

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

## Supported Contribution

```text
A reproducible biomedical signal benchmark pathway with explicit evidence-freeze, morphology-review, and claim-boundary controls.
```

## Unsupported Contribution

```text
No clinical validity, diagnostic utility, patient-level interpretation, denoising superiority, method endorsement, biomedical deployment readiness, or generalized model-performance claim is made.
```
