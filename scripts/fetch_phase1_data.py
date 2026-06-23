#!/usr/bin/env python
"""Optionally cache Phase 1 PhysioNet data outside git.

This script downloads only public Phase 1 records. Keep the target directory
outside tracked source control or under an ignored local data directory.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import wfdb

from ecg_denoising.data.records import MITDB_PN_DIR, NSTDB_PHASE1_RECORDS, NSTDB_PN_DIR


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Fetch Phase 1 public PhysioNet records")
    parser.add_argument("--data-root", type=Path, required=True, help="Local data root outside git")
    parser.add_argument("--overwrite", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    args.data_root.mkdir(parents=True, exist_ok=True)

    nstdb_records = sorted({row.record for row in NSTDB_PHASE1_RECORDS})
    mitdb_records = sorted({row.clean_record for row in NSTDB_PHASE1_RECORDS})

    wfdb.dl_database(
        NSTDB_PN_DIR,
        dl_dir=str(args.data_root / "nstdb"),
        records=nstdb_records,
        keep_subdirs=False,
        overwrite=args.overwrite,
    )
    wfdb.dl_database(
        MITDB_PN_DIR,
        dl_dir=str(args.data_root / "mitdb"),
        records=mitdb_records,
        keep_subdirs=False,
        overwrite=args.overwrite,
    )
    print(f"cached {len(nstdb_records)} NSTDB records and {len(mitdb_records)} MITDB records under {args.data_root}")


if __name__ == "__main__":
    main()
