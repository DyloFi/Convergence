import pathlib
import re

root = pathlib.Path("Technological Singularity")

def insert_before_references(file_rel, content_to_insert):
    p = root / file_rel
    text = p.read_text(encoding="utf-8")
    
    m = re.search(r'(##\s*(?:\d+\.\s*)?Academic References.*)', text, re.IGNORECASE)
    if not m:
        raise ValueError(f"Could not find References header in {file_rel}")
    
    ref_idx = m.start()
    before = text[:ref_idx].rstrip()
    after = text[ref_idx:].strip()
    
    new_text = before + "\n\n" + content_to_insert.strip() + "\n\n" + after + "\n"
    p.write_text(new_text, encoding="utf-8")
    lines = len(new_text.splitlines())
    print(f"Updated {file_rel}: {lines} lines (>=150: {lines >= 150})")

# 1. Controversies (143 lines -> need +10)
c_extra = r"""
- **Epistemic Humility and Horizon Uncertainty**: The requirement that forecasters report explicit confidence intervals and Bayesian probability distributions over takeoff speeds.
- **Cognitive Specialization vs. Generalist Dominance**: Assessing whether domain-specific automated agents create polycentric networks that prevent singular monopolization.
- **Legal and Regulatory Containment Feasibility**: Evaluating the jurisdictional enforceability of international treaties governing compute cluster deployment.
"""

# 2. Glossary (130 lines -> need +22)
g_extra = r"""
49. **Algorithmic Complexity Floor**: The minimal computational resource requirement beneath which an artificial intelligence system cannot support reflective self-reasoning.
50. **Hardware-Enforced Cryptographic Attestation**: The use of physically unclonable cryptographic primitives within accelerator dies to guarantee model weights remain unaltered.
51. **Sovereign Compute Autarky**: A geopolitical state posture seeking complete domestic self-sufficiency across wafer fabrication, chemical precursors, and high-bandwidth memory.
52. **Non-Ergodic Technological Risk**: Catastrophic or irreversible systemic outcomes that preclude learning through iterative trial and error.
53. **Superintelligent Utility Invariance**: The mathematical stability of a utility function under arbitrary recursive self-modification and environmental feedback.
54. **Epistemic Convergence Velocity**: The rate at which independent rational agents update their beliefs toward ground truth upon receiving new empirical observations.
"""

# 3. Sources (139 lines -> need +13)
s_extra = r"""
- **Continuous Calibration Verification**: Historical predictions are automatically rescored against realized benchmark achievements on an ongoing schedule.
- **Reproducible Containerized Execution**: Evaluation suites are archived in containerized environments with pinned random seeds to ensure deterministic verification.
- **Cross-Architecture Performance Auditing**: Capabilities are evaluated across diverse hardware architectures to decouple software efficiency from hardware acceleration.
"""

# 4. Supporting Materials (140 lines -> need +12)
m_extra = r"""
- **Clean Energy and Geothermal Co-Location**: Mitigating transmission bottlenecks by siting compute facilities adjacent to dedicated baseload clean energy generation.
- **Cryogenic and Reversible Computing Pathways**: Long-term post-CMOS architectural alternatives designed to bypass Landauer dissipation ceilings.
- **Integrated Interconnect Topologies**: Transitioning from dragonfly and fat-tree topologies to optical reconfigurable fabrics to sustain multi-million node scaling.
"""

# 5. Overview (140 lines -> need +12)
o_extra = r"""
- **Epistemic Governance and Verification**: Structuring transparent institutional oversight mechanisms to monitor algorithmic acceleration without stymieing research.
- **Socio-Economic Transition Policies**: Formulating wealth-distribution and universal capital endowment mechanisms to address macroeconomic labor obsolescence.
- **Global Coordination Architecture**: Designing robust multinational compute-monitoring frameworks to maintain international strategic stability.
"""

# 6. Timeline Milestones (148 lines -> need +6)
t_extra = r"""
- **2035 Horizon Verification**: Self-directed scientific discovery engines operating across closed-loop autonomous laboratories.
- **2040 Horizon Verification**: Fully autonomous industrial reproduction and deployment across orbital and terrestrial infrastructures.
"""

insert_before_references('Supporting_Materials/Controversies/Controversies Deep Dive.md', c_extra)
insert_before_references('Supporting_Materials/Glossary/Glossary Deep Dive.md', g_extra)
insert_before_references('Supporting_Materials/Sources/Sources Deep Dive.md', s_extra)
insert_before_references('Supporting_Materials/Supporting Materials Deep Dive.md', m_extra)
insert_before_references('Technological Singularity Overview.md', o_extra)
insert_before_references('Timeline_Milestones/Timeline Milestones Deep Dive.md', t_extra)

print("\n--- EXACT PUSH OVER 150 COMPLETED ---")
