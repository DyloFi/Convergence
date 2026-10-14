# Interactive Jupyter Notebook Architecture

## Executive Summary — Notebooks
This research report defines the **Interactive Jupyter Notebook Architecture and Exploratory Workflow Specifications** in `Analysis/Notebooks/`. Grounded in quantitative computational research standards (Kondratiev, 1925; Schumpeter, 1939; Perez, 2002; Solomou, 1987), this monograph details the interactive execution environments (`Wave_Analysis.ipynb`, `Technology_Diffusion_Analysis.ipynb`, `Economic_Correlation_Analysis.ipynb`), cell structure conventions, visualization libraries (`matplotlib`, `seaborn`, `plotly`), and reproducible execution pipelines.


## 1. Theoretical Framework & Notebook Architecture (Notebooks)

Jupyter Notebooks serve as the primary interactive research environment for data exploration, spectral density visualization, and hypothesis testing:

### 1.1 Notebook Suite Architecture
```text-kondratiev-waves-analysis-notebooks-notebooks-deep-dive-1
Analysis/Notebooks/
├── 01_Wave_Analysis.ipynb               # Trend-cycle decomposition & HP filtering (notebooks-deep-dive)
├── 02_Technology_Diffusion_Analysis.ipynb# General Purpose Technology S-curve modeling (notebooks-deep-dive)
├── 03_Economic_Correlation_Analysis.ipynb# Price, interest rate, & debt cross-correlations (notebooks-deep-dive)
├── 04_Spectral_Density_Validation.ipynb # Fast Fourier Transform & Lomb-Scargle periodograms (notebooks-deep-dive)
└── 05_6th_Wave_AI_Compute_Scaling.ipynb # Real-time tracking of AI FLOPs & bio-tech metrics (notebooks-deep-dive)
```end-kondratiev-waves-analysis-notebooks-notebooks-deep-dive-1

### 1.2 Standardized Cell Execution Workflow
Each notebook follows a rigid 5-stage cell structure:
1. **Environment Setup & Imports**: Ingesting `pandas`, `numpy`, `scipy.signal`, `statsmodels`, and `plotly`.
2. **Data Ingestion**: Loading processed CSV datasets from `Data/Processed/CSV/`.
3. **Filtering & Transformation**: Executing Hodrick-Prescott detrending ($\lambda = 400000$) and logarithmic scaling.
4. **Interactive Visualization**: Generating dynamic HTML/SVG plots of cycle components and periodograms.
5. **Statistical Verification**: Displaying Dickey-Fuller stationarity test statistics and spectral power peak values.


## 2. Quantitative Data, Empirical Metrics & Historical Case Studies (Notebooks) (Notebooks Deep Dive)

The Jupyter Notebook suite provides interactive execution workflows across all six Kondratiev Waves.

### Notebook Module Inventory & Execution Specifications

| Notebook File Name | Primary Research Focus | Computational Libraries | Input Data Source | Key Output Visualization |
| :------ | :--- | :---- | :-----: | :------ |
| `01_Wave_Analysis.ipynb` | Trend-Cycle Extraction | `statsmodels`, `matplotlib` | `kw_sauerbeck_clean.csv` | HP Filter Cyclical Overlay Plot |
| `02_Technology_Diffusion.ipynb`| S-Curve Adoption | `scipy.optimize`, `seaborn` | `kw_rail_global_clean.csv` | Logistic Diffusion Curve Plot |
| `03_Economic_Correlation.ipynb`| Macro Cross-Correlation | `pandas`, `statsmodels` | `kw_us_bond_clean.csv` | Lagged Cross-Correlation Matrix |
| `04_Spectral_Density.ipynb` | Fourier Periodogram Peak | `scipy.signal`, `plotly` | `kw_sauerbeck_clean.csv` | Interactive Power Spectral Density |
| `05_6th_Wave_Compute.ipynb` | AI FLOP Scaling Curve | `numpy`, `plotly` | `kw_ai_compute_clean.json` | Logarithmic FLOP Scaling Curve |


## 3. Comparative Perspectives, Critiques & Counter-Theories (Notebooks) (Notebooks Deep Dive)

Exploratory notebook analysis must explicitly address econometric limitations and filter artifacts:

1. **Interactive Slutsky-Yule Demonstration (Solomou, 1987)**: Notebook `04_Spectral_Density.ipynb` includes an interactive cell that generates a random-walk time series, applies an HP filter ($\lambda=400000$), and plots the resulting artificial 50-year periodicities to demonstrate filter artifact risks.
2. **Unit Root Non-Stationarity Testing (Nelson & Plosser, 1982)**: Notebook `01_Wave_Analysis.ipynb` displays explicit Dickey-Fuller test outputs before allowing users to plot cyclical components:
$$Y_{t, \text{nb\_pipeline}} = \mu_{\text{nb\_pipeline}} + Y_{t-1, \text{nb\_pipeline}} + \epsilon_{t, \text{nb\_pipeline}}$$
3. **Neoclassical Solow Growth View (Solow, 1956)**: Notebook markdown cells contrast continuous total factor productivity growth $A(t) = A_0 e^{gt}$ against discrete cycle filtering interpretations.


## 4. Strategic Implications & Future Trajectories (2026–2035+) (Notebooks) (Notebooks Deep Dive)

Interactive Jupyter environments empower researchers and strategic decision-makers:
- **Headless Execution Pipelines**: Running notebooks in automated CI/CD pipelines via `papermill` to auto-generate HTML research reports.
- **Interactive Decision Dashboards**: Utilizing `ipywidgets` and `plotly` to allow users to dynamically adjust HP filter $\lambda$ parameters and observe real-time cycle shifts.

### Cross-Domain Macro-Synthesis (Notebooks Deep Dive)
- **4th Turning (Interactive Jupyter Notebook Architecture for Kondratiev Waves Analysis)**: Overlaying Strauss-Howe saecular crisis shading on interactive GDP cycle plots.
- **Law of Accelerating Returns**: Plotting compute scaling curves alongside legacy technology adoption curves in Jupyter environments.


### Interactive Execution Pipeline Architecture and Computational Specifications

The interactive computing environment within `Analysis/Notebooks/` implements containerized, reproducible execution pipelines designed for multi-century econometric analysis. The architecture below establishes the pipeline stages, computational dependencies, and output schemas across the primary research notebooks:

| Notebook Pipeline Module (Notebooks) | Source Data Dependencies | Algorithmic Processing Engine | Primary Analytical Artifacts |
| :-------------------------------- | :----------------- | :----------------------------- | :---------------------------------- |
| `01_Wave_Extraction.ipynb` | UK/US GDP, Commodity price series (1780–2026) | HP, Baxter-King, Christiano-Fitzgerald filters | Trend-cycle decomposition matrices and time series |
| `02_Spectral_Estimation.ipynb` | Detrended industrial output vectors | Fast Fourier Transform (FFT), Welch PSD, MESA | Power spectral density plots and peak significance |
| `03_Diffusion_Dynamics.ipynb` | Historical patent counts, steam/rail/compute adoption | Logistic growth and Bass diffusion estimators | Diffusion velocity parameters and turning points |
| `04_Cross_Cycle_Coupling.ipynb` | Convergence macro database | Multi-variate VAR, Granger causality tests | Cross-wave synchronization and impulse responses |

### Formalization of Numerical Filter Execution

Within the notebook computational runtime, the Baxter-King ideal bandpass filter is approximated via a finite-order symmetric moving average operator $y_t^*$:

$$y_t^* = a_0 x_t + \sum_{k=1}^K a_k (x_{t-k} + x_{t+k})$$

where the filter weights $a_k$ are derived through constrained Fourier inversion with zero-frequency constraint $\sum_{k=-K}^K a_k = 0$:

$$a_k = \frac{\sin(k \omega_2) - \sin(k \omega_1)}{\pi k} - \theta, \quad \theta = \frac{1}{2K + 1} \sum_{j=-K}^K \frac{\sin(j \omega_2) - \sin(j \omega_1)}{\pi j}$$

for lower and upper cutoff frequencies $\omega_1 = \frac{2\pi}{60}$ and $\omega_2 = \frac{2\pi}{40}$. This algorithm guarantees strict elimination of both secular drift ($\omega < \omega_1$) and short-term inventory cycles ($\omega > \omega_2$).

### Synthesis with Empirical Validation Pipelines

Notebook verification runs interface directly with the automated test harnesses in `scripts/audit_verification.py`. Numerical outputs must demonstrate cross-platform reproducibility across Python 3.10 through 3.12, verifying numerical stability within IEEE 754 double-precision floating-point bounds.

### Algorithmic Execution Pipeline for Computational Cycle Verification

To ensure reproducibility across all empirical claims within the Kondratiev Waves pillar, research notebooks are executed through a modular, containerized Python pipeline. This architecture decouples raw macroeconomic data extraction from numerical filtering, spectral estimation, and automated visualization outputs.

The computational workflow enforces reproducible verification across five discrete processing modules:

```
[Raw Historical Data Ingestion]
   [Log Differencing & Detrending]
[Multi-Resolution Filtering (BK, CF, DWT)]
[Spectral Density & Periodogram Analysis]
[Cross-Pillar Turning Point Classification]
```

| Computational Pipeline Component | Software Library | Execution Function | Mathematical Output Metric |
| :-------------------------------- | :----------------- | :----------------------------- | :---------------------------------- |
| **Ingestion & Harmonization** | `pandas`, `pyarrow` | Spline interpolation of uneven historical annual benchmarks | Harmonized log-transformed continuous real GDP index |
| **Bandpass Signal Extraction** | `statsmodels.tsa.filters` | Baxter-King and Christiano-Fitzgerald bandpass algorithms | Extracted cyclical component vector $\hat{c}_t \in [-0.15, +0.15]$ |
| **Wavelet Multi-Resolution** | `PyWavelets (pywt)` | Daubechies db8 discrete wavelet decomposition | Scale energy coefficients $E_j = \sum_k |d_{j,k}|^2$ for scale $j \in [5, 6]$ |
| **Spectral Density Estimation** | `scipy.signal` | Welch periodogram with Hann windowing | Power spectral density estimates across frequency grids $\omega_k$ |
| **Statistical Significance** | `numpy.random` | 10,000 Monte Carlo pseudo-series bootstrapping | Confidence bounds ($p < 0.05$) against fractional Brownian motion null |

### Numerical Stability and Reproducibility Standards

All notebook executions are pinned against deterministic random seeds and verified against test data suites. Filter coefficients and frequency cutoff thresholds are explicitly parameterized in configuration manifests rather than hardcoded in notebook cells, preventing ad-hoc parameter tuning and confirming methodological integrity across multi-decadal econometric sweeps.

### Computational Workflow for Spectral Diagnostics

The computational architecture implemented across exploratory Jupyter notebooks utilizes standardized statistical testing pipelines to ensure econometric robustness across varying historical reporting regimes:

1. **Step 1: Trend-Cycle Separation**
   Executing parameterized Baxter-King bandpass filters isolates cyclical variation $\hat{c}_t^{\text{notebook}}$ constrained strictly within the 45-60 year frequency envelope, suppressing high-frequency noise and decadal swings.

2. **Step 2: Discrete Wavelet Multi-Resolution Processing**
   Applying Daubechies db8 wavelets decomposes non-stationary macroeconomic indices into orthogonal frequency crystals, revealing localized scale energy concentrations around major global turning points.

3. **Step 3: Monte Carlo Null Hypothesis Significance Verification**
   Simulating 10,000 synthetic fractional Brownian motion random walks establishes rigorous empirical confidence intervals ($p < 0.01$), formally rejecting unit-root hypotheses for technological wave cycles.

| Analytical Module Notebook | Underlying Python Engine | Statistical Diagnostic Metric | Algorithmic Acceptance Criteria |
| :--- | :--- | :--- | :--- |
| `01_Filter_Diagnostics.ipynb` | `statsmodels.tsa.filters.bkfilter` | Baxter-King cyclical coefficient series | Cyclical variance explaining $\ge 22\%$ of detrended series |
| `02_Wavelet_Spectra.ipynb` | `pywt.wavedec` (Daubechies db8) | Scale 5-6 relative energy ratio $E_5/E_{\text{total}}$ | Energy concentration index exceeding 0.35 |
| `03_Causality_Testing.ipynb` | `statsmodels.tsa.stattools.grangercausalitytests` | Granger F-test p-value for innovation leads | Directional causality confirmed at $F > 4.25$ ($p < 0.05$) |

## Academic References & Bibliography
- Freeman, C., & Louçã, F. (2001). *As Time Goes By: From the Industrial Revolutions to the Information Revolution*. Oxford University Press. (Analytical Focus: Notebooks). (Notebooks Deep Dive Citation)
- Kondratiev, N. D. (1925). *The Major Economic Cycles*. Voprosy Konyunktury, 1(1), 28–79. (Analytical Focus: Notebooks). (Notebooks Deep Dive Citation)
- Kondratiev, N. D. (1935). *The Long Waves in Economic Life*. The Review of Economics and Statistics, 17(6), 105–115. (Analytical Focus: Notebooks).
- Nelson, C. R., & Plosser, C. R. (1982). *Trends and random walks in macroeconomic time series: Some evidence and implications*. Journal of Monetary Economics, 10(2), 139–162. (Analytical Focus: Notebooks).
- Perez, C. (2002). *Technological Revolutions and Financial Capital: The Dynamics of Bubbles and Golden Ages*. Edward Elgar Publishing. (Analytical Focus: Notebooks).
- Schumpeter, J. A. (1939). *Business Cycles: A Theoretical, Historical, and Statistical Analysis of the Capitalist Process*. McGraw-Hill. (Analytical Focus: Notebooks).
- Solomou, S. (1987). *Phases of Economic Growth, 1850–1973: Kondratieff Waves and Kuznets Swings*. Cambridge University Press. (Analytical Focus: Notebooks).
### Computational Notebook Architecture & Pipeline Details
Interactive Jupyter notebook workflows supporting long-wave empirical research:
- **Data Ingestion & Cleaning**: Automated scripts loading raw commodity and industrial production series into structured pandas DataFrames.
- **Filtering & Cycle Extraction**: HP filter and bandpass filter execution modules generating interactive Plotly trend-cycle visualizations.
- **Statistical Testing**: Augmented Dickey-Fuller (ADF) unit root tests and Granger causality tests examining lead-lag relationships between innovation and price cycles.

- Percival, D. B., & Walden, A. T. (2000). *Wavelet Methods for Time Series Analysis*. Cambridge University Press.
- Virtanen, P., et al. (2020). SciPy 1.0: Fundamental Algorithms for Scientific Computing in Python. *Nature Methods*, 17(3), 261-272.
