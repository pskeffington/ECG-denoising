from __future__ import annotations

import csv

from ecg_denoising.bench.real import (
    BASELINE_SIGNAL_QUALITY_FIELDS,
    RealBenchmarkResult,
    results_as_rows,
    validate_methods,
    write_baseline_signal_quality,
)


def sample_result(method: str = "bandpass") -> RealBenchmarkResult:
    return RealBenchmarkResult(
        dataset="nstdb",
        record="118e00",
        clean_record="118",
        method=method,
        snr_level_db=0,
        channel=0,
        sample_rate=360.0,
        n_samples=5000,
        rmse=0.1,
        prd=2.0,
        pearson_corr=0.99,
        snr_improvement_db=3.5,
    )


def test_results_as_rows_matches_schema() -> None:
    rows = results_as_rows([sample_result()])
    assert tuple(rows[0].keys()) == BASELINE_SIGNAL_QUALITY_FIELDS


def test_write_baseline_signal_quality_writes_expected_fields(tmp_path) -> None:
    output = tmp_path / "baseline_signal_quality.csv"
    n_rows = write_baseline_signal_quality(output, [sample_result("bandpass"), sample_result("notch")])
    assert n_rows == 2
    with output.open(newline="") as handle:
        reader = csv.DictReader(handle)
        assert tuple(reader.fieldnames or ()) == BASELINE_SIGNAL_QUALITY_FIELDS
        rows = list(reader)
    assert [row["method"] for row in rows] == ["bandpass", "notch"]


def test_validate_methods_preserves_requested_order() -> None:
    assert validate_methods(["notch", "bandpass"]) == ("notch", "bandpass")
