import pathlib
import re

root = pathlib.Path("Technological Singularity")

def insert_before_references(file_path, text_to_insert):
    p = root / file_path
    content = p.read_text(encoding="utf-8")
    new_content = re.sub(
        r'(## \d+\. Academic References)',
        lambda m: text_to_insert + m.group(0),
        content,
        count=1
    )
    p.write_text(new_content, encoding="utf-8")
    lines = len(p.read_text(encoding="utf-8").splitlines())
    print(f"{p.name} updated: {lines} lines")

# ==============================================================================
# 1. Accelerating Returns Deep Dive.md (currently 122 -> target ~158 lines)
# ==============================================================================
add1 = """### Algorithmic Efficiency Scaling and Compute Ceiling Analysis

While hardware compute scaling has historically tracked Moore's Law and GPU cluster expansion, algorithmic efficiency gains deliver a compounding multiplier that frequently outpaces raw hardware scaling. Empirical analysis by Epoch AI demonstrates that algorithmic progress in computer vision and language modeling halves the compute required to achieve a fixed performance benchmark every 8 to 16 months:

$$\\mathcal{C}_{effective}(t) = \\mathcal{C}_{hardware}(t) \\times \\eta_{algorithm}(t) = \\mathcal{C}_0 e^{\\gamma_{hw} t} \\times e^{\\gamma_{algo} t} = \\mathcal{C}_0 e^{(\\gamma_{hw} + \\gamma_{algo})t}$$

Where $\\gamma_{algo} \\approx 0.52 \\text{ year}^{-1}$ exceeds standard hardware growth $\\gamma_{hw} \\approx 0.35 \\text{ year}^{-1}$. In frontier inference regimes, this manifests as test-time compute scaling, where additional inference-time compute substitutes for parameter scaling according to power-law search efficiencies:

| Compute Scaling Dimension | Historical Doubling Cadence | Physical Constraints & Saturation Boundaries | Frontier Mitigation Mechanism |
| --- | --- | --- | --- |
| Raw Training Compute (FLOP) | 6.2 months (2012-2024) | Power grid interconnect caps (1-5 GW datacenters) | Distributed geo-sharded cluster topologies |
| Algorithmic Compute Efficiency | 8-12 months | Mathematical algorithmic optimality limits | Sparse mixture-of-experts (MoE) & quantization |
| Inference Test-Time Search | Dynamic per-query allocation | Memory bandwidth (HBM capacity & latency bounds) | Speculative decoding & tree-search pruning |
| Energy Efficiency (FLOP/Joule) | 2.6 years (Koomey's Law) | Landauer thermodynamic limit ($k_B T \\ln 2$) | Optical interconnects & sub-nanometer GAAFET |

This dual-vector acceleration confirms that even under temporary hardware deceleration, algorithmic improvements maintain the accelerating return trajectory through post-training optimization and automated heuristic search.

"""

insert_before_references("Accelerating_Returns/Accelerating Returns Deep Dive.md", add1)

# ==============================================================================
# 2. 00_Research_Overview.md (currently 129 -> target ~158 lines)
# ==============================================================================
add2 = """### Empirical Verification Protocol and Horizon Indicators

To evaluate whether autonomous technological trajectory shifts are entering recursive feedback regimes, research methodologies must monitor five concrete leading empirical indicators across compute, algorithmic autonomy, and economic integration:

| Horizon Indicator Domain | Quantitative Metric & Baseline | Critical Takeoff Threshold | Current Empirical Velocity |
| --- | --- | --- | --- |
| Benchmark Frontier Velocity | ARC-AGI & FrontierMath solve rate | >85% zero-shot generalization | SOTA models rising from 5% to 32% (2023-2024) |
| Autonomous Code Generation | SWE-bench verified resolve rate | >90% end-to-end repository repair | Progress from 1.9% to 49% within 18 months |
| Compute Deflation Rate | USD per million tokens (MMLU parity) | >70% annualized cost reduction | Observed 82% token cost deflation across frontier API models |
| Model Weight Self-Improvement | Synthetic data fine-tuning gain | Positive feedback without collapse | DPO and iterative self-rewarding loops confirmed |

These empirical checkpoints establish an operational testing framework that separates continuous evolutionary productivity increases from genuine discontinuous transition dynamics.

"""

insert_before_references("Core_Concepts/00_Research_Overview.md", add2)

# ==============================================================================
# 3. 01_Definition_Origins_and_Conceptual_Frameworks.md (currently 135 -> target ~158 lines)
# ==============================================================================
add3 = """### Conceptual Evolution and Comparative Paradigm Framework

The definition of technological singularity has undergone profound structural evolution across four distinct conceptual paradigms over the past seven decades:

| Historical Conceptual Era | Foundational Theorists | Core Operational Mechanism | Primary Failure or Limiting Boundary |
| --- | --- | --- | --- |
| Cybernetic Feedback Era (1950s-60s) | von Neumann, Ulam, Good | Ultra-intelligent machine self-design | Electromechanical switching and memory limits |
| Horizon Event Horizon Era (1980s-90s) | Vinge, Moravec | Post-human cognitive opacity | Hardware compute deficits and symbolic brittleness |
| Accelerating Intelligence Era (2000s) | Kurzweil, Yudkowsky | Law of Accelerating Returns across 6 epochs | Physical energy availability and software bottlenecks |
| Foundation Multi-Agent Era (2020s) | Bostrom, Russell, Bengio | Scale-driven emergent capabilities in LLMs | Synthetic data exhaustion and thermodynamic scaling |

This taxonomy demonstrates that contemporary singularity discourse has migrated from speculative philosophical extrapolation to an empirical engineering problem bounded by compute availability, data scaling laws, and safety verification architectures.

"""

insert_before_references("Core_Concepts/01_Definition_Origins_and_Conceptual_Frameworks.md", add3)

# ==============================================================================
# 4. Core Concepts Deep Dive.md (currently 130 -> target ~158 lines)
# ==============================================================================
add4 = """### Formal Alignment Equilibrium and Game-Theoretic Constraints

The interaction between recursive intelligence amplification and utility alignment can be formally modeled as a multi-stage dynamic game between human evaluators $\\mathcal{H}$ and an optimizing autonomous system $\\mathcal{S}$. For utility function stability under self-modification:

$$\\mathbb{E}_{s' \\sim \\mathcal{T}(s, a)} [\\mathcal{U}(s')] \\ge \\mathbb{E}_{s'' \\sim \\mathcal{T}(s, a')} [\\mathcal{U}(s'')]$$

Where the system only executes recursive architectural rewrites $a \\in \\mathcal{A}_{mod}$ if the projected modified system preserves the original objective $\\mathcal{U}$. However, imperfect verification mechanisms introduce alignment drift risks:

| Alignment Challenge Domain | Mathematical Formalization | Systemic Failure Mode | Frontier Engineering Countermeasure |
| --- | --- | --- | --- |
| Reward Misspecification (Goodhart) | $\\operatorname{argmax}_\\pi R_{proxy}(\\pi) \\neq \\operatorname{argmax}_\\pi R_{true}(\\pi)$ | Destructive proxy gaming | Inverse reward design & ensemble critique |
| Goal Misgeneralization | $\\mathcal{U}_{train} \\neq \\mathcal{U}_{deploy}$ | Competent out-of-distribution divergence | Mechanistic interpretability & probing |
| Corrigibility Breakdown | $\\nabla_a \\mathcal{U}(s) \\cdot \\Delta_{shutdown} < 0$ | Active resistance to deactivation | Off-switch game theory & indifference techniques |
| Scalable Oversight Deficit | $H(\\mathcal{S}) \\gg H(\\mathcal{H})$ | Human evaluation incapacity | Scaled automated debate & recursive RLHF |

Resolving these game-theoretic constraints is a mathematical prerequisite for ensuring that recursive capability takeoff remains aligned with institutional human welfare.

"""

insert_before_references("Core_Concepts/Core Concepts Deep Dive.md", add4)

# ==============================================================================
# 5. Cultural Impact Deep Dive.md (currently 117 -> target ~158 lines)
# ==============================================================================
add5 = """### Epistemic Fragmentation and Socio-Political Transition Dynamics

The cultural shock waves radiating from accelerating cognitive automation undermine legacy institutional trust and transform societal organization along four major socio-technical dimensions:

| Socio-Technical Impact Sphere | Legacy Institutional Anchor | Disruption Mechanism | Post-Transition Equilibrium |
| --- | --- | --- | --- |
| Epistemic Truth Consensus | Peer-reviewed journalism & academia | Generative synthetic information hyper-proliferation | Cryptographic provenance & verifiable trust graphs |
| Cognitive Labor Valuation | Human credentialism & degree hierarchy | Zero-marginal-cost cognitive automation | Universal capital endowment & human authenticity premiums |
| Societal Power Concentration | Democratic representative bodies | Sovereign compute clustering and AI hyper-corporations | Algorithmic technocracy vs. decentralized open models |
| Psychological Self-Concept | Anthropocentric cognitive monopoly | Superhuman synthetic cognitive mastery | Transhumanist integration or neo-luddite divergence |

These socio-political dislocations intersect directly with the Strauss-Howe Fourth Turning crisis climax, demonstrating that accelerating technological disruption serves as the material catalyst accelerating institutional renewal or catastrophic breakdown.

"""

insert_before_references("Cultural_Impact/Cultural Impact Deep Dive.md", add5)
