#!/usr/bin/env python
"""Run the Phase 1 NSTDB real-data benchmark locally.

Raw PhysioNet waveform files are streamed through wfdb or cached by wfdb
outside git. This script writes only derived metric rows.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path

from ecg_denoising.bench.real import real_result_as_row, run_nstdb_record
from ecg_denoising.data.records import NSTDB_PHASE1_RECORDS


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run local NSTDB Phase 1 benchmark")
    parser.add_argument("--output", type=Path, default=Path("results/baseline_signal_quality.csv"))
    parser.add_argument("--channel", type=int, default=0)
    parser.add_argument("--sampto", type=int, default=None, help="Optional sample limit for smoke tests")
    parser.add_argument("--data-root", type=Path, default=None, help="Optional local WFDB cache root outside git")
    parser.add_argument("--method", type=str, default="bandpass", help="One of highpass, bandpass, notch, bandpass_notch")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    rows = [
        real_result_as_row(
            run_nstdb_record(
                row,
                channel=args.channel,
                sampto=args.sampto,
                data_root=args.data_root,
                method=args.method,
            )
        )
        for row in NSTDB_PHASE1_RECORDS
    ]
    fieldnames = list(rows[0].keys())
    with args.output.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"wrote {len(rows)} rows to {args.output}")


if __name__ == "__main__":
    main()
