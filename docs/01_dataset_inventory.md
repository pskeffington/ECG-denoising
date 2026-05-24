# Dataset Inventory

## Phase 1: Open and Reproducible Datasets

| Dataset | Role | Access | Signal Type | Phase |
|---|---|---|---|---|
| MIT-BIH Noise Stress Test Database | Primary benchmark noise source | Open PhysioNet | ECG plus noise recordings | Phase 1 |
| MIT-BIH Arrhythmia Database | ECG source and arrhythmia context | Open PhysioNet | Annotated ECG | Phase 1 |
| PTB-XL | Clinical ECG morphology and diagnostic context | Open PhysioNet | 12-lead ECG | Phase 1 |
| PTB-XL+ | Fiducial and feature-based ECG morphology extension | Open PhysioNet | ECG features and median beats | Phase 1 |

## Phase 2: Credentialed Large-Scale Clinical Datasets

| Dataset | Role | Access | Signal Type | Phase |
|---|---|---|---|---|
| MIMIC-IV-ECG | Large diagnostic ECG extension | Credentialed PhysioNet | 12-lead ECG | Phase 2 |
| MIMIC-III Waveform Database | ICU waveform/noise realism extension | Credentialed PhysioNet | ICU ECG and other waveforms | Phase 2 |

## Dataset Inclusion Criteria

- Public or credentialed academic access
- ECG waveform data or ECG-derived fiducial features
- Usable for denoising, morphology preservation, or downstream classification
- Documentation sufficient for reproducible use

## Dataset Exclusion Criteria

- Closed commercial datasets
- Datasets without accessible waveform-level data
- Datasets without clear provenance
- Datasets requiring unshareable preprocessing assumptions

## Phase 1 Priority

The MIT-BIH Noise Stress Test Database is the first benchmark anchor because it provides noise recordings suitable for controlled ECG noise-stress experiments.
