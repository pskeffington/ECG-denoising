"""Wavelet method placeholders for future benchmark passes."""

from __future__ import annotations

import numpy as np


def dwt_threshold_placeholder(signal: np.ndarray) -> np.ndarray:
    """Return input unchanged until DWT thresholding is implemented."""
    return np.asarray(signal, dtype=float).copy()


def swt_threshold_placeholder(signal: np.ndarray) -> np.ndarray:
    """Return input unchanged until SWT thresholding is implemented."""
    return np.asarray(signal, dtype=float).copy()
