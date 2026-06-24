# Benchmark Readiness Matrix

Author: Paul Skeffington, MS, MPH  
GitHub: `@pskeffington-github`  
Public contact: `paulskeffington@gmail.com`  
Status: v1 benchmark-readiness artifact  
Last updated: 2026-06-24

## Purpose

This document defines the benchmark-readiness standard for ECG denoising experiments focused on morphology preservation, noise robustness, reproducibility, and bounded biomedical-AI evaluation claims.

The goal is to evaluate signal-processing and machine-learning methods without losing clinically meaningful waveform structure or overstating comparative results.

## Operating Question

```text
Can a denoising method reduce noise while preserving the morphology needed for trustworthy downstream interpretation?
```

## Benchmark Object Chain

```text
dataset_record
  -> signal_segment
  -> noise_condition
  -> denoising_method
  -> morphology_feature
  -> preservation_metric
  -> benchmark_result
  -> claim_boundary
  -> readiness_report
```

## Benchmark Readiness Matrix

| Benchmark Area | Readiness Requirement | Evidence Object | Failure Mode | Review Status |
|---|---|---|---|---|
| Dataset Inventory | Public datasets, access requirements, records, leads, sampling rates, and use constraints are documented. | `dataset_record` | Results cannot be traced or reproduced. | required |
| Segment Registry | Signal segments have identifiers, lead labels, time windows, and preprocessing notes. | `signal_segment` | Segment drift or hidden preprocessing effects. | required |
| Noise Taxonomy | Noise sources and severity levels are defined before method comparison. | `noise_condition` | Unclear robustness claims or unfair comparisons. | required |
| Method Registry | Denoising methods, parameters, versions, and assumptions are documented. | `denoising_method` | Irreproducible or incomparable method outputs. | required |
| Morphology Features | Clinically relevant waveform structures are defined before scoring. | `morphology_feature` | Noise reduction masks clinically important distortion. | required |
| Preservation Metrics | Metrics measure both noise reduction and morphology retention. | `preservation_metric` | High numerical score with degraded clinical signal structure. | required |
| Benchmark Results | Results link methods, segments, noise conditions, and metrics. | `benchmark_result` | Unsupported aggregate claims. | required |
| Claim Boundary | Supported, unsupported, and future-validation claims are explicit. | `claim_boundary` | Overclaiming or premature clinical interpretation. | required |
| Readiness Report | Tables, limitations, and review notes are packaged for inspection. | `readiness_report` | Evidence scattered across files. | planned |

## Minimum Dataset Record

```yaml
dataset_id: string
dataset_name: string
dataset_source: string
access_status: string
license_or_use_note: string
record_count: integer
lead_information: string
sampling_rate_hz: number
known_limitations: list
review_status: string
```

## Minimum Signal Segment

```yaml
segment_id: string
dataset_id: string
record_id: string
lead_id: string
start_time_seconds: number
end_time_seconds: number
segment_duration_seconds: number
preprocessing_status: string
quality_note: string
```

## Noise Taxonomy

Noise conditions should be defined before comparing methods.

```yaml
noise_id: string
noise_type: string
noise_source: string
severity_level: string
injection_method: string
signal_to_noise_ratio: string
validation_status: string
```

Recommended initial noise categories:

```text
baseline_wander
powerline_interference
muscle_artifact
electrode_motion
white_noise
mixed_noise
unknown_or_unclassified
```

Recommended severity levels:

```text
low
moderate
high
extreme
```

## Denoising Method Registry

```yaml
method_id: string
method_name: string
method_family: string
implementation_path: string
parameter_summary: string
version: string
training_required: boolean
input_requirements: list
output_format: string
review_status: string
```

Initial method families:

```text
filtering
wavelet
adaptive_filtering
statistical_decomposition
lightweight_deep_learning
hybrid
baseline_or_no_denoising
```

## Morphology Feature Registry

Morphology preservation should be evaluated using features tied to waveform structure rather than noise reduction alone.

```yaml
feature_id: string
feature_name: string
feature_family: string
clinical_relevance_note: string
extraction_method: string
required_lead_context: string
validation_status: string
```

Initial morphology feature families:

```text
p_wave_presence
qrs_complex_shape
r_peak_location
qrs_duration
st_segment_shape
t_wave_shape
pr_interval_stability
qt_interval_stability
amplitude_preservation
beat_to_beat_consistency
```

## Preservation Metrics

Metrics should capture both signal quality and morphology fidelity.

```yaml
metric_id: string
metric_name: string
metric_family: string
metric_definition: string
required_inputs: list
interpretation_note: string
known_limitations: list
```

Initial metric families:

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

## Benchmark Result Object

```yaml
benchmark_result_id: string
dataset_id: string
segment_id: string
noise_id: string
method_id: string
feature_ids: list
metric_ids: list
result_summary: string
uncertainty_note: string
created_at: datetime
review_status: string
```

## Benchmark Constraints

A benchmark should not be treated as ready for comparative claims until:

- datasets are registered
- segment selection is documented
- noise conditions are defined
- methods are versioned
- morphology features are defined
- metrics are interpreted with limitations
- baseline comparisons are included
- claim boundaries are explicit
- generated results can be reproduced

## Current Claim Boundary

Supported at this stage:

- The repository can define a reproducible ECG denoising benchmark framework.
- Morphology preservation should be evaluated separately from noise reduction.
- Benchmark-readiness requires dataset, segment, noise, method, feature, metric, and claim-boundary objects.
- Future ML tasks can be prepared once deterministic benchmark objects exist.

Not supported at this stage:

- Clinical performance claims.
- Diagnostic claims.
- Claims that a method is superior without completed benchmark results.
- Claims that denoising preserves all clinically relevant morphology across datasets.
- Claims that benchmark outcomes generalize beyond documented datasets and noise conditions.

Required future validation:

- public dataset inventory
- reproducible segment extraction
- metric implementation
- baseline comparison
- sensitivity analysis
- independent reruns
- reviewer notes
- generated benchmark report

## ML Readiness

Future machine-learning tasks should remain assistive and review-gated.

Candidate ML tasks:

```text
noise-condition classification
method-output quality triage
morphology-distortion detection
robustness scoring
benchmark-result clustering
outlier segment review
```

Minimum ML safety requirements:

- deterministic benchmark objects exist first
- labels or weak labels are documented
- metrics are bounded by limitations
- reviewer adjudication remains required
- model outputs include uncertainty notes
- clinical claims remain out of scope unless separately validated

## Cross-Repository Alignment

| Repo | Signal-Evaluation Link |
|---|---|
| `pskeffington/Portfolio` | Proof-packet evidence for resilient sensing and trustworthy AI evaluation. |
| `pskeffington/authentication-audit-compiler` | Audit events and reviewer actions for benchmark artifacts. |
| `pskeffington/cipher-topology-lab` | Evaluation-readiness and claim-boundary discipline. |
| `pskeffington/CDC-mod` | Health-security sensing and public-health AI evaluation context. |
| `pskeffington/McDowell-County-Commission-on-Aging-Inc.` | Transferable degraded-signal and infrastructure-monitoring evaluation logic. |

## Public Safety Boundary

Do not include:

- protected health information
- restricted datasets
- credentials
- live clinical system details
- non-public patient data
- unbounded clinical claims
- implementation-specific operational controls

Public-facing examples should use public datasets, synthetic examples, and bounded benchmark language.

## Next Implementation Tasks

1. Add structured YAML or JSON benchmark objects.
2. Add a validation script for required fields.
3. Create a dataset inventory table.
4. Create a noise taxonomy fixture.
5. Create a morphology-feature registry.
6. Create a generated benchmark-readiness report.
7. Add reviewer notes and claim-boundary checks.

## Claim Boundary

This document is a benchmark-readiness artifact. It supports reproducibility, morphology-preservation planning, and bounded biomedical-AI evaluation. It does not establish diagnostic validity, clinical safety, or comparative method superiority.
