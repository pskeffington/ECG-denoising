"""Morphology-preservation metrics for ECG denoising benchmarks.

The functions in this module support offline research comparisons only. They
use conservative, documented assumptions and do not provide clinical validation,
diagnostic logic, or patient-care decisions.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from scipy import signal as sp_signal


@dataclass(frozen=True)
class EcgFiducials:
    """Minimal morphology features extracted from one ECG-like signal."""

    r_peaks: np.ndarray
    mean_qrs_width_ms: float
    mean_st_deviation_mv: float


def _as_1d(signal: np.ndarray) -> np.ndarray:
    """Return signal as a one-dimensional float array."""
    arr = np.asarray(signal, dtype=float)
    if arr.ndim != 1:
        raise ValueError("signal must be one-dimensional")
    if arr.size < 4:
        raise ValueError("signal must contain at least four samples")
    return arr


def _validate_sample_rate(sample_rate: float) -> float:
    """Validate and return sample rate."""
    fs = float(sample_rate)
    if fs <= 0.0:
        raise ValueError("sample_rate must be positive")
    return fs


def detect_r_peaks(
    signal: np.ndarray,
    sample_rate: float,
    min_distance_ms: float = 250.0,
    prominence: float | None = None,
) -> np.ndarray:
    """Detect candidate R peaks using a simple prominence-based detector.

    This detector is intended for reproducible benchmark fixtures and first-pass
    morphology comparisons. It should be replaced or calibrated before any
    manuscript claim depends on morphology outcomes.
    """
    arr = _as_1d(signal)
    fs = _validate_sample_rate(sample_rate)
    if min_distance_ms <= 0.0:
        raise ValueError("min_distance_ms must be positive")
    distance = max(int(round(fs * min_distance_ms / 1000.0)), 1)
    peak_prominence = float(prominence) if prominence is not None else max(float(np.std(arr)) * 0.75, 1e-9)
    peaks, _ = sp_signal.find_peaks(arr, distance=distance, prominence=peak_prominence)
    if peaks.size == 0:
        raise ValueError("no R peaks detected")
    return peaks.astype(int)


def estimate_qrs_width_ms(
    signal: np.ndarray,
    r_peaks: np.ndarray,
    sample_rate: float,
    rel_height: float = 0.5,
) -> float:
    """Estimate mean QRS width in milliseconds using peak half-height widths."""
    arr = _as_1d(signal)
    fs = _validate_sample_rate(sample_rate)
    peaks = np.asarray(r_peaks, dtype=int)
    if peaks.size == 0:
        raise ValueError("at least one R peak is required")
    widths, *_ = sp_signal.peak_widths(arr, peaks, rel_height=rel_height)
    return float(np.mean(widths) * 1000.0 / fs)


def estimate_st_deviation_mv(
    signal: np.ndarray,
    r_peaks: np.ndarray,
    sample_rate: float,
    offset_ms: float = 80.0,
    window_ms: float = 40.0,
) -> float:
    """Estimate mean post-QRS ST deviation from fixed windows after R peaks."""
    arr = _as_1d(signal)
    fs = _validate_sample_rate(sample_rate)
    peaks = np.asarray(r_peaks, dtype=int)
    if peaks.size == 0:
        raise ValueError("at least one R peak is required")
    if offset_ms <= 0.0 or window_ms <= 0.0:
        raise ValueError("offset_ms and window_ms must be positive")

    offset = max(int(round(fs * offset_ms / 1000.0)), 1)
    width = max(int(round(fs * window_ms / 1000.0)), 1)
    values: list[float] = []
    for peak in peaks:
        start = int(peak) + offset
        stop = min(start + width, arr.size)
        if start < arr.size and stop > start:
            values.append(float(np.mean(arr[start:stop])))
    if not values:
        raise ValueError("no valid ST windows found")
    return float(np.mean(values))


def extract_fiducials(signal: np.ndarray, sample_rate: float) -> EcgFiducials:
    """Extract minimal reproducible morphology features from one signal."""
    peaks = detect_r_peaks(signal, sample_rate=sample_rate)
    return EcgFiducials(
        r_peaks=peaks,
        mean_qrs_width_ms=estimate_qrs_width_ms(signal, peaks, sample_rate=sample_rate),
        mean_st_deviation_mv=estimate_st_deviation_mv(signal, peaks, sample_rate=sample_rate),
    )


def match_peak_indices(
    reference_peaks: np.ndarray,
    estimate_peaks: np.ndarray,
    sample_rate: float,
    tolerance_ms: float = 75.0,
) -> tuple[np.ndarray, np.ndarray, int, int]:
    """Match reference and estimated peaks within a tolerance.

    Returns matched reference peaks, matched estimate peaks, missed count, and
    false-positive count.
    """
    fs = _validate_sample_rate(sample_rate)
    if tolerance_ms <= 0.0:
        raise ValueError("tolerance_ms must be positive")
    ref = np.asarray(reference_peaks, dtype=int)
    est = np.asarray(estimate_peaks, dtype=int)
    tolerance = int(round(fs * tolerance_ms / 1000.0))

    matched_ref: list[int] = []
    matched_est: list[int] = []
    used_est: set[int] = set()
    for ref_peak in ref:
        if est.size == 0:
            continue
        distances = np.abs(est - ref_peak)
        order = np.argsort(distances)
        for idx in order:
            if int(idx) not in used_est and int(distances[idx]) <= tolerance:
                used_est.add(int(idx))
                matched_ref.append(int(ref_peak))
                matched_est.append(int(est[idx]))
                break

    missed = int(ref.size - len(matched_ref))
    false_positive = int(est.size - len(used_est))
    return np.asarray(matched_ref, dtype=int), np.asarray(matched_est, dtype=int), missed, false_positive


def missed_r_peak_rate(reference_peaks: np.ndarray, estimate_peaks: np.ndarray, sample_rate: float) -> float:
    """Return missed R-peak rate using tolerance-based matching."""
    ref = np.asarray(reference_peaks, dtype=int)
    if ref.size == 0:
        raise ValueError("at least one reference peak is required")
    _, _, missed, _ = match_peak_indices(ref, estimate_peaks, sample_rate=sample_rate)
    return float(missed / ref.size)


def false_r_peak_rate(reference_peaks: np.ndarray, estimate_peaks: np.ndarray, sample_rate: float) -> float:
    """Return false R-peak rate relative to the number of estimated peaks."""
    est = np.asarray(estimate_peaks, dtype=int)
    if est.size == 0:
        raise ValueError("at least one estimated peak is required")
    _, _, _, false_positive = match_peak_indices(reference_peaks, est, sample_rate=sample_rate)
    return float(false_positive / est.size)


def r_peak_timing_error_ms(reference_peaks: np.ndarray, estimate_peaks: np.ndarray, sample_rate: float) -> float:
    """Return mean absolute R-peak timing error in milliseconds."""
    ref = np.asarray(reference_peaks, dtype=float)
    est = np.asarray(estimate_peaks, dtype=float)
    if ref.shape != est.shape:
        raise ValueError("peak arrays must have the same shape")
    fs = _validate_sample_rate(sample_rate)
    if ref.size == 0:
        raise ValueError("at least one peak is required")
    return float(np.mean(np.abs(ref - est)) * 1000.0 / fs)


def morphology_corr(reference: np.ndarray, estimate: np.ndarray) -> float:
    """Return Pearson correlation between two morphology windows/signals."""
    ref = _as_1d(reference)
    est = _as_1d(estimate)
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
