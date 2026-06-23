from __future__ import annotations

from ecg_denoising.bench.run import result_as_row, run_synthetic_baseline


def test_synthetic_baseline_returns_row() -> None:
    result = run_synthetic_baseline(length=512, snr_level_db=0.0, seed=5)
    row = result_as_row(result)
    assert row["method"] == "bandpass_placeholder"
    assert row["snr_level_db"] == 0.0
    assert "rmse" in row
    assert "prd" in row
    assert "pearson_corr" in row
    assert "snr_improvement_db" in row
