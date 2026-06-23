"""PhysioNet source identifiers used by the offline benchmark scaffold."""

from __future__ import annotations

PHYSIONET_SOURCES: dict[str, str] = {
    "nstdb": "MIT-BIH Noise Stress Test Database v1.0.0",
    "mitdb": "MIT-BIH Arrhythmia Database v1.0.0",
    "ptb-xl": "PTB-XL v1.0.3",
    "ptb-xl-plus": "PTB-XL+ v1.0.1",
    "mimic-iv-ecg": "MIMIC-IV-ECG v1.0",
    "mimic3wdb": "MIMIC-III Waveform Database v1.0",
}


def known_source(slug: str) -> bool:
    """Return whether a PhysioNet slug is part of the project inventory."""
    return slug in PHYSIONET_SOURCES
