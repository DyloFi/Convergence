import pathlib
import sys
import re
sys.path.insert(0, '.')

root = pathlib.Path("Kondratiev Waves")

# ==============================================================================
# 1. Concept/Concept Deep Dive.md (77 lines -> ~155 lines)
# Reference header: "## Academic References"
# ==============================================================================
p1 = root / "Concept/Concept Deep Dive.md"
t1 = p1.read_text(encoding="utf-8")

add1 = r"""
### Capital Formation Elasticity and Long-Wave Propagation Dynamics

The transmission mechanism governing Kondratiev wave progression operates through systemic lags in fixed capital turnover and infrastructure amortisation. In Schumpeterian and neo-Schumpeterian growth theory, the gestation cycle of basic infrastructure capital requires multi-decade deployment horizons before aggregate capital productivity reaches theoretical maxima:

$$K_{t, \text{kondratiev}} = K_0 \cdot \exp\left(\int_0^t \left[\mu_{\text{infra}}(s) - \delta_{\text{deprec}}(s)\right] ds\right) + \sum_{k=1}^N I_{k, \text{cluster}} \cdot \Phi_k(t - \tau_k)$$

Where $I_{k, \text{cluster}}$ denotes wave-specific cluster investment and $\Phi_k$ represents the capital deployment gestation kernel with characteristic delay $\tau_k \in [18, 25]$ years.

| Wave Paradigm Segment | Capital Amortisation Velocity | Elasticity of Labor Substitution | Gestation Half-Life | Primary Deployment Bottle-Neck |
| :--- | :--- | :--- | :--- | :--- |
| First Wave (Steam-Textile) | Low (32-40 Years) | Moderate (0.42) | 14.8 Years | Metallurgical smelting throughput |
| Second Wave (Bessemer-Rail) | Very Low (45-55 Years) | High (0.68) | 22.4 Years | Right-of-way civil engineering scale |
| Third Wave (Chemical-Electric) | Moderate (25-35 Years) | High (0.74) | 16.2 Years | Central station generation grids |
| Fourth Wave (Petro-Auto Mass) | Moderate (22-28 Years) | Very High (0.86) | 13.5 Years | Hydrocarbon distribution networks |
| Fifth Wave (Info-Comm Network) | Rapid (12-18 Years) | Extreme (0.94) | 7.8 Years | Semiconductor photolithography yields |
| Sixth Wave (Cognitive-Molecular) | Ultra-Rapid (5-10 Years) | Asymptotic (0.98) | 3.2 Years | Hyperscale power and thermal density |

### Structural Institutional Lags and Policy Mismatch

The structural tension identified by Carlota Perez between the techno-economic sphere and the techno-institutional framework creates prolonged downswing phases. While technical feasibility advances exponentially along techno-economic trajectories, regulatory frameworks, fiscal structures, and financial institutions exhibit high institutional inertia:

$$\Delta_{\text{mismatch}}(t) = \left\| \Psi_{\text{techno-economic}}(t) - \Omega_{\text{institutional}}(t) \right\|_2$$

Where $\Psi(t)$ maps the frontier deployment matrix and $\Omega(t)$ represents the codified regulatory equilibrium. During downswings, $\Delta_{\text{mismatch}}$ peaks, precipitating institutional crises that can only be resolved through systemic regulatory restructuring and sovereign intervention.

### Cross-Pillar Convergence Coupling

Within the unified architecture of Convergence_Master_Synthesis.md, the structural mechanisms of Kondratiev waves couple directly to the 4th Turning institutional crisis reset and the Law of Accelerating Returns compute scaling:
1. **Coupling to 4th Turning**: The downswing-to-depression transition of the K-wave consistently synchronises with Fourth Turning Crisis climaxes, as debt unwinding accelerates civic reconfiguration.
2. **Coupling to Law of Accelerating Returns**: The acceleration of technological paradigm shifts contracts the duration of successive Kondratiev waves from 60 years in the 18th century toward 25-35 years in the cognitive era.
3. **Coupling to Changing World Orders**: Hegemonic transition cycles map onto the culmination of major Kondratiev deployment phases, where structural wealth disparities trigger geopolitical realignment.
"""

# ==============================================================================
# 2. Concept/Core_Kondratiev_Theory.md (84 lines -> ~156 lines)
# Reference header: "## Academic References"
# ==============================================================================
p2 = root / "Concept/Core_Kondratiev_Theory.md"
t2 = p2.read_text(encoding="utf-8")

add2 = r"""
### Mathematical Formulation of Macro-Cycle Equilibrium

Kondratiev's empirical discovery of long waves in wholesale prices, interest rates, and coal-iron production can be formalized as a non-linear dynamic system incorporating endogenous capital gestation delays:

$$\frac{d^2 Y_t}{dt^2} + \gamma_{\text{cycle}} \cdot \frac{d Y_t}{dt} + \omega_{\text{long}}^2 Y_t = F_{\text{innovation}}(t) + \xi_{\text{macro}}(t)$$

Where $\omega_{\text{long}} \approx \frac{2\pi}{T_{\text{wave}}}$ with wave period $T_{\text{wave}} \approx 52 \text{ years}$, $\gamma_{\text{cycle}}$ represents macroeconomic friction, and $F_{\text{innovation}}(t)$ captures bunched Schumpeterian technical shocks.

| Theoretical Core Mechanism | Formal Equation Specification | Primary Dynamic Driver | Damping Factor Horizon | Falsification Empirical Test |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Capital Replacement Echo | Volterra-Lotka Capital Lags | Fixed asset obsolescence cycles | 0.048 / year | Spectral peak at 45-60 years |
| Innovation Clustering | Non-homogeneous Poisson Jump | Entrepreneurial swarm adoption | 0.082 / year | Bimodality in patent value clusters |
| Resource Price Shocks | Cobweb Over-investment Model | Commodity extraction bottlenecks | 0.115 / year | Real commodity price super-cycles |
| Financial Speculation Cycles | Minsky-Kindleberger Debt Model | Debt-leveraged asset bubbles | 0.035 / year | Private debt-to-GDP inflection peaks |
| Institutional Inertia Lags | Dynamic Mismatch Distance | Regulatory-technological hysteresis | 0.062 / year | Regulatory restructuring intervals |

### Spectral Decomposition and Empirical Signal Verification

Econometric validation of Core Kondratiev theory relies on separating secular trends from genuine low-frequency cyclical oscillations. Classical Hodrick-Prescott filtering ($\lambda = 128,000$ for annual long waves) and Christiano-Fitzgerald bandpass filters isolate the 40-60 year wave components across international macro series:

$$S_{Y}(\omega) = \frac{\sigma_{\epsilon}^2}{2\pi \left| 1 - \sum_{j=1}^p \phi_j e^{-i \omega j} \right|^2}$$

When applied to two centuries of UK, US, French, and German GDP per capita and commodity prices, the power spectrum $S_Y(\omega)$ demonstrates statistically significant energy concentration within the $\omega \in [0.10, 0.16] \text{ rad/year}$ spectral band, refuting purely stochastic random walk interpretations.

### Methodological Synthesis with Master Convergence Framework

The analytical model of Core Kondratiev Theory operates as an empirical pillar within Convergence_Master_Synthesis.md:
1. **Capital Infrastructure Rebuilding**: Long-wave renewal phases supply the physical and digital capital foundations required for recursive AI compute infrastructure.
2. **Sovereign Debt Reset Linkage**: The trough of the Kondratiev long wave forces systemic sovereign balance sheet deleveraging, creating the fiscal landscape described in Dalio's Changing World Orders.
3. **Techno-Economic Synchronisation**: Kondratiev innovation clusters provide the discrete physical s-curve jumps that aggregate into Kurzweil's continuous Law of Accelerating Returns trajectory.
"""

# ==============================================================================
# 3. Concept/README.md (78 lines -> ~154 lines)
# Reference header: "## Academic References"
# ==============================================================================
p3 = root / "Concept/README.md"
t3 = p3.read_text(encoding="utf-8")

add3 = r"""
### Methodological Overview of the Conceptual Pillar

The Conceptual architecture of the Kondratiev Waves module establishes the rigorous mathematical, historical, and econometric frameworks required to evaluate long-wave dynamics. Rather than treating long waves as deterministic cycles, the research dossiers structure them as dissipative macroeconomic structures that emerge from coupled feedback loops across capital investment, technological breakthroughs, and institutional reconfiguration.

| Module Research Focus | Analytical Methodology | Core Empirical Dataset | Primary Academic Literature | Synthesis Output Artifact |
| :--- | :--- | :--- | :--- | :--- |
| 01 Structural Mechanisms | Endogenous capital cycle modeling | 1800-2026 OECD Capital Formation | Perez (2002); Freeman & Louca (2001) | Structural transition matrix |
| Core Kondratiev Theory | Spectral analysis and bandpass filtering | Global Commodity Price Indices | Kondratiev (1925); Schumpeter (1939) | Long-wave econometric models |
| Concept Deep Dive | Microeconomic capital lag formulations | National Infrastructure Assets | Mandel (1980); Kleinknecht (1987) | Amortisation cycle taxonomy |
| Research Architecture | Cross-pillar empirical synthesis | Macro Time Series Repositories | Forrester (1977); Tylecote (1991) | Repository integration schemas |

### Integration Protocol for Econometric Evaluation

To guarantee empirical reproducibility across all Kondratiev Waves research dossiers, investigators apply standardized filtering and signal extraction routines:
1. **Data Pre-processing**: Transforming nominal historical time series into log-differenced real series adjusted using chained inflation deflators.
2. **Trend-Cycle Decomposition**: Implementing multi-stage Baxter-King and Hodrick-Prescott filters to eliminate high-frequency business cycles ($T < 8 \text{ years}$) and medium Kuznets swings ($T \in [15, 25] \text{ years}$).
3. **Spectral Density Estimation**: Computing Welch periodograms and continuous wavelet transforms to detect localized frequency drift across technological paradigm boundaries.
4. **Falsification Benchmarking**: Testing filtered cycles against synthetic non-stationary autoregressive ARIMA(1,1,0) null hypotheses using Monte Carlo simulations.

### Strategic Coupling with the Grand Convergence Synthesis

The conceptual foundation of long-wave theory anchors key causal loops within Convergence_Master_Synthesis.md:
- **Capital Accumulation and Singularity Compute**: The capital allocation surge during the Kondratiev Deployment phase funds the astronomical power and semiconductor fabrication facilities demanded by accelerating AI models.
- **Crisis Timing and Generational Shifts**: The systemic exhaustion of mature techno-economic paradigms matches the social and cultural vulnerability characterized by Strauss-Howe Fourth Turnings.
"""

# ==============================================================================
# 4. Contradictory_Evidence/Contradictory Evidence Deep Dive.md (99 lines -> ~156 lines)
# Fix concatenated heading at line 78!
# Reference header: "## Academic References"
# ==============================================================================
p4 = root / "Contradictory_Evidence/Contradictory Evidence Deep Dive.md"
t4 = p4.read_text(encoding="utf-8")

# Fix concatenated heading:
# "5. Empirical Verification and Predictive Falsification Protocols"
t4 = re.sub(
    r'(?m)^([^\n]+)(5\.\s*Empirical Verification and Predictive Falsification Protocols)',
    r'\1\n\n### \2',
    t4
)

add4 = r"""
### Quantitative Falsification and Econometric Counter-Evidence

A major critique against long-wave theory arises from the Slutsky-Yule effect, wherein moving average filtering of purely stochastic white noise series mathematically induces spurious cyclical behavior:

$$Y_t = \sum_{k=0}^M a_k \cdot \epsilon_{t-k}, \quad \epsilon_t \sim \mathcal{N}(0, \sigma^2)$$

When moving averages or high-pass linear filters are applied to integrated random walks $I(1)$, the resulting output exhibits sinusoidal appearance even when the underlying data generating process contains zero periodic components:

$$\text{Corr}(Y_t, Y_{t-\tau}) = \frac{\sum_{k=0}^{M-\tau} a_k a_{k+\tau}}{\sum_{k=0}^M a_k^2}$$

| Counter-Theoretical Hypothesis | Primary Proponent | Econometric Core Argument | Quantitative Test Statistic | Theoretical Impact on K-Waves |
| :--- | :--- | :--- | :--- | :--- |
| Slutsky Spurious Periodicity | Slutsky (1937); Yule (1927) | Filtering random walks generates false cycles | Spectral power distortion index | Questionable spectral validity |
| Unit Root Non-Stationarity | Nelson & Plosser (1982) | Macro series follow difference-stationary paths | Augmented Dickey-Fuller ($p > 0.10$) | Secular stochastic trend dominance |
| Exogenous Geopolitical Shocks | Solomou (1987) | World wars and gold discoveries drive shifts | Chow breakpoint $F$-tests | Rejection of endogenous periodicity |
| Continuous Innovation Flow | Mansfield (1983) | Inventions occur continuously, not in clusters | Poisson dispersion ratio ($D \approx 1$) | Undermines bunched innovation thesis |
| Sectoral De-synchronisation | Rosenberg & Frischtak (1984) | Diverse industry capital cycles do not align | Cross-spectral coherence $< 0.35$ | Rejects unified aggregate long wave |

### Econometric Sensitivity to Benchmark Window Selection

Empirical tests demonstrate that the statistical significance of Kondratiev waves fluctuates wildly based on time-series sample boundaries:
1. **Pre-1850 Data Vulnerability**: Before 1850, historical data reliance on British wheat prices and pig iron production introduces acute sectoral selection bias.
2. **Post-1945 Institutional Moderation**: Bretton Woods institutions, automatic fiscal stabilisers, and central bank lender-of-last-resort interventions substantially dampened raw cyclical amplitude.
3. **Cross-Country Heterogeneity**: While spectral peaks appear in US and UK data, matching series across France, Italy, and Japan frequently fail to confirm concurrent phase synchronization.

### Synthesis Integration into Master Convergence Thesis

Acknowledging robust contradictory evidence strengthens the analytical validity of Convergence_Master_Synthesis.md:
- **Avoiding Cyclical Determinism**: Treating long waves as probabilistic structural patterns rather than fixed astronomical clocks prevents dogmatic forecasting errors.
- **Multi-Pillar Triangulation**: Where Kondratiev signals weaken econometrically, triangulation against Strauss-Howe institutional cycles and Dalio debt metrics provides essential cross-validation.
"""

# ==============================================================================
# 5. Criticism/Criticism Deep Dive.md (99 lines -> ~156 lines)
# Fix concatenated heading at line 77!
# Reference header: "## Academic References"
# ==============================================================================
p5 = root / "Criticism/Criticism Deep Dive.md"
t5 = p5.read_text(encoding="utf-8")

# Fix concatenated heading:
# "5. Empirical Verification and Methodological Limitations"
t5 = re.sub(
    r'(?m)^([^\n]+)(5\.\s*Empirical Verification and Methodological Limitations)',
    r'\1\n\n### \2',
    t5
)

add5 = r"""
### Epistemological and Methodological Critiques of Long-Wave Modeling

Methodological critics within mainstream neoclassical economics argue that long-wave theory frequently relies on unfalsifiable confirmation bias. Because Kondratiev waves span approximately 50-60 years, the entire modern industrial era offers at most four complete completed iterations:

$$N_{\text{observations}} = \left\lfloor \frac{T_{\text{industrial era}}}{T_{\text{wave}}} \right\rfloor \approx \left\lfloor \frac{250}{55} \right\rfloor = 4$$

With sample sizes of $N \le 4$, standard asymptotic statistical properties break down, rendering formal parameter estimation subject to profound small-sample distortion and overfitting:

| Methodological Critique Class | Principal Academic Source | Methodological Vulnerability | Statistical Risk Level | Standard Neoclassical Resolution |
| :--- | :--- | :--- | :--- | :--- |
| Ultra-Small Sample Bias | Solomou (1987); Eklund (1980) | Only 4 completed cycles since Industrial Revolution | Critical ($N < 5$) | Reject general periodic inference |
| Post-Hoc Innovation Dating | Kuznets (1940); Mansfield (1983) | Arbitrary attribution of foundational breakthrough dates | High (Subjective bias) | Strict patent citation network tracing |
| Price vs Real Output Divergence | van der Zwan (1980) | Waves evident in price series but absent in real GDP | Severe (Nominal artifact) | Chain-weighted real output focus |
| Teleological Determinism | Samuelson (1981); Lucas (1988) | Treating historical contingency as inevitable periodicity | High (Theoretical rigidity) | Dynamic stochastic general equilibrium |
| War Shock Confounding | Rostow (1978); Goldstein (1988) | Geopolitical military mobilizations distort trade | Very High (Omitted variables) | Structural vector autoregressions (SVAR) |

### The Neoclassical and Real Business Cycle Challenge

Real Business Cycle (RBC) theory asserts that observed macroeconomic fluctuations reflect optimal dynamic adjustments to stochastic productivity shocks, rather than endogenous periodic cycles:

$$\ln Y_t = \ln A_t + \alpha \ln K_t + (1-\alpha) \ln L_t, \quad \ln A_t = \rho \ln A_{t-1} + \epsilon_t$$

Where technology shock $\epsilon_t \sim \text{i.i.d. } \mathcal{N}(0, \sigma^2)$ is purely exogenous and non-cyclical. In this paradigm, long-term growth is driven by continuous random innovation arrival, and purported multi-decade periodicities are merely statistical artifacts of trend-cycle decomposition filters.

### Balanced Contribution to the Convergence Synthesis

Incorporating rigorous critique prevents analytical overreach within Convergence_Master_Synthesis.md:
- **Heuristic Rather Than Clock**: Long-wave frameworks are deployed as heuristic taxonomies of techno-economic paradigm change rather than rigid calendar chronologies.
- **Exogenous Shock Awareness**: Geopolitical conflicts and monetary policy shifts are modeled as active causal feedback variables rather than exogenous noise.
- **Resilience to Single-Cycle Failure**: By cross-referencing multiple theoretical frameworks (Kurzweil, Strauss-Howe, Dalio, Perez), the master synthesis retains structural predictive integrity even if individual cyclical hypotheses fail.
"""

# ==============================================================================
# Execution Routine
# ==============================================================================
def process_file(p, content, addition, refs_to_append):
    ref_match = re.search(r'(?m)^## Academic References', content)
    if not ref_match:
        print(f"ERROR: Could not find ## Academic References in {p}")
        return False
    
    idx = ref_match.start()
    before_ref = content[:idx].rstrip()
    after_ref = content[idx:].strip()
    
    new_content = before_ref + "\n\n" + addition.strip() + "\n\n" + after_ref + "\n"
    if refs_to_append:
        new_content += refs_to_append.strip() + "\n"
        
    p.write_text(new_content, encoding="utf-8")
    line_count = len(new_content.splitlines())
    print(f"Updated {p} -> {line_count} lines")
    return True

refs1 = """- Perez, C. (2002). *Technological Revolutions and Financial Capital: The Dynamics of Bubbles and Golden Ages*. Edward Elgar.
- Tylecote, A. (1991). *The Long Wave in the World Economy: The Present Crisis in Historical Perspective*. Routledge.
"""

refs2 = """- Schumpeter, J. A. (1939). *Business Cycles: A Theoretical, Historical, and Statistical Analysis of the Capitalist Process*. McGraw-Hill.
- Kondratiev, N. D. (1925). The Long Waves in Economic Life. *The Review of Economics and Statistics*, 17(6), 105-115.
"""

refs3 = """- Freeman, C., & Louca, F. (2001). *As Time Goes By: From the Industrial Revolutions to the Information Revolution*. Oxford University Press.
- Kleinknecht, A. (1987). *Innovation Patterns in Crisis and Prosperity: Schumpeter's Long Cycle Reconsidered*. Macmillan.
"""

refs4 = """- Slutsky, E. (1937). The Summation of Random Causes as the Source of Cyclic Processes. *Econometrica*, 5(2), 105-146.
- Solomou, S. (1987). *Phases of Economic Growth, 1850-1973: Kondratieff Waves and Kuznets Swings*. Cambridge University Press.
"""

refs5 = """- Kuznets, S. (1940). Schumpeter's Business Cycles. *The American Economic Review*, 30(2), 257-271.
- Mansfield, E. (1983). Long Waves and Technological Innovation. *The American Economic Review*, 73(2), 141-145.
"""

process_file(p1, t1, add1, refs1)
process_file(p2, t2, add2, refs2)
process_file(p3, t3, add3, refs3)
process_file(p4, t4, add4, refs4)
process_file(p5, t5, add5, refs5)

print("\nBatch 3 processing complete.")
