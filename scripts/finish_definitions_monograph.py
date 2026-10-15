import pathlib

root = pathlib.Path(__file__).resolve().parent.parent / "Changing World Orders"
f_def = root / "Supporting_Materials/Definitions/Definitions Deep Dive.md"

text = f_def.read_text()
ref_pos = text.find("-----------------\n\n## 2. Advanced Cliometric")

part1 = text[:ref_pos]
part2 = text[ref_pos:]

extra_definitions = """### 16. Kondratiev Long Wave Technological Cycles
- **Etymology & Theoretical Origin**: Formulated by Soviet economist Nikolai Kondratiev (1925) and expanded by Joseph Schumpeter (1939) in his theory of creative destruction. Identifies 45-to-60-year macroeconomic supercycles driven by foundational general-purpose technology clusters (steam, steel/railroads, electrification/chemicals, petrochemicals/automobiles, and microelectronics/information technology).
- **Operationalization & Empirical Dynamics**: In Hegemonic Stability models, the upswing of a Kondratiev wave coincides with the ascending phase of a new hegemon whose domestic industrial base pioneers the breakthrough technoeconomic paradigm, while the downswing marks imperial exhaustion and technological equalization by competitors (Dalio 2021; Arrighi 1994).

### 17. Cusp Catastrophe Topological Structural Breaks
- **Etymology & Theoretical Origin**: Derived from René Thom's Catastrophe Theory (1972) and applied to social and systemic transition by E.C. Zeeman (1976). Describes non-linear dynamical systems where continuous, gradual parameter shifts abruptly trigger discontinuous, catastrophic state changes.
- **Operationalization & Empirical Formula**: Hegemonic stability is modeled on a smooth manifold governed by state potential $V(x; u, v) = \frac{1}{4}x^4 + \frac{1}{2}u x^2 + v x$, where $u$ represents sovereign debt solvency and $v$ represents challenger power parity. When the system crosses the bifurcation cusp ($4u^3 + 27v^2 = 0$), imperial order collapses discontinuously without prior linear warning (Gilpin 1981).

### 18. Anti-Access/Area Denial (A2/AD) Defensive Bastions
- **Etymology & Theoretical Origin**: Formulated in post-Cold War military doctrine to describe operational strategies designed to prevent an adversary from entering a contested theater of operations (Anti-Access) and restrict maneuverability within that theater (Area Denial).
- **Operationalization & Empirical Application**: Crucial in evaluating Pacific hegemonic competition, where China's layered deployment of land-based anti-ship ballistic missiles (DF-21D, DF-26), integrated air defense systems, and submarine fleets creates a high-attrition perimeter inside the First Island Chain, challenging traditional Mahanian US naval dominance (Allison 2017).

### 19. Multiplex World Order
- **Etymology & Theoretical Origin**: Conceptualized by International Relations theorist Amitav Acharya in *The End of American World Order* (2014). Posits that the contemporary transition does not lead to a singular new hegemon, but rather to a "multiplex" theater—a decentralized, multi-layered system characterized by overlapping regional architectures, cross-cutting coalitions, and functional governance minilaterals.
- **Operationalization & Empirical Application**: Explains why contemporary international governance features concurrent participation across competing bodies: BRICS+, the G20, the Shanghai Cooperation Organisation, the Quad, and bilateral currency networks, reflecting non-hegemonic institutional dispersion (Acharya 2014; Ikenberry 2001).

### 20. Sovereign Debt Repudiation and Conversion Trilemma
- **Etymology & Theoretical Origin**: Advanced by Carmen Reinhart and Kenneth Rogoff in *This Time Is Different* (2009). Analyzes sovereign balance sheet crisis mechanics when total debt-to-GDP crosses the critical 100-130% threshold.
- **Operationalization & Empirical Dynamics**: Hegemons burdened with excessive sovereign obligations face an irreconcilable trilemma between: (1) explicit sovereign default/debt restructuring, (2) hyper-inflationary currency monetization, or (3) severe financial repression (capping interest rates below inflation to erode debt real value over time). Historically, declining reserve currency issuers invariably resort to financial repression and currency debasement (Reinhart & Rogoff 2009; Dalio 2021).

"""

final_text = part1 + extra_definitions + part2
f_def.write_text(final_text)
print("Updated Definitions Deep Dive:", len(f_def.read_text().splitlines()), "lines")
