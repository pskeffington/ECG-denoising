"""Morphology-preservation metric placeholders.

These functions provide conservative scaffold behavior. Future passes should
replace placeholders with validated ECG fiducial-detection logic.
"""

from __future__ import annotations

import numpy as np


def r_peak_timing_error_ms(reference_peaks: np.ndarray, estimate_peaks: np.ndarray, sample_rate: float) -> float:
    """Return mean absolute R-peak timing error in milliseconds."""
    ref = np.asarray(reference_peaks, dtype=float)
    est = np.asarray(estimate_peaks, dtype=float)
    if ref.shape != est.shape:
        raise ValueError("peak arrays must have the same shape")
    if sample_rate <= 0:
        raise ValueError("sample_rate must be positive")
    if ref.size == 0:
        raise ValueError("at least one peak is required")
    return float(np.mean(np.abs(ref - est)) * 1000.0 / sample_rate)


def morphology_corr(reference: np.ndarray, estimate: np.ndarray) -> float:
    """Return signal correlation as a conservative morphology placeholder."""
    ref = np.asarray(reference, dtype=float)
    est = np.asarray(estimate, dtype=float)
    if ref.shape != est.shape:
        raise ValueError("reference and estimate must have the same shape")
    if np.std(ref) == 0.0 or np.std(est) == 0.0:
        raise ValueError("signals must have nonzero variance")
    return float(np.corrcoef(ref, est)[0, 1])


def qrs_width_distortion_ms(reference_width_ms: float, estimate_width_ms: float) -> float:
    """Return absolute QRS width difference in milliseconds."""
    return abs(float(estimate_width_ms) - float(reference_width_ms))


def st_deviation_change(reference_mv: float, estimate_mv: float) -> float:
    """Return absolute ST-segment deviation change in millivolts."""
    return abs(float(estimate_mv) - float(reference_mv))
