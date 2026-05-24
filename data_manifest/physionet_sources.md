# PhysioNet Source Manifest

Raw PhysioNet datasets are not stored in this repository. This manifest records dataset roles, access constraints, and benchmark phase.

## Sources

| Dataset | Role | Access | Storage Policy | Phase |
|---|---|---|---|---|
| MIT-BIH Noise Stress Test Database | Primary ECG noise benchmark | Open PhysioNet | Download locally only | Phase 1 |
| MIT-BIH Arrhythmia Database | ECG rhythm and annotation context | Open PhysioNet | Download locally only | Phase 1 |
| PTB-XL | Clinical 12-lead ECG morphology context | Open PhysioNet | Download locally only | Phase 1 |
| PTB-XL+ | Fiducial and feature extension | Open PhysioNet | Download locally only | Phase 1 |
| MIMIC-IV-ECG | Large-scale diagnostic extension | Credentialed PhysioNet | Download locally only | Phase 2 |
| MIMIC-III Waveform Database | ICU waveform extension | Credentialed PhysioNet | Download locally only | Phase 2 |

## Local Data Rule

Place local data outside the git repository or under a gitignored `data/raw/` directory. Do not commit waveform files, credentialed data, or derived patient-level data.

## Reproducibility Rule

All scripts should operate from configurable local paths and should export only aggregate benchmark results, summary tables, and non-identifying figures.
