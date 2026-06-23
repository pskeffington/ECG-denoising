from __future__ import annotations

from ecg_denoising.data.records import NSTDB_PHASE1_RECORDS, find_nstdb_record


def test_nstdb_manifest_has_twelve_records() -> None:
    assert len(NSTDB_PHASE1_RECORDS) == 12


def test_nstdb_records_map_to_clean_sources() -> None:
    clean_records = {row.clean_record for row in NSTDB_PHASE1_RECORDS}
    assert clean_records == {"118", "119"}


def test_find_nstdb_record() -> None:
    row = find_nstdb_record("118e00")
    assert row.clean_record == "118"
    assert row.snr_db == 0
