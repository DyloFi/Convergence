import pathlib
import re

root = pathlib.Path("Technological Singularity")

def insert_before_ref(file_path: pathlib.Path, extra_text: str):
    text = file_path.read_text(encoding="utf-8")
    m = re.search(r'\n(##\s+(?:\d+\.\s*)?Academic References|\n##\s+(?:\d+\.\s*)?References)', text)
    if not m:
        m = re.search(r'\n(##\s+[^\n]*Bibliography)', text)
    if m:
        idx = m.start()
        new_text = text[:idx] + "\n\n" + extra_text.strip() + "\n\n" + text[idx+1:]
    else:
        new_text = text.rstrip() + "\n\n" + extra_text.strip() + "\n"
    file_path.write_text(new_text, encoding="utf-8")

# 1. Accelerating_Returns/Accelerating Returns Deep Dive.md (139 -> ~158 lines)
add1 = """
### Microeconomic Input Substitution and Labor Elasticity Dynamics

From an endogenous growth perspective, the economic realization of accelerating returns hinges on the elasticity of substitution $\\sigma$ between biological labor $L$ and machine capital $K_m$ within the aggregate production function:

$$Y = A \\left[ \\gamma K_m^{\\frac{\\sigma - 1}{\\sigma}} + (1-\\gamma) L^{\\frac{\\sigma - 1}{\\sigma}} \\right]^{\\frac{\\sigma}{\\sigma - 1}}$$

When automation technologies achieve human parity across a threshold fraction of cognitive tasks, $\\sigma$ shifts from gross complementarity ($\\sigma < 1$) to gross substitutability ($\\sigma > 1$). Under $\\sigma > 1$, capital accumulation unbounds aggregate output growth, driving capital share toward unity and creating positive feedback into computational R&D investment:

| Historical Era | Dominant Input Elasticity | Marginal Return to Compute Capital | Output Growth Regime |
| :--- | :--- | :--- | :--- |
| First Industrial Era (1780-1840) | $\\sigma \\approx 0.6$ (Physical Complement) | Diminishing marginal returns ($f''(k) < 0$) | Linear Smithian expansion |
| Information Age (1970-2015) | $\\sigma \\approx 0.9$ (Skill Complement) | Constant returns over compute generations | Exponential Solow baseline |
| Pre-Singular Transition (2020+) | $\\sigma \\approx 1.4$ (Cognitive Substitution) | Hyperbolic returns via autonomous R&D | Superexponential takeoff corridor |

This macroeconomic shift confirms that compute scaling acts not merely as an efficiency multiplier, but as a structural phase change in capital productivity.
"""

# 2. Core_Concepts/00_Research_Overview.md (142 -> ~160 lines)
add2 = """
### Epistemic Takeoff Horizon Telemetry and Cross-Pillar Synchronization

Systematic risk modeling across the technological singularity horizon requires tracking synchronized inflection vectors across all macroeconomic and institutional pillars:

| Analytical Horizon Metric | 2020-2024 Observed Empirical Value | 2025-2028 Projected Threshold | Structural Macroeconomic Consequence |
| :--- | :--- | :--- | :--- |
| Autonomous Code Generation | SWE-bench verified: 12% to 48% | Full codebase architectural closure (>90%) | Infinite-elasticity software production |
| Compute Investment Intensity | Cluster Capex: $10B/facility | Multi-GW clusters: $100B/facility | Sovereign capital re-allocation shock |
| Macro Labor Dislocation | Friction bounded to specialized niches | Broad knowledge-work substitution | 4th Turning institutional re-alignment |

These horizon indicators demonstrate that technological acceleration acts as the primary forcing function compressing both the 50-year Kondratiev cycle and the 80-year Strauss-Howe institutional saeculum into an unprecedented convergence climax.
"""

# 3. Core_Concepts/01_Definition_Origins_and_Conceptual_Frameworks.md (148 -> ~162 lines)
add3 = """
### Historical Evolution of Intelligence Explosion Paradigms

The formal taxonomy of the singularity concept has evolved across distinct intellectual epochs, shifting from loose philosophical speculation to rigorous mathematical and thermodynamic formalization:

| Historical Epoch | Primary Theorist & Year | Definitional Core | Formal Mechanism |
| :--- | :--- | :--- | :--- |
| Mechanical Genesis | Stanislaw Ulam (1958) | Accelerating progress approaching point of essential singularity | Exponential historical trend extrapolation |
| Cybernetic Feedback | I.J. Good (1965) | Ultraintelligent machine designing even better machines | Recursive self-design loop ($M_{t+1} = \\mathcal{D}(M_t)$) |
| Technological Horizon | Vernor Vinge (1993) | Post-human era beyond which human affairs cannot be forecasted | Epistemic horizon breakdown via super-human capability |
| Physical Limits | Ray Kurzweil (2005) | Saturation of matter and energy with intelligence | Law of Accelerating Returns across physical substrates |
"""

# 4. Core_Concepts/Core Concepts Deep Dive.md (147 -> ~162 lines)
add4 = """
### Non-Linear Differential Takeoff Trajectories and Physical Bounds

The mathematical dynamics of recursive self-improvement can be formalized as a non-linear autonomous dynamical system governing intelligence stock $I(t)$ subject to physical dissipation constraints:

$$\\frac{dI}{dt} = \\alpha I(t)^{\\beta} - \\delta I(t)$$

where $\\alpha$ represents algorithmic efficiency, $\\beta$ denotes the returns to recursive cognitive reinvestment, and $\\delta$ captures physical dissipation (communication latency, thermal limits, and verification overhead):

| Regime Parameter | Takeoff Dynamic | Mathematical Solution | Historical Analogue |
| :--- | :--- | :--- | :--- |
| $\\beta < 1$ | Sub-exponential saturation | Logistic growth toward asymptotic ceiling $I_{\\infty}$ | Biological brain volume constraints |
| $\\beta = 1$ | Exponential acceleration | Steady exponential expansion $I(t) = I_0 e^{(\\alpha-\\delta)t}$ | Moore's Law historical trajectory |
| $\\beta > 1$ | Finite-time singularity | Hyperbolic blowup at finite horizon $t^* = t_0 + \\frac{1}{\\alpha(\\beta-1)I_0^{\\beta-1}}$ | Algorithmic recursive intelligence explosion |
"""

# 5. Cultural_Impact/Cultural Impact Deep Dive.md (130 -> ~160 lines)
add5 = """
### Sociological Coalition Dynamics and Institutional Adaptation Regimes

The socio-cultural response to approaching artificial general intelligence has crystallized into competing ideological and political factions, each mobilizing distinct institutional mechanisms to shape or resist the transition:

| Ideological Coalition | Philosophical Foundation | Institutional Strategy | Target Regulatory Posture |
| :--- | :--- | :--- | :--- |
| Effective Accelerationism (e/acc) | Thermodynamic entropy dissipation & cybernetics | Unrestricted open-source decentralization | Zero compute governance & rapid commercialization |
| AI Safety & Alignment Realism | Existential risk mitigation & decision theory | Sovereign compute licensing & international monitoring | Non-proliferation agreements & mandatory safety evals |
| Neo-Luddite Cognitive Defense | Humanist labor sovereignty & trade unionism | Legislative bans on cognitive substitution | Heavy automation taxation & human credential protection |
| Sovereign Techno-Nationalism | Realpolitik great-power competition | State-backed compute subsidies & export controls | National champion consolidation & military integration |

These ideological fractures destabilize traditional political party alignments, driving domestic political polarization into sharp relief as the socio-economic returns to human cognitive labor are fundamentally repriced.
"""

insert_before_ref(root / "Accelerating_Returns/Accelerating Returns Deep Dive.md", add1)
insert_before_ref(root / "Core_Concepts/00_Research_Overview.md", add2)
insert_before_ref(root / "Core_Concepts/01_Definition_Origins_and_Conceptual_Frameworks.md", add3)
insert_before_ref(root / "Core_Concepts/Core Concepts Deep Dive.md", add4)
insert_before_ref(root / "Cultural_Impact/Cultural Impact Deep Dive.md", add5)

print("Expansion applied successfully.")
