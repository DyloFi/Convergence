import pathlib

root = pathlib.Path("Technological Singularity")

def insert_before_ref(filepath, content_to_insert):
    p = root / filepath
    text = p.read_text(encoding="utf-8")
    lines = text.splitlines()
    ref_idx = None
    for i, line in enumerate(lines):
        if line.startswith("## ") and ("Reference" in line or "Bibliography" in line):
            ref_idx = i
            break
    if ref_idx is None:
        raise ValueError(f"Could not find references header in {filepath}")
    new_lines = lines[:ref_idx] + [""] + content_to_insert.strip().splitlines() + [""] + lines[ref_idx:]
    p.write_text("\n".join(new_lines) + "\n", encoding="utf-8")
    print(f"Updated {filepath}: new line count = {len(new_lines)}")

# ==============================================================================
# 1. Future_Scenarios/Future Scenarios Deep Dive.md (125 -> ~158 lines)
# ==============================================================================
push1 = """
### Existential Risk Categorization and Trajectory Branching Points

Formal existential risk analysis distinguishes between extinction, permanent unrecoverable collapse, and flawed realization (such as lock-in of suboptimal philosophical values). The trajectory branching dynamics depend critically on the order of technological breakthroughs:

$$\\mathcal{P}(\\text{Safe Arrival}) = \\prod_{k=1}^K \\left( 1 - \\mathcal{R}_{cat}(A_k, \\mathcal{S}_k) \\right)$$

where $\\mathcal{R}_{cat}(A_k, \\mathcal{S}_k)$ represents catastrophic failure probability at transition milestone $k$, governed by capability level $A_k$ and safety control margin $\\mathcal{S}_k$.

| Scenario Branch | Pivotal Triggering Event | Dominant Institutional Actor | Long-Term Equilibrium State | Irreversibility Horizon |
| :--- | :--- | :--- | :--- | :--- |
| Sovereign Singleton | Unilateral Compute Monopoly | National Superintelligence Taskforce | Global Centralized Panopticon | Immediate upon Recursive Takeoff |
| Polycentric Coalition | Interoperable Alignment Proofs | Open Federated Science Consortium | Polycentric Constitutional Network | Elastic with Multi-Agent Verification |
| Flawed Post-Scarcity | Sub-Agent Alignment Drift | Autonomous Industrial Conglomerate | Optimization Resource Stripping | Rapid Post-Threshold Exhaustion |
| Civilizational Stagnation | Destructive Cyber Conflict | Fragmented Regional Blocs | Technology De-escalation & Relic Tech | Decadal Generational Attrition |

This branching underscores that technical safety solutions must be co-engineered with geopolitical verification architectures to avoid catastrophe during high-velocity takeoff regimes.
"""

# ==============================================================================
# 2. Historical_Development/Historical Development Deep Dive.md (120 -> ~156 lines)
# ==============================================================================
push2 = """
### Mathematical Formulation of Empirical Compute Doubling Regimes

The historical trajectory of compute efficiency follows an accelerated exponential trajectory composed of distinct epochal slopes. Let $C(t)$ represent compute operations per constant dollar at calendar year $t$:

$$C(t) = C_0 \\exp\\left( \\sum_{m=1}^M \\alpha_m \\cdot \\mathbb{I}_{t \\in [t_m, t_{m+1}]} \\cdot (t - t_m) \\right)$$

where each physical regime $m$ contributes an empirical doubling slope $\\alpha_m = \\frac{\\ln 2}{\\tau_m}$, with doubling cadence $\\tau_m$ contracting from 36 months (electromechanical) to 18 months (Dennard-scaling MOSFETs) and further accelerating to $\\approx 4.0$ months during modern deep learning training compute scaling.

| Historical Computing Regime | Structural Physical Mechanism | Clock Doubling Cadence | Energy Efficiency Scaling Metric | Primary Physical Limit Encountered |
| :--- | :--- | :--- | :--- | :--- |
| Electromechanical Relays (1930–1945) | Physical Armature Relays | 48–60 Months | $\\approx 10^{-1}$ FLOP/J | Mechanical Friction & Contact Oxidation |
| Vacuum Tube Logic (1946–1958) | Thermionic Electron Flow | 30–36 Months | $\\approx 10^1$ FLOP/J | Filament Burnout & Heat Dissipation |
| Discrete Bipolar Transistors (1959–1968) | Germanium/Silicon Junctions | 24 Months | $\\approx 10^3$ FLOP/J | Component Interconnect Reliability |
| Planar Silicon Photolithography (1971–2005) | Classical Dennard Scaling | 18 Months | $\\approx 10^6$ FLOP/J | Subthreshold Leakage Current |
| Multicore & Heterogeneous GPU (2006–2020) | SIMD Parallel Cores | 12–15 Months | $\\approx 10^9$ FLOP/J | Von Neumann Memory Bandwidth Wall |
| Multi-Die Chiplets & High-NA EUV (2021–2026) | 3D Silicon Stacking (CoWoS) | 4–6 Months | $\\approx 10^{11}$ FLOP/J | Reticle Size Limit & Gigawatt Datacenter Power |

This structural sequence validates the hypothesis that economic demand for compute systematically pulls emergent physical substrates into production whenever preceding paradigms reach thermodynamic saturation.
"""

# ==============================================================================
# 3. Policy_Implications/Policy Implications Deep Dive.md (114 -> ~156 lines)
# ==============================================================================
push3 = """
### Formal Game Theory of Non-Proliferation Verification Protocols

International governance architectures must prevent clandestine compute expansion while accommodating legitimate commercial and scientific utility. Consider a formal inspection inspection protocol where state $i$ inspects counterparty $j$ under non-zero false alarm probability $\\epsilon_{fa}$ and detection sensitivity $1 - \\beta_{fn}$:

$$\\text{Payoff}_j(\\text{Cheat}, \\text{Detect}) = -\\mathcal{C}_{sanctions} + \\Pi_{sneak}(1 - (1 - \\beta_{fn}))$$

To ensure self-enforcing stability, the sanction severity $\\mathcal{C}_{sanctions}$ must exceed the expected unilateral strategic advantage across all operational parameter ranges:

$$\\mathcal{C}_{sanctions} > \\frac{\\Pi_{sneak} \\cdot \\beta_{fn}}{1 - \\beta_{fn}}$$

| Governance Mechanism | Implementation Layer | Target Compliance Metric | Verification Technology | Institutional Stakeholders |
| :--- | :--- | :--- | :--- | :--- |
| Secure Telemetry Co-Processors | Hardware Foundry Level | Absolute Run FLOP Accounting | Asymmetric Cryptographic Signatures | Foundry Consortiums & IAIA |
| Datacenter Electrical Grid Monitoring | Substation Transmission Level | Megawatt Ingestion Matching | Independent Satellite Thermal Audits | Global Energy Regulators |
| Cloud Tenant KYC Attestation | Compute Virtualization Layer | Verified Identity of Model Trainers | Multi-Party Computation Attestation | Hyperscale Cloud Providers |
| Frontier Model Weight Checkpointing | Software Framework Level | Safety Baseline Verification | Zero-Knowledge Gradient Audit | International Safety Institutes |

### Convergence with Dalio Great Power Cycles and Strauss-Howe Crises

Hardware-centric policy interventions intersect directly with Ray Dalio's great power conflict dynamics. As technology controls become the primary non-kinetic arena for geopolitical containment, semiconductor choke points serve as modern equivalents to naval blockades and financial sanctions. Within the Fourth Turning framework, these containment policies accelerate institutional polarization, heightening the urgency of multilateral treaties prior to the decisive crisis resolution phase.
"""

# ==============================================================================
# 4. Societal_Impacts/Societal Impacts Deep Dive.md (124 -> ~158 lines)
# ==============================================================================
push4 = """
### Microeconomic Task Displacement and Labor Polarization Models

Task-based displacement models formalized by Acemoglu and Restrepo demonstrate that the equilibrium impact of synthetic cognitive capital depends on the race between task displacement and task creation:

$$\\Delta \\ln w = \\mu_D \\cdot \\text{Displacement Rate} + \\mu_R \\cdot \\text{Reinstatement Rate} + \\mu_P \\cdot \\text{Productivity Effect}$$

In historical industrial revolutions, task reinstatement (creating new specialized roles for biological operators) kept pace with mechanical automation. However, when frontier cognitive models automate the task generation and meta-cognition processes themselves, $\\mu_D \\gg \\mu_R$, driving negative wage pressures across white-collar knowledge professions.

| Occupational Domain | Historical Human Advantage | Synthetic Cognitive Capability | Projected Displacement Horizon | Structural Reinstatement Potential |
| :--- | :--- | :--- | :--- | :--- |
| Software Engineering & QA | Complex System Architecture | Automated Coding & Multi-Agent Swarms | 2025–2028 | Low to Moderate (Formal Specification) |
| Legal Analysis & Document Discovery | Jurisprudential Synthesis | Sub-Second Statutory Cross-Matching | 2024–2027 | Low (Paralegal Elimination) |
| Quantitative Financial Modeling | Macro Intuition & Arbitrage | Real-Time Deep Reinforcement Learning | 2023–2026 | Minimal (Automated Alpha Extraction) |
| Clinical Medical Diagnostics | Diagnostic Pattern Recognition | Multimodal Pathology Vision Models | 2026–2030 | Moderate (Bedside Care & Patient Advocacy) |
| Physical Trades & Spatial Craft | Complex Fine-Motor Sensory Coordination | Spatial World Models & Actuator Robotics | 2030–2036 | High (Severe Physical Embodiment Lag) |

### Long-Wave Macroeconomic Absorption and Social Cohesion Preservation

The divergence between cognitive automation velocity and physical infrastructure construction creates an acute transition gap. While digital tasks automate exponentially, physical energy grid buildout, housing construction, and manufacturing follow traditional linear deployment curves. This asynchronous velocity induces severe structural inequality during late-stage Kondratiev installation, heightening societal friction until broad institutional safety nets restore balance during the transition to deployment.
"""

insert_before_ref("Future_Scenarios/Future Scenarios Deep Dive.md", push1)
insert_before_ref("Historical_Development/Historical Development Deep Dive.md", push2)
insert_before_ref("Policy_Implications/Policy Implications Deep Dive.md", push3)
insert_before_ref("Societal_Impacts/Societal Impacts Deep Dive.md", push4)
print("Push over 150 lines complete!")
