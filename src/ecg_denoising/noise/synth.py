"""Synthetic ECG-like signal helpers for tests and placeholder benchmarks."""

from __future__ import annotations

import numpy as np


def synthetic_ecg(length: int = 1000, sample_rate: float = 250.0) -> np.ndarray:
    """Create a simple deterministic ECG-like waveform.

    This is not a clinical simulator. It is only a placeholder signal for
    package tests and offline benchmark plumbing.
    """
    if length <= 0:
        raise ValueError("length must be positive")
    if sample_rate <= 0:
        raise ValueError("sample_rate must be positive")

    t = np.arange(length, dtype=float) / sample_rate
    base = 0.08 * np.sin(2.0 * np.pi * 1.2 * t)
    qrs = np.zeros_like(t)
    beat_gap = max(int(sample_rate * 0.8), 1)
    for center in range(beat_gap // 2, length, beat_gap):
        width = max(int(sample_rate * 0.025), 1)
        idx = np.arange(length)
        qrs += np.exp(-0.5 * ((idx - center) / width) ** 2)
    return base + qrs


def white_noise(length: int, seed: int = 1729) -> np.ndarray:
    """Create deterministic standard normal noise."""
    if length <= 0:
        raise ValueError("length must be positive")
    rng = np.random.default_rng(seed)
    return rng.normal(0.0, 1.0, size=length)
