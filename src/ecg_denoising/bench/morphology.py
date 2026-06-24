"""Morphology-preservation output helpers for offline ECG benchmarks."""

from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from ecg_denoising.metrics.morphology import (
    EcgFiducials,
    false_r_peak_rate,
    missed_r_peak_rate,
    morphology_corr,
    qrs_width_distortion_ms,
    r_peak_timing_error_ms,
    st_deviation_change,
)

MORPHOLOGY_PRESERVATION_FIELDS: tuple[str, ...] = (
    "dataset",
    "record",
    "clean_record",
    "method",
    "snr_level_db",
    "channel",
    "sample_rate",
    "n_samples",
    "r_peak_timing_error_ms",
    "missed_r_peak_rate",
    "false_r_peak_rate",
    "qrs_width_distortion_ms",
    "st_deviation_change_mv",
    "morphology_corr",
)


@dataclass(frozen=True)
class MorphologyResult:
    """Single morphology-preservation result row."""

    dataset: str
    record: str
    clean_record: str
    method: str
    snr_level_db: int
    channel: int
    sample_rate: float
    n_samples: int
    r_peak_timing_error_ms: float
    missed_r_peak_rate: float
    false_r_peak_rate: float
    qrs_width_distortion_ms: float
    st_deviation_change_mv: float
    morphology_corr: float


def compare_fiducials(
    dataset: str,
    record: str,
    clean_record: str,
    method: str,
    snr_level_db: int,
    channel: int,
    sample_rate: float,
    reference_signal,
    estimate_signal,
    reference_fiducials: EcgFiducials,
    estimate_fiducials: EcgFiducials,
) -> MorphologyResult:
    """Compare extracted fiducials for one denoising result."""
    return MorphologyResult(
        dataset=dataset,
        record=record,
        clean_record=clean_record,
        method=method,
        snr_level_db=snr_level_db,
        channel=channel,
        sample_rate=sample_rate,
        n_samples=len(reference_signal),
        r_peak_timing_error_ms=r_peak_timing_error_ms(
            reference_fiducials.r_peaks,
            estimate_fiducials.r_peaks,
            sample_rate=sample_rate,
        ),
        missed_r_peak_rate=missed_r_peak_rate(
            reference_fiducials.r_peaks,
            estimate_fiducials.r_peaks,
            sample_rate=sample_rate,
        ),
        false_r_peak_rate=false_r_peak_rate(
            reference_fiducials.r_peaks,
            estimate_fiducials.r_peaks,
            sample_rate=sample_rate,
        ),
        qrs_width_distortion_ms=qrs_width_distortion_ms(
            reference_fiducials.mean_qrs_width_ms,
            estimate_fiducials.mean_qrs_width_ms,
        ),
        st_deviation_change_mv=st_deviation_change(
            reference_fiducials.mean_st_deviation_mv,
            estimate_fiducials.mean_st_deviation_mv,
        ),
        morphology_corr=morphology_corr(reference_signal, estimate_signal),
    )


def morphology_result_as_row(result: MorphologyResult) -> dict[str, float | int | str]:
    """Return a CSV-ready dictionary for one morphology result."""
    return {
        "dataset": result.dataset,
        "record": result.record,
        "clean_record": result.clean_record,
        "method": result.method,
        "snr_level_db": result.snr_level_db,
        "channel": result.channel,
        "sample_rate": result.sample_rate,
        "n_samples": result.n_samples,
        "r_peak_timing_error_ms": result.r_peak_timing_error_ms,
        "missed_r_peak_rate": result.missed_r_peak_rate,
        "false_r_peak_rate": result.false_r_peak_rate,
        "qrs_width_distortion_ms": result.qrs_width_distortion_ms,
        "st_deviation_change_mv": result.st_deviation_change_mv,
        "morphology_corr": result.morphology_corr,
    }


def morphology_results_as_rows(results: Iterable[MorphologyResult]) -> list[dict[str, float | int | str]]:
    """Return CSV-ready dictionaries for morphology results."""
    return [morphology_result_as_row(result) for result in results]


def write_morphology_preservation(path: Path, results: Iterable[MorphologyResult]) -> int:
    """Write morphology-preservation results and return row count."""
    rows = morphology_results_as_rows(results)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(MORPHOLOGY_PRESERVATION_FIELDS))
        writer.writeheader()
        writer.writerows(rows)
    return len(rows)
