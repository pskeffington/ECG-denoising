# Benchmark Protocol

## Objective

Compare ECG denoising methods under a common open-data protocol and evaluate both signal-quality improvement and clinical morphology preservation.

## Signal Selection

Phase 1 uses open ECG records suitable for noise injection and reproducible benchmarking. Raw data are not committed to the repository.

## Noise Injection

Noise sources include baseline wander, muscle artifact, electrode-motion artifact, and synthetic powerline interference.

## SNR Levels

The initial benchmark uses fixed SNR levels:

- -6 dB
- 0 dB
- 6 dB
- 12 dB

## Phase 1 Denoising Methods

- High-pass filtering
- Bandpass filtering
- Notch filtering
- Combined bandpass plus notch filtering
- DWT thresholding
- SWT thresholding

## Classical Baseline Parameters

The first executable baselines are deterministic, sample-rate-aware research filters implemented with SciPy. They are benchmark baselines only and are not clinical deployment code.

| Method name | Implementation | Default parameters | Primary benchmark role |
|---|---|---|---|
| `highpass` | Butterworth SOS high-pass with zero-phase filtering | cutoff = 0.5 Hz; order = 4 | Baseline-wander reduction |
| `bandpass` | Butterworth SOS bandpass with zero-phase filtering | low = 0.5 Hz; high = 40 Hz; order = 4 | General ECG denoising baseline |
| `notch` | IIR notch with zero-phase filtering | notch = 60 Hz; quality factor = 30 | Powerline interference baseline |
| `bandpass_notch` | Bandpass followed by notch | bandpass defaults plus notch defaults | Combined common-noise baseline |

The real-data NSTDB benchmark can select these methods by name with `--method`. For Phase 1, method comparisons should be interpreted as reproducible preprocessing benchmarks, not clinical validation.

## Signal-Quality Metrics

- SNR improvement
- Root mean square error
- Percentage root-mean-square difference
- Pearson correlation

## Morphology-Preservation Metrics

- R-peak timing error
- Missed R-peak rate
- False R-peak rate
- RR interval distortion
- QRS width distortion
- ST-segment deviation change
- Morphology correlation

## Output Tables

| Table | Description |
|---|---|
| baseline_signal_quality.csv | Method-by-noise-by-SNR signal-quality results |
| morphology_preservation.csv | Method-by-noise-by-SNR clinical morphology preservation results |
| dataset_manifest.csv | Dataset source, access, and role information |

## Output Figures

- Clean/noisy/denoised ECG overlay
- Metric comparison by SNR level
- Morphology distortion plots

## Reproducibility Controls

- No raw PhysioNet data committed
- Local data paths configured through ignored environment files
- Fixed random seeds for noise injection where applicable
- Versioned benchmark outputs
- Documented preprocessing parameters
