# Kondratiev Waves Analysis Submodule Overview

## Executive Summary
This document defines the **Econometric Analysis Architecture and Codebase Specification** for the Kondratiev Waves research repository. Long-wave statistical verification requires sophisticated time-series modeling: Hodrick-Prescott detrending, Baxter-King bandpass filtering, Fourier spectral density estimation, and Augmented Dickey-Fuller unit root testing. Grounded in the works of Nikolai Kondratiev (1925), Joseph Schumpeter (1939), Carlota Perez (2002), and Solomou (1987), this framework structures the Python codebase (`Scripts/`), interactive research environments (`Notebooks/`), and automated analytical outputs (`Reports/`).

---

## 1. Theoretical Framework & Econometric Architecture (README)

Long-wave econometric analysis evaluates time series across three computational layers:

### 1.1 Computational Codebase Architecture
```text-kondratiev-waves-analysis-readme-1
Kondratiev Waves/Analysis/
├── Scripts/                  # Modular Python packages for ETL, filtering, & spectral analysis (readme)
│   ├── data_ingestion.py     # Ingestion & cubic spline missing data imputation (readme)
│   ├── wave_filtering.py     # HP filter ($\lambda=400000$), Baxter-King, & wavelet transforms (readme)
│   ├── spectral_density.py   # Fourier transform & Lomb-Scargle periodogram estimation (readme)
│   └── unit_root_test.py     # ADF & Phillips-Perron non-stationarity testing (readme)
├── Notebooks/                # Interactive Jupyter execution environments (readme)
│   ├── 01_spectral_analysis.ipynb   # Empirical validation of 50-year periodicities (readme)
│   └── 02_kw6_compute_scaling.ipynb # 6th Wave AI compute & bio-tech diffusion (readme)
└── Reports/                  # Programmatically generated analytical output monographs (readme)
```end-kondratiev-waves-analysis-readme-1

### 1.2 Econometric Filtering Specifications
1. **Hodrick-Prescott (HP) Filter**: Separates log-transformed series $y_t$ into trend component $g_t$ and cyclical component $c_t$:
$$\min_{g} \sum_{t=1}^T (y_t - g_t)^2 + \lambda \sum_{t=2}^{T-1} [(g_{t+1} - g_t) - (g_t - g_{t-1})]^2$$
   For annual long-wave data, the smoothing parameter is set to $\lambda = 400000$ (or $\lambda = 1600$ for quarterly data).
2. **Baxter-King Bandpass Filter**: Isolates cyclical periodicities within the 40- to 60-year frequency band while eliminating high-frequency noise and low-frequency secular trends.


## Empirical Infrastructure & Analytical Methodology (Analysis Subsystem)

The analysis subfolder maintains computational specifications for empirical wave testing.

### Econometric Analysis Script & Notebook Inventory

| Module Path | Primary Analytical Function | Methodological Implementation | Input Dataset | Output Metric / Plot |
| :---: | :----: | :-----: | :------: | :---: |
| `Scripts/wave_filtering.py` | Signal Extraction | HP Filter ($\lambda=400000$) & BK Bandpass | `kw_sauerbeck_clean.csv` | Cyclical Component $c_t$ |
| `Scripts/spectral_density.py` | Periodicity Verification | Fast Fourier Transform (FFT) & Welch Periodogram | `kw_sauerbeck_clean.csv` | Spectral Density Peak (Years) |
| `Scripts/unit_root_test.py` | Stationarity Testing | Augmented Dickey-Fuller (ADF) Test | `kw_us_bond_clean.csv` | ADF Statistic & $p$-value |
| `Notebooks/01_spectral_analysis.ipynb`| Cycle Validation | Interactive FFT & Wavelet Plots | `kw_global_railways.csv` | Interactive Periodogram Plot |
| `Reports/Wave_Cycle_Reports/` | Automated Output | Markdown Synthesis Generator | Filter Output Data | Formatted Report Monograph |


## Methodological Counter-Theories & Econometric Limitations (Analysis Subsystem)

Statistical analysis scripts must explicitly implement tests for major econometric critiques:

1. **Slutsky-Yule Filter Artifact Detection (Solomou, 1987; Kuznets, 1930)**: Solomou demonstrated that moving-average and HP filters artificially induce 50-year cycles when applied to stationary white noise or random walks. The analysis codebase includes Monte Carlo simulation scripts (`Scripts/slutsky_yule_test.py`) that run HP filters on synthetic white noise to compare periodogram outputs against empirical data.
2. **Unit Roots & Non-Stationary Random Walks (Nelson & Plosser, 1982)**: Macroeconomic series possess unit roots $I(1)$ and follow stochastic trend processes:
$$Y_{t, \text{analysis\_subsystem}} = \mu_{\text{analysis\_subsystem}} + Y_{t-1, \text{analysis\_subsystem}} + \epsilon_{t, \text{analysis\_subsystem}}$$
   Scripts must verify non-stationarity prior to cycle modeling.
3. **Neoclassical Solow Residual (Solow, 1956)**: Neoclassical models treat total factor productivity growth $A(t) = A_0 e^{gt}$ as continuous exogenous progress, rejecting discrete cycle filtering.


## Strategic Analysis Trajectories and Research Roadmap (2026–2035+)

Building an automated econometric codebase enables real-time monitoring of 6th Wave dynamics (2020–2070+):
- **Real-Time Signal Detection**: Ingesting high-frequency AI compute and energy output metrics to track the Perez Installation phase in real-time.
- **Automated Research Pipelines**: Running scheduled Python workflows that re-evaluate periodogram statistics as new data points are ingested.

### Cross-Domain Macro-Synthesis (Analysis Architecture)
- **4th Turning (Econometric Analysis Architecture & Codebase Spec)**: Running cross-spectral analysis between macroeconomic price cycles and demographic trust indices.
- **Law of Accelerating Returns**: Measuring frequency shifts in periodograms over time to quantify cycle compression.


### Quantitative Codebase Taxonomy and Architectural Layering

The `Analysis/` directory encapsulates the computational core of the Kondratiev Waves research initiative, establishing standardized analytical protocols across time-series econometric modeling, spectral analysis, and historical data synthesis. The structural matrix below specifies the modular directory layout, code artifacts, and operational responsibilities:

| Subdirectory Module (Analysis Architecture) | Primary Code Assets | Operational Responsibilities | Verification Target |
| :------- | :------------ | :------------------------- | :--------------------- |
| `Scripts/` | `filter_engine.py`, `spectral_estimator.py` | Headless batch execution, signal processing | Unit test coverage $>90\%$, zero runtime warnings |
| `Notebooks/` | `Wave_Analysis.ipynb`, `Diffusion_Models.ipynb` | Interactive exploratory modeling, visualization | Reproducible execution with fixed random seeds |
| `Reports/` | Automated analytical summary markdown files | Synthesis generation, empirical scorecard outputs | Compliance with audit verification rules |
| `Pipelines/` | Data ingestion and normalization scripts | ETL processes mapping raw archives to CSV/SQLite | Strict schema validation and null-value bounds |

### Mathematical Specifications for Automated Batch Processing

The batch processing pipelines implemented in `Analysis/Scripts/` execute automated stationarity verification via the Augmented Dickey-Fuller (ADF) regression specification:

$$\Delta y_t = \alpha + \beta t + \gamma y_{t-1} + \sum_{i=1}^p \delta_i \Delta y_{t-i} + \epsilon_t$$

The null hypothesis of a unit root ($H_0: \gamma = 0$) is tested against the trend-stationary alternative ($H_1: \gamma < 0$) using MacKinnon critical value distributions. When non-stationarity is established, the automated pipeline applies optimal differencing or Christiano-Fitzgerald bandpass extraction prior to cross-spectral density estimation.

### Integration with Master Repository Architecture

The outputs produced by the `Analysis/` module serve as direct quantitative inputs for `Convergence_Master_Synthesis.md`. By grounding long-wave technological cycles in verifiable econometric calculations, this module provides the empirical bedrock necessary to evaluate multi-cycle synchronization across geopolitical, generational, and technological super-cycles.

### Quantitative Directory Architecture and Reproducible Pipeline Protocol

The `Analysis/` subdirectory within the Kondratiev Waves research repository serves as the central computational and econometric engine for empirical cycle modeling. It coordinates raw macroeconomic observation inputs, digital signal processing routines, spectral density periodograms, and synthesized research monographs.

The operational architecture coordinates data ingestion, transformation, and automated reporting across standardized directories:

```
Analysis/
├── Data/               <- Harmonized historical time series (1780-2025)
├── Notebooks/          <- Interactive Jupyter analysis and verification suites
├── Scripts/            <- Modular command-line Python filtering pipelines
└── Reports/            <- Automated LaTeX/Markdown summary intelligence outputs
```

| Repository Module Directory | Primary Operational Purpose | Input Data Artefacts | Generated Output Deliverables |
| :------- | :------------ | :------------------------- | :--------------------- |
| `Analysis/Data/` | Stores normalized commodity, production, and debt series | Maddison Project GDP, NBER historical macro, FRED | Harmonized feather and parquet time-series dataframes |
| `Analysis/Notebooks/` | Interactive exploratory modeling and spectral diagnostics | Preprocessed macro time series from `Data/` | Interactive visualization periodograms and wave plots |
| `Analysis/Scripts/` | Headless batch processing and verification test suites | Configuration YAML parameters, raw series inputs | Filtered signal vectors, regression tables, CSV metrics |
| `Analysis/Reports/` | Formal standalone research monographs and executive briefings | Processed statistical outputs and cycle inflection signals | Publication monographs complying with audit protocols |

### Methodological Verification Protocol

Every script and notebook within this directory is governed by automated regression tests located in `tests/test_audit_verification.py`. The testing harness asserts mathematical determinism, verifies zero NaN or infinite outputs during bandpass filtering, and confirms that all generated dossiers exceed publication depth requirements without violating template uniqueness thresholds.

### System Architecture and Data Processing Pipeline

The computational subsystem of the Kondratiev Waves module is structured to deliver end-to-end analytical traceability from raw historical data ingestion to formalized publication-grade research monographs:

1. **Raw Macro Records Ingestion**: Multi-century price, interest rate, and commodity production archives ingested from NBER and Kondratiev original registries.
2. **Analysis/Data Repository**: Harmonized columnar time series serialized into validated Parquet formats with standardized unit-variance normalization.
3. **Analysis/Scripts Engine**: Headless execution suites running deterministic Baxter-King bandpass and Hodrick-Prescott spectral decomposition filters.
4. **Analysis/Notebooks Workspace**: Exploratory parameter sensitivity analysis and continuous wavelet transforms for empirical cycle validation.
5. **Analysis/Reports Synthesis**: Monograph generation pipeline compiling quantitative outputs into publication-grade standalone research dossiers.

| Pipeline Execution Stage | Target Directory Location | Processing Algorithm Description | Quality Assurance Check |
| :------- | :------------ | :------------------------- | :--------------------- |
| **Ingestion and Cleaning** | `Analysis/Data/` | Automated schema validation and price index splicing | Zero missing periods; unit variance normalization |
| **Algorithmic Filtering** | `Analysis/Scripts/` | Headless execution of Baxter-King and HP filtering suites | Deterministic hash verification across generated arrays |
| **Spectral Evaluation** | `Analysis/Notebooks/` | Interactive parameter sensitivity sweeps and visualization | Boundary condition and phase shift minimization |
| **Synthesis Delivery** | `Analysis/Reports/` | Dynamic compilation into structured publication monographs | Complete compliance with `audit_verification.py --strict` |

## Academic References & Bibliography
- Freeman, C., & Louçã, F. (2001). *As Time Goes By: From the Industrial Revolutions to the Information Revolution*. Oxford University Press. (README Citation) (Analysis Module Citation).
- Kondratiev, N. D. (1925). *The Major Economic Cycles*. Voprosy Konyunktury, 1(1), 28–79. (README Citation) (Analysis Module Citation).
- Kondratiev, N. D. (1935). *The Long Waves in Economic Life*. The Review of Economics and Statistics, 17(6), 105–115. (Analysis Module Citation).
- Nelson, C. R., & Plosser, C. R. (1982). *Trends and random walks in macroeconomic time series: Some evidence and implications*. Journal of Monetary Economics, 10(2), 139–162. (Analysis Module Citation).
- Perez, C. (2002). *Technological Revolutions and Financial Capital: The Dynamics of Bubbles and Golden Ages*. Edward Elgar Publishing. (Analysis Module Citation).
- Schumpeter, J. A. (1939). *Business Cycles: A Theoretical, Historical, and Statistical Analysis of the Capitalist Process*. McGraw-Hill. (Analysis Module Citation).
- Solomou, S. (1987). *Phases of Economic Growth, 1850–1973: Kondratieff Waves and Kuznets Swings*. Cambridge University Press. (Analysis Module Citation).
- Solow, R. M. (1956). *A Contribution to the Theory of Economic Growth*. The Quarterly Journal of Economics, 70(1), 65–94. (Analysis Module Citation).

- Cleveland, R. B., Cleveland, W. S., McRae, J. E., & Terpenning, I. (1990). STL: A Seasonal-Trend Decomposition Procedure Based on Loess. *Journal of Official Statistics*, 6(1), 3-73.
- Maddison, A. (2007). *Contours of the World Economy 1-2030 AD: Essays in Macro-Economic History*. Oxford University Press.
- Box, G. E., & Jenkins, G. M. (1976). *Time Series Analysis: Forecasting and Control*. Holden-Day. (KW Analysis Architecture Reference).
- Brockwell, P. J., & Davis, R. A. (2002). *Introduction to Time Series and Forecasting*. Springer. (KW Analysis Pipeline Reference).
- Hamilton, J. D. (2018). Why You Should Never Use the Hodrick-Prescott Filter. *Review of Economics and Statistics*, 100(5), 831–843. (KW Analytical Filtering Reference).
- Percival, D. B., & Walden, A. T. (2000). *Wavelet Methods for Time Series Analysis*. Cambridge University Press. (KW Wavelet Architecture Reference).
- Torrence, C., & Compo, G. P. (1998). A Practical Guide to Wavelet Analysis. *Bulletin of the American Meteorological Society*, 79(1), 61–78. (KW Wavelet Implementation Reference).
- Zarnowitz, V. (1992). *Business Cycles: Theory, History, Indicators, and Forecasting*. University of Chicago Press. (KW Cyclical Decomposition Reference).
