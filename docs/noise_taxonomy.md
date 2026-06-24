# ECG Noise Taxonomy

Author: Paul Skeffington, MS, MPH  
GitHub: `@pskeffington-github`  
Public contact: `paulskeffington@gmail.com`  
Status: v1 validation-support artifact  
Milestone: M2 Validation

## Purpose

This document defines the initial noise taxonomy for ECG denoising benchmark work. It supports reproducible comparison by separating noise type, source, severity, documentation status, and benchmark use.

The taxonomy is designed to support morphology-preservation benchmarking. Noise labels should help reviewers determine whether a denoising method improves signal quality without damaging clinically meaningful waveform structure.

## Operating Question

```text
What noise condition is being tested, how severe is it, and what morphology-preservation risks does it create?
```

## Noise Condition Object

```yaml
noise_condition:
  noise_id: string
  noise_type: string
  noise_family: string
  noise_source: string
  severity_level: string
  signal_to_noise_ratio: string
  affected_morphology: list
  injection_method: string
  reproducible_seed: string
  validation_status: string
  review_note: string
```

## Taxonomy Table

| Noise Type | Noise Family | Common Source | Morphology Risk | Benchmark Concern |
|---|---|---|---|---|
| `baseline_wander` | low_frequency_drift | respiration, movement, electrode drift | ST segment and amplitude distortion | May make ST and amplitude metrics unreliable. |
| `powerline_interference` | periodic_interference | electrical environment | false periodic artifact, amplitude masking | May inflate frequency-domain improvement claims. |
| `muscle_artifact` | high_frequency_biological | muscle activity | QRS edge and T-wave distortion | May damage high-frequency morphology if overfiltered. |
| `electrode_motion` | contact_artifact | sensor movement, poor contact | false peaks, amplitude shifts, dropouts | May create misleading peak-detection results. |
| `white_noise` | synthetic_random | injected benchmark noise | broad waveform degradation | Useful for reproducibility but limited realism. |
| `mixed_noise` | combined | overlapping sources | multiple simultaneous distortions | Harder to attribute method success or failure. |
| `unknown_or_unclassified` | unknown | undocumented | uncertain | Should not support strong claims. |

## Severity Levels

| Severity | Definition | Benchmark Use |
|---|---|---|
| `low` | Noise is visible but does not dominate the waveform. | Useful for sensitivity testing. |
| `moderate` | Noise affects interpretation of some waveform features. | Core benchmark condition. |
| `high` | Noise substantially disrupts morphology or peak detection. | Robustness testing only. |
| `extreme` | Signal may be partly unrecoverable. | Stress testing; avoid broad claims. |
| `unknown` | Severity has not been characterized. | Requires review before comparison. |

## Source Types

```text
observed
synthetic
augmented
mixed
unknown
```

Observed noise may better represent real-world signal degradation but is harder to control. Synthetic noise improves reproducibility but may not fully capture realistic artifact patterns.

## Morphology Risk Tags

Noise conditions should identify which waveform structures are at risk.

```text
p_wave
qrs_complex
r_peak
st_segment
t_wave
pr_interval
qt_interval
amplitude
beat_consistency
false_peak_risk
signal_dropout
```

## Validation Status

```text
draft
reviewed
validated
deprecated
```

A noise condition should not be used for comparative claims until it is at least `reviewed`.

## Minimum Review Checklist

A noise condition is review-ready when:

- the noise type is assigned
- the source is documented
- severity is defined or estimated
- signal-to-noise ratio is reported when available
- affected morphology tags are assigned
- synthetic injection method is documented when used
- random seed is recorded when applicable
- limitations are noted

## Example Noise Condition

```yaml
noise_condition:
  noise_id: "noise_0001"
  noise_type: "baseline_wander"
  noise_family: "low_frequency_drift"
  noise_source: "synthetic"
  severity_level: "moderate"
  signal_to_noise_ratio: "defined_in_fixture"
  affected_morphology:
    - "st_segment"
    - "amplitude"
  injection_method: "documented_synthetic_injection"
  reproducible_seed: "seed_0001"
  validation_status: "draft"
  review_note: "Synthetic example for benchmark-readiness testing only."
```

## ML Readiness

This taxonomy supports future machine-learning tasks only after deterministic benchmark objects are in place.

Candidate ML tasks:

```text
noise-condition classification
noise-severity triage
artifact-pattern clustering
morphology-risk prediction
outlier segment review
```

Minimum readiness requirements:

- noise labels are documented
- severity labels are reviewed
- source type is known
- morphology-risk tags are present
- reviewer notes are preserved
- claims remain bounded to tested datasets and conditions

## Claim Boundary

This taxonomy supports ECG denoising benchmark organization and reproducible evaluation. It does not establish diagnostic validity, clinical safety, or general performance across untested datasets, devices, patient populations, or clinical settings.

## Cross-Repository Alignment

| Repo | Alignment |
|---|---|
| `pskeffington/Portfolio` | Provides resilient-sensing evidence for proof packets. |
| `pskeffington/cipher-topology-lab` | Shares evaluation-readiness and claim-boundary discipline. |
| `pskeffington/authentication-audit-compiler` | Can audit benchmark runs, reviewer actions, and release packets. |
| `pskeffington/CDC-mod` | Links degraded-signal evaluation to health-security decision support. |
| `pskeffington/McDowell-County-Commission-on-Aging-Inc.` | Transfers risk-feature thinking to infrastructure sensing and monitoring. |
