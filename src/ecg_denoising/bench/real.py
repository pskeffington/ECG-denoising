"""Offline real-data benchmark runner for Phase 1 PhysioNet records."""

from __future__ import annotations

from dataclasses import dataclass

from ecg_denoising.data.records import NstdbRecord
from ecg_denoising.data.wfdb_io import load_nstdb_pair
from ecg_denoising.methods.classical import bandpass_placeholder
from ecg_denoising.metrics.signal_quality import pearson_corr, prd, rmse, snr_improvement


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


def run_nstdb_record(row: NstdbRecord, channel: int = 0, sampto: int | None = None) -> RealBenchmarkResult:
    """Run the current baseline on one NSTDB record.

    This function loads real PhysioNet data through wfdb. It is still a
    non-operational offline benchmark and does not imply clinical validation.
    """
    pair = load_nstdb_pair(row, channel=channel, sampto=sampto)
    denoised = bandpass_placeholder(pair.noisy)
    return RealBenchmarkResult(
        dataset="nstdb",
        record=pair.record,
        clean_record=pair.clean_record,
        method="bandpass_placeholder",
        snr_level_db=pair.snr_db,
        channel=pair.channel,
        sample_rate=pair.sample_rate,
        n_samples=len(pair.clean),
        rmse=rmse(pair.clean, denoised),
        prd=prd(pair.clean, denoised),
        pearson_corr=pearson_corr(pair.clean, denoised),
        snr_improvement_db=snr_improvement(pair.clean, pair.noisy, denoised),
    )


def real_result_as_row(result: RealBenchmarkResult) -> dict[str, float | int | str]:
    """Return a CSV-ready dictionary for one real-data benchmark result."""
    return {
        "dataset": result.dataset,
        "record": result.record,
        "clean_record": result.clean_record,
        "method": result.method,
        "snr_level_db": result.snr_level_db,
        "channel": result.channel,
        "sample_rate": result.sample_rate,
        "n_samples": result.n_samples,
        "rmse": result.rmse,
        "prd": result.prd,
        "pearson_corr": result.pearson_corr,
        "snr_improvement_db": result.snr_improvement_db,
    }
