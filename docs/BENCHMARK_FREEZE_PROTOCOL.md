# ECG Public Benchmark Freeze Protocol

## Purpose

This document defines the minimum evidence contract required before a real-data ECG benchmark result can be described as a reviewed public portfolio artifact. It governs evidence packaging, reproducibility, morphology-preservation review, and claim boundaries for the Phase 1 MIT-BIH Noise Stress Test Database (NSTDB) benchmark.

Passing this protocol does **not** establish clinical validity, diagnostic utility, device performance, deployment readiness, or denoising superiority. It establishes only that a bounded, non-clinical benchmark result has been generated and documented reproducibly enough for public scholarly review.

## Phase 1 benchmark object

The canonical benchmark object is produced by:

```bash
python scripts/run_nstdb_real_benchmark.py \
  --methods all \
  --output results/baseline_signal_quality.csv
```

A smoke run using `--sampto` is useful for pipeline verification but is not itself eligible for a public result freeze unless the sample bound is explicitly preserved in the artifact name and documentation.

## Dataset contract

Phase 1 uses the versioned PhysioNet paths encoded in the repository:

- noisy data: `nstdb/1.0.0`
- clean references: `mitdb/1.0.0`

The current benchmark set contains 12 electrode-motion noise records:

| Noisy record | Clean reference | SNR (dB) |
|---|---|---:|
| 118e_6 | 118 | -6 |
| 118e00 | 118 | 0 |
| 118e06 | 118 | 6 |
| 118e12 | 118 | 12 |
| 118e18 | 118 | 18 |
| 118e24 | 118 | 24 |
| 119e_6 | 119 | -6 |
| 119e00 | 119 | 0 |
| 119e06 | 119 | 6 |
| 119e12 | 119 | 12 |
| 119e18 | 119 | 18 |
| 119e24 | 119 | 24 |

Raw PhysioNet waveforms remain outside git. Only derived metrics and reproducibility metadata are eligible for the public repository.

## Method contract

The first public freeze is limited to the four deterministic classical baselines implemented in `src/ecg_denoising/methods/classical.py`:

1. `highpass`
2. `bandpass`
3. `notch`
4. `bandpass_notch`

Current default parameters are part of the evidence object and must be recorded with the freeze:

- high-pass cutoff: 0.5 Hz
- band-pass range: 0.5–40 Hz
- notch frequency: 60 Hz
- notch quality factor: 30
- Butterworth filter order: 4

Any parameter change creates a new benchmark configuration and must not overwrite a previously frozen result without an explicit version change.

## Expected result cardinality

For the current Phase 1 set:

- 12 NSTDB noisy records
- 4 classical methods
- 1 selected channel per run

Therefore a complete one-channel benchmark must contain exactly **48 derived result rows** before any documented exclusions.

If a row is excluded or fails, the freeze packet must record:

- record identifier
- method
- failure or exclusion reason
- whether the exclusion was decided before or after metric inspection

Silent row removal is not permitted.

## Canonical result schema

`results/baseline_signal_quality.csv` must preserve the repository-defined fields in this order:

1. `dataset`
2. `record`
3. `clean_record`
4. `method`
5. `snr_level_db`
6. `channel`
7. `sample_rate`
8. `n_samples`
9. `rmse`
10. `prd`
11. `pearson_corr`
12. `snr_improvement_db`

Required structural checks:

- dataset value is `nstdb`
- all record / clean-reference pairs match the Phase 1 registry
- all four methods are represented for every included record
- SNR levels match the registry
- channel is constant within a single freeze unless multi-channel analysis is explicitly declared
- `sample_rate` and `n_samples` are present and positive
- metric fields are finite numeric values
- row count matches the expected cardinality after documented exclusions

## Reproducibility metadata

Every public freeze must include a companion metadata file containing at minimum:

- freeze date in UTC
- repository commit SHA used for execution
- Python version
- package/environment lock or dependency snapshot
- PhysioNet dataset paths and versions
- command used to execute the benchmark
- selected channel
- `sampto` value or explicit `null/full-record` declaration
- method names and parameter values
- expected row count
- actual row count
- SHA-256 digest of the result CSV
- reviewer name or review state

Suggested path:

```text
results/baseline_signal_quality.freeze.json
```

## Morphology-preservation gate

The signal-quality table alone is insufficient for a comparative portfolio claim. Before method-level comparative language is promoted, the freeze must also document morphology-preservation review appropriate to the repository's stated scope.

Minimum gate:

- R-peak timing preservation method defined and reproducible
- QRS distortion measure defined and reproducible
- ST-segment preservation approach defined or explicitly deferred with rationale
- failure thresholds or review criteria declared before comparative interpretation
- any records with unstable or uninterpretable morphology metrics flagged rather than silently removed

Until this gate passes, public language must remain at the level of **benchmark execution and signal-quality measurement**, not method superiority.

## Review checklist

A result packet is eligible for public scholarly freeze only when all items below are satisfied:

- [ ] Full benchmark command recorded.
- [ ] Repository commit SHA recorded.
- [ ] PhysioNet versions recorded.
- [ ] Result CSV exists and matches the canonical schema.
- [ ] Expected row cardinality reconciled with actual rows.
- [ ] No undocumented exclusions.
- [ ] Method parameters recorded.
- [ ] Result CSV SHA-256 recorded.
- [ ] Re-run from the same configuration reproduces the result within declared numerical tolerance.
- [ ] Morphology-preservation gate reviewed.
- [ ] Limitations and non-clinical boundary retained.
- [ ] No diagnostic, device, deployment, or clinical-superiority language introduced.

## Allowed public claims after structural freeze only

Examples of bounded claims that become supportable once the structural/reproducibility portion of this protocol passes:

- "Implemented and reproducibly executed a versioned NSTDB/WFDB ECG denoising benchmark across deterministic classical baselines."
- "Produced a provenance-controlled signal-quality table spanning defined electrode-motion noise levels and classical filtering methods."
- "Built reproducibility controls linking PhysioNet versions, filter parameters, benchmark rows, and derived signal-quality metrics."

These claims do not require comparative superiority.

## Claims requiring the morphology-preservation gate

Comparative statements about preserving ECG morphology, reducing distortion, or identifying a preferable method require the morphology-preservation gate plus a reviewed result table. Any such claim must state the benchmark scope and must not be generalized to clinical performance.

## Unsupported claims

This protocol does not support statements that a method:

- improves diagnosis
- improves patient outcomes
- is clinically validated
- is safe for patient monitoring
- is suitable for a medical device
- is superior in clinical practice
- preserves clinically meaningful morphology under all conditions

## Promotion rule for the CV portfolio

The ECG project may be described as an **executable biomedical signal benchmark** now. It should be promoted to a **demonstrated comparative biomedical result** only after a reviewed freeze packet satisfies this protocol and the corresponding evidence files are committed.
