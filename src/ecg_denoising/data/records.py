"""Record definitions for real Phase 1 PhysioNet benchmark data."""

from __future__ import annotations

from dataclasses import dataclass


NSTDB_PN_DIR = "nstdb/1.0.0"
MITDB_PN_DIR = "mitdb/1.0.0"


@dataclass(frozen=True)
class NstdbRecord:
    """MIT-BIH Noise Stress Test Database record mapping."""

    record: str
    clean_record: str
    snr_db: int
    noise_kind: str = "electrode_motion"
    noisy_pn_dir: str = NSTDB_PN_DIR
    clean_pn_dir: str = MITDB_PN_DIR


NSTDB_PHASE1_RECORDS: tuple[NstdbRecord, ...] = (
    NstdbRecord("118e_6", "118", -6),
    NstdbRecord("118e00", "118", 0),
    NstdbRecord("118e06", "118", 6),
    NstdbRecord("118e12", "118", 12),
    NstdbRecord("118e18", "118", 18),
    NstdbRecord("118e24", "118", 24),
    NstdbRecord("119e_6", "119", -6),
    NstdbRecord("119e00", "119", 0),
    NstdbRecord("119e06", "119", 6),
    NstdbRecord("119e12", "119", 12),
    NstdbRecord("119e18", "119", 18),
    NstdbRecord("119e24", "119", 24),
)


def find_nstdb_record(record: str) -> NstdbRecord:
    """Return the NSTDB metadata row for a record name."""
    for row in NSTDB_PHASE1_RECORDS:
        if row.record == record:
            return row
    raise KeyError(f"unknown NSTDB record: {record}")
