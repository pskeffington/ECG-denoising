# Dataset Inventory

This inventory keeps the project in non-operational research-benchmark mode. It records dataset role, access type, source, citation target, phase, and acquisition notes. Raw waveform files are not committed to this repository.

## Phase 1: Open and Reproducible Datasets

| Dataset | Role | Access | Signal Type | Source | Citation Target | Phase | Acquisition Notes |
|---|---|---|---|---|---|---|---|
| MIT-BIH Noise Stress Test Database | Primary benchmark noise source | Open PhysioNet | ECG plus noise recordings | PhysioNet `nstdb` v1.0.0 | Moody, Muldrow, and Mark noise-stress paper plus standard PhysioNet citation | Phase 1 | Use as the first controlled noise benchmark. Do not commit raw `.dat`, `.hea`, or annotation files. |
| MIT-BIH Arrhythmia Database | Clean ECG source and arrhythmia annotation context | Open PhysioNet | Annotated two-channel ambulatory ECG | PhysioNet `mitdb` v1.0.0 | Moody and Mark MIT-BIH Arrhythmia Database paper plus standard PhysioNet citation | Phase 1 | Use records and annotations for clean ECG context. Do not commit raw waveform or annotation files. |
| PTB-XL | Clinical ECG morphology and diagnostic context | Open PhysioNet | 12-lead ECG | PhysioNet `ptb-xl` v1.0.3 | Wagner et al. PTB-XL PhysioNet citation plus Scientific Data paper | Phase 1 | Use for morphology and diagnostic context after benchmark scaffold is stable. Store only manifests and derived non-sensitive outputs in git. |
| PTB-XL+ | Fiducial and feature-based ECG morphology extension | Open PhysioNet | ECG features, median beats, fiducial points, and labels | PhysioNet `ptb-xl-plus` v1.0.1 | Strodthoff et al. PTB-XL+ PhysioNet citation plus Scientific Data paper | Phase 1 | Use to support morphology-preservation evaluation. Do not commit extracted feature tables unless they are small, permitted, and explicitly versioned as derived metadata. |

## Phase 2: Credentialed or Large-Scale Clinical Extensions

| Dataset | Role | Access | Signal Type | Source | Citation Target | Phase | Acquisition Notes |
|---|---|---|---|---|---|---|---|
| MIMIC-IV-ECG | Large diagnostic ECG extension | PhysioNet access; treat as credential-sensitive for project workflow | 12-lead diagnostic ECG | PhysioNet `mimic-iv-ecg` v1.0 | Gow et al. MIMIC-IV-ECG PhysioNet citation | Phase 2 | Do not use until Phase 1 pipeline is reproducible. Do not commit waveforms, patient-level records, local paths, or credential notes. |
| MIMIC-III Waveform Database | ICU waveform/noise realism extension | PhysioNet access; large clinical waveform corpus | ICU ECG and other physiologic waveforms | PhysioNet `mimic3wdb` v1.0 | Moody et al. MIMIC-III Waveform Database citation plus MIMIC-III clinical database citation where applicable | Phase 2 | Use only for later waveform realism checks. Do not commit waveform files, patient-level records, local paths, or credential notes. |

## Dataset Inclusion Criteria

- Public or credentialed academic access.
- ECG waveform data or ECG-derived fiducial features.
- Usable for denoising, morphology preservation, or downstream classification research.
- Documentation sufficient for reproducible use.
- Compatible with non-operational offline benchmarking.

## Dataset Exclusion Criteria

- Closed commercial datasets.
- Datasets without accessible waveform-level data.
- Datasets without clear provenance.
- Datasets requiring unshareable preprocessing assumptions.
- Data that would require clinical deployment, live monitoring, or patient-specific decision logic in this repository.

## Phase 1 Priority

The MIT-BIH Noise Stress Test Database is the first benchmark anchor because it provides baseline wander, muscle artifact, and electrode-motion noise recordings suitable for controlled ECG noise-stress experiments. The benchmark protocol should begin with offline reproduction on Phase 1 data or synthetic placeholders and should not depend on Phase 2 clinical extensions.

## Data Handling Rules

- Commit manifests, documentation, tests, and reproducible code only.
- Do not commit raw PhysioNet waveform data.
- Do not commit local filesystem paths.
- Do not commit credentialed-data access notes.
- Use ignored local configuration for machine-specific dataset locations.
- Keep all filenames and package objects plain Latin characters.
