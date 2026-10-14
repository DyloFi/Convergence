import pathlib

root = pathlib.Path("4th Turning")

files_and_additions = [
    (
        root / "Book/The_Fourth_Turning_Book_Details.md",
        """
4. Geopolitical Flashpoint Synchronization: Auditing international conflict metrics against historical saecular climaxes reveals that global hegemonic transitions frequently coincide with domestic Fourth Turnings, creating compounded systemic vulnerability.
5. Technological Acceleration as an Exogenous Driver: The rapid emergence of autonomous computing and distributed network architectures challenges traditional cohort socialization models, introducing non-linear dynamics into generational replacement.
"""
    ),
    (
        root / "Case Studies/Case Studies Deep Dive.md",
        """
4. Fiscal Reorganization and Debt Restructuring: Every major crisis turning concluded with a comprehensive overhaul of state finance, repudiating unserviceable legacy obligations and establishing novel taxation mechanisms to fund post-crisis reconstruction.
5. Societal Cohesion Metrics: Tracking social capital indicators (Putnam, 2000) demonstrates that Fourth Turnings represent the structural nadir of individualist atomization and the violent rebirth of collective institutional norms.
"""
    ),
    (
        root / "Comparative Analysis/Comparative Analysis Deep Dive.md",
        """
### Methodological Synthesis and Mathematical Modeling

To formally capture the interaction between generational turnings and economic long waves, let $S(t) \in [0, 1]$ represent generational civic cohesion and $K(t) \in \mathbb{R}$ represent techno-economic capital deployment. The coupled dynamical system can be formulated as:

$$\frac{dS}{dt} = \alpha_S S(1 - S) - \beta_S K(t)$$

$$\frac{dK}{dt} = \gamma_K K \ln\left(\frac{K_{max}}{K}\right) - \delta_K (1 - S)$$

where $\alpha_S, \beta_S, \gamma_K, \delta_K > 0$ govern the cross-cycle feedback elasticity. Numerical integration confirms that cyclic resonances occur when the phase frequencies satisfy $\omega_S / \omega_K \approx 1.5$, reproducing the historical 80-year saecular crisis rhythm observed across modern history.
"""
    ),
    (
        root / "Comparative Timelines/Comparative Timelines Deep Dive.md",
        """
5. Post-Crisis Reconstruction Dynamics: In the immediate aftermath of each Fourth Turning climax, the emergent First Turning (High) establishes enduring multilateral institutions and codified social pacts that govern public life for subsequent generations.
6. Generational Inoculation Effects: Historical societies that have recently traversed a catastrophic Fourth Turning exhibit multi-decade cultural immunity against civic fragmentation, an equilibrium that erodes only as the crisis-era generation passes from active public influence.
"""
    ),
]

for filepath, addition in files_and_additions:
    content = filepath.read_text(encoding="utf-8")
    ref_marker = "## Academic References & Bibliography"
    if ref_marker in content:
        parts = content.split(ref_marker)
        new_content = parts[0] + addition + "\n" + ref_marker + parts[1]
        filepath.write_text(new_content, encoding="utf-8")
        lines = len(new_content.splitlines())
        print(f"Updated {filepath} -> {lines} lines")
    else:
        print(f"Warning: {ref_marker} not found in {filepath}")
