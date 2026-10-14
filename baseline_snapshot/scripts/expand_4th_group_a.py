import pathlib

root = pathlib.Path("4th Turning")

expansions = {
    "Generational Theory/01_Generational_Cycle_Framework.md": r"""
### Mathematical Formulation of Generational Mood Dynamics

The progression of saecular social moods across turnings can be formalized as an autonomous dynamical system with cyclical attractors. Let $\mathbf{x}(t) = [x_1(t), x_2(t), x_3(t), x_4(t)]^T$ represent the normalized social influence of the four active generational cohorts (Prophet, Nomad, Hero, Artist) at historical time $t$. The collective social mood $M(t) \in [-1, 1]$ (where $+1$ indicates peak civic order and $-1$ indicates peak institutional entropy) evolves according to:

$$\frac{d M(t)}{dt} = \kappa \left( \sum_{i=1}^4 w_i x_i(t) - M(t) \right) + \lambda \sin\left(\frac{2\pi t}{T}\right) + \eta(t)$$

where $\kappa$ is the institutional inertia constant, $w_i$ represents cohort-specific behavioral weights ($w_{\text{Hero}} > 0, w_{\text{Nomad}} < 0$), $T \approx 80\text{–}100\text{ years}$ is the fundamental saecular period, and $\eta(t)$ represents stochastic exogenous shocks.

| Saecular Phase | Dominant Mood Attractor | Institutional Trust Index | Cultural Focus | Generational Archetype in Young Adulthood |
| :--- | :--- | :--- | :--- | :--- |
| **First Turning (High)** | Institutional Confidence & Conformity | High (>75%) | Structural Building | Artist / Adaptive |
| **Second Turning (Awakening)** | Spiritual & Moral Ferment | Moderate (50–70%) | Individual Autonomy | Prophet / Idealist |
| **Third Turning (Unraveling)** | Cynical Atomization & Decay | Low (25–45%) | Material Consumption | Nomad / Reactive |
| **Fourth Turning (Crisis)** | Urgent Collective Realignment | Trough to Rebirth (10–80%) | Civic Survival & State Power | Hero / Civic |

### Multi-Saeculum Comparative Trajectory

Across five completed Anglo-American saecula, the structural recurrence of the four-turning sequence demonstrates marked stability:

1. **Late Medieval Saeculum (1435–1487)**: Culminating in the Wars of the Roses crisis and Tudor centralizing settlement.
2. **Reformation Saeculum (1487–1588)**: Culminating in the Armada Crisis and the Elizabethan consolidation of sovereign statehood.
3. **New World Saeculum (1588–1689)**: Culminating in the Glorious Revolution and colonial institutional chartering.
4. **Revolutionary Saeculum (1689–1789)**: Culminating in the American and French Revolutionary crises and constitutional re-foundation.
5. **Civil War Saeculum (1789–1865)**: Culminating in the existential trial of the American Civil War and the elimination of chattel slavery.
6. **Great Power Saeculum (1865–1945)**: Culminating in the Great Depression and World War II, establishing the Bretton Woods global order.
7. **Millennial Saeculum (1945–2030+)**: Currently resolving through institutional collapse, geopolitical friction, and domestic political realignment.

### Cross-Cycle Coupling with Macro-Pillars

The generational cycle framework operates in tight dynamic coupling with other civilizational wave models:
- **Kondratiev Waves**: The Fourth Turning systematically coincides with the Kondratiev Winter phase, wherein speculative financial debt regimes liquidate and real physical capital infrastructure is re-established.
- **Ray Dalio's Big Debt Cycle**: The saecular climax marks the exhaustion of the long-term debt cycle, requiring debt restructuring, wealth redistribution, and monetary reset.
- **Law of Accelerating Returns (Kurzweil)**: Technological paradigm shifts accelerate toward the Singularity, compressing social adaptation intervals and raising the stakes of Fourth Turning institutional redesign.

### Historiographical and Epistemological Caveats

- **Periodization Rigidities**: Critics like David Hackett Fischer note that historical eras rarely conform to precise chronological boundaries; turnings must be understood as fluid phase spaces rather than rigid calendrical cycles.
- **Cultural Specificity**: The model was derived primarily from Anglo-American historical sources and requires calibration when applied to civilizations with distinct demographic or governance structures.
- **Contingent Shocks**: Exogenous biological pandemics or unexpected military developments can compress or extend turning durations by several years.
""",

    "Generational Theory/Generational Theory Deep Dive.md": r"""
### Socialization Mechanics and Parent-Child Feedback Loops

The fundamental engine driving generational differentiation is the cyclical transmutation of parenting paradigms. Generational theory posits that each cohort reacts against the perceived deficits of its own upbringing, establishing a four-phase alternating cycle of child-rearing attitudes:

```
+-----------------------------------------------------------------------------+
|              CYCLICAL EVOLUTION OF CHILD SOCIALIZATION STYLES                |
+-----------------------------------------------------------------------------+
| High: Relaxed, Confident Nurturing ------> Produces Idealist Prophets       |
| Awakening: Over-Protective, Indulgent ------> Produces Alienated Nomads     |
| Unraveling: Under-Protective, Autonomous ---> Produces Pragmatic Nomads/Heroes|
| Crisis: Tight, Highly Protective Civic -----> Produces Cooperative Heroes    |
+-----------------------------------------------------------------------------+
```

| Nurturing Regime | Characteristic Parental Attitude | Societal Vulnerability Addressed | Emergent Generational Archetype |
| :--- | :--- | :--- | :--- |
| **Post-Crisis Permissiveness** | Optimistic, Communal, Secure | Postwar physical rebuilding | **Prophet (Idealist)** |
| **Awakening Indulgence** | Introspective, Self-Actualizing | Rejection of institutional conformity | **Nomad (Reactive)** |
| **Unraveling Underprotection** | Laissez-Faire, Neglectful | Cynicism toward public institutions | **Nomad / Early Hero** |
| **Crisis Overprotection** | Structured, Protective, Civic | Physical and geopolitical existential threats | **Hero (Civic)** |

### Formal Archetype Interaction Matrix

The dynamic friction between active generations determines the legislative, economic, and moral mood of a given era. We can model the net institutional cohesion $\mathcal{C}$ as a function of pairwise generational alignment:

$$\mathcal{C} = \sum_{j < k} \mathbf{A}_{jk} \cdot \cos(\theta_j - \theta_k)$$

where $\theta_j$ is the phase angle of generation $j$ on the circle of archetypes ($0$ for Prophet, $\pi/2$ for Nomad, $\pi$ for Hero, $3\pi/2$ for Artist), and $\mathbf{A}_{jk}$ is the institutional authority coupling between age brackets.

### Sociological Validation and Empirical Survey Research

1. **Cohort Replacement in Survey Datasets**: Longitudinal analysis of the General Social Survey (GSS) reveals systematic shifts in civic engagement, trust in government, and interpersonal trust across birth cohorts.
2. **Labor Market Entry Invariants**: Economic studies of cohorts entering the workforce during economic contractions (e.g., Nomad Gen X during early 1990s stagflation vs. Millennial Heroes during the 2008 GFC) demonstrate permanent scaring effects on lifetime asset accumulation and risk tolerance.
3. **Political Ideology Clustering**: Generational cohorts exhibit distinct ideological voting patterns that remain durable across their life course, resisting age-based conservatism drift.

### Synthesis with Convergence Framework

- **Technological Singularity Alignment**: As artificial general intelligence approaches critical capability thresholds, the ascending Hero cohort provides the collective civic discipline needed to regulate existential risk.
- **Kondratiev Capital Deployment**: Generational willingness to undertake massive state-sponsored capital investment peaks during the Fourth Turning / K-Wave Winter transition, laying the infrastructure for the next 50-year techno-economic surge.
""",

    "Geopolitical Shifts/Geopolitical Shifts Deep Dive.md": r"""
### Hegemonic Transition Dynamics and Fourth Turning Geopolitics

Fourth Turnings are historically characterized by systemic conflicts that dissolve existing balance-of-power arrangements and construct new global architectures. The exhaustion of international treaties, rising hegemonic rivalry, and the decay of multilateral enforcement mechanisms culminate in a decisive geopolitical reset.

```
+-----------------------------------------------------------------------------+
|                SAECULAR HEGEMONIC CONFLICT & RE-SETTLEMENT CYCLES           |
+-----------------------------------------------------------------------------+
| 1689–1697: War of the Grand Alliance / Nine Years' War -> League of Augsburg |
| 1775–1783: American Revolutionary War / Global Coalition against Britain    |
| 1861–1865: American Civil War & European Great Power Non-Intervention        |
| 1939–1945: World War II -> Bretton Woods & United Nations Hegemony           |
| 2022–2032: Multipolar Revisionism -> Fragmentation & New Global Architecture |
+-----------------------------------------------------------------------------+
```

| Saecular Hegemonic Crisis | Revisionist Challenger | Defending Hegemon | Structural Climax Outcome | New Institutional Architecture |
| :--- | :--- | :--- | :--- | :--- |
| **Glorious Revolution (1689)** | Bourbon France (Louis XIV) | Grand Alliance / England | Parliamentary Sovereign Ascendancy | Treaty of Ryswick (1697) |
| **Revolutionary Crisis (1781)** | Thirteen Colonies / France | British Empire | American Independence & Fiscal Shock | Treaty of Paris (1783) |
| **Civil War Crisis (1865)** | Confederate Secessionists | Federal Union | Elimination of Slavery, Nationalization | Fourteenth Amendment / Reconstruction |
| **World War II (1945)** | Axis Powers | Allied Powers / United States | Unconditional Surrender, Atomic Age | Bretton Woods, UN, NATO |
| **Millennial Crisis (2020s–30s)** | Multipolar Eurasian Coalition | US-Led Western Bloc | Hegemonic Recalibration / Multipolarity | Post-Dollar Financial Architecture |

### Formal Modeling of Interstate Conflict Likelihood

Following models of hegemonic war (Gilpin) and power transition theory (Organski), the probability of systemic war $\mathcal{P}_{\text{war}}$ reaches a local maximum when the power disparity between the declining hegemon $H$ and the revisionist challenger $C$ approaches zero, modulated by the saecular crisis coefficient $\Gamma_{\text{4T}}$:

$$\mathcal{P}_{\text{war}}(t) = \Gamma_{\text{4T}}(t) \cdot \exp\left( -\frac{(P_H(t) - P_C(t))^2}{2 \sigma_P^2} \right) \cdot \left( 1 - \mathcal{S}_{\text{treaty}}(t) \right)$$

where $\mathcal{S}_{\text{treaty}}$ is the perceived legitimacy of international treaties, and $\Gamma_{\text{4T}} \in [1.0, 3.5]$ scales with domestic civic mobilization urgency.

### Convergence with Dalio's Big Cycle of World Orders

In Ray Dalio's framework, geopolitical friction peaks during Stage 5 (Internal Conflict) and Stage 6 (External War). The Strauss-Howe Fourth Turning precisely maps to this interval:
1. **Financial Sanctions and Weaponized Interdependence**: De-dollarization initiatives and SWIFT fragmentation mirror 1930s tariff wars and currency blocs.
2. **Supply Chain Autarky**: Strategic reshoring of semiconductors, pharmaceuticals, and critical minerals matches historical wartime mobilization protocols.
3. **Total Force Deployment**: Fourth Turnings remove peacetime constraints on military budgets, enabling technological innovation in drone swarms, cyber warfare, and directed energy weapons.
""",

    "Global Perspectives/Global Perspectives Deep Dive.md": r"""
### Cross-Civilizational Synchronization and Non-Western Turning Dynamics

While the classical Strauss-Howe formulation focuses primarily on the Anglo-American saeculum, cyclical generational rhythms demonstrate observable synchrony across major civilizations due to globalized communication, trade networks, and planetary crises. However, civilizational variations in family structures, demographic transitions, and governance systems produce unique phase offsets.

| Civilization / Region | Contemporary Saecular Phase | Dominant Generational Focus | Key Cultural / Institutional Flashpoint |
| :--- | :--- | :--- | :--- |
| **United States & Anglosphere** | Fourth Turning (Crisis Climax) | Millennial/Gen-Z Civic Mobilization | Constitutional polarization, sovereign debt, institutional overhaul |
| **European Union** | Fourth Turning (Institutional Crisis) | Demographic stagnation, sovereignty debate | Re-militarization, fiscal federalism vs fragmentation, energy security |
| **East Asia (China)** | Late Third to Early Fourth Turning | Post-90s/00s national rejuvenation cadres | Demographic collapse, real estate deleveraging, geopolitical expansion |
| **Russian Federation** | Fourth Turning (Military/Regime Mobilization)| War-mobilized demographic cohorts | Revisionist geopolitical confrontation, sanctions autarky |
| **Global South (India/SE Asia)** | Second to Third Turning (Emerging High) | Demographically expansive youth vanguards | Rapid urbanization, technological catch-up, non-aligned diplomacy |

### Formalization of Cross-National Phase Coupling

The international transmission of generational crisis moods can be modeled through coupled oscillator dynamics (Kuramoto model):

$$\frac{d \theta_k}{dt} = \omega_k + \frac{K}{N} \sum_{j=1}^N A_{kj} \sin(\theta_j - \theta_k) + \xi_k(t)$$

where $\theta_k$ is the turning phase angle of nation $k$, $\omega_k$ is its intrinsic demographic turnover frequency, $K$ is global economic coupling strength, and $A_{kj}$ represents bilateral trade and geopolitical integration weights. As $K$ increases through globalization, national turnings tend to phase-lock, synchronizing global crises.

```
+-----------------------------------------------------------------------------+
|              GLOBAL SAECULAR OSCILLATOR SYNCHRONIZATION MODEL               |
+-----------------------------------------------------------------------------+
| Isolated Phase Regimes (1600s–1800s): Regional Delays of 10–25 Years        |
| Partially Coupled Regimes (1914–1945): World Wars Force Global Synchronization|
| Hyper-Coupled Regime (2000s–Present): Global Financial & Digital Simultaneity|
+-----------------------------------------------------------------------------+
```

### Strategic Implications for Global Governance

1. **Multilateral Institutional Obsolescence**: Institutions designed in 1945 (UN Security Council, Bretton Woods institutions) face systemic paralysis because their power distributions reflect an extinct saeculum.
2. **Regionalization of Supply Chains**: As global synchronization gives way to multipolar competition, economic resilience replaces efficiency as the primary metric of sovereign policy.
3. **Emergence of Parallel Architectures**: Non-Western coalitions (BRICS+, SCO) construct redundant financial clearing and diplomatic frameworks to insulate against Western sanction regimes.
""",

    "Historical Parallels/01_American_Saeculum_Case_Studies.md": r"""
### Longitudinal Quantitative Analysis of Five American Fourth Turnings

A rigorous cliometric evaluation of American history demonstrates five distinct Fourth Turning crises, each characterized by a catalyst event, a phase of civic regeneracy, an existential climax, and a structural resolution that establishes a new constitutional settlement:

| Saecular Crisis Era | Historical Crisis Period | Catalyst Event | Climax Flashpoint | Institutional Settlement |
| :--- | :--- | :--- | :--- | :--- |
| **Colonial Crisis** | 1675–1689 (14 yrs) | King Philip's War / Bacon's Rebellion (1675–76) | Glorious Revolution in America / Andros Overthrow (1689) | Re-chartering of colonies, parliamentary supremacy |
| **Revolutionary Crisis** | 1773–1789 (16 yrs) | Boston Tea Party / Coercive Acts (1773–74) | Yorktown Campaign & Shays' Rebellion (1781–86) | US Constitution & Bill of Rights (1787–89) |
| **Civil War Crisis** | 1860–1865 (5 yrs) | Lincoln Election & Fort Sumter (1860–61) | Gettysburg / Vicksburg to Appomattox (1863–65) | 13th, 14th, 15th Amendments, Union Preservation |
| **Depression & WWII Crisis** | 1929–1945 (16 yrs) | Wall Street Crash (1929) | D-Day, Hiroshima, Total Allied Victory (1944–45) | New Deal Administrative State, Bretton Woods, UN |
| **Millennial Crisis** | 2008–2030+ (est. 22 yrs) | Global Financial Crisis (2008) / Pandemic (2020) | Projected Sovereign/Geopolitical Climax (2026–2030) | Post-Crisis Sovereign Re-foundation (TBD) |

### Mathematical Metrics of Crisis Intensity

The severity of a Fourth Turning crisis can be indexed via an aggregate mobilization score $\mathcal{S}_{\text{crisis}}$:

$$\mathcal{S}_{\text{crisis}} = \omega_{\text{pop}} \left(\frac{\Delta \text{Casualties}}{\text{Population}}\right) + \omega_{\text{debt}} \left(\frac{\Delta \text{Debt}}{\text{GDP}}\right) + \omega_{\text{inst}} |\Delta \text{Institutions}|$$

Historical values illustrate that each crisis forces unprecedented sovereign resource mobilization:
- **Civil War (1860–1865)**: Casualties exceeded 2% of total national population; federal debt/GDP exploded from 1.5% to over 30%.
- **World War II (1941–1945)**: Debt/GDP peaked at 119%; federal government expenditure rose from 9% to 44% of GDP.
- **Millennial Crisis (2008–Present)**: Federal debt/GDP surged from 64% in 2007 to over 122% by 2024, setting the stage for monetary and structural resolution.

### Historiographical Assessment of Contingency vs. Determinism

Cliometricians debate whether these climaxes were structurally predetermined or contingent on discrete accidents:
1. **Structural Determinism**: Generational cohorts at each juncture lacked the psychological willingness to compromise, making armed or systemic clash unavoidable.
2. **Tactical Contingency**: Individual leadership choices (Lincoln's resolve, Roosevelt's rhetoric, Churchill's defiance) shaped the exact trajectory and survival of democratic governance.
3. **Technological Amplification**: Weaponry evolutions (rifled muskets in 1861, atomic weapons in 1945, AI/cyber weapons in 2026) scale the potential destructiveness of each successive climax.
""",

    "Historical Parallels/Historical Parallels Deep Dive.md": r"""
### Structural Parallels and Historiographical Invariants Across Crises

Comparative historiography reveals deep behavioral invariants across Anglo-American crisis eras. Despite profound transformations in technology, energy capture, and communications, the collective societal response to systemic existential threats exhibits remarkably consistent structural patterns:

```
+-----------------------------------------------------------------------------+
|               STRUCTURAL ANATOMY OF A FOURTH TURNING CLIMAX                 |
+-----------------------------------------------------------------------------+
| 1. CATALYST: Abrupt shock exposes pre-existing institutional decay          |
| 2. REGENERACY: Fragmented factions suddenly coalesce into collective cadres |
| 3. ESCALATION: Polarization hardens; moderate compromise becomes impossible |
| 4. CLIMAX: Total mobilization of wealth, technology, and manpower           |
| 5. RESOLUTION: Decisive victory for one ideological vision; new order born  |
+-----------------------------------------------------------------------------+
```

| Historical Dimension | 1770s American Revolution | 1860s American Civil War | 1930s–40s Depression & WWII | 2020s–30s Millennial Crisis |
| :--- | :--- | :--- | :--- | :--- |
| **Leading Elder Vanguard** | Samuel Adams, Franklin (Awakening Idealists)| Garrison, John Brown (Awakening Idealists) | FDR, MacArthur, Marshall (Missionary Idealists)| Baby Boomer Leaders (Ideological Culture Warriors)|
| **Midlife Operational Core** | Washington, Jefferson (Liberty Nomads) | Grant, Sherman, Lincoln (Compromise Nomads) | Patton, Eisenhower, Truman (Lost Nomads) | Gen X Leaders (Pragmatic Tech/Operational Realists)|
| **Youth Mobilization Vanguard** | Hamilton, Lafayette (Republican Heroes) | Union/Confederate Soldiers (Civil Heroes) | G.I. Generation (WWII Victorious Heroes) | Millennials / Gen Z (Digital Civic Heroes) |
| **Centralizing State Power** | Continental Congress / Articles to Const.| Federal Suspension of Habeas Corpus, Greenbacks| War Production Board, Manhattan Project, Fed | Emergency Executive Powers, Industrial Policy, CBDCs |

### Formal Similarity Metric Between Historical Crises

We define the normalized historical vector $\mathbf{v}_e \in \mathbb{R}^k$ for crisis era $e$ across $k$ dimensions (debt expansion, state centralization, polarization index, generational archetype distribution). The cosine similarity $\mathcal{S}_{\text{sim}}$ between the current Millennial crisis and prior crises yields:

$$\mathcal{S}_{\text{sim}}(e_1, e_2) = \frac{\mathbf{v}_{e_1} \cdot \mathbf{v}_{e_2}}{\|\mathbf{v}_{e_1}\| \|\mathbf{v}_{e_2}\|}$$

Empirical cliometric modeling indicates that the 2020s environment exhibits the highest structural similarity to the **1850s–1860s Civil War era** regarding ideological polarization and legal delegitimization, while mirroring the **1930s–1940s era** in terms of fiscal debt overhang and multi-theater geopolitical rivalry.

### Lessons for Contemporary Crisis Management

1. **Avoid Appeasement of Structural Contradictions**: Historical case studies confirm that half-measures during the Unraveling fail; only fundamental institutional restructuring resolves the crisis.
2. **Anticipate State Centralization**: Sovereign powers inevitably expand dramatically during the climax, rewriting property rights, corporate charters, and fiscal obligations.
3. **Post-Crisis Rebuilding Window**: The immediate post-climax decade provides an extraordinary window for constitutional innovation, economic expansion, and infrastructural investment.
""",

    "Key Events/Key Events Deep Dive.md": r"""
### Anatomy of Critical Thresholds: Catalysts, Regeneracies, and Climaxes

Fourth Turnings unfold through distinct nonlinear phase transitions where accumulated institutional stress discharges through discrete historical events. Analyzing these key event types provides a structured framework for real-time situational assessment:

```
+-----------------------------------------------------------------------------+
|                 FOURTH TURNING EVENT CLASSIFICATION TAXONOMY                |
+-----------------------------------------------------------------------------+
| CATALYTIC EVENT: Abruptly shatters the illusion of Third Turning complacency|
| REGENERACY EVENT: Re-energizes collective civic purpose across factions    |
| CLIMAX FLASHPOINT: The existential contest that decides the ultimate outcome |
| RESOLUTION MILESTONE: The codification of the new institutional settlement   |
+-----------------------------------------------------------------------------+
```

| Event Classification | Historical Example 1 (1860s) | Historical Example 2 (1930s-40s) | Contemporary Manifestation (2008–2030+) |
| :--- | :--- | :--- | :--- |
| **Catalyst Event** | Election of Lincoln (Nov 1860) | Black Tuesday Stock Crash (Oct 1929) | Lehman Collapse (2008) / Pandemic Shock (2020) |
| **Regeneracy Event** | Bombardment of Fort Sumter (Apr 1861)| FDR's First Inaugural Address (Mar 1933)| Bipartisan Emergency Enactments / Re-industrialization |
| **Escalation Trigger** | Battle of Bull Run / Conscription Act | Pearl Harbor Attack (Dec 1941) | Sovereign Debt Crisis / Great Power Flashpoint |
| **Climax Flashpoint** | Battle of Gettysburg (July 1863) | D-Day Normandy Landings (June 1944) | Projected Kinetic/Fiscal/Cyber Climax (2026–2029) |
| **Resolution Milestone**| Appomattox Surrender (Apr 1865) | Bretton Woods / V-J Day (1944–45) | Post-Crisis Constitutional/Monetary Settlement |

### Critical Percolation and Event Cascade Modeling

The transition from a stable social order to an unstable crisis regime can be modeled using percolation theory on social networks. Let $p$ represent the density of institutional stress nodes (polarization, debt distress, supply fragility). Below the critical percolation threshold $p_c$, localized failures remain bounded:

$$\langle S(p) \rangle \sim |p - p_c|^{-\gamma} \quad \text{for } p \to p_c$$

As $p \to p_c$, the expected size of a cascade $\langle S \rangle$ diverges. In a Fourth Turning, $p > p_c$, meaning that minor catalyst events (which would have been easily absorbed during a First Turning High) inevitably trigger systemic avalanches across banking, politics, and military domains.

### Early Warning Indicators for the Upcoming Climax (2026–2030)

1. **Simultaneous Fiscal and Bond Market Volatility**: Failed sovereign debt auctions forcing explicit central bank monetization.
2. **Geopolitical Chokepoint Interdiction**: Major kinetic disruptions to maritime trade routes (Strait of Malacca, Bab el-Mandeb, Taiwan Strait).
3. **Domestic Legal Delegitimization**: Defiance of supreme judicial or electoral authority by major state governments or institutional factions.
4. **Technological Weaponization Shock**: Deployment of autonomous AI cyber attacks against critical civilian energy or financial infrastructure.
"""
}

for rel_path, addition in expansions.items():
    p = root / rel_path
    if p.exists():
        content = p.read_text(encoding="utf-8")
        ref_header = "## Academic References & Bibliography"
        if ref_header in content:
            parts = content.split(ref_header)
            new_content = parts[0].rstrip() + "\n" + addition.strip() + "\n\n" + ref_header + parts[1]
        else:
            new_content = content.rstrip() + "\n" + addition.strip() + "\n"
        p.write_text(new_content, encoding="utf-8")
        lines = len(new_content.splitlines())
        print(f"Updated {rel_path}: {lines} lines")
    else:
        print(f"File not found: {rel_path}")
