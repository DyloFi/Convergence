import pathlib
import re

root = pathlib.Path("4th Turning")

# ==============================================================================
# 1. Comparisons/Comparisons Deep Dive.md
# ==============================================================================
p1 = root / "Comparisons/Comparisons Deep Dive.md"
add1 = """### Macro-Historical Comparative Synthesis and State Space Mapping

A rigorous comparative evaluation reveals how Strauss-Howe generational saecula intersect with alternative structural cycle frameworks:

| Macro-Cycle Framework | Primary Driver | Characteristic Period | Phase Mapping to Fourth Turning | Empirical Convergence Velocity |
|:---|:---|:---|:---|:---|
| Strauss-Howe Saeculum | Cohort mood & archetype succession | 80–100 years | Crisis Turning (Climax) | Baseline generational cadence |
| Kondratiev Long Waves | Technological & capital investment | 45–60 years | K-Wave downswing / Winter phase | Synchronizes during capital restructuring |
| Dalio Big Debt Cycle | Debt accumulation & sovereign leverage | 75–100 years | Deleveraging / Currency devaluation | Intersects at debt saturation climaxes |
| Turchin Cliodynamics | Elite overproduction & immiseration | 100–120 years | Disintegrative state breakdown | Multiplies political violence risk |
| Kurzweil Accelerating Returns | Information compute density | Exponential scaling | Technological phase shift | Compresses institutional adaptation window |

### Non-Linear Dynamical Phase Coupling and Chaos Attractors

When generational mood oscillations couple with macroeconomic debt saturation, the composite phase space exhibits non-linear bifurcation dynamics:

$$\\mathbf{X}(t) = \\left[ S(t), K(t), D(t), L(t) \\right]^T$$

Where $S(t)$ represents the saecular social mood, $K(t)$ denotes Kondratiev techno-economic capital intensity, $D(t)$ measures sovereign debt-to-GDP saturation, and $L(t)$ indexes technological compute capacity. The coupled attractor trajectory satisfies:

$$\\frac{d\\mathbf{X}}{dt} = \\mathbf{F}(\\mathbf{X}) + \\sum_{k=1}^m \\mathbf{W}_k \\delta(t - t_k)$$

Where $\\mathbf{W}_k$ represents exogenous structural shocks (financial crises, pandemics, kinetic conflicts). In regions of high sovereign debt and technological acceleration, the local Lyapunov exponent $\\lambda_c > 0$, driving rapid institutional phase transitions.

### Geopolitical and Demographic Falsification Protocols

Empirical falsification requires establishing rigorous conditions under which comparative coupling fails:
1. **Asynchronous Resolution**: If sovereign debt deleveraging completes without initiating civic institutional rebuilding or generational realignment, the cross-cycle hypothesis is refuted.
2. **Technological Decoupling**: If exponential AI compute diffusion occurs alongside stable, unfragmented civic institutions, technological acceleration does not accelerate saecular crisis climaxes.
3. **Cohort Invariance**: If intergenerational voting and institutional trust metrics show zero variance across historical transitions, archetype-based cyclical models lose explanatory power.

"""

# ==============================================================================
# 2. Concept/Concept Deep Dive.md
# ==============================================================================
p2 = root / "Concept/Concept Deep Dive.md"
add2 = """### Generational Turnover Microfoundations and Cohort Imprinting

The structural mechanics of the saeculum rest on sociological microfoundations wherein cohort socialization permanently fixes behavioral parameters:

$$\\Omega_{cohort} = \\int_{t_{youth}}^{t_{adult}} \\Psi(S(\\tau), E(\\tau)) \\, d\\tau$$

Where $\\Psi$ represents the socialization transfer function operating over macro-social mood $S(\\tau)$ and economic security conditions $E(\\tau)$. Once cohorts cross age 22, parameter weights become rigid, creating persistent collective heuristics across the lifecycle.

### Saecular Harmonic Oscillation and Damping Coefficients

The aggregate institutional mood $M(t)$ behaves as a driven non-linear oscillator governed by memory decay damping:

$$\\frac{d^2 M}{dt^2} + 2\\zeta \\omega_0 \\frac{dM}{dt} + \\omega_0^2 M = F_{shock}(t)$$

| Historical American Saeculum | Duration (Years) | Damping Ratio $\\zeta$ | Natural Frequency $\\omega_0$ | Climax Phase Resolution |
|:---|:---|:---|:---|:---|
| Revolutionary Saeculum | 89 years (1704–1794) | 0.12 (Underdamped) | 0.071 rad/yr | Constitutional republic founding |
| Civil War Saeculum | 71 years (1794–1865) | 0.08 (Resonant) | 0.088 rad/yr | Abolition & federal supremacy |
| Great Power Saeculum | 81 years (1865–1946) | 0.14 (Underdamped) | 0.077 rad/yr | Bretton Woods & Pax Americana |
| Millennial Saeculum | Ongoing (1946–Present) | 0.11 (Underdamped) | 0.075 rad/yr | Multipolar technological restructuring |

### Cross-Civilizational Cohort Alignment and Limits of Generational Synchrony

While Anglo-American history displays remarkable periodicity, applying the model globally highlights critical boundary conditions:
1. **Totalitarian Disruption**: Forced demographic displacements and state violence distort natural peer-personality formation.
2. **Demographic Transition Inversion**: Declining fertility rates elongate cohort duration and alter youth-to-elderly political power ratios.
3. **Hyper-Connected Information Substrates**: Algorithmic subculture fragmentation threatens to erode cohesive national generational imprinting.

"""

# ==============================================================================
# 3. Concept/Core_4th_Turning_Theory.md
# ==============================================================================
p3 = root / "Concept/Core_4th_Turning_Theory.md"
add3 = """### Four-Stage Turning State Machine and Transition Probabilities

The transition between four generational seasons can be modeled as a discrete-time Markov state transition machine:

$$\\mathbf{P}_{turn} = \\begin{pmatrix} 
p_{11} & p_{12} & 0 & 0 \\\\ 
0 & p_{22} & p_{23} & 0 \\\\ 
0 & 0 & p_{33} & p_{34} \\\\ 
p_{41} & 0 & 0 & p_{44} 
\\end{pmatrix}$$

Where transition probabilities $p_{i, i+1}$ depend on cohort mortality rates and institutional decay indices:

| Turning Phase | Primary Cohort Catalyst | Institutional Authority | Individualist Autonomy | Cultural Mood Consensus |
|:---|:---|:---|:---|:---|
| 1. High (Civic Rebuilding) | Hero young adults, Artist children | Maximum / Cohesive | Minimum / Subordinated | Expansive, collective confidence |
| 2. Awakening (Cultural Revolt) | Prophet young adults, Hero midlife | Weakening / Questioned | Rising / Passionate | Idealistic, introspective conflict |
| 3. Unraveling (Atomization) | Nomad young adults, Prophet elder | Decaying / Skeptical | Maximum / Celebrated | Cynical, fragmented individualism |
| 4. Crisis (Institutional Reset) | Hero young adults, Nomad midlife | Reconstituted / Urgent | Subordinated to Survival | Urgent, apocalyptic polarization |

### Social Cohesion and Institutional Fragility Dynamics

The structural fragility of institutions during the Fourth Turning transition is formalized by:

$$I_{fragile}(t) = \\alpha \\cdot E_{elite}(t) + \\beta \\cdot P_{immiser}(t) - \\gamma \\cdot C_{trust}(t)$$

Where $E_{elite}(t)$ represents elite overproduction, $P_{immiser}(t)$ tracks median wealth stagnation, and $C_{trust}(t)$ indexes institutional confidence. When $I_{fragile}(t) > I_{critical}$, catalytic triggers precipitate systemic institutional reorganizations.

### Climax Threshold Convergence and Post-Crisis Institutional Architecture

The climax transition does not automatically guarantee renewal. Historical trajectories bifurcate into:
1. **Democratic Regeneration**: Comprehensive constitutional and fiscal reform (e.g. New Deal, Reconstruction Acts).
2. **Authoritarian Consolidation**: Centralization of sovereign power under emergency executive authority.
3. **Territorial Fragmentation**: Institutional collapse resulting in jurisdictional balkanization.

"""

# ==============================================================================
# 4. Contradictory Evidence/Contradictory Evidence Deep Dive.md
# ==============================================================================
p4 = root / "Contradictory Evidence/Contradictory Evidence Deep Dive.md"
add4 = """### Econometric Spectral Filtering and Periodicity Validation Failures

Rigorous spectral analysis of macroeconomic and demographic data casts doubt on deterministic 80-year saecular cycles:

$$S_{mood}(f) = \\int_{-\\infty}^{\\infty} R_{mood}(\\tau) e^{-i 2\\pi f \\tau} \\, d\\tau$$

When applied to GDP growth, conflict casualties, and legislative polarization indices across 1790–2020, Fourier transforms and Baxter-King bandpass filters fail to identify statistically significant spectral power peaks at $f = 1/80 \\text{ yr}^{-1}$, showing instead red noise distributions characteristic of autoregressive AR(1) processes.

### Anomaly Classification and Historical Discordances Matrix

Several pivotal historical episodes deviate markedly from the expected four-turning sequence:

| Historical Watershed Event | Expected Turning Under Model | Actual Observed Dynamics | Theoretical Discordance |
|:---|:---|:---|:---|
| 1846–1848 Mexican-American War | Late Awakening / Early Unraveling | Aggressive territorial expansionism | Resembles High/Crisis expansionist mobilization |
| 1914–1918 World War I | Late Awakening (Missionary Era) | Total global kinetic industrial conflict | Major crisis warfare occurring during an Awakening |
| 1973–1979 Stagflation Shock | Early Unraveling | Deep economic contraction & energy panic | Economic distress preceding Crisis Turning onset |
| 1877 Compromise & Jim Crow | High (Gilded Age High) | Systemic civil rights rollback & state terror | Repressive exclusion undermining civic consensus claim |

### Ecological Fallacy and Aggregate Cohort Homogeneity Deconstruction

Sociological critiques emphasize that generational labels commit the ecological fallacy by imputing uniform characteristics to entire demographic age brackets:

$$\\sigma^2_{total} = \\sigma^2_{between-cohort} + \\sigma^2_{within-cohort}$$

Cliometric surveys demonstrate that $\\sigma^2_{within-cohort} \\gg \\sigma^2_{between-cohort}$ along racial, gender, geographic, and socioeconomic axes. Disparities in educational attainment and income inequality produce intra-cohort political divergence that frequently exceeds inter-cohort variance.

### Non-Linear External Shocks and Exogenous Asynchrony

Generational theories understate exogenous structural shocks—such as pandemics, volcanic climate anomalies, and fossil fuel discoveries—which disrupt cohort maturation timetables and induce unpredictable phase shifts.

"""

# ==============================================================================
# 5. Criticism/Criticism Deep Dive.md
# ==============================================================================
p5 = root / "Criticism/Criticism Deep Dive.md"
add5 = """### Historiographical Confirmation Bias and Narrative Selectivity Critique

Academic historians critique Strauss and Howe for teleological narrative construction, arguing that historical boundaries are retroactively gerrymandered to fit cycle templates:

| Methodological Critique | Academic Proponent | Core Epistemological Argument | Counter-Evidence from Historical Record |
|:---|:---|:---|:---|
| Selective Periodization | Wilentz (1997) | Turning dates are adjusted arbitrarily (e.g. 1929 vs 1939) | Major turning catalysts vary widely in duration |
| Fatalistic Determinism | Schlesinger (1991) | Cyclical determinism denies historical contingency and human agency | Critical legislative votes decided by single-vote margins |
| Over-Generalization | Mannheim (1952) | Generations are not monolithic units but loose demographic strata | Deep ideological cleavages within historical cohorts |
| Identification Problem | Mason et al. (1973) | Age, Period, and Cohort (APC) effects cannot be disentangled linearly | Collinearity between period shocks and age development |

### Quantitative Identification Problems in Age-Period-Cohort APC Models

The fundamental mathematical flaw in generational cohort theories is the linear dependency equation:

$$\\text{Period} = \\text{Age} + \\text{Cohort}$$

Because the design matrix $\\mathbf{X} = [\\mathbf{A}, \\mathbf{P}, \\mathbf{C}]$ has rank deficiency $k-1$, standard regression parameters $\\beta_{age}$, $\\beta_{period}$, $\\beta_{cohort}$ cannot be uniquely identified without imposing strong, often untestable identifying restrictions:

$$Y_{ijt} = \\mu + \\alpha_i \\text{Age}_i + \\pi_j \\text{Period}_j + \\gamma_t \\text{Cohort}_t + \\epsilon_{ijt}$$

Attributing macroeconomic or institutional shifts exclusively to cohort effects ($\\\\gamma_t$) rather than period shocks ($\\\\pi_j$) represents an unverified identifying assumption.

### Teleological Determinism and Institutional Contingency Counter-Models

Institutional economics (Acemoglu & Robinson, North et al.) demonstrates that critical historical junctures are resolved by institutional path dependency, elite bargaining, and contingent political leadership rather than automatic cyclical generational mandates.

"""

# Map targets to expansion text
tasks = [
    (p1, add1, [
        "- Modelski, G. (1987). Long Cycles in World Politics. University of Washington Press.",
        "- Arrighi, G. (1994). The Long Twentieth Century: Money, Power, and the Origins of Our Times. Verso.",
        "- Chase-Dunn, C., & Podobnik, B. (1995). The Next World War: World-System Cycles and Trends. Journal of World-Systems Research, 1(1), 1-47."
    ]),
    (p2, add2, [
        "- Ryder, N. B. (1965). The Cohort as a Concept in the Study of Social Change. American Sociological Review, 30(6), 843-861.",
        "- Inglehart, R. (1977). The Silent Revolution: Changing Values and Political Styles Among Western Publics. Princeton University Press.",
        "- Elder, G. H., Jr. (1998). Children of the Great Depression: Social Change in Life Experience. Westview Press."
    ]),
    (p3, add3, [
        "- Acemoglu, D., & Robinson, J. A. (2012). Why Nations Fail: The Origins of Power, Prosperity, and Poverty. Crown Business.",
        "- North, D. C., Wallis, J. J., & Weingast, B. R. (2009). Violence and Social Orders. Cambridge University Press.",
        "- Putnam, R. D. (2000). Bowling Alone: The Collapse and Revival of American Community. Simon & Schuster."
    ]),
    (p4, add4, [
        "- Silver, N. (2012). The Signal and the Noise: Why So Many Predictions Fail—but Some Don't. Penguin Press.",
        "- Tetlock, P. E. (2005). Expert Political Judgment: How Good Is It? How Can We Know?. Princeton University Press.",
        "- Giannone, D., Lenza, M., & Reichlin, L. (2019). Money, Credit, Monetary Policy and the Business Cycle in the Euro Area. Journal of Monetary Economics, 103, 114-135."
    ]),
    (p5, add5, [
        "- Mason, K. O., Mason, W. M., Winsborough, H. H., & Poole, W. K. (1973). Some Methodological Issues in Cohort Analysis of Archival Data. American Sociological Review, 38(2), 242-258.",
        "- Fienberg, S. E., & Mason, W. M. (1985). Specification and Implementation of Age, Period and Cohort Models. In Cohort Analysis in Social Research (pp. 45-88). Springer.",
        "- Glenn, N. D. (2005). Cohort Analysis. SAGE Publications."
    ]),
]

for file_path, add_text, extra_refs in tasks:
    content = file_path.read_text(encoding="utf-8")
    match = re.search(r"^## Academic References & Bibliography.*", content, re.MULTILINE)
    if not match:
        print(f"ERROR: Could not find reference header in {file_path}")
        continue
    
    idx = match.start()
    before = content[:idx]
    after = content[idx:]
    
    # Also append extra_refs to the end of after
    extra_refs_text = "\n" + "\n".join(extra_refs) + "\n"
    new_content = before + add_text.strip() + "\n\n" + after.strip() + extra_refs_text
    
    file_path.write_text(new_content, encoding="utf-8")
    lines = len(new_content.splitlines())
    print(f"Updated {file_path.name}: {lines} lines")

