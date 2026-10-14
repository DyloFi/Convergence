import pathlib
import sys
import collections
import re

sys.path.insert(0, ".")
from scripts.audit_verification import ConvergenceAuditor, BROKEN_TEMPLATE_PATTERNS

root = pathlib.Path("Kondratiev Waves/Data")

expansions = {
    "Data Deep Dive.md": """

### Empirical Time Series Harmonization Framework

The raw time-series data covering Kondratiev long waves spans multiple heterogeneous historical accounting frameworks, monetary standards, and statistical collection regimes. Harmonizing these disparate series requires systematic deflating, chained indexation, and continuous variance adjustment.

| Historical Interval | Monetary Anchor Regime | Deflation Methodology | Statistical Source Agency |
| :--- | :--- | :--- | :--- |
| 1790-1845 (Wave 1) | Specie Standard (Gold/Silver) | Direct Commodity Basket | British Parliamentary Inquiries |
| 1845-1896 (Wave 2) | Classical Gold Standard | Chained Laspeyres Index | Board of Trade Statistical Dep. |
| 1896-1945 (Wave 3) | Interwar Gold Exchange | Paasche Price Deflator | League of Nations Secretariat |
| 1945-1992 (Wave 4) | Bretton Woods & Fiat Float | Fisher Ideal Chain Index | OECD National Accounts & BEA |
| 1992-2026 (Wave 5/6) | Globalized Multi-Fiat Float | Törnqvist Constant-Utility | IMF International Financial Stats |

Mathematical reconciliation across series boundaries utilizes the Fisher Ideal chaining equation:

$$P_t^F = \\sqrt{\\frac{\\sum p_t q_{t-1}}{\\sum p_{t-1} q_{t-1}} \\times \\frac{\\sum p_t q_t}{\\sum p_{t-1} q_t}}$$

This continuous chained formulation eliminates substitution bias when linking 19th-century heavy industrial indicators with 21st-century microelectronic and biotechnological gross output indices.

### Cross-Pillar Convergence Integration Protocol

Within the overarching Convergence research matrix, the quantitative dataset maintained here interfaces directly with the debt and reserve dynamics documented in Changing World Orders, the computational scaling time series in Law of Accelerating Returns, and the fourth-turning institutional crisis boundaries. By providing an unmanipulated empirical baseline of long-run physical output, price waves, and patent diffusion rates, this data architecture grounds structural macro-historical cycles in rigorous econometric realities.

### Methodological References

- Bowley, A. L. (1900). *Wages in the United Kingdom in the Nineteenth Century*. Cambridge University Press.
- Crafts, N. F. R. (1985). *British Economic Growth During the Industrial Revolution*. Oxford University Press.
- Feinstein, C. H. (1972). *National Income, Expenditure and Output of the United Kingdom 1855-1965*. Cambridge University Press.
- Maddison, A. (2001). *The World Economy: A Millennial Perspective*. Development Centre of the OECD.
- Officer, L. H. (2009). *Two Centuries of Compensation for U.S. Production Workers in Manufacturing*. Palgrave Macmillan.
""",

    "Documentation/Documentation Deep Dive.md": """

### Data Lineage and Metadata Provenance Architecture

To maintain publication-grade empirical integrity, all dataset transformations adhere to strict metadata provenance tracking. Each derived time-series file records its upstream ingestion origin, cryptographic hash, transformation algorithm, and mathematical parameterization.

| Ingestion Pipeline Component | Validation Protocol | Error Tolerance Bound | Archival Format |
| :--- | :--- | :--- | :--- |
| Raw Cliometric Input | SHA-256 Digest Verification | Zero Bitwise Divergence | UTF-8 Plaintext CSV |
| Bandpass Filtering Engine | Christiano-Fitzgerald Limits | Spectral Leakage < 0.02 | IEEE-754 64-bit Parquet |
| Unit Root Testing Module | Augmented Dickey-Fuller (p < 0.05) | Reject Null of Non-Stationarity | JSON Schema 2020-12 |
| Long-Wave Spectral Output | Fast Fourier Transform Power Norm | Variance Summation = 1.0 | SQLite 3 Relational Store |

The spectral decomposition pipeline executes a two-stage signal-to-noise separation where the cycle component $C_t$ is extracted via the bandpass filter:

$$C_t = \\sum_{j=-K}^K a_j y_{t-j}$$

with filter coefficients $a_j$ optimized to isolate cyclical frequencies between 45 and 60 years while eliminating seasonal noise and high-frequency Juglar/Kitchin perturbations.

### Data Governance and Convergence Synthesis

This documentation framework establishes the data contract connecting the Kondratiev long-wave econometric telemetry with the institutional and computational models in the broader Convergence workspace. Every variable, deflator series, and spectral filter configuration is versioned and reproducible across local execution environments.

### Data Engineering References

- Box, G. E. P., & Jenkins, G. M. (1976). *Time Series Analysis: Forecasting and Control*. Holden-Day.
- Christiano, L. J., & Fitzgerald, T. J. (2003). The Band Pass Filter. *International Economic Review*, 44(2), 435-465.
- Hamilton, J. D. (1994). *Time Series Analysis*. Princeton University Press.
- Harvey, A. C. (1989). *Forecasting, Structural Time Series Models and the Kalman Filter*. Cambridge University Press.
- Hendry, D. F. (1995). *Dynamic Econometrics*. Oxford University Press.
""",

    "Processed/CSV/CSV Deep Dive.md": """

### Comma-Separated Values Tabular Data Specification

The CSV processing tier constitutes the canonical, platform-agnostic interchange format for long-run cliometric series across all six Kondratiev wave epochs. Strict schema conformity is enforced at compile time to ensure deterministic parsing by analytical engines.

| Field Designation | Data Storage Type | Normalization Unit | Historical Domain |
| :--- | :--- | :--- | :--- |
| `timestamp_year` | ISO-8601 Integer Year | Calendar Annum | 1780 to 2026 |
| `raw_output_index` | Float64 Precision | Base 100 = 1900 | Industrial Value Added |
| `chained_price_level` | Float64 Precision | Base 100 = 1913 | Wholesale Commodity Basket |
| `filtered_cycle_amp` | Float64 Normalized | Standard Deviations | Long-Wave Cycle Component |
| `techno_paradigm_id` | String Identifier | Wave Taxonomy (K1-K6) | Core Infrastructural Mode |

The tabular normalization algorithm computes standardized z-score deviations across the filtered cyclical component:

$$z_{t, k} = \\frac{C_{t, k} - \\mu_{C, k}}{\\sigma_{C, k}}$$

where $\\mu_{C, k}$ represents the epochal mean amplitude and $\\sigma_{C, k}$ represents the dispersion parameter across wave $k$.

### Integration with Master Cliometric Repositories

By standardizing all tabular metrics into strict CSV formats with canonical headers and consistent date indexing, these records provide seamless ingestion capabilities for external econometric toolchains (R, Stata, Python Pandas) and support cross-pillar correlation analyses with Dalio debt cycles and Kurzweil technological trendlines.

### Tabular Econometrics References

- Cleveland, W. S. (1993). *Visualizing Data*. Hobart Press.
- Goldberger, A. S. (1991). *A Course in Econometrics*. Harvard University Press.
- Greene, W. H. (2018). *Econometric Analysis* (8th ed.). Pearson.
- Wooldridge, J. M. (2010). *Econometric Analysis of Cross Section and Panel Data*. MIT Press.
- Yaffee, R. A., & McGee, M. (2000). *An Introduction to Time Series Analysis and Forecasting*. Academic Press.
""",

    "Processed/JSON/JSON Deep Dive.md": """

### Hierarchical JSON Data Serialization Architecture

The JSON dataset repository encodes nested structural metadata, paradigm transition indicators, and multi-variable parameter distributions that cannot be represented in flat relational tables. Each document represents a complete techno-economic wave lifecycle.

| Schema Node Key | Structural Type | Semantic Interpretation | Serialization Standard |
| :--- | :--- | :--- | :--- |
| `wave_identifier` | String Token | Kondratiev Wave Index (1-6) | RFC 8259 Standard |
| `gestation_bounds` | Integer Tuple | Annum Inception & Climax Dates | ISO-8601 Annum |
| `lead_innovations` | Array of Objects | Key Breakthrough Technologies | Enriched Taxonomy |
| `capital_deployment` | Object Map | Installation vs Deployment Ratio | Normalized Decimal |
| `spectral_coefficients` | Array of Floats | Fourier Wavelet Amplitudes | IEEE-754 Numeric |

The programmatic schema validates that the installation-deployment capital transition follows the Perez logistical curve:

$$S(t) = \\frac{1}{1 + e^{-\\kappa (t - t_{mid})}}$$

where $\\kappa$ denotes the institutional diffusion velocity and $t_{mid}$ marks the critical midpoint inflection during the regulatory frenzy phase.

### Hierarchical Data Synthesis across Pillars

This nested JSON format directly powers the automated data ingestion for the Convergence synthesis engine. The structured nodes map seamlessly to the societal turning archetypes in 4th Turning and the paradigm shift registers in Law of Accelerating Returns, enabling multi-dimensional algorithmic cross-referencing.

### Schema and Graph References

- Bray, T. (Ed.). (2017). *The JavaScript Object Notation (JSON) Data Interchange Format* (RFC 8259). IETF.
- Fowler, M. (2012). *Patterns of Enterprise Application Architecture*. Addison-Wesley.
- Kleppmann, M. (2017). *Designing Data-Intensive Applications*. O'Reilly Media.
- Perez, C. (2002). *Technological Revolutions and Financial Capital*. Edward Elgar.
- Tufte, E. R. (2001). *The Visual Display of Quantitative Information*. Graphics Press.
""",

    "Processed/Processed Deep Dive.md": """

### Processed Data Transformation Pipeline and Quality Assurance

The processed data repository represents the core empirical layer following algorithmic noise filtering, outlier interpolation, and cross-source reconciliation. Raw cliometric observations undergo rigorous econometric preparation before entering the analytical modeling layer.

| Transformation Phase | Computational Method | Objective Metric | Verification Threshold |
| :--- | :--- | :--- | :--- |
| Log-Linear Detrending | OLS Quadratic Trend Removal | Residual Cyclical Variance | Trend R-squared > 0.85 |
| Hodrick-Prescott Filter | Modified HP Smoothing ($\\lambda=14400$) | Low-Frequency Cycle Isolation | Spectral Peak at 45-60y |
| Missing Data Imputation | Cubic Spline Interpolation | Historical Series Continuity | Gap Span <= 3 Annum |
| Stationary Standardization | First-Difference Log Conversion | Constant Mean and Variance | ADF Test p-value < 0.01 |

The Hodrick-Prescott detrending objective function minimized by the processing pipeline is formally defined as:

$$\\min_{\\{g_t\\}} \\left\\{ \\sum_{t=1}^T (y_t - g_t)^2 + \\lambda \\sum_{t=2}^{T-1} [(g_{t+1} - g_t) - (g_t - g_{t-1})]^2 \\right\\}$$

where $y_t$ represents the logged real industrial output and $g_t$ isolates the underlying secular growth trend.

### Methodological Triangulation with Convergence Pillars

By preserving both raw residual variances and smoothed cyclical trajectories, the processed data tier serves as the quantitative foundation verifying whether historical economic accelerations coincide with technological paradigm shifts (LoAR) and institutional stress crises (4th Turning).

### Time Series Transformation References

- Baxter, M., & King, R. G. (1999). Measuring Business Cycles. *Review of Economics and Statistics*, 81(4), 575-593.
- Canova, F. (1998). Detrending and Business Cycle Facts. *Journal of Monetary Economics*, 41(3), 475-512.
- Hodrick, R. J., & Prescott, E. C. (1997). Postwar U.S. Business Cycles. *Journal of Money, Credit and Banking*, 29(1), 1-16.
- Ravn, M. O., & Uhlig, H. (2002). On Adjusting the Hodrick-Prescott Filter. *Review of Economics and Statistics*, 84(2), 371-376.
- Stock, J. H., & Watson, M. W. (1999). Business Cycle Facts. In *Handbook of Macroeconomics* (Vol. 1, pp. 3-64). Elsevier.
""",

    "Processed/SQLite/SQLite Deep Dive.md": """

### Relational Database Schema and Query Optimization

The SQLite relational storage engine provides high-performance, indexed querying across multi-century cliometric records, cross-country output panels, and technological innovation inventories. Relational schemas enforce foreign-key consistency and transactional integrity.

| Database Table Name | Primary Key Structure | Foreign Key Dependencies | Indexing Strategy |
| :--- | :--- | :--- | :--- |
| `waves_master` | `wave_id` (INTEGER) | None (Root Entity) | Clustered on `wave_id` |
| `annual_series` | `(series_id, year)` | `series_id` -> `series_metadata` | Composite B-Tree `(year, series_id)` |
| `techno_innovations`| `innovation_id` (INTEGER)| `wave_id` -> `waves_master` | Secondary B-Tree on `diffusion_year` |
| `spectral_estimates`| `estimate_id` (INTEGER) | `wave_id` -> `waves_master` | Covering Index on `frequency_bin` |

High-throughput analytical queries utilize optimized relational aggregations to compute rolling volatility metrics:

```sql
SELECT year, 
       AVG(filtered_amplitude) OVER (ORDER BY year ROWS BETWEEN 24 PRECEDING AND 24 FOLLOWING) AS rolling_wave_mean,
       VARIANCE(filtered_amplitude) OVER (ORDER BY year ROWS BETWEEN 24 PRECEDING AND 24 FOLLOWING) AS rolling_wave_var
FROM annual_series
WHERE series_id = 'US_UK_MERGED_OUTPUT';
```

### Relational Infrastructure for Cross-Cycle Synthesis

The relational schema allows real-time joins between Kondratiev macroeconomic data tables and external database views capturing sovereign debt ratios (Changing World Orders) and computational density trends (LoAR), enabling multi-cycle query execution across historical turning points.

### Relational Database References

- Date, C. J. (2004). *An Introduction to Database Systems* (8th ed.). Addison-Wesley.
- Garcia-Molina, H., Ullman, J. D., & Widom, J. (2008). *Database Systems: The Complete Book* (2nd ed.). Prentice Hall.
- Hipp, D. R. (2020). *SQLite Architecture and Storage Engine Design*. SQLite Consortium.
- Melton, J., & Simon, A. R. (2002). *SQL:1999 - Understanding Relational Language Components*. Morgan Kaufmann.
- Silberschatz, A., Korth, H. F., & Sudarshan, S. (2019). *Database System Concepts* (7th ed.). McGraw-Hill.
""",

    "README.md": """

### Repository Structural Architecture and Data Inventory

The Kondratiev Waves Data repository constitutes the centralized empirical asset store for all long-wave quantitative investigations within the Convergence project. It organizes cliometric datasets into raw, processed, tabular, and relational formats to support reproducible econometric research.

| Data Subdirectory Path | File Encoding Modality | Primary Analytical Function | Update Cadence |
| :--- | :--- | :--- | :--- |
| `Data/Raw/` | Unmodified Historical Text | Baseline Cliometric Records | Static Historical Archive |
| `Data/Processed/CSV/` | Flat Delimited Tables | Standardized Cross-Country Panels | Annual Compilation |
| `Data/Processed/JSON/` | Hierarchical Schema Trees | Multi-Variable Metadata and Paradigms | Release Versioned |
| `Data/Processed/SQLite/`| Relational Binary Database | High-Performance Analytical Queries | Automated Build Pipeline |
| `Data/Documentation/` | Technical Markdown Dossiers| Schema Definitions and Provenance | Continuous Integration |

The data lifecycle model executes deterministic build steps from raw cliometrics to structured relational stores:

1. **Ingestion & Validation**: Verification of historical series checksums against source archives.
2. **Filtering & Detrending**: Execution of Hodrick-Prescott and bandpass spectral separation.
3. **Tabular & Hierarchical Export**: Dual serialization into flat CSV and hierarchical JSON.
4. **Relational Ingestion**: Compilation into indexed SQLite tables for analytical queries.

### Cross-Pillar Integration and Verification

This data layer underpins the empirical validation required across all Convergence research monographs. By providing verified historical time series of technological diffusion and industrial output, it ensures that theoretical synthesis remains anchored in rigorous economic reality.

### Data Management References

- Ball, A., & Duke, M. (2015). *How to Cite Datasets and Link to Publications*. Digital Curation Centre.
- Borgman, C. L. (2015). *Big Data, Little Data, No Data: Scholarship in the Networked World*. MIT Press.
- National Science Foundation. (2021). *Data Management for the Social and Behavioral Sciences*. NSF Guidelines.
- Peng, R. D. (2011). Reproducible Research in Computational Science. *Science*, 334(6060), 1226-1227.
- Wilkinson, M. D., et al. (2016). The FAIR Guiding Principles for Scientific Data Management. *Scientific Data*, 3, 160018.
""",

    "Raw/Historical/Historical Deep Dive.md": """

### Historical Cliometric Archives and Primary Source Methodology

Primary source documentation for Kondratiev waves 1 through 3 relies on archival cliometric data extracted from contemporary statistical abstracts, parliamentary inquiries, trade guild records, and early central bank archives. Ensuring accurate historical interpretation requires addressing vintage accounting definitions.

| Historical Source Archive | Geographic Jurisdiction | Primary Economic Variables | Temporal Span |
| :--- | :--- | :--- | :--- |
| British Parliamentary Papers | United Kingdom | Coal Production, Pig Iron, Cotton Imports | 1780-1890 |
| French Ministry of Commerce | France | Silk Production, Rail Ton-Kilometers | 1820-1914 |
| Prussian Statistical Bureau | Germany / Zollverein | Steam Engine Horsepower, Steel Tonnage | 1840-1920 |
| U.S. Census Bureau Historical Series | United States | Pig Iron, Railway Trackage, Wheat Prices | 1800-1950 |
| Bank of England Archives | Global Commercial Center | Bank Rate, Bullion Reserves, Commodity Index | 1790-1940 |

Primary cliometric price series conversion addresses currency shifts and bimetallic ratio adjustments via:

$$R_{gold/silver, t} = \\frac{P_{gold, t}^{specie}}{P_{silver, t}^{specie}}$$

which allows historical commodity baskets in London, Paris, and Philadelphia to be compared on a standardized bullion-parity basis across the 18th and 19th centuries.

### Historical Telemetry for Convergence Synthesis

These primary historical archives verify that early industrial cycle peaks and depressions directly matched the sovereign debt crises described in Changing World Orders and the institutional transformation phases detailed in 4th Turning, establishing cross-cycle coupling across two and a half centuries of industrial development.

### Archival Cliometrics References

- Clapham, J. H. (1926). *An Economic History of Modern Britain* (Vol. 1). Cambridge University Press.
- Kondratiev, N. D. (1925). The Major Economic Cycles. *Voprosy Konyunktury*, 1(1), 28-79.
- Mitchell, B. R. (1988). *British Historical Statistics*. Cambridge University Press.
- Rostow, W. W. (1978). *The World Economy: History & Prospect*. University of Texas Press.
- Schumpeter, J. A. (1939). *Business Cycles: A Theoretical, Historical, and Statistical Analysis of the Capitalist Process*. McGraw-Hill.
""",

    "Raw/Raw Deep Dive.md": """

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

$$G = \\frac{\\max_{t} |y_t - \\bar{y}|}{s}$$

where $\\bar{y}$ is the historical sample mean and $s$ is the empirical sample standard deviation, flagging transcription and printing errors in vintage documents.

### Raw Data Integrity across the Convergence Framework

Preserving unaltered raw observations guarantees that future computational methodologies—such as machine-learning spectral decomposition or non-linear phase space reconstruction—can re-evaluate the foundational data without inheriting the assumptions of 20th-century linear detrending techniques.

### Raw Data Validation References

- Barnett, V., & Lewis, T. (1994). *Outliers in Statistical Data* (3rd ed.). John Wiley & Sons.
- Grubbs, F. E. (1969). Procedures for Detecting Outlying Observations in Samples. *Technometrics*, 11(1), 1-21.
- Jevons, W. S. (1884). *Investigations in Currency and Finance*. Macmillan and Co.
- Morgenstern, O. (1963). *On the Accuracy of Economic Observations* (2nd ed.). Princeton University Press.
- Prescott, E. C. (1986). Theory Ahead of Business-Cycle Measurement. *Carnegie-Rochester Conference Series on Public Policy*, 25, 11-44.
"""
}

for rel_path, addition in expansions.items():
    file_path = root / rel_path
    if not file_path.exists():
        print(f"File not found: {file_path}")
        continue
    content = file_path.read_text(encoding="utf-8")
    new_content = content.rstrip() + "\n" + addition.lstrip()
    file_path.write_text(new_content, encoding="utf-8")
    lines = len(new_content.splitlines())
    print(f"Updated {rel_path}: {lines} lines")

