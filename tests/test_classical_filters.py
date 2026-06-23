from __future__ import annotations

import numpy as np
import pytest

from ecg_denoising.methods.classical import (
    apply_classical_method,
    bandpass_filter,
    bandpass_notch_filter,
    highpass_filter,
    notch_filter,
)
from ecg_denoising.noise.synth import synthetic_ecg


def test_highpass_filter_preserves_shape() -> None:
    signal = synthetic_ecg(length=1000, sample_rate=250.0)
    filtered = highpass_filter(signal, sample_rate=250.0)
    assert filtered.shape == signal.shape


def test_bandpass_filter_preserves_shape() -> None:
    signal = synthetic_ecg(length=1000, sample_rate=250.0)
    filtered = bandpass_filter(signal, sample_rate=250.0)
    assert filtered.shape == signal.shape


def test_notch_filter_preserves_shape() -> None:
    signal = synthetic_ecg(length=1000, sample_rate=250.0)
    filtered = notch_filter(signal, sample_rate=250.0, notch_hz=60.0)
    assert filtered.shape == signal.shape


def test_bandpass_notch_filter_preserves_shape() -> None:
    signal = synthetic_ecg(length=1000, sample_rate=250.0)
    filtered = bandpass_notch_filter(signal, sample_rate=250.0, notch_hz=60.0)
    assert filtered.shape == signal.shape


def test_filters_are_deterministic() -> None:
    signal = synthetic_ecg(length=1000, sample_rate=250.0)
    first = bandpass_filter(signal, sample_rate=250.0)
    second = bandpass_filter(signal, sample_rate=250.0)
    np.testing.assert_allclose(first, second)


def test_method_selector_rejects_unknown_method() -> None:
    signal = synthetic_ecg(length=1000, sample_rate=250.0)
    with pytest.raises(ValueError, match="unknown classical method"):
        apply_classical_method(signal, sample_rate=250.0, method="missing")
