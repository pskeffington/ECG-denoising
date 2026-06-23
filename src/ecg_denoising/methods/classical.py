"""Classical baseline filters for offline ECG denoising benchmarks.

These filters are deterministic, sample-rate-aware research baselines. They
are not clinical deployment code and do not imply diagnostic validation.
"""

from __future__ import annotations

from collections.abc import Callable

import numpy as np
from scipy import signal as sp_signal


DEFAULT_HIGHPASS_HZ = 0.5
DEFAULT_BANDPASS_LOW_HZ = 0.5
DEFAULT_BANDPASS_HIGH_HZ = 40.0
DEFAULT_NOTCH_HZ = 60.0
DEFAULT_NOTCH_Q = 30.0
DEFAULT_FILTER_ORDER = 4


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


def _sos_filter(signal: np.ndarray, sos: np.ndarray) -> np.ndarray:
    """Apply a stable zero-phase SOS filter with fallback padding."""
    arr = _as_1d(signal)
    try:
        return sp_signal.sosfiltfilt(sos, arr)
    except ValueError:
        return sp_signal.sosfiltfilt(sos, arr, padlen=0)


def highpass_filter(
    signal: np.ndarray,
    sample_rate: float,
    cutoff_hz: float = DEFAULT_HIGHPASS_HZ,
    order: int = DEFAULT_FILTER_ORDER,
) -> np.ndarray:
    """Apply a Butterworth high-pass filter for baseline-wander reduction."""
    fs = _validate_sample_rate(sample_rate)
    if cutoff_hz <= 0.0 or cutoff_hz >= fs / 2.0:
        raise ValueError("cutoff_hz must be between 0 and Nyquist")
    sos = sp_signal.butter(order, cutoff_hz, btype="highpass", fs=fs, output="sos")
    return _sos_filter(signal, sos)


def bandpass_filter(
    signal: np.ndarray,
    sample_rate: float,
    low_hz: float = DEFAULT_BANDPASS_LOW_HZ,
    high_hz: float = DEFAULT_BANDPASS_HIGH_HZ,
    order: int = DEFAULT_FILTER_ORDER,
) -> np.ndarray:
    """Apply a Butterworth bandpass filter for common ECG benchmark range."""
    fs = _validate_sample_rate(sample_rate)
    if low_hz <= 0.0:
        raise ValueError("low_hz must be positive")
    if high_hz >= fs / 2.0:
        raise ValueError("high_hz must be below Nyquist")
    if low_hz >= high_hz:
        raise ValueError("low_hz must be lower than high_hz")
    sos = sp_signal.butter(order, [low_hz, high_hz], btype="bandpass", fs=fs, output="sos")
    return _sos_filter(signal, sos)


def notch_filter(
    signal: np.ndarray,
    sample_rate: float,
    notch_hz: float = DEFAULT_NOTCH_HZ,
    quality_factor: float = DEFAULT_NOTCH_Q,
) -> np.ndarray:
    """Apply a zero-phase IIR notch filter for powerline interference."""
    fs = _validate_sample_rate(sample_rate)
    if notch_hz <= 0.0 or notch_hz >= fs / 2.0:
        raise ValueError("notch_hz must be between 0 and Nyquist")
    if quality_factor <= 0.0:
        raise ValueError("quality_factor must be positive")
    b, a = sp_signal.iirnotch(w0=notch_hz, Q=quality_factor, fs=fs)
    arr = _as_1d(signal)
    try:
        return sp_signal.filtfilt(b, a, arr)
    except ValueError:
        return sp_signal.filtfilt(b, a, arr, padlen=0)


def bandpass_notch_filter(
    signal: np.ndarray,
    sample_rate: float,
    low_hz: float = DEFAULT_BANDPASS_LOW_HZ,
    high_hz: float = DEFAULT_BANDPASS_HIGH_HZ,
    notch_hz: float = DEFAULT_NOTCH_HZ,
    quality_factor: float = DEFAULT_NOTCH_Q,
    order: int = DEFAULT_FILTER_ORDER,
) -> np.ndarray:
    """Apply bandpass filtering followed by powerline notch filtering."""
    bandpassed = bandpass_filter(signal, sample_rate, low_hz=low_hz, high_hz=high_hz, order=order)
    return notch_filter(bandpassed, sample_rate, notch_hz=notch_hz, quality_factor=quality_factor)


CLASSICAL_METHODS: dict[str, Callable[[np.ndarray, float], np.ndarray]] = {
    "highpass": highpass_filter,
    "bandpass": bandpass_filter,
    "notch": notch_filter,
    "bandpass_notch": bandpass_notch_filter,
}


def apply_classical_method(signal: np.ndarray, sample_rate: float, method: str) -> np.ndarray:
    """Apply a named classical baseline method."""
    try:
        fn = CLASSICAL_METHODS[method]
    except KeyError as exc:
        valid = ", ".join(sorted(CLASSICAL_METHODS))
        raise ValueError(f"unknown classical method: {method}; valid methods: {valid}") from exc
    return fn(signal, sample_rate)


# Backward-compatible aliases used by the initial scaffold tests and runners.
def moving_average(signal: np.ndarray, window: int) -> np.ndarray:
    """Return centered moving average with edge padding."""
    if window <= 0:
        raise ValueError("window must be positive")
    arr = _as_1d(signal)
    pad = window // 2
    padded = np.pad(arr, (pad, pad), mode="edge")
    kernel = np.ones(window, dtype=float) / float(window)
    return np.convolve(padded, kernel, mode="valid")[: arr.shape[0]]


def highpass_baseline(signal: np.ndarray, sample_rate: float = 360.0) -> np.ndarray:
    """Backward-compatible high-pass baseline alias."""
    return highpass_filter(signal, sample_rate=sample_rate)


def bandpass_placeholder(signal: np.ndarray, sample_rate: float = 360.0) -> np.ndarray:
    """Backward-compatible alias for the validated bandpass baseline."""
    return bandpass_filter(signal, sample_rate=sample_rate)


def notch_placeholder(signal: np.ndarray, sample_rate: float = 360.0) -> np.ndarray:
    """Backward-compatible alias for the validated notch baseline."""
    return notch_filter(signal, sample_rate=sample_rate)
