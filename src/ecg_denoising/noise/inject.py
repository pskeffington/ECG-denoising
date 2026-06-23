"""Deterministic noise injection for offline research benchmarks."""

from __future__ import annotations

import numpy as np


def signal_power(signal: np.ndarray) -> float:
    """Return mean squared signal power."""
    arr = np.asarray(signal, dtype=float)
    return float(np.mean(arr * arr))


def scale_noise_to_snr(signal: np.ndarray, noise: np.ndarray, snr_db: float) -> np.ndarray:
    """Scale noise so signal-to-noise ratio equals ``snr_db``.

    Inputs must have identical shape. The function is deterministic and does
    not mutate either input array.
    """
    clean = np.asarray(signal, dtype=float)
    raw_noise = np.asarray(noise, dtype=float)
    if clean.shape != raw_noise.shape:
        raise ValueError("signal and noise must have the same shape")

    p_signal = signal_power(clean)
    p_noise = signal_power(raw_noise)
    if p_signal == 0.0:
        raise ValueError("signal power must be nonzero")
    if p_noise == 0.0:
        raise ValueError("noise power must be nonzero")

    target_noise_power = p_signal / (10.0 ** (snr_db / 10.0))
    return raw_noise * np.sqrt(target_noise_power / p_noise)


def add_noise_at_snr(signal: np.ndarray, noise: np.ndarray, snr_db: float) -> np.ndarray:
    """Return ``signal`` with ``noise`` scaled to the requested SNR."""
    clean = np.asarray(signal, dtype=float)
    return clean + scale_noise_to_snr(clean, noise, snr_db)
