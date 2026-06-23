"""Generic signal-quality metrics for ECG denoising benchmarks."""

from __future__ import annotations

import numpy as np


def _as_pair(reference: np.ndarray, estimate: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    ref = np.asarray(reference, dtype=float)
    est = np.asarray(estimate, dtype=float)
    if ref.shape != est.shape:
        raise ValueError("reference and estimate must have the same shape")
    return ref, est


def rmse(reference: np.ndarray, estimate: np.ndarray) -> float:
    """Return root mean square error."""
    ref, est = _as_pair(reference, estimate)
    return float(np.sqrt(np.mean((ref - est) ** 2)))


def prd(reference: np.ndarray, estimate: np.ndarray) -> float:
    """Return percentage root-mean-square difference."""
    ref, est = _as_pair(reference, estimate)
    denom = np.sqrt(np.sum(ref * ref))
    if denom == 0.0:
        raise ValueError("reference energy must be nonzero")
    return float(100.0 * np.sqrt(np.sum((ref - est) ** 2)) / denom)


def pearson_corr(reference: np.ndarray, estimate: np.ndarray) -> float:
    """Return Pearson correlation for two one-dimensional signals."""
    ref, est = _as_pair(reference, estimate)
    if ref.ndim != 1:
        raise ValueError("signals must be one-dimensional")
    if np.std(ref) == 0.0 or np.std(est) == 0.0:
        raise ValueError("signals must have nonzero variance")
    return float(np.corrcoef(ref, est)[0, 1])


def snr_db(reference: np.ndarray, estimate: np.ndarray) -> float:
    """Return SNR in dB using reference and estimate error."""
    ref, est = _as_pair(reference, estimate)
    signal_power = np.mean(ref * ref)
    noise_power = np.mean((ref - est) ** 2)
    if signal_power == 0.0:
        raise ValueError("reference power must be nonzero")
    if noise_power == 0.0:
        return float("inf")
    return float(10.0 * np.log10(signal_power / noise_power))


def snr_improvement(reference: np.ndarray, noisy: np.ndarray, denoised: np.ndarray) -> float:
    """Return denoised SNR minus noisy SNR."""
    return snr_db(reference, denoised) - snr_db(reference, noisy)
