"""Offline real-data benchmark runner for Phase 1 PhysioNet records."""

from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from ecg_denoising.data.records import NSTDB_PHASE1_RECORDS, NstdbRecord
from ecg_denoising.data.wfdb_io import load_nstdb_pair
from ecg_denoising.methods.classical import CLASSICAL_METHODS, apply_classical_method
from ecg_denoising.metrics.signal_quality import pearson_corr, prd, rmse, snr_improvement

BASELINE_SIGNAL_QUALITY_FIELDS: tuple[str, ...] = (
    "dataset",
    "record",
    "clean_record",
    "method",
    "snr_level_db",
    "channel",
    "sample_rate",
    "n_samples",
    "rmse",
    "prd",
    "pearson_corr",
    "snr_improvement_db",
)


@dataclass(frozen=True)
class RealBenchmarkResult:
    """Single real-data benchmark result row."""

    dataset: str
    record: str
    clean_record: str
    method: str
    snr_level_db: int
    channel: int
    sample_rate: float
    n_samples: int
    rmse: float
    prd: float
    pearson_corr: float
    snr_improvement_db: float


def validate_methods(methods: Iterable[str]) -> tuple[str, ...]:
    """Validate and return requested classical benchmark methods."""
    selected = tuple(methods)
    if not selected:
        raise ValueError("at least one method is required")
    invalid = sorted(set(selected) - set(CLASSICAL_METHODS))
    if invalid:
        valid = ", ".join(sorted(CLASSICAL_METHODS))
        bad = ", ".join(invalid)
        raise ValueError(f"unknown classical method(s): {bad}; valid methods: {valid}")
    return selected


def run_nstdb_record(
    row: NstdbRecord,
    channel: int = 0,
    sampto: int | None = None,
    data_root: Path | None = None,
    method: str = "bandpass",
) -> RealBenchmarkResult:
    """Run a named classical baseline on one NSTDB record.

    This function loads real PhysioNet data through wfdb or from a local cache.
    It is still a non-operational offline benchmark and does not imply clinical
    validation.
    """
    validate_methods((method,))
    pair = load_nstdb_pair(row, channel=channel, sampto=sampto, data_root=data_root)
    denoised = apply_classical_method(pair.noisy, pair.sample_rate, method=method)
    return RealBenchmarkResult(
        dataset="nstdb",
        record=pair.record,
        clean_record=pair.clean_record,
        method=method,
        snr_level_db=pair.snr_db,
        channel=pair.channel,
        sample_rate=pair.sample_rate,
        n_samples=len(pair.clean),
        rmse=rmse(pair.clean, denoised),
        prd=prd(pair.clean, denoised),
        pearson_corr=pearson_corr(pair.clean, denoised),
        snr_improvement_db=snr_improvement(pair.clean, pair.noisy, denoised),
    )


def run_nstdb_table(
    records: Iterable[NstdbRecord] = NSTDB_PHASE1_RECORDS,
    methods: Iterable[str] = tuple(sorted(CLASSICAL_METHODS)),
    channel: int = 0,
    sampto: int | None = None,
    data_root: Path | None = None,
) -> list[RealBenchmarkResult]:
    """Run selected classical methods across selected NSTDB records."""
    selected_methods = validate_methods(methods)
    results: list[RealBenchmarkResult] = []
    for record in records:
        for method in selected_methods:
            results.append(
                run_nstdb_record(
                    record,
                    channel=channel,
                    sampto=sampto,
                    data_root=data_root,
                    method=method,
                )
            )
    return results


def real_result_as_row(result: RealBenchmarkResult) -> dict[str, float | int | str]:
    """Return a CSV-ready dictionary for one real-data benchmark result."""
    return {
        "dataset": result.dataset,
        "record": result.record,
        "clean_record": result.clean_record,
        "method": result.method,
        "snr_level_db": result.snr_db if hasattr(result, "snr_db") else result.snr_level_db,
        "channel": result.channel,
        "sample_rate": result.sample_rate,
        "n_samples": result.n_samples,
        "rmse": result.rmse,
        "prd": result.prd,
        "pearson_corr": result.pearson_corr,
        "snr_improvement_db": result.snr_improvement_db,
    }


def results_as_rows(results: Iterable[RealBenchmarkResult]) -> list[dict[str, float | int | str]]:
    """Return CSV-ready dictionaries for benchmark results."""
    return [real_result_as_row(result) for result in results]


def write_baseline_signal_quality(path: Path, results: Iterable[RealBenchmarkResult]) -> int:
    """Write baseline signal-quality results and return row count."""
    rows = results_as_rows(results)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(BASELINE_SIGNAL_QUALITY_FIELDS))
        writer.writeheader()
        writer.writerows(rows)
    return len(rows)
