"""Classical baseline filters for offline ECG denoising benchmarks."""

from __future__ import annotations

import numpy as np


def moving_average(signal: np.ndarray, window: int) -> np.ndarray:
    """Return centered moving average with edge padding."""
    if window <= 0:
        raise ValueError("window must be positive")
    arr = np.asarray(signal, dtype=float)
    if arr.ndim != 1:
        raise ValueError("signal must be one-dimensional")
    pad = window // 2
    padded = np.pad(arr, (pad, pad), mode="edge")
    kernel = np.ones(window, dtype=float) / float(window)
    return np.convolve(padded, kernel, mode="valid")[: arr.shape[0]]


def highpass_baseline(signal: np.ndarray, window: int = 125) -> np.ndarray:
    """Simple baseline-removal high-pass placeholder."""
    arr = np.asarray(signal, dtype=float)
    return arr - moving_average(arr, window=window)


def bandpass_placeholder(signal: np.ndarray, low_window: int = 125, high_window: int = 5) -> np.ndarray:
    """Simple offline bandpass placeholder using moving averages.

    This is not a production clinical filter. It is a deterministic scaffold
    method for package plumbing and later replacement with validated filters.
    """
    hp = highpass_baseline(signal, window=low_window)
    return moving_average(hp, window=high_window)


def notch_placeholder(signal: np.ndarray) -> np.ndarray:
    """Return input unchanged until validated notch implementation is added."""
    return np.asarray(signal, dtype=float).copy()
