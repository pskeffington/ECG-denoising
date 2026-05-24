# Method Review Matrix

This file indexes ECG denoising studies by method family, noise target, dataset, metric, reproducibility, and clinical preservation focus.

## Matrix Columns

| Column | Definition |
|---|---|
| Method | Denoising method or model |
| Family | Classical, adaptive, wavelet/time-frequency, deep learning, or hybrid |
| Noise target | Baseline wander, muscle artifact, electrode motion, powerline, or mixed noise |
| Dataset | Dataset used for evaluation |
| Metrics | Reported signal-quality or clinical metrics |
| Clinical preservation measured? | Whether morphology, intervals, R-peaks, ST segment, or downstream diagnosis were evaluated |
| Open code? | Whether implementation is public |
| Limitations | Primary reproducibility or clinical limitation |
| Citation | Verified citation entry |

## Seed Matrix

| Method | Family | Noise target | Dataset | Metrics | Clinical preservation measured? | Open code? | Limitations | Citation |
|---|---|---|---|---|---|---|---|---|
| High-pass filter | Classical | Baseline wander | TBD | SNR, RMSE, PRD | Partial | Yes, internal | Parameter-sensitive | TBD |
| Bandpass filter | Classical | Mixed common ECG noise | TBD | SNR, RMSE, PRD | Partial | Yes, internal | May suppress relevant frequency content | TBD |
| Notch filter | Classical | Powerline interference | Synthetic | SNR, RMSE | No | Yes, internal | Narrow use case | TBD |
| DWT thresholding | Wavelet/time-frequency | Baseline wander, muscle artifact | TBD | SNR, RMSE, PRD | TBD | Planned | Wavelet/threshold selection sensitive | TBD |
| SWT thresholding | Wavelet/time-frequency | Baseline wander, muscle artifact | TBD | SNR, RMSE, PRD | TBD | Planned | Computationally heavier than DWT | TBD |
| Denoising autoencoder | Deep learning | Mixed noise | TBD | SNR, correlation | TBD | Planned | Requires training protocol | TBD |

## Review Target

The first literature pass should index at least 25 studies. Each included paper must be classified by method family and assessed for whether it evaluates clinical waveform preservation, not only generic signal quality.
