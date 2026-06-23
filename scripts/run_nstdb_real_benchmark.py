#!/usr/bin/env python
"""Run the Phase 1 NSTDB real-data benchmark locally.

Raw PhysioNet waveform files are streamed through wfdb or cached by wfdb
outside git. This script writes only derived metric rows.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from ecg_denoising.bench.real import run_nstdb_table, write_baseline_signal_quality
from ecg_denoising.methods.classical import CLASSICAL_METHODS


def parse_methods(raw_methods: str) -> tuple[str, ...]:
    """Parse a comma-separated method list or the keyword all."""
    if raw_methods.strip().lower() == "all":
        return tuple(sorted(CLASSICAL_METHODS))
    return tuple(method.strip() for method in raw_methods.split(",") if method.strip())


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run local NSTDB Phase 1 benchmark")
    parser.add_argument("--output", type=Path, default=Path("results/baseline_signal_quality.csv"))
    parser.add_argument("--channel", type=int, default=0)
    parser.add_argument("--sampto", type=int, default=None, help="Optional sample limit for smoke tests")
    parser.add_argument("--data-root", type=Path, default=None, help="Optional local WFDB cache root outside git")
    parser.add_argument("--methods", type=str, default="all", help="Comma-separated methods or all")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    methods = parse_methods(args.methods)
    results = run_nstdb_table(
        methods=methods,
        channel=args.channel,
        sampto=args.sampto,
        data_root=args.data_root,
    )
    n_rows = write_baseline_signal_quality(args.output, results)
    print(f"wrote {n_rows} rows to {args.output}")


if __name__ == "__main__":
    main()
