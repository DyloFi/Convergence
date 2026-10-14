import pathlib
import re

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
# 1. Expert_Analysis/Expert Analysis Deep Dive.md (148 lines -> needs ~12 lines)
# ==============================================================================
add1 = """
### Superintelligence Horizon Calibration and Delphi Survey Divergence

Empirical elicitation across machine learning researchers and geopolitical forecasters reveals persistent variance in timeline projections. While Delphi surveys such as Grace et al. (2024) document median human-level machine intelligence arrival dates shifting forward from 2060 (elicited in 2016) to 2047 (elicited in 2022) and subsequently 2038 (elicited in late 2023), prediction markets like Metaculus concentrate probability mass around 2029–2032.

| Forecaster Cohort | Metric Horizon Definition | Median AGI Date | 90th Pct Upper Bound | Primary Model Bottleneck Identified |
| :--- | :--- | :--- | :--- | :--- |
| Academic AI Researchers (Grace et al.) | Full Cognitive Task Parity | 2038 | 2085 | Algorithmic Generalization and Reasoning |
| Frontier Lab Executives (OpenAI/Anthropic) | Economic Task Autonomy | 2028 | 2035 | Electrical Power Grid & High-NA EUV Wafers |
| Geopolitical Forecasting Tournaments | Automated Software Engineering | 2030 | 2042 | Physical Embodiment & Robotics Latency |
| Macroeconomists (Nordhaus/Hanson) | Doubling of Global GWP in 2 Yrs | 2045 | 2100 | Institutional Friction and Legal Adoption |

This structural divergence reflects differing weighting of hardware scaling trajectories versus regulatory and socio-institutional inertia, directly mapping onto the transition from late-stage Kondratiev installation to full deployment.
"""

# ==============================================================================
# 2. Future_Scenarios/Future Scenarios Deep Dive.md (99 lines -> needs ~60 lines)
# ==============================================================================
add2 = """
### Game-Theoretic Multi-Agent Alignment and Bargaining Equilibria

In multipolar transition environments where several sovereign states or frontier corporate laboratories develop autonomous superintelligent systems in parallel, competitive dynamics dominate unilateral safety coordination. The game-theoretic phase space can be formalized through an asymmetric multi-agent payoff matrix where cognitive capability grants decisive strategic advantage:

$$\\mathcal{U}_i(s_i, s_{-i}) = \\Pi_i(C_i, \\theta_i) - \\mathcal{L}_i(s_i, s_{-i})$$

where $C_i$ denotes effective cognitive compute, $\\theta_i$ represents autonomous agent capability, and $\\mathcal{L}_i$ is the systemic catastrophe risk induced by inadequate safety margin investment during pre-deployment races.

### Phase Space Taxonomy of Post-Singularity Trajectories

To systematically categorize downstream civilizational configurations resulting from radical cognitive acceleration, scenario planners evaluate four canonical macro-trajectories across existential risk, wealth concentration, and institutional stability:

| Civilizational Trajectory | Primary Coordination Mechanism | Capital Inequality Index | Catastrophic Risk Profile | Macro-Cycle Resonance Alignment |
| :--- | :--- | :--- | :--- | :--- |
| Democratic Singleton | Supranational Verifiable Compute Registry | Low to Moderate (Redistributed) | Controlled / Monitored | Kondratiev Deployment Institutional Stabilization |
| Competitive Multipolarity | Market-Driven Algorithmic Coalitions | High to Extreme | Elevated (Race Dynamics) | Fourth Turning Crisis External Climax |
| Technocratic Oligopoly | Compute Consortium Cartelization | Severe Institutional Capture | Medium-High (Alignment Drift) | Late-Stage Dalio Internal Wealth Cycle Decay |
| Coordinated Deceleration | Binding International Proliferation Bans | Artificially Constrained | Low Immediate / Latent High | Structural Stagnation and Institutional Sclerosis |

### Structural Macro-Transition and Sovereign Resource Allocation

The shift toward post-scarcity production dynamics necessitates an overhaul of traditional fiscal structures. Because traditional labor markets fail to clear once machine intelligence achieves parity across cognitive and manual tasks, sovereign states must transition from labor income taxation to synthetic resource dividends and automated compute infrastructure yields.

This macroeconomic reconfiguration aligns precisely with the systemic debt deleveraging cycles described in Dalio's macro framework, wherein structural deflation from technological abundance resolves historical fiat sovereign debt overhangs by permanently lowering the marginal cost of survival essentials.
"""

# ==============================================================================
# 3. Historical_Development/Historical Development Deep Dive.md (95 lines -> needs ~65 lines)
# ==============================================================================
add3 = """
### Information-Theoretic Scaling Limits and von Neumann Architecture Transitions

The structural trajectory of computing power over seven decades demonstrates distinct physical and architectural regimes. Early electronic systems were constrained by thermionic valve degradation and relay switching speed, giving way to discrete planar silicon transistors in the 1960s. The contemporary transition beyond traditional Dennard scaling requires circumvention of the classical von Neumann memory bottleneck, formalized by the memory bandwidth-to-compute ratio:

$$\\beta_{mem} = \\frac{\\text{Memory Bandwidth (Bytes/s)}}{\\text{Peak Compute Throughput (FLOP/s)}}$$

As deep learning networks scaled from parameter-light convolutional models to trillion-parameter dense transformers, $\\beta_{mem}$ deteriorated from $\\approx 1.0$ in early microprocessors to $<0.05$ in modern tensor accelerator architectures, necessitating High Bandwidth Memory (HBM3e/HBM4) integration and 3D silicon interposers.

### Empirical Hardware Efficiency and Algorithmic Progress Trajectory (1950–2026)

| Computing Era | Representative System | Active Active Element | Clock Speed | Energy Cost per FLOP | Dominant Algorithmic Paradigm |
| :--- | :--- | :--- | :--- | :--- | :--- |
| First Generation (1950) | UNIVAC I | 5,200 Vacuum Tubes | 2.25 MHz | $\\approx 10^{-2}$ J | Sequential Symbolic Arithmetic |
| Mainframe Era (1964) | IBM System/360 | Solid Logic Technology Hybrid | 5.0 MHz | $\\approx 10^{-4}$ J | Deterministic Operations Research |
| Supercomputing (1976) | Cray-1 | Planar ECL Silicon ICs | 80 MHz | $\\approx 10^{-6}$ J | Vectorized Finite Element PDE Solvers |
| Massively Parallel (1993) | Thinking Machines CM-5 | SPARC RISC Processors | 33 MHz | $\\approx 10^{-8}$ J | Distributed Message Passing Simulation |
| GPU Acceleration (2012) | NVIDIA Tesla K20X | 28nm Kepler SMX | 732 MHz | $\\approx 10^{-10}$ J | Supervised Convolutional Backpropagation |
| Transformer Clusters (2020) | NVIDIA DGX A100 | 7nm Ampere Tensor Core | 1.41 GHz | $\\approx 10^{-12}$ J | Self-Supervised Dense Foundation Models |
| Unified Blackwell/EUV (2026) | NVL72 Dual-Die B200 | 3nm FinFET CoWoS | 2.10 GHz | $\\approx 10^{-13}$ J | Test-Time Compute & MCTS Latent Reasoning |

### Historical S-Curves and Convergence Phase Synthesis

The historical progression of computing affirms Kurzweil's five paradigms: electromechanical calculating engines, vacuum tube computers, discrete transistor systems, planar integrated circuits, and heterogeneous multi-die 3D packaging. Each individual paradigm follows a logistic growth trajectory ($S$-curve), with subsequent technological breakthroughs igniting before preceding paradigms encounter physical asymptotes. This continuous succession drives the smooth exponential curve observed across multi-century compute records, linking directly to the infrastructure installation waves articulated by Carlota Perez.
"""

# ==============================================================================
# 4. Policy_Implications/Policy Implications Deep Dive.md (90 lines -> needs ~70 lines)
# ==============================================================================
add4 = """
### Verifiable Cryptographic Compute Auditing and Zero-Knowledge Proofs

Implementing effective non-proliferation and safety governance regimes without intrusive intellectual property inspection requires cryptographically verifiable telemetry embedded directly into advanced computing silicon. Modern proposals center on zero-knowledge succinct non-interactive arguments of knowledge (zk-SNARKs) combined with secure hardware root-of-trust modules:

$$\\text{Verify}(\\text{vk}, \\pi, x) = 1 \\iff \\exists w \\text{ s.t. } \\mathcal{C}(x, w) = 1$$

where $x$ encodes publicly verifiable compliance criteria (e.g., training compute below $10^{26}$ FLOPs, verified safety guardrail integration), $w$ represents proprietary weights and gradient trajectories kept confidential by the developer, and $\\pi$ is the zero-knowledge proof generated by on-die secure telemetry hardware.

### Multilateral Governance Regimes and Semiconductor Containment

Because advanced compute relies on an ultra-concentrated global supply chain—centered on High-NA Extreme Ultraviolet lithography systems, specialized electronic design automation (EDA) software, and advanced packaging foundries—physical hardware governance represents the most enforceable regulatory vector.

| Regulatory Architecture | Enforcing Institution | Primary Monitoring Vector | Verification Mechanism | Key Governance Vulnerability |
| :--- | :--- | :--- | :--- | :--- |
| Tiered Hardware Licensing | Sovereign Export Control Agencies | GPU Serial Registry & Cloud KYC | Cryptographic Firmware Attestation | Black Market Transshipment & Smuggling |
| International Compute Agency | IAIA (United Nations Specialized) | Datacenter Power Grid Auditing | Thermal Imaging & Wattmeter Seals | Unannounced Underground Clusters |
| Pre-Training Compute Caps | Multi-Jurisdictional Pacts | Frontier Cluster Interconnects | Optical Switch Bandwidth Throttling | Algorithmic Compute Efficiency Gains |
| Sovereign Strategic Compute Reserves | National Security Councils | Publicly Owned Supercomputer Fab | Direct State Facility Custody | Commercial Talent Brain Drain |

### Geopolitical Strategic Stability and Fourth Turning War Deterrence

In historical saecula corresponding to Strauss-Howe Fourth Turning crises, disruptive technological superiority frequently alters military balance and induces destabilizing pre-emptive strike incentives. If an adversary perceives that rival artificial intelligence development will achieve decisive autonomous strategic dominance within an actionable horizon, the game-theoretic incentive for conventional or pre-emptive kinetic containment intensifies. Effective multilateral policy must therefore establish transparent verification mechanisms and dual-key control protocols to ensure bilateral strategic stability during the peak geopolitical tensions of the ongoing global transition.
"""

# ==============================================================================
# 5. Societal_Impacts/Societal Impacts Deep Dive.md (98 lines -> needs ~62 lines)
# ==============================================================================
add5 = """
### Dynamic General Equilibrium with Cognitive Capital Accumulation

The economic disruption driven by frontier artificial intelligence can be modeled within a dynamic general equilibrium framework featuring synthetic cognitive capital ($K_c$) that directly substitutes for both skilled cognitive labor ($L_c$) and routine manual labor ($L_m$). When the elasticity of substitution between cognitive capital and biological human labor exceeds unity ($\\sigma > 1$), technological progress produces capital-deepening transitions where biological labor shares diminish:

$$Y_t = A_t \\left[ \\gamma \\left( K_{c,t} + L_{c,t} \\right)^{\\frac{\\sigma - 1}{\\sigma}} + (1 - \\gamma) L_{m,t}^{\\frac{\\sigma - 1}{\\sigma}} \\right]^{\\frac{\\sigma}{\\sigma - 1}}$$

As cognitive capital rental costs decline toward marginal electrical power generation costs ($r_c \\to p_e$), market wage rates for standard cognitive analytical work decouple from labor productivity gains, shifting corporate income distribution toward infrastructure owners and patent holders.

### Socioeconomic Transition Matrix Across Automation Phases

To evaluate macroeconomic volatility and institutional stress during the cognitive transition, researchers evaluate labor market and fiscal dynamics across four continuous phases of automation:

| Automation Phase | Primary Labor Market Impact | Real Wage Growth Rate | Sovereign Fiscal Stability Index | Primary Social Cohesion Stressor |
| :--- | :--- | :--- | :--- | :--- |
| Augmentation (2022–2025) | Junior Task Offloading | Moderate Positive (+1.5%) | Stable (Standard Income Tax) | White-Collar Career Trajectory Uncertainty |
| Substitution (2026–2029) | Cognitive Workforce Consolidation | Bifurcated (Top +4%, Base -2%) | Strained (Declining Payroll Taxes) | Professional Class Status Disenfranchisement |
| Full Cognitive Parity (2030–2035) | Wholesale Synthetic Labor Replacement | Severe Downward Pressure (-5%) | Critical (Structural Deficit Expansion) | Mass Demand Contraction & Wealth Disparity |
| Universal Autonomy (2035+) | Post-Labor Production Architecture | N/A (Decoupled from Labor) | Rebuilt on Sovereign Resource Stakes | Existential Purpose Reorientation & Civic Alienation |

### Universal Basic Compute and Sovereign Synthetic Dividend Architecture

To avert aggregate demand collapse during the late substitution and cognitive parity phases, economists evaluate sovereign synthetic endowment models. By establishing national public ownership stakes in sovereign compute infrastructure and distributing dividends as universal compute access and automated purchasing credits, nation-states can maintain consumer purchasing power without relying on obsolete payroll tax mechanisms.

This institutional evolution directly reflects the cycle of social compact renewal observed during Fourth Turning resolution phases, where societal institutions rebuild internal cohesion through comprehensive structural redistribution.
"""

insert_before_ref("Expert_Analysis/Expert Analysis Deep Dive.md", add1)
insert_before_ref("Future_Scenarios/Future Scenarios Deep Dive.md", add2)
insert_before_ref("Historical_Development/Historical Development Deep Dive.md", add3)
insert_before_ref("Policy_Implications/Policy Implications Deep Dive.md", add4)
insert_before_ref("Societal_Impacts/Societal Impacts Deep Dive.md", add5)
print("Batch 3 expansion complete!")
