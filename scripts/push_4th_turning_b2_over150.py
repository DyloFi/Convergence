import pathlib

root = pathlib.Path("4th Turning")

files_and_additions = [
    (
        root / "Book/Book Deep Dive.md",
        """
### Cross-Disciplinary Synthesis and Paradigm Integration

Integrating the Strauss-Howe thesis with modern evolutionary macro-sociology (Turchin, 2016; Modelski, 1987) demonstrates that generational turnings reflect endogenous institutional feedback mechanisms rather than astrological or mystical determinism. When social trust and civic solidarity peak during a High, institutions underinvest in resilience against tail risks. As the generational memory of existential sacrifice fades through the Awakening and Unraveling, structural inequality and elite overproduction destabilize the socio-political equilibrium, culminating inevitably in a systemic Fourth Turning realignment.
"""
    ),
    (
        root / "Book/The_Fourth_Turning_Book_Details.md",
        """
### Empirical Falsification Criteria and Quantitative Demographics

Rigorous empirical testing of the book's core hypotheses requires tracking quantitative demographic and economic indicators across birth cohorts:

1. Institutional Trust Trajectories: Longitudinal survey data from the General Social Survey (GSS) and Gallup confirm that public trust in key democratic institutions (Congress, the presidency, the judiciary, mainstream press) declined monotonically from over 75% in the mid-1960s (late High / early Awakening) to under 25% by the 2020s (mid-Crisis turning).
2. Generational Wealth Accumulation Disparities: Federal Reserve distribution tables highlight acute divergences between the Silent/Boomer asset accumulation trajectory and that of Generation X and Millennials, driven by asset price inflation, housing unaffordability, and student debt burdens.
3. Civic Re-alignment Dynamics: Testing whether younger cohorts exhibit the coordinated civic mobilization characteristic of the historical "Hero" archetype requires measuring voter participation rates, community organizing density, and military/civilian service enrollment patterns across the 2020-2030 decadal window.
"""
    ),
    (
        root / "Case Studies/Case Studies Deep Dive.md",
        """
### Historiographical Lessons and Post-Crisis Institutional Architecture

Synthesizing historical case studies across centuries of Anglo-American Fourth Turnings reveals core principles of post-crisis institutional endurance:

1. Hegemonic Restructuring: Every resolved Fourth Turning established a new sovereign order and fiscal constitution—from the Tudor bureaucratic monarchy after Bosworth, to the Bill of Rights after 1689, the Federal Constitution after 1787, the 14th Amendment industrial union after 1865, and the Bretton Woods system after 1945.
2. Generational Turnover in State Leadership: The resolution of each crisis coincided with the ascension of a new generational archetype to supreme leadership. In 1865, Lincoln and Grant represented the pragmatic resolve of the Prophet/Nomad vanguard; in 1945, Roosevelt and Marshall directed the organized power of the G.I. Hero cohort.
3. Resilience Against Authoritarian Degeneration: A critical hazard identified across comparative case studies is the risk of authoritarian consolidation during the crisis climax, where existential emergencies justify extraordinary executive prerogatives that outlast the crisis window.
"""
    ),
    (
        root / "Comparative Analysis/Comparative Analysis Deep Dive.md",
        """
### Inter-Paradigm Synchronization and Multi-Frequency Harmonics

A unified model of macro-historical cyclicality requires synthesizing the distinctive phase frequencies of leading cyclic theories:

| Analytical Framework | Principal Theorists | Dominant Cycle Period | Underlying Causal Mechanism |
| :--- | :--- | :--- | :--- |
| Generational Theory | Strauss & Howe (1997) | 80–100 Years | Four-generation archetype turnover & social mood |
| Long Wave Econometrics | Kondratiev (1926), Perez (2002) | 50–60 Years | Techno-economic paradigms & basic capital renewal |
| Structural-Demographic | Turchin (2016), Goldstone (1991) | 50 & 200 Years | Elite overproduction, popular immiseration & fiscal strain |
| Long-Term Debt Cycle | Dalio (2018), Minsky (1986) | 75–100 Years | Private/public debt capacity exhaustion & currency debasement |
| War and Hegemony | Modelski (1987), Toynbee (1934) | 100–120 Years | Global leadership challenge & naval/economic preeminence |

When multiple independent cycles reach phase synchronization—such as the coincidence of a Fourth Turning crisis climax with a Kondratiev long-wave trough and a Dalio sovereign debt deleveraging—the resulting socio-political upheaval experiences exponential amplification.
"""
    ),
    (
        root / "Comparative Timelines/Comparative Timelines Deep Dive.md",
        """
### Comparative Epochal Chronology and Structural Milestone Markers

Mapping historical milestones across American saecular timelines demonstrates remarkable structural congruence in the cadence of political realignments:

1. Revolutionary Saeculum (1704–1794): The Great Awakening of the 1740s catalyzed anti-hierarchical religious individualism, eroding imperial deference and paving the way for the 1773–1789 Revolutionary Crisis.
2. Civil War Saeculum (1794–1865): The Second Great Awakening of the 1820s–1830s birthed radical abolitionist and temperance movements, creating irreconcilable moral polarization that fractured the republic by 1860.
3. Great Power Saeculum (1865–1946): The Missionary Awakening of the 1890s produced Progressive moral crusades, leading through the 1920s jazz-age Unraveling into the total mobilization of the 1930s–1940s.
4. Millennial Saeculum (1946–2030s): The Consciousness Revolution of the 1960s–1970s triggered institutional decay and cultural fragmentation, establishing the foundational preconditions for the current Fourth Turning crisis.
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
