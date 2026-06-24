# Morphology Metric Dictionary

Author: Paul Skeffington, MS, MPH  
GitHub: `@pskeffington-github`  
Public contact: `paulskeffington@gmail.com`  
Repository: `pskeffington/ECG-denoising`  
Status: draft v1  
Milestone: M2 Validation

## Purpose

This document defines the initial morphology metric dictionary for ECG denoising benchmark work. It supports morphology-preservation review, benchmark comparability, signal-integrity validation, and responsible resilient-sensing evaluation.

The dictionary separates general noise reduction from preservation of waveform structures needed for trustworthy downstream interpretation.

## Operating Question

```text
Which waveform features must be preserved, how should preservation be measured, and what limitations bound the resulting claim?
```

## Metric Object Model

Each metric should be represented as a small, reviewable object.

```yaml
morphology_metric:
  metric_id: string
  metric_name: string
  metric_family: string
  target_feature: string
  required_inputs:
    - string
  calculation_summary: string
  preferred_unit: string
  interpretation: string
  known_limitations:
    - string
  review_status: string
  claim_boundary: string
```

## Feature Families

| Feature Family | Description | Primary Risk During Denoising |
|---|---|---|
| `p_wave` | Atrial depolarization feature visibility and shape. | Low-amplitude features may be smoothed away. |
| `qrs_complex` | Ventricular depolarization shape, width, and energy. | Sharp morphology may be distorted or over-smoothed. |
| `r_peak` | Peak timing and detectability. | False peaks, missed peaks, or shifted timing. |
| `st_segment` | Segment shape and deviation after QRS. | Baseline correction can distort ST morphology. |
| `t_wave` | Repolarization feature shape and amplitude. | Broad low-frequency features may be altered. |
| `intervals` | PR, QRS, QT, and beat-to-beat timing. | Filtering can shift boundaries or feature timing. |
| `amplitude` | Relative waveform amplitude preservation. | Normalization or filtering can change magnitude relationships. |
| `beat_consistency` | Consistency across consecutive beats. | Method may preserve isolated beats but fail across sequences. |

## Initial Metric Registry

| Metric ID | Metric Name | Family | Target Feature | Unit | Interpretation | Review Status |
|---|---|---|---|---|---|---|
| mm_001 | r_peak_localization_error | peak_alignment | r_peak | milliseconds | Lower error indicates better peak timing preservation. | draft |
| mm_002 | qrs_duration_error | interval_stability | qrs_complex | milliseconds | Lower error indicates better QRS width preservation. | draft |
| mm_003 | qrs_amplitude_error | amplitude_error | qrs_complex | normalized amplitude | Lower error indicates better amplitude preservation. | draft |
| mm_004 | st_segment_deviation_error | morphology_distortion | st_segment | millivolts or normalized amplitude | Lower error indicates less ST distortion. | draft |
| mm_005 | p_wave_preservation_score | waveform_similarity | p_wave | score | Higher score indicates better preservation of low-amplitude P-wave structure. | draft |
| mm_006 | t_wave_preservation_score | waveform_similarity | t_wave | score | Higher score indicates better T-wave morphology preservation. | draft |
| mm_007 | beat_detection_agreement | peak_alignment | r_peak | percent agreement | Higher agreement indicates fewer missed or false beats. | draft |
| mm_008 | false_peak_rate | morphology_distortion | r_peak | rate | Lower rate indicates fewer artifact-induced peaks. | draft |
| mm_009 | morphology_distortion_flag_rate | morphology_distortion | multiple | rate | Lower rate indicates fewer visually or algorithmically unacceptable distortions. | draft |
| mm_010 | beat_to_beat_consistency_error | interval_stability | beat_consistency | score or milliseconds | Lower error indicates better sequence-level morphology stability. | draft |

## Metric Definitions

### mm_001: r_peak_localization_error

Purpose:

Measure timing shift between reference R-peak locations and denoised-output R-peak locations.

Required inputs:

```text
reference_r_peak_locations
denoised_r_peak_locations
sampling_rate_hz
```

Claim boundary:

This metric supports peak-timing review only. It does not prove diagnostic validity or full morphology preservation.

### mm_002: qrs_duration_error

Purpose:

Measure difference between reference QRS duration and denoised-output QRS duration.

Required inputs:

```text
reference_qrs_onset_offset
denoised_qrs_onset_offset
sampling_rate_hz
```

Claim boundary:

This metric supports QRS width preservation review only when onset and offset annotations are reliable.

### mm_003: qrs_amplitude_error

Purpose:

Measure amplitude distortion in the QRS complex after denoising.

Required inputs:

```text
reference_qrs_amplitude
denoised_qrs_amplitude
normalization_method
```

Claim boundary:

Amplitude comparisons are sensitive to preprocessing and normalization decisions.

### mm_004: st_segment_deviation_error

Purpose:

Measure ST-segment distortion introduced or preserved after denoising.

Required inputs:

```text
reference_st_segment_value
denoised_st_segment_value
reference_point_definition
```

Claim boundary:

This metric is clinical-adjacent and must not be used for diagnostic claims without separate clinical validation.

### mm_005: p_wave_preservation_score

Purpose:

Assess whether low-amplitude P-wave morphology remains visible or structurally similar after denoising.

Required inputs:

```text
reference_p_wave_window
denoised_p_wave_window
similarity_metric
review_flag
```

Claim boundary:

This metric supports benchmark review only and requires caution because P-wave annotations may be limited.

### mm_006: t_wave_preservation_score

Purpose:

Assess whether T-wave shape is preserved after denoising.

Required inputs:

```text
reference_t_wave_window
denoised_t_wave_window
similarity_metric
review_flag
```

Claim boundary:

This metric supports morphology-preservation review only and does not establish clinical interpretation safety.

### mm_007: beat_detection_agreement

Purpose:

Compare beat-detection agreement between reference and denoised signal outputs.

Required inputs:

```text
reference_beat_labels
denoised_beat_labels
matching_tolerance_ms
```

Claim boundary:

Agreement supports downstream task readiness review but does not prove diagnostic performance.

### mm_008: false_peak_rate

Purpose:

Estimate artifact-induced false peaks after denoising.

Required inputs:

```text
reference_peak_set
denoised_peak_set
matching_tolerance_ms
segment_duration_seconds
```

Claim boundary:

False-peak rate depends on detector configuration and should be interpreted with detector limitations.

### mm_009: morphology_distortion_flag_rate

Purpose:

Track outputs flagged as morphologically unacceptable by rule-based or reviewer-based criteria.

Required inputs:

```text
reviewed_segments
distortion_flags
reviewer_or_rule_source
```

Claim boundary:

Reviewer-based flags require adjudication rules and should not be treated as universal labels.

### mm_010: beat_to_beat_consistency_error

Purpose:

Assess sequence-level stability across consecutive beats after denoising.

Required inputs:

```text
beat_sequence_features
reference_consistency_measure
denoised_consistency_measure
```

Claim boundary:

This metric supports sequence stability review but may be sensitive to rhythm variability and segment selection.

## Minimum Metric Validation Checklist

A metric is validation-ready when it has:

- a unique metric ID
- a defined metric family
- a target morphology feature
- required input fields
- calculation summary
- preferred unit or score type
- interpretation guidance
- known limitations
- review status
- claim boundary

## Metric Family Values

```text
noise_reduction
waveform_similarity
peak_alignment
interval_stability
amplitude_error
morphology_distortion
method_runtime
robustness_across_noise
```

## Review Status Values

```text
draft
reviewed
validated
deprecated
released
```

## Future M3 Outputs

Expected downstream artifacts:

```text
outputs/noise_condition_registry.csv
outputs/example_benchmark_registry.csv
outputs/model_comparison_report.md
outputs/claim_boundary_report.md
```

## ML Readiness Path

Current status:

```text
validation_candidate
```

Candidate future ML tasks:

```text
morphology-distortion detection
method-output quality triage
noise-condition classification
robustness scoring
benchmark-result clustering
outlier segment review
```

Minimum readiness requirements:

- dataset inventory
- segment registry
- reviewed noise labels
- implemented metric calculations
- baseline comparison outputs
- reviewer adjudication notes
- claim-boundary checks

## Cross-Repository Alignment

| Repository | Metric Link |
|---|---|
| `pskeffington/Portfolio` | Uses metric evidence in resilient-sensing proof packets. |
| `pskeffington/CDC-mod` | Links signal reliability to health-security monitoring and decision support. |
| `pskeffington/authentication-audit-compiler` | Can audit benchmark runs, reviewer actions, and release status. |
| `pskeffington/cipher-topology-lab` | Provides evaluation discipline and claim-boundary review. |
| `pskeffington/McDowell-County-Commission-on-Aging-Inc.` | Transfers metric-dictionary logic to infrastructure monitoring and feature validation. |

## Public-Safety Boundary

This dictionary must not include protected health information, restricted patient data, live clinical system details, credentials, or unbounded diagnostic claims.

Use public datasets, synthetic examples, benchmark language, and explicit claim boundaries.

## Claim Boundary

This dictionary supports morphology-preservation benchmark planning and metric validation. It does not establish diagnostic validity, clinical safety, comparative method superiority, regulatory approval, or generalizability beyond documented datasets, metrics, and noise conditions.
