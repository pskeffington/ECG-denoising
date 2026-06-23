from __future__ import annotations

import numpy as np

from ecg_denoising.metrics.morphology import qrs_width_distortion_ms, r_peak_timing_error_ms
from ecg_denoising.metrics.signal_quality import pearson_corr, prd, rmse, snr_db


def test_rmse_zero_for_identical_signals() -> None:
    signal = np.array([1.0, 2.0, 3.0])
    assert rmse(signal, signal) == 0.0


def test_prd_zero_for_identical_signals() -> None:
    signal = np.array([1.0, 2.0, 3.0])
    assert prd(signal, signal) == 0.0


def test_corr_one_for_identical_signals() -> None:
    signal = np.array([1.0, 2.0, 3.0])
    assert np.isclose(pearson_corr(signal, signal), 1.0)


def test_snr_infinite_for_identical_signals() -> None:
    signal = np.array([1.0, 2.0, 3.0])
    assert snr_db(signal, signal) == float("inf")


def test_r_peak_timing_error_ms() -> None:
    ref = np.array([100, 200, 300])
    est = np.array([101, 198, 303])
    assert np.isclose(r_peak_timing_error_ms(ref, est, sample_rate=1000.0), 2.0)


def test_qrs_width_distortion_ms() -> None:
    assert qrs_width_distortion_ms(90.0, 94.5) == 4.5
