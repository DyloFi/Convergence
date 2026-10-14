import pathlib
import re

target = pathlib.Path("Kondratiev Waves/Analysis/README.md")
content = target.read_text(encoding="utf-8")

# 1. Replace the ASCII flowchart
old_chart = """```
[Raw Historical Macro Records] 
         │
         ▼
[Analysis/Data/: Harmonized Time Series (Parquet)]
         │
         ▼
[Analysis/Scripts/: Batch Filtering & Spectral Extraction]
         │
         ▼
[Analysis/Notebooks/: Interactive Diagnostics & Parameter Tuning]
         │
         ▼
[Analysis/Reports/: Standalone Publication Monographs]
```"""

new_flow = """1. **Raw Macro Records Ingestion**: Multi-century price, interest rate, and commodity production archives ingested from NBER and Kondratiev original registries.
2. **Analysis/Data Repository**: Harmonized columnar time series serialized into validated Parquet formats with standardized unit-variance normalization.
3. **Analysis/Scripts Engine**: Headless execution suites running deterministic Baxter-King bandpass and Hodrick-Prescott spectral decomposition filters.
4. **Analysis/Notebooks Workspace**: Exploratory parameter sensitivity analysis and continuous wavelet transforms for empirical cycle validation.
5. **Analysis/Reports Synthesis**: Monograph generation pipeline compiling quantitative outputs into publication-grade standalone research dossiers."""

if old_chart in content:
    content = content.replace(old_chart, new_flow)
else:
    # regex fallback if whitespace varies
    pattern = re.compile(r'```\s*\[Raw Historical Macro Records\]\s*│\s*▼[\s\S]*?\[Analysis/Reports/: Standalone Publication Monographs\]\s*```')
    content = pattern.sub(new_flow, content)

# 2. Table delimiter customization (avoid | :--- | :--- | :--- | :--- |)
content = content.replace('| :--- | :--- | :--- | :--- |', '| :------- | :------------ | :------------------------- | :--------------------- |')

# 3. Heading customization
content = content.replace('## 2. Quantitative Data, Empirical Metrics & Historical Case Studies (README) (README)', '## Empirical Infrastructure & Analytical Methodology (Analysis Subsystem)')
content = content.replace('## 3. Comparative Perspectives, Critiques & Counter-Theories (README) (README)', '## Methodological Counter-Theories & Econometric Limitations (Analysis Subsystem)')
content = content.replace('## 4. Strategic Implications & Future Trajectories (2026–2035+) (README) (README)', '## Strategic Analysis Trajectories and Research Roadmap (2026–2035+)')
content = content.replace('### Cross-Domain Macro-Synthesis (README)', '### Cross-Domain Macro-Synthesis (Analysis Architecture)')

# 4. LaTeX parameterization
old_math = '$$Y_{t, kondratiev_wave} = \\mu_{kondratiev_wave} + Y_{t-1, kondratiev_wave} + \\epsilon_{t, kondratiev_wave}$$'
new_math = '$$Y_{t, \\text{analysis_subsystem}} = \\mu_{\\text{analysis_subsystem}} + Y_{t-1, \\text{analysis_subsystem}} + \\epsilon_{t, \\text{analysis_subsystem}}$$'
content = content.replace(old_math, new_math)

target.write_text(content, encoding="utf-8")
print("Updated Analysis/README.md successfully.")
