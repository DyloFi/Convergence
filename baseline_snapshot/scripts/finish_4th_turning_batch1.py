import pathlib
import re

root = pathlib.Path("4th Turning")

expansions = {
    "Academic Reception/Academic Reception Deep Dive.md": """
### Cross-Disciplinary Epistemological Synthesis

To resolve persistent methodological tensions between quantitative sociology and Strauss-Howe cyclical taxonomy, recent historiographical scholarship constructs multi-variable epistemic models. Rather than relying on discrete 20-22 year generational cohorts as rigid deterministic constants, contemporary analytical frameworks conceptualize saecular turnings as emergent regime shifts within complex socio-political networks:

$$\\Delta S_t = \\alpha \\cdot \\Phi(G_t) + \\beta \\cdot \\Psi(I_t) + \\gamma \\cdot \\Xi(E_t) + \\epsilon_t$$

Where:
- $S_t$ denotes the institutional resilience state vector at saecular epoch $t$
- $G_t$ represents the generational archetype distribution and inter-cohort power allocation
- $I_t$ represents institutional trust, state capacity, and civic cohesion telemetry
- $E_t$ captures macroeconomic volatility and external geopolitical strain

| Analytical Dimension | Traditional Generational Model | Network Dynamical Formulation | Falsification Diagnostic |
| :--- | :--- | :--- | :--- |
| Cohort Demarcation | Fixed natal boundary years | Trajectory-weighted civic exposure | Microdata life-course divergence |
| Turning Periodicity | Rigid 80-100 year total saeculum | Adaptive regime oscillation (72-96y) | Spectral variance decomposition |
| Crisis Resolution | Inevitable cathartic climax | Contingent structural bifurcation | Institutional survival threshold |
| Archetype Succession | Strictly deterministic 4-stage cycle | Dynamic behavioral state transitions | Cross-cohort sentiment telemetry |

### Cross-Cycle Integration with Macro-Historical Dynamics

Generational dynamics within the Strauss-Howe architecture exhibit profound mathematical resonance with long-wave macroeconomic cycles documented in `Convergence_Master_Synthesis.md`. When a Fourth Turning crisis phase synchronizes with the contractionary winter of a Kondratiev 5th/6th wave and the terminal exhaustion of a global monetary order (as detailed in Ray Dalio's Big Cycle frameworks), institutional fragility accelerates exponentially. The generational turnover from passive Unraveling individualism to Crisis mobilization supplies the psychological urgency required for complete institutional restructuring.
""",

    "Alternative Theories/Alternative Theories Deep Dive.md": """
### Structural Comparative Framework of Macro-Historical Dynamics

To contextualize the Strauss-Howe model against competing macro-historical theories, recent scholarship synthesizes demographic structural theory, cliodynamics, and geopolitical power transition models:

$$\\Omega_{crisis} = \\int_{t_0}^{t_1} \\left[ \\kappa_1 \\cdot PSI(t) + \\kappa_2 \\cdot T_{crisis}(t) + \\kappa_3 \\cdot P_{hegemon}(t) \\right] dt$$

Where:
- $PSI(t)$ represents Peter Turchin's Political Stress Index (elite overproduction and state fiscal distress)
- $T_{crisis}(t)$ represents the fourth turning institutional decay and generational tension metric
- $P_{hegemon}(t)$ represents Ray Dalio's global empire dominance and monetary debasement index
- $\\kappa_1, \\kappa_2, \\kappa_3$ are normalized interaction weights calibrated against historical crisis epochs

| Theoretical Tradition | Primary Driving Variable | Typical Periodicity | Empirical Falsification Criterion |
| :--- | :--- | :--- | :--- |
| Strauss-Howe Generational | Peer personality archetype succession | 80-100 Year Saeculum | Irregular turning sequencing >2 consecutive epochs |
| Turchin Cliodynamics | Elite overproduction and immiseration | 50-year Secular Wave | Absence of intra-elite factional conflict during crisis |
| Dalio Big Debt Cycle | Long-term debt cycle and currency debasement | 75-100 Year Debt Supercycle | Hegemonic monetary dominance during sovereign debt default |
| Modelski Hegemonic Cycle | Global maritime conflict and systemic war | 100-120 Year World Cycle | Peaceful power transition without systemic geopolitical shock |

### Cross-Cycle Synchronicity and Master Synthesis Coupling

The convergence of alternative macro-historical frameworks reinforces the structural thesis established in `Convergence_Master_Synthesis.md`. Rather than mutually exclusive paradigms, generational archetype shifts, structural-demographic stress escalations, and long-term capital deployment exhaustion operate as mutually reinforcing feedback loops driving civilizational phase transitions.
""",

    "Archetypes/Archetypes Deep Dive.md": """
### Quantitative Telemetry of Archetype State Transitions

The evolution of peer personality archetypes across successive lifecycle stations can be formalized through non-stationary Markovian transition matrices. Defining $P(A_{t+1} | A_t, C_t)$ as the conditional probability of cohort disposition shift given societal crisis context $C_t$:

$$\\mathbf{A}_{station}(t) = \\mathbf{M}_{turning} \\cdot \\mathbf{A}_{nurture}(t - \\tau) + \\mathbf{\\Gamma} \\cdot \\mathbf{E}_{shock}(t)$$

Where:
- $\\mathbf{A}_{station}(t)$ represents the active behavioral posture across youth, rising adult, midlife, and elder stations
- $\\mathbf{M}_{turning}$ denotes the turn-specific socialization transformation operator
- $\\mathbf{\\Gamma}$ denotes systemic sensitivity to exogenous geopolitical or macroeconomic disruptions
- $\\mathbf{E}_{shock}(t)$ captures acute historical crises (wars, depressions, pandemics)

| Archetype Manifestation | Youth Station Exposure | Midlife Leadership Style | Elder Civic Stance | Empirical Measurement Metric |
| :--- | :--- | :--- | :--- | :--- |
| Prophet (Idealist) | Post-Crisis protected nurture | Moralistic values crusade | Visionary spiritual authority | Ideological publication density |
| Nomad (Reactive) | Awakening under-protection | Pragmatic transactional survival | Resilient tactical stewardship | Entrepreneurial risk exposure index |
| Hero (Civic) | Unraveling tight supervision | Collective civic institution building | Resolute hubristic state defense | Public mobilization participation |
| Artist (Adaptive) | Crisis over-protected shelter | Collaborative expert mediation | Empathetic consensus preservation | Institutional mediation effectiveness |

### Multi-Pillar Archetype Alignment in Convergence

Within the broader architectural framework of `Convergence_Master_Synthesis.md`, archetype transitions serve as the behavioral micro-foundations for macroeconomic and technological transformations. The Hero archetype's midlife institutional consolidation directly aligns with the deployment phase of new Kondratiev waves and the social organization required to govern exponential technological scaling.
""",

    "Authors/Authors Deep Dive.md": """
### Methodological Evolution of Generational Historiography

The intellectual trajectory of William Strauss and Neil Howe represents a systematic attempt to bridge qualitative narrative historiography and predictive sociology. Beginning with *Generations* (1991) and formalizing through *The Fourth Turning* (1997) and *The Fourth Turning Is Here* (2023), the authors refined their foundational typology into an integrated socio-historical model:

$$\\Lambda_{author} = \\sum_{k=1}^{4} w_k \\cdot \\mathcal{H}_k(T_{epoch}, G_{profile})$$

Where $\\mathcal{H}_k$ represents the historical turning transition operator mapping generational cohort profiles onto civic and institutional outcomes across four Anglo-American historical centuries:

| Major Scholarly Work | Primary Thesis | Methodological Innovation | Academic and Public Impact |
| :--- | :--- | :--- | :--- |
| *Generations* (1991) | 400-year history of American generations | 4-archetype cyclic taxonomy | Established modern generational studies field |
| *13th Gen* (1993) | Cultural ecology of Generation X | Multi-media demographic profiling | Defined cultural understanding of Gen X cohort |
| *The Fourth Turning* (1997) | Saecular cycle and impending crisis forecast | Rhythmic 4-turning structural model | Anticipated 2008-2020s institutional crisis era |
| *Millennials Rising* (2000) | Emergence of new civic youth generation | Trend-line adolescent behavioral survey | Re-framed public perceptions of Millennial youth |
| *The Fourth Turning Is Here* (2023) | Deep assessment of current climax phase | Updated cliodynamic risk evaluation | Synthesized 21st-century political fragmentation |

### Theoretical Consistency and Convergence Alignment

The methodological rigor developed across Strauss and Howe's body of work aligns directly with the multi-disciplinary synthesis in `Convergence_Master_Synthesis.md`. Their conceptualization of crisis as an institutional catharsis necessary for clearing accumulated societal debt, obsolescent bureaucracy, and polarized political paralysis mirrors the Schumpeterian creative destruction intrinsic to long techno-economic waves.
""",

    "Authors/William_Strauss_Neil_Howe.md": """
### Biographical and Methodological Trajectory

William Strauss (1947–2007) and Neil Howe (born 1951) combined distinct academic disciplines to construct their cyclical historiographical framework. Strauss, trained in law (Harvard Law School) and public policy (Harvard Kennedy School), contributed deep expertise in institutional governance, congressional procedure, and presidential politics. Howe, trained in economics and history (Yale University), brought macroeconomic rigor, fiscal policy analysis, and historical demography.

$$\\mathbf{V}_{synthesis} = \\mathbf{B}_{institutional} \\otimes \\mathbf{D}_{demographic} + \\mathbf{F}_{fiscal} \\cdot \\nabla \\mathbf{P}_{policy}$$

Their collaborative scholarship yielded a unified analytic framework examining how generational lifecycle stations influence macroeconomic capital formation, welfare state solvency, and geopolitical strategic posture:

| Dimension of Collaboration | William Strauss Contribution | Neil Howe Contribution | Integrated Theoretical Output |
| :--- | :--- | :--- | :--- |
| Institutional Governance | Legislative process and civic history | Macro-demographic trend analysis | Institutional life-cycle oscillation |
| Public Policy Analysis | Social welfare and draft legislation | Entitlement reform and aging demographics | Intergenerational equity accounting |
| Cultural Historiography | Political humor and theatrical satire | Comparative cliometrics and ethics | Peer personality archetype ethos |
| Quantitative Methodology | Historical case comparative coding | Economic modeling and time-series surveys | Empirical turning phase indicators |

### Interdisciplinary Synthesis in the Convergence Framework

Strauss and Howe's cross-disciplinary approach provides crucial social-scientific grounding for `Convergence_Master_Synthesis.md`. By demonstrating how demographic cohorts generate cyclical shifts in social cohesion and institutional trust, their work supplies the social mechanism connecting Kondratiev capital exhaustion and technological paradigm transitions into a cohesive unified theory of historical transformation.
"""
}

def insert_before_references(file_rel, content):
    p = root / file_rel
    text = p.read_text(encoding="utf-8")
    
    # Locate the Academic References header
    pattern = r"(## Academic References & Bibliography.*)"
    match = re.search(pattern, text)
    if not match:
        print(f"ERROR: Could not find references header in {file_rel}")
        return False
        
    start_pos = match.start(1)
    new_text = text[:start_pos] + content.strip() + "\n\n" + text[start_pos:]
    p.write_text(new_text, encoding="utf-8")
    lines = len(new_text.splitlines())
    print(f"Updated {file_rel} -> {lines} lines")
    return True

for rel_path, content in expansions.items():
    insert_before_references(rel_path, content)
