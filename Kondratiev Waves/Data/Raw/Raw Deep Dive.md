# Raw Data Ingestion & Provenance Architecture

## Executive Summary — Raw
This research report defines the **Raw Data Ingestion and Provenance Architecture** for the Kondratiev Waves research repository. Grounded in empirical economic history and archival data standards (Kondratiev, 1925; Schumpeter, 1939; Mitchell, 1998; Solomou, 1987), this monograph details the raw dataset inventory, primary archival sources, file format standards, ingestion validation protocols, and immutable provenance tracking required to preserve un-modified historical time series spanning 1780 to 2026+.

---------------

## 1. Theoretical Framework & Raw Ingestion Principles (Raw)

Raw data preservation requires strict immutability protocols to ensure scientific reproducibility across long-wave research:

### 1.1 Immutability & Provenance Tracking
The `Data/Raw/` directory serves as an immutable primary archive. Files stored in this folder are **never overwritten or altered**. Every raw file includes a companion metadata sidecar (`.meta.json`) detailing:
- **Source Archive**: Direct URL, physical archive reference, or publication citation (e.g., Bank of England Millennium of Data Release 2017).
- **Ingestion Date & Hash**: Timestamp of ingestion and SHA-256 cryptographic checksum.
- **Licensing & Access**: Open Data Commons Attribution License (ODC-By) or public domain designation.

### 1.2 Multi-Century Primary Archives
1. **Historical Archives (1780–1950)**: Digitized records from Sauerbeck (1886), Jevons (1884), Mitchell (1998), NBER Macro History Database, and US Census Historical Statistics.
2. **Modern Digital Archives (1950–2026+)**: Automated API feeds from FRED (Federal Reserve Bank of St. Louis), Bank of England, World Bank, OECD, and Epoch AI compute databases.


## 2. Quantitative Data, Empirical Metrics & Historical Case Studies (Raw) (Raw Deep Dive)

The raw data subfolder maintains un-transformed primary source files across all six Kondratiev Waves.

### Primary Raw Dataset Inventory Across K-Waves 1–6 (1780–2026+)

| Raw File Name | Primary Source Archive | Geographic Scope | Time Horizon Covered | Native File Format | SHA-256 Hash Verification Status |
| :--- | :---- | :----- | :------ | :--- | :---- |
| `raw_sauerbeck_1780_1914.csv` | Sauerbeck / Statist Archives | Great Britain | 1780–1914 | CSV Text | Verified (SHA-256 Match) |
| `raw_boe_millennium_data.xlsx`| Bank of England Research | Great Britain | 1700–2016 | XLSX Binary | Verified (SHA-256 Match) |
| `raw_mitchell_iron_steel.csv` | Mitchell International Stats | UK / Germany / US | 1820–1980 | CSV Text | Verified (SHA-256 Match) |
| `raw_nber_macro_history.csv`  | NBER Macro History Database | United States | 1870–1960 | CSV Text | Verified (SHA-256 Match) |
| `raw_fred_treasury_10y.csv`   | Federal Reserve FRED API | United States | 1962–2026 | CSV Text | Verified (SHA-256 Match) |
| `raw_epoch_ai_compute.json`   | Epoch AI Scaling Database | Global | 2012–2026 | JSON Text | Verified (SHA-256 Match) |


## 3. Comparative Perspectives, Critiques & Counter-Theories (Raw) (Raw Deep Dive)

Raw data collection in long-wave economics faces substantial academic and econometric challenges:

1. **Raw vs. Filtered Data Integrity (Solomou, 1987; Kuznets, 1930)**: Solomou showed that moving-average filters create artificial 50-year periodicities from random noise (the Slutsky-Yule Effect). Retaining un-altered raw data is essential to allow independent spectral density testing.
2. **Unit Roots in Raw Macro Series (Nelson & Plosser, 1982)**: Raw macroeconomic series possess unit roots $I(1)$ and follow non-stationary stochastic trends:
$$Y_{t, \text{kondratiev\_wave}} = \mu_{\text{kondratiev\_wave}} + Y_{t-1, \text{kondratiev\_wave}} + \epsilon_{t, \text{kondratiev\_wave}}$$
   Raw series must not be assumed stationary prior to formal ADF unit root testing.
3. **Archival Boundary & Base Shift Errors (Kondratiev, 1925)**: Historical raw data prior to 1850 contains non-standardized price quotes, changing currency denominations, and territorial boundary shifts that require explicit raw metadata logging.


## 4. Strategic Implications & Future Trajectories (2026–2035+) (Raw) (Raw Deep Dive)

Establishing an immutable raw data repository guarantees long-term empirical validity for 6th Wave research:
- **Automated Ingestion Scripts**: Ingesting daily/monthly macro series via Python scripts that compute SHA-256 hashes and generate sidecar metadata.
- **Open Data Integrity**: Allowing external researchers to verify data provenance directly against original primary archives.

### Cross-Domain Macro-Synthesis (Raw Deep Dive)
- **4th Turning (Raw Data Ingestion & Provenance Architecture for Kondratiev Waves)**: Preserving raw demographic and Pew survey data alongside raw economic price series.
- **Law of Accelerating Returns**: Archiving raw hardware scaling benchmarks across 5 computing paradigms.


## Academic References & Bibliography
- Freeman, C., & Louçã, F. (2001). *As Time Goes By: From the Industrial Revolutions to the Information Revolution*. Oxford University Press. (Raw Deep Dive Citation).
- Jevons, W. S. (1884). *Investigations in Currency and Finance*. Macmillan and Co.
- Kondratiev, N. D. (1925). *The Major Economic Cycles*. Voprosy Konyunktury, 1(1), 28–79. (Raw Deep Dive Citation).
- Mitchell, B. R. (1998). *International Historical Statistics: Europe, 1750–1993*. Stockton Press.
- Nelson, C. R., & Plosser, C. R. (1982). *Trends and random walks in macroeconomic time series: Some evidence and implications*. Journal of Monetary Economics, 10(2), 139–162.
- Perez, C. (2002). *Technological Revolutions and Financial Capital: The Dynamics of Bubbles and Golden Ages*. Edward Elgar Publishing.
- Schumpeter, J. A. (1939). *Business Cycles: A Theoretical, Historical, and Statistical Analysis of the Capitalist Process*. McGraw-Hill.
- Solomou, S. (1987). *Phases of Economic Growth, 1850–1973: Kondratieff Waves and Kuznets Swings*. Cambridge University Press.
### Primary Archival Sources & Raw Data Provenance
Raw historical datasets for long-wave economic analysis are compiled from primary statistical repositories:
- **Bank of England Millennium Macroeconomic Dataset**: Contains continuous annual series for UK GDP, wholesale prices, real wages, and long-term interest rates from 1700 to 2026.
- **US Bureau of Economic Analysis (BEA) & Census Bureau Archives**: Historical statistics of the United States from colonial times to the present, capturing pig iron production, railway track mileage, and electrical power generation.
- **Sauerbeck-Statist Wholesale Commodity Price Index**: Monthly and annual commodity price series spanning 1785–1952, providing the empirical backbone for Kondratiev's original 1925 price cycle charts.## 5. Raw Ingestion Pipelines & Data Quality Verification (Raw Supplement)

Raw macroeconomic ingestion requires automated ETL (Extract, Transform, Load) pipelines equipped with schema validation standards and missing-value imputation protocols:

### 5.1 Automated Ingestion Architecture & Data Ingestion Schema
The Python raw ingestion pipeline processes primary historical archives through strict type-casting contracts:

| Field Name | Storage Data Type | Unit of Measure | Missing Value Imputation | Validation Range |
| :--------- | :---------------- | :-------------- | :----------------------- | :--------------- |
| `series_timestamp` | `INT64` | Calendar Year (YYYY) | Strict Reject | `1500` to `2026` |
| `raw_commodity_index` | `FLOAT64` | Base Index (1913=100) | Cubic Spline Interpolation | `0.0` to `5000.0` |
| `pig_iron_production` | `FLOAT64` | Metric Tons (Thousands) | Piecewise Linear Interpolation | `0.0` to `100000.0` |
| `wheat_price_standard` | `FLOAT64` | Shillings per Quarter | Historical Ledger Search | `0.0` to `500.0` |
| `patent_filings_count` | `INT64` | Annual Count | Zero-Padding | `0` to `1000000` |

### 5.2 Provenance Documentation & Historical Archives
Raw time series are ingested from four authoritative academic data repositories:
1. **UK Parliamentary Papers & Board of Trade Ledgers**: Annual historical pig iron, coal, and textile export volumes (1780–1914).
2. **Beveridge Wheat Price Database**: Longitudinal European wheat price series spanning 1500–1869 (Beveridge 1921).
3. **Sauerbeck-Statist Commodity Index**: Monthly wholesale price indices for 45 primary commodities (1846–1950).
4. **US Patent and Trademark Office (USPTO) Historical Archives**: Annual patent grant counts categorized by General Purpose Technology classes (1790–2026).

---

## 6. Academic References & Bibliography (Raw Supplement)

- Beveridge, W. H. (1921). *Weather and Harvest Cycles*. Economic Journal, 31(124), 429–452.
- Mitchell, B. R. (1988). *British Historical Statistics*. Cambridge University Press.
- Sauerbeck, A. (1886). *Prices of Commodities and the Precious Metals*. Journal of the Statistical Society of London, 49(3), 581–648.
### Raw Data Ingestion Protocol and Raw Observation Taxonomy

The raw data tier preserves the pristine, unadjusted economic observations before any smoothing, logarithmic conversion, or seasonal deflation. Retaining exact raw values is essential for reproducible sensitivity audits and alternative econometric filtering regimes.

| Data Collection Domain | Physical Measurement Unit | Source Agency Record | Sampling Interval |
| :--- | :--- | :--- | :--- |
| UK Coal Output | Imperial Long Tons (Millions) | Board of Trade Mining Division | Annual Ingestion |
| US Pig Iron Production | Metric Tons (Thousands) | American Iron and Steel Institute | Annual Ingestion |
| World Cotton Consumption | Running Bales (Thousands) | International Cotton Advisory Committee| Annual Ingestion |
| Global Commercial Fleet | Gross Register Tonnage (Millions) | Lloyd's Register of Shipping | Annual Ingestion |
| Benchmark Commodity Index | Index Base Year Currency Units | Sauerbeck-Statist Price Index | Monthly Ingestion |

The raw ingestion validation harness executes automated checksum matching and anomalous outlier identification using Grubbs test statistic:

$$G = \frac{\max_{t} |y_t - \bar{y}|}{s}$$

where $\bar{y}$ is the historical sample mean and $s$ is the empirical sample standard deviation, flagging transcription and printing errors in vintage documents.

### Raw Data Integrity across the Convergence Framework

Preserving unaltered raw observations guarantees that future computational methodologies—such as machine-learning spectral decomposition or non-linear phase space reconstruction—can re-evaluate the foundational data without inheriting the assumptions of 20th-century linear detrending techniques.

### Raw Data Validation References

- Barnett, V., & Lewis, T. (1994). *Outliers in Statistical Data* (3rd ed.). John Wiley & Sons.
- Grubbs, F. E. (1969). Procedures for Detecting Outlying Observations in Samples. *Technometrics*, 11(1), 1-21.
- Jevons, W. S. (1884). *Investigations in Currency and Finance*. Macmillan and Co.
- Morgenstern, O. (1963). *On the Accuracy of Economic Observations* (2nd ed.). Princeton University Press.
- Prescott, E. C. (1986). Theory Ahead of Business-Cycle Measurement. *Carnegie-Rochester Conference Series on Public Policy*, 25, 11-44.
### Raw Observation Ingestion Protocols and Immutable Staging Architecture

The integrity of quantitative cliometrics rests upon an unassailable foundation of immutable raw data ingestion. Once transcribed from primary archives or downloaded from official institutional repositories (Bank of England, NBER, FRED, Maddison Project), raw files are permanently locked against manual in-place alteration.

```
Raw Data Ingestion Lifecycle:
[Archival Source Transcription] ---> [Ingestion Staging Area]
                                             |
                                             v
[Automated Hash Registration] ------> [Immutable Raw Storage (Read-Only)]
                                             |
                                             v
[Raw Data Quarantine Gate] ---------> [Audit Verification Manifest]
```

The raw observation ingestion protocol enforces strict administrative rules:
- **Write-Once-Read-Many (WORM) Storage**: Raw data directories operate with file-system read-only permissions (`chmod 444`), preventing inadvertent overwrites.
- **Sidecar Metadata Registration**: Every raw artifact is paired with an immutable JSON sidecar specifying source URL, transcription date, archival shelfmark, and transcriptionist identity.
- **Quarantine and Anomaly Isolation**: Newly ingested raw observations exhibiting unexpected formatting shifts, encoding mismatches, or structural anomalies are quarantined until manual verification is performed.
- **Bi-annual Integrity Audits**: Automated cron daemons recompute cryptographic hashes across all raw files quarterly to guarantee zero silent bit-rot or media degradation.

This rigorous ingestion discipline ensures that any downstream transformation can be traced back to bit-identical primary source captures, maintaining reproducibility for computational economics research.

### Archival Systems and Data Ingestion Citations

- Dataverse Project. (2021). *Dataverse: An Open Source Research Data Repository*. Harvard Institute for Quantitative Social Science.
- Austin, C. C., Bloom, T., Dallmeier-Tiessen, S., Hallett, R., Kambuzuma, D., & Nurnberger, A. (2017). Research Data Repositories: Review of Current Features, Gaps, and Future Directions. *D-Lib Magazine*, 23(11/12), 1-12.
- Wilkinson, M. D., Dumontier, M., Aalbersberg, I. J., Appleton, G., Axton, M., Baak, A., ... & Mons, B. (2016). The FAIR Guiding Principles for Scientific Data Management and Stewardship. *Scientific Data*, 3, 160018.
- Borer, E. T., Seabloom, E. W., Jones, M. B., & Schildhauer, M. (2009). Some Simple Guidelines for Effective Data Management. *Bulletin of the Ecological Society of America*, 90(2), 205-214.
- Corti, L., Van den Eynden, V., Bishop, L., & Woollard, M. (2019). *Managing and Sharing Research Data: A Guide to Good Practice* (2nd ed.). SAGE Publications.
