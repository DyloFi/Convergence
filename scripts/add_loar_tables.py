import pathlib
import shutil

root = pathlib.Path(__file__).resolve().parent.parent

loar_tables = {
    'LoAR/Core_Concepts/00_Research_Plan.md': """
### 1.3 Empirical Paradigm Trajectory Across Historical Substrates
The macro-trajectory of LoAR spans five successive physical substrates, illustrated in Table 1 below:

| Paradigm # | Substrate Technology | Historical Era | Canonical Milestone System | Compute Price-Performance (cps/$1k) | Limiting Physical Mechanism |
|---|---|---|---|---|---|
| Paradigm 1 | Electromechanical Calculation | 1890–1940 | Hollerith Tabulator (1890) | ~0.001–0.01 cps/$1k | Mechanical relay friction, contact wear, inertia |
| Paradigm 2 | Thermionic Vacuum Tubes | 1940–1955 | ENIAC (1946) | ~10–100 cps/$1k | Filament burnout, thermal dissipation, vacuum seals |
| Paradigm 3 | Discrete Transistors | 1955–1968 | IBM 7090 (1959) | ~1,000–10,000 cps/$1k | Discrete wiring interconnect delay, solder joint reliability |
| Paradigm 4 | Silicon Monolithic ICs | 1968–2000 | Intel 4004 (1971), Pentium (1993) | ~10^6–10^9 cps/$1k | Photolithographic wavelength limits, gate oxide leakage |
| Paradigm 5 | 3D Heterogeneous CMOS / Accelerators | 2000–Present | NVIDIA H100 (2022), B200 (2024) | ~10^12–10^14 cps/$1k | Dennard breakdown, thermal dissipation, memory bandwidth wall |
""",

    'LoAR/Core_Concepts/Core Concepts Deep Dive.md': """
### 1.3 Mathematical Dynamics: Single vs. Double Exponential Growth
To formalize the distinction between standard technological progression and Kurzweil's accelerating returns, Table 1 contrasts single exponential growth with double-exponential dynamics and logistic saturation envelopes:

| Dimension | Single Exponential Model ($V_0 e^{\lambda t}$) | Double-Exponential Model ($P_0 \cdot 2^{2^{kt}}$) | Sigmoidal S-Curve Envelopes ($K / (1 + e^{-r(t-t_0)})$) |
|---|---|---|---|
| Growth Rate $\lambda(t)$ | Constant parameter ($\lambda = \text{const}$) | Exponential growth ($\lambda(t) = W e^{kt}$) | Declining past inflection point ($d\lambda/dt < 0$) |
| Doubling Cadence $\tau$ | Invariant period ($\tau = \ln 2 / \lambda$) | Collapsing period ($\tau(t) \to 0$) | Decelerating towards asymptotic ceiling $K$ |
| Primary Feedback Driver | Linear capital re-investment | Autonomous EDA & AI-designed architectures | Resource exhaustion, physical substrate boundaries |
| Long-Horizon Trajectory | Exponential divergence | Hyperbolic singularity at finite horizon $t^*$ | Saturation followed by next-paradigm transition |
""",

    'LoAR/Key_Principles/Key Principles Deep Dive.md': """
### 1.3 Physical and Algorithmic Laws Governing Key Principles
The axiomatic principles of LoAR operate within well-defined thermodynamic and computer-architectural boundaries, formalized in Table 1 below:

| Axiomatic Principle | Physical / Computational Boundary | Mathematical Formulation | Architectural Implication for LoAR |
|---|---|---|---|
| Substrate Independence | Landauer's Thermodynamic Bound | $E_{\min} = k_B T \ln(2)$ | Minimum energy dissipation ($3 \times 10^{-21}$ J at 300K) per irreversible bit erasure |
| Autonomous Acceleration | Amdahl vs. Gustafson Parallel Laws | $S(N) = \frac{1}{(1-p) + p/N}$ vs $S(N) = N - \alpha(N-1)$ | Limits parallel scaling speedup unless problem dataset scales with compute capacity |
| R&D Capital Compounding | Dennard Scaling Breakdown | $P/A = \kappa \cdot V^2 f$ ($V$ scaling stopped ~2005) | Forced transition from single-thread clock scaling to parallel SIMD/MIMD architectures |
| Paradigm Shifting | Moore's Law Retrenchment | Component density doubling cadence slowing to ~36 mo | Shifts compute scaling to 3D packaging, optical interconnects, and domain-specific ASICs |
""",

    'LoAR/Supporting_Evidence/Supporting Evidence Deep Dive.md': """
### 1.3 Empirical Price-Performance Historical Time-Series
The long-run historical trajectory of computing performance per constant dollar spanning eight decades is detailed in Table 1 below:

| Historical Era | Benchmark Architecture | Calendar Year | Operations per Second (FLOP/s) | Unit Cost (Constant 2026 USD) | FLOP/s per $1,000 | Effective Doubling Period |
|---|---|---|---|---|---|---|
| Electromechanical | Zuse Z3 | 1941 | ~2 FLOP/s | $50,000 | ~0.04 FLOP/s | ~3.0 years |
| Vacuum Tube | ENIAC | 1946 | 5,000 FLOP/s | $500,000 | 10 FLOP/s | ~2.5 years |
| Discrete Transistor | IBM 7090 | 1959 | 229,000 FLOP/s | $3,000,000 | ~76 FLOP/s | ~2.0 years |
| Monolithic Microprocessor | Intel 8086 | 1978 | 330,000 FLOP/s | $360 | ~9.2 × 10^5 FLOP/s | ~1.8 years |
| Superscalar Microprocessor | Intel Pentium Pro | 1995 | 200 × 10^6 FLOP/s | $1,000 | ~2.0 × 10^8 FLOP/s | ~1.6 years |
| Many-Core Tensor GPU | NVIDIA Tesla V100 | 2017 | 125 × 10^12 FLOP/s (Tensor FP16) | $10,000 | ~1.25 × 10^13 FLOP/s | ~1.2 years |
| Heterogeneous Cluster | NVIDIA B200 NVL72 | 2024 | 4.5 × 10^15 FLOP/s (Dense FP8) | $35,000 | ~1.28 × 10^14 FLOP/s | ~1.1 years |
""",

    'LoAR/Supporting_Materials/Bibliography/Bibliography Deep Dive.md': """
### 1.1 Methodological Taxonomy of Primary Literature
To organize the multidisciplinary body of research supporting and evaluating LoAR, Table 1 categorizes primary citations by theoretical domain and empirical contribution:

| Academic Domain | Primary Authors & Citations | Seminal Publication | Foundational Theoretical / Empirical Contribution |
|---|---|---|---|
| Double-Exponential Mechanics | Kurzweil (2001, 2005) | *The Singularity Is Near* | Formulation of $P(t) = P_0 \cdot 2^{2^{kt}}$ and five-paradigm substrate evolution |
| Historical Compute Deflators | Nordhaus (2007) | *Two Centuries of Productivity: Computing* | 200-year continuous price index demonstrating double-exponential compute deflation |
| Stagnation Counter-Theories | Gordon (2016) | *The Rise and Fall of American Growth* | Diminishing marginal utility of information technology compared to Great Inventions |
| Endogenous Growth Drag | Bloom, Jones, Van Reenen, Webb (2020) | *Are Ideas Getting Harder to Find?* | Empirical documentation of ~50% research productivity decline every 13 years |
| Machine Learning Compute Scaling | Sevilla et al. / Epoch AI (2022) | *Compute Trends in Machine Learning* | Documentation of 3.4-month doubling cadence in ML training compute from 2010 to 2024 |
""",

    'LoAR/Supporting_Materials/Glossary/Glossary Deep Dive.md': """
### 1.1 Core Terminological Taxonomy and Dimensional Units
To ground the conceptual definitions in physical and mathematical reality, Table 1 summarizes the primary terms, mathematical representations, and SI units used throughout the LoAR research suite:

| Conceptual Term | Mathematical Representation | Dimensional / SI Units | Core Analytical Relevance |
|---|---|---|---|
| Law of Accelerating Returns | $\lambda(t) = W e^{kt}$, $\frac{dV}{dt} = \lambda(t) V(t)$ | Inverse time ($t^{-1}$) | Fundamental governing model for autonomous R&D acceleration |
| Landauer's Bound | $E_{\min} = k_B T \ln(2)$ | Joules per bit ($J / \text{bit}$) | Ultimate physical lower limit on energy dissipated per irreversible bit erasure |
| Dennard Scaling Exponent | $P/A = \kappa \cdot V^2 f = \text{const}$ | Watts per area ($W / \text{cm}^2$) | Constant power density scaling rule that ceased circa 2005 |
| Compute Density Metric | $\Phi = \text{FLOP/s} / (\text{cm}^3 \cdot W)$ | Operations per $(m^3 \cdot J)$ | Volumetric and thermodynamic substrate efficiency benchmark |
| S-Curve Envelope | $K / (1 + \exp(-r(t-t_0)))$ | Domain metric over time | Macro-trajectory generated by cascading consecutive micro-paradigms |
"""
}

for rel_path, table_snippet in loar_tables.items():
    file_path = root / rel_path
    if not file_path.exists():
        print(f"File not found: {rel_path}")
        continue
    content = file_path.read_text(encoding='utf-8')
    
    # Backup
    bak_path = file_path.with_name(file_path.name + '.bak.md')
    if not bak_path.exists():
        shutil.copy2(file_path, bak_path)
        print(f"Created backup: {bak_path.relative_to(root)}")
    
    # Find insertion point: after section 1.2 or after section 1 header
    if '## 2. ' in content:
        parts = content.split('## 2. ', 1)
        new_content = parts[0].rstrip() + '\n\n' + table_snippet.strip() + '\n\n---\n\n## 2. ' + parts[1]
    elif '## 1. ' in content:
        # If no Section 2, find next ##
        lines = content.splitlines()
        insert_idx = len(lines)
        for i, l in enumerate(lines):
            if l.startswith('## ') and not l.startswith('## 1.') and not l.startswith('## Executive'):
                insert_idx = i
                break
        new_content = '\n'.join(lines[:insert_idx]) + '\n\n' + table_snippet.strip() + '\n\n---\n\n' + '\n'.join(lines[insert_idx:])
    else:
        new_content = content + '\n\n' + table_snippet.strip() + '\n'
        
    file_path.write_text(new_content, encoding='utf-8')
    print(f"Updated: {rel_path}")

print("All 6 LoAR tables successfully added!")
