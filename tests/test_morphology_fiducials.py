from __future__ import annotations

import csv

import numpy as np

from ecg_denoising.bench.morphology import (
    MORPHOLOGY_PRESERVATION_FIELDS,
    compare_fiducials,
    morphology_result_as_row,
    write_morphology_preservation,
)
from ecg_denoising.metrics.morphology import (
    detect_r_peaks,
    estimate_qrs_width_ms,
    estimate_st_deviation_mv,
    extract_fiducials,
    false_r_peak_rate,
    match_peak_indices,
    missed_r_peak_rate,
)


def fixture_signal(length: int = 1000, peaks: tuple[int, ...] = (100, 300, 500, 700, 900)) -> np.ndarray:
    signal = np.zeros(length, dtype=float)
    x = np.arange(length)
    for peak in peaks:
        signal += np.exp(-0.5 * ((x - peak) / 4.0) ** 2)
    return signal


def test_detect_r_peaks_on_fixture_signal() -> None:
    signal = fixture_signal()
    peaks = detect_r_peaks(signal, sample_rate=250.0, prominence=0.2)
    np.testing.assert_allclose(peaks, np.array([100, 300, 500, 700, 900]), atol=1)


def test_extract_fiducials_returns_positive_width() -> None:
    fiducials = extract_fiducials(fixture_signal(), sample_rate=250.0)
    assert fiducials.r_peaks.size == 5
    assert fiducials.mean_qrs_width_ms > 0.0
    assert np.isfinite(fiducials.mean_st_deviation_mv)


def test_qrs_and_st_estimators_are_finite() -> None:
    signal = fixture_signal()
    peaks = np.array([100, 300, 500, 700, 900])
    assert estimate_qrs_width_ms(signal, peaks, sample_rate=250.0) > 0.0
    assert np.isfinite(estimate_st_deviation_mv(signal, peaks, sample_rate=250.0))


def test_peak_matching_rates() -> None:
    ref = np.array([100, 300, 500])
    est = np.array([102, 700])
    matched_ref, matched_est, missed, false_positive = match_peak_indices(ref, est, sample_rate=250.0)
    assert matched_ref.tolist() == [100]
    assert matched_est.tolist() == [102]
    assert missed == 2
    assert false_positive == 1
    assert missed_r_peak_rate(ref, est, sample_rate=250.0) == 2 / 3
    assert false_r_peak_rate(ref, est, sample_rate=250.0) == 1 / 2


def test_morphology_output_schema_and_writer(tmp_path) -> None:
    reference = fixture_signal()
    estimate = fixture_signal(peaks=(101, 301, 501, 701, 901))
    reference_fiducials = extract_fiducials(reference, sample_rate=250.0)
    estimate_fiducials = extract_fiducials(estimate, sample_rate=250.0)
    result = compare_fiducials(
        dataset="fixture",
        record="synthetic",
        clean_record="synthetic_clean",
        method="bandpass",
        snr_level_db=0,
        channel=0,
        sample_rate=250.0,
        reference_signal=reference,
        estimate_signal=estimate,
        reference_fiducials=reference_fiducials,
        estimate_fiducials=estimate_fiducials,
    )
    assert tuple(morphology_result_as_row(result).keys()) == MORPHOLOGY_PRESERVATION_FIELDS

    output = tmp_path / "morphology_preservation.csv"
    assert write_morphology_preservation(output, [result]) == 1
    with output.open(newline="") as handle:
        reader = csv.DictReader(handle)
        assert tuple(reader.fieldnames or ()) == MORPHOLOGY_PRESERVATION_FIELDS
        rows = list(reader)
    assert rows[0]["method"] == "bandpass"
