# Model Comparison Report

Author: Paul Skeffington, MS, MPH  
GitHub: `@pskeffington-github`  
Public contact: `paulskeffington@gmail.com`  
Repository: `pskeffington/ECG-denoising`  
Status: draft v1  
Milestone: M4 ML Readiness

## Purpose

This report summarizes the first Resilient Sensing comparison layer for the repository. It reviews the benchmark registry and noise-condition registry to determine whether the repository has enough structure to support evaluation-candidate status for synthetic morphology-preservation and signal-quality workflows.

This report is limited to synthetic benchmark governance. It does not establish clinical validity, diagnostic accuracy, device safety, denoising superiority, production readiness, or medical decision support.

## Artifacts Reviewed

```text
docs/benchmark_readiness_matrix.md
docs/noise_taxonomy.md
docs/morphology_metric_dictionary.md
outputs/example_benchmark_registry.csv
outputs/noise_condition_registry.csv
docs/resilient_sensing_proof_packet.md
```

## Evaluation Summary

```text
Current readiness level: 3
Current readiness status: evaluation_candidate
Production status: not_ready
Clinical status: not_ready
Reviewer required: true
```

The repository has moved from validation-candidate status toward evaluation-candidate status because it now contains a benchmark registry, noise-condition registry, morphology metric dictionary, and explicit claim-boundary controls.

## Object Chain

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

## Registry Coverage

| Artifact | Records | Status | Notes |
|---|---:|---|---|
| `outputs/example_benchmark_registry.csv` | 10 | present | Synthetic benchmark rows cover multiple noise conditions, methods, morphology metrics, and review statuses. |
| `outputs/noise_condition_registry.csv` | 10 | present | Noise rows define noise families, severity, signal regions, expected effects, and related metric IDs. |

## Noise Coverage

| Noise Condition | Coverage Status | Notes |
|---|---|---|
| baseline_wander | present | Low and moderate examples exist. |
| powerline_interference | present | Periodic artifact example exists. |
| muscle_artifact | present | High-frequency artifact example exists. |
| electrode_motion | present | Motion artifact example exists. |
| white_noise | present | Random artifact example exists. |
| mixed_noise | present | High and extreme composite examples exist. |
| unknown_or_unclassified | present | Uncertainty category retained for claim-boundary testing. |
| signal_dropout | present | Missingness artifact added for future benchmark expansion. |

## Metric Coverage

| Metric ID | Metric | Coverage Status | Notes |
|---|---|---|---|
| mm_001 | r_peak_localization_error | present | Timing metric for R-peak review. |
| mm_002 | qrs_duration_error | present | QRS duration metric. |
| mm_003 | qrs_amplitude_error | present | Amplitude metric. |
| mm_004 | st_segment_deviation_error | present | Clinical-adjacent metric; benchmark planning only. |
| mm_005 | p_wave_preservation_score | present | Requires annotation/reviewer protocol before validation. |
| mm_006 | t_wave_preservation_score | present | Synthetic morphology review only. |
| mm_007 | beat_detection_agreement | present | Downstream readiness review only. |
| mm_008 | false_peak_rate | present | Detector-configuration dependent. |
| mm_009 | morphology_distortion_flag_rate | present | Requires reviewer or rule adjudication. |
| mm_010 | beat_to_beat_consistency_error | present | Useful for uncertainty and missingness review. |

## Comparison Interpretation

The current benchmark registry contains synthetic metric values and method labels. These rows support workflow testing, coverage review, and future comparison-report generation.

They do not support claims that any denoising method is better, safer, clinically useful, diagnostically valid, or device-ready.

## Quality Checks

| Check ID | Check | Result | Notes |
|---|---|---|---|
| rs_001 | Benchmark IDs are present | pass | Benchmark registry uses `bench_001` through `bench_010`. |
| rs_002 | Noise IDs are present | pass | Noise registry uses `noise_001` through `noise_010`. |
| rs_003 | Noise conditions are normalized | pass | Registry aligns to documented noise taxonomy plus signal dropout expansion. |
| rs_004 | Metric IDs are documented | pass | Benchmark rows map to morphology metric IDs. |
| rs_005 | Related metrics are documented | pass | Noise registry links noise conditions to related metric IDs. |
| rs_006 | Claim boundaries are present | pass | Rows include review-required and public-safe boundaries. |
| rs_007 | Clinical claims are excluded | pass | Notes explicitly exclude clinical and diagnostic interpretation. |
| rs_008 | Reviewer status is explicit | pass | Rows remain draft or review-required. |

## Readiness Gate Assessment

| Gate | Requirement | Status | Notes |
|---|---|---|---|
| Gate 1 | Evidence object exists | pass | Benchmark and noise-condition registries exist. |
| Gate 2 | Validation artifact exists | pass | Noise taxonomy and morphology metric dictionary exist. |
| Gate 3 | Claim boundary exists | pass | Clinical, device, diagnostic, and superiority claims are excluded. |
| Gate 4 | Bounded evaluation task exists | pass | Morphology-preservation and noise-condition review are bounded synthetic tasks. |
| Gate 5 | Evaluation output exists | pass | This model comparison report provides the first evaluation output. |

## Candidate Evaluation Tasks

The repository can support bounded synthetic evaluation development for:

```text
noise-condition coverage review
morphology-metric coverage review
method-output quality triage
morphology-distortion flag review
false-peak risk review
uncertainty-category handling
signal-dropout benchmark expansion
```

## Candidate ML Tasks

Candidate future ML tasks remain bounded and synthetic:

```text
noise-condition classification
morphology-distortion detection
method-output quality triage
robustness scoring
benchmark-result clustering
outlier segment review
```

## Remaining Gaps

Remaining gaps before stronger ML-readiness claims:

```text
additional synthetic signal segments
failure-case benchmark rows
annotation protocol
baseline comparison script
model-card or experiment-card template
metric uncertainty documentation
reviewer adjudication protocol
external benchmark mapping
```

## Supported Claims

This report supports the following bounded claims:

- The repository contains a synthetic benchmark registry.
- The repository contains a synthetic noise-condition registry.
- The repository contains a noise taxonomy and morphology metric dictionary.
- The repository can support synthetic morphology-preservation and noise-condition evaluation workflows.
- The repository is ready for evaluation-candidate work using synthetic benchmark examples.

## Unsupported Claims

This report does not support claims that:

- any denoising method is superior
- any result is clinically valid
- any result supports diagnosis or treatment
- any device is safe or effective
- any model has been trained or validated
- any benchmark result is externally valid
- any output should be used for medical decision support

## Public-Safety Boundary

This report excludes:

- protected health data
- private user data
- clinical decisions
- diagnostic claims
- treatment recommendations
- device approval claims
- production deployment claims
- operational monitoring claims

All reviewed artifacts are synthetic, public-safe, and claim-bounded.

## Readiness Decision

```text
Decision: advance to Level 3 for bounded synthetic evaluation work
Status: evaluation_candidate
Production status: not_ready
Clinical status: not_ready
Reviewer required: true
```

## Next Artifacts

Recommended next artifacts:

```text
outputs/signal_quality_error_registry.csv
docs/annotation_protocol.md
outputs/resilient_sensing_ml_readiness_report.md
scripts/compare_morphology_metrics.py
```

## Claim Boundary

This report establishes Resilient Sensing readiness for synthetic morphology-preservation and noise-condition evaluation workflows only. It does not establish clinical validity, diagnostic accuracy, device safety, denoising superiority, production readiness, legal compliance, or general AI safety.
