# ECG Denoising Benchmark Roadmap

## Purpose

This roadmap defines the near-term priorities for turning the repository from a foundation scaffold into a reproducible ECG denoising benchmark. The project should remain conservative: no comparative method claims should be treated as final until dataset access, preprocessing, noise handling, and metric validation are documented.

## Core Research Question

Among open ECG datasets, how do classical filtering, adaptive filtering, wavelet/time-frequency methods, and lightweight deep-learning denoisers compare in reducing common ECG noise while preserving clinically relevant ECG morphology?

## Current Operating Stage

The repository is in v0.1.0 foundation mode. The immediate goal is not to produce final benchmark results. The immediate goal is to make the benchmark design explicit enough that later experiments can be run, audited, repeated, and translated into manuscript claims without overreach.

## Tonight's Priorities

### Priority 1: Lock the Minimum Viable Benchmark

Define the smallest benchmark that can produce useful, reproducible information.

Initial minimum viable benchmark:

- Dataset: MIT-BIH Noise Stress Test Database
- Noise focus: baseline wander, muscle artifact, electrode-motion artifact, and powerline interference where available or constructible
- Baseline methods: one classical filter and one wavelet/time-frequency method
- Metrics: SNR improvement, RMSE, PRD, Pearson correlation, and R-peak timing error
- Exclusions: no deep-learning claims, no clinical superiority claims, and no cross-dataset generalization claims in v0.1.0

Deliverable:

- A concise `docs/minimum_viable_benchmark.md` or equivalent section defining the exact first comparison.

### Priority 2: Clarify Dataset Inventory

Create a dataset manifest that records what each dataset contributes and what remains unresolved.

Phase 1 datasets:

- MIT-BIH Noise Stress Test Database
- MIT-BIH Arrhythmia Database
- PTB-XL
- PTB-XL+

Phase 2 datasets:

- MIMIC-IV-ECG
- MIMIC-III Waveform Database

For each dataset, document:

- Source and access path
- License or credential constraints
- Signal format
- Sampling frequency
- Lead configuration
- Annotation availability
- Noise labels or noise-injection suitability
- Intended role in the benchmark

Deliverable:

- `data_manifest/dataset_inventory.md`

### Priority 3: Build the Noise Taxonomy

Define each noise class before coding transformations or filters.

Initial taxonomy:

- Baseline wander
- Muscle artifact
- Electrode-motion artifact
- Powerline interference

For each noise class, document:

- Physiological or technical origin
- Expected signal appearance
- Frequency-domain characteristics where relevant
- How it appears in available datasets
- Whether it is measured directly, labeled, simulated, or injected
- Which methods are expected to handle it well or poorly

Deliverable:

- `docs/noise_taxonomy.md`

### Priority 4: Define the Method Matrix

Create a method matrix that separates method families from individual implementations.

Method families:

- Classical filters
- Adaptive filters
- Wavelet and time-frequency methods
- Lightweight deep-learning denoisers

For each candidate method, record:

- Family
- Input assumptions
- Tunable parameters
- Expected strengths
- Expected weaknesses
- Morphology-preservation risk
- Implementation status
- Citation status

Deliverable:

- `docs/method_matrix.md`

### Priority 5: Define Morphology-Preservation Metrics

The project's main contribution depends on separating generic signal-quality improvement from ECG morphology preservation. Metrics should therefore be split into two groups.

General signal-quality metrics:

- SNR improvement
- RMSE
- PRD
- Pearson correlation

Morphology-preservation metrics:

- R-peak timing error
- QRS distortion
- ST-segment preservation

First metric to formalize:

- R-peak timing error

Working definition:

R-peak timing error measures the absolute temporal difference between reference R-peak locations and R-peak locations detected after denoising. Lower error indicates that the denoising method preserved beat timing and did not distort the QRS complex enough to shift peak detection.

Deliverable:

- `docs/metrics_plan.md`

### Priority 6: Establish Reproducibility Rules

Before adding benchmark outputs, define rules for how results will be generated and reported.

Required rules:

- Every result must identify dataset, record, lead, sampling frequency, preprocessing path, noise condition, method, parameters, and metric version.
- Every method comparison must be traceable to a script or notebook.
- Exploratory notebooks may exist, but final results should be generated from scripts.
- Manuscript claims must reference validated outputs only.
- Failed or inconclusive results should be retained in notes rather than silently discarded.

Deliverable:

- `docs/reproducibility_rules.md`

## Roadmap by Phase

### Phase 0: Foundation Documentation

Goal: make the benchmark auditable before running comparisons.

Tasks:

- Add dataset inventory
- Add noise taxonomy
- Add method matrix
- Add metrics plan
- Add reproducibility rules
- Define minimum viable benchmark

Exit condition:

- A reader can understand what will be benchmarked, why, how, and what claims are not yet permitted.

### Phase 1: Data Access and Loading

Goal: load initial open ECG records reproducibly.

Tasks:

- Confirm access to MIT-BIH Noise Stress Test Database
- Confirm access to MIT-BIH Arrhythmia Database
- Add basic data-loading script or notebook
- Record sampling frequency and signal channels
- Save no restricted data directly into the repository

Exit condition:

- One ECG record can be loaded, inspected, and referenced through a documented path.

### Phase 2: Baseline Preprocessing

Goal: standardize signal preparation before comparing denoising methods.

Tasks:

- Define segment length
- Define lead selection rules
- Define normalization rules
- Define train/test or record split if needed
- Define where synthetic noise injection is allowed

Exit condition:

- A clean baseline signal segment can be passed consistently to multiple methods.

### Phase 3: Baseline Methods

Goal: implement the first non-deep-learning comparison.

Initial candidates:

- Classical bandpass or notch filtering
- Wavelet denoising

Exit condition:

- Two baseline methods can process the same segment and produce comparable metric outputs.

### Phase 4: Metric Validation

Goal: ensure metrics measure the intended property.

Tasks:

- Validate SNR improvement, RMSE, PRD, and Pearson correlation on controlled inputs
- Validate R-peak timing error on known annotations or stable detector outputs
- Document edge cases where metrics fail or mislead

Exit condition:

- Metric outputs are interpretable and not merely numerical artifacts.

### Phase 5: Controlled Benchmark Run

Goal: run the first constrained benchmark.

Tasks:

- Run minimum viable benchmark
- Store results in `results/`
- Add result metadata
- Produce one summary table
- Avoid final comparative claims until reviewed

Exit condition:

- The repository contains one reproducible, limited benchmark result with clear caveats.

### Phase 6: Manuscript Scaffold

Goal: convert benchmark structure into a manuscript-ready outline.

Tasks:

- Draft introduction
- Draft methods framework
- Draft dataset table
- Draft metric table
- Draft limitations section

Exit condition:

- Manuscript claims remain aligned with actual benchmark maturity.

## Immediate Next Actions

1. Create `data_manifest/dataset_inventory.md`.
2. Create `docs/noise_taxonomy.md`.
3. Create `docs/method_matrix.md`.
4. Create `docs/metrics_plan.md` with R-peak timing error as the first fully defined metric.
5. Create `docs/reproducibility_rules.md`.
6. Create or update a minimal script plan under `src/` only after documentation anchors are in place.

## Guardrails

- Do not claim clinical superiority.
- Do not compare methods without documented preprocessing.
- Do not treat exploratory notebook outputs as final results.
- Do not commit raw restricted datasets.
- Do not let deep-learning implementation outrun the benchmark scaffold.
- Do not collapse morphology preservation into generic signal-quality improvement.

## Tonight's Success Criteria

A successful work session ends with:

- One roadmap document committed
- One dataset inventory scaffold started
- One metric plan scaffold started
- One clear next coding task identified
- No premature benchmark claims
