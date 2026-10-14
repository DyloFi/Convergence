import pathlib
import shutil

root = pathlib.Path('/Users/dylanboyle/Desktop/Convergence')

# 1. Update Convergence_Master_Synthesis.md heading 8
cms = root / 'Convergence_Master_Synthesis.md'
if cms.exists():
    text = cms.read_text(encoding='utf-8')
    text = text.replace('## 8. Authoritative Academic Bibliography', '## 8. References & Academic Bibliography')
    cms.write_text(text, encoding='utf-8')
    print("Updated Convergence_Master_Synthesis.md heading 8")

# 2. Fix 01_US_China_Competition_and_Multipolarity.md
f1 = root / 'Changing World Orders/Current_Geopolitical/01_US_China_Competition_and_Multipolarity.md'
if f1.exists():
    text1 = f1.read_text(encoding='utf-8')
    
    # Replace the broken ASCII box with a clean markdown table
    old_box = """┌── [ Figure 1: Changing World Orders Current Geopolitical 01 US China Competition and Multipolarity Architecture ] ──┐
                         │   US-CHINA COMPETITION    │
└── [ End Figure 1: Changing World Orders Current Geopolitical 01 US China Competition and Multipolarity ] ──┘
                                       │
┌── [ Figure 2: Changing World Orders Current Geopolitical 01 US China Competition and Multipolarity Architecture ] ──┐
      ▼                   ▼                     ▼                   ▼
FINANCIAL WAR       TECHNOLOGY WAR        GEOPOLITICAL WAR    MILITARY WAR
- De-dollarization  - Semiconductor bans  - Global South      - Taiwan Strait
- SWIFT alternatives- AI compute control  - BRICS+ expansion  - South China Sea
- FX Reserve Freezes- Rare Earth control  - Belt & Road       - Blue-water fleet
```end-changing-world-orders-current-geopolitical-01-us-china-competition-and-multipolarity-1"""

    new_table = """### Table 1: The Four Asymmetric Warfronts of Hegemonic Competition

| Warfront Category | Primary Conflict Vector | Strategic Offensive Mechanisms | Contested Frontlines / Theater |
|---|---|---|---|
| **Financial War** | Reserve currency hegemony & clearing access | De-dollarization, SWIFT alternatives, FX reserve sanctions, bilateral currency swaps | Cross-Border Interbank Payment System (CIPS), mBridge multi-CBDC network |
| **Technology War** | Advanced compute, photolithography & critical minerals | Semiconductor export bans (EAR/FDPR), advanced EDA tool embargos, gallium/germanium controls | Leading-edge logic fab (TSMC/SMEE), AI compute training clusters, EUV lithography |
| **Geopolitical War** | Spheres of influence & maritime choke points | BRICS+ diplomatic expansion, Belt and Road Initiative (BRI), bilateral resource pacts | Global South realignment, Malacca Strait, Horn of Africa maritime corridors |
| **Military War** | Anti-access/area-denial (A2/AD) & kinetic deterrence | Blue-water naval expansion, hypersonic glide vehicles, distributed maritime operations | Taiwan Strait, First Island Chain, South China Sea artificial bastions |"""

    if old_box in text1:
        text1 = text1.replace(old_box, new_table)
        f1.write_text(text1, encoding='utf-8')
        print("Updated 01_US_China_Competition_and_Multipolarity.md")
    else:
        print("Could not find exact old_box in f1, searching lines...")

# 3. Fix Foundations Deep Dive.md
f2 = root / 'Changing World Orders/Foundations/Foundations Deep Dive.md'
if f2.exists():
    text2 = f2.read_text(encoding='utf-8')
    
    old_box2 = """```text-changing-world-orders-foundations-foundations-deep-dive-2
┌── [ Figure 2: Changing World Orders Foundations Foundations Deep Dive Architecture ] ──┐
│               CAUSAL SEQUENCE OF THE EIGHT POWER METRICS              │
└── [ End Figure 2: Changing World Orders Foundations Foundations Deep Dive ] ──┘
                                   │
 1. EDUCATION ──────► 2. INNOVATION & ────► 3. COMPETITIVENESS ────► 4. ECONOMIC
                      TECHNOLOGY                                       OUTPUT
                                                                         │
                                                                         ▼
 8. RESERVE CURRENCY ◄─ 7. FINANCIAL ◄───── 6. MILITARY POWER ◄───── 5. WORLD TRADE
    STATUS               CENTER STATUS                                 SHARE
```end-changing-world-orders-foundations-foundations-deep-dive-2"""

    new_table2 = """### Table 1: Dalio's Causal Sequence of the Eight Core Power Metrics

| Sequence Order | Measure of Power | Metric Lifecycle Category | Historical Causal Dynamic across Great Empires |
|---|---|---|---|
| 1. Education | Broad-based literacy, mathematical training, and values | Leading Indicator | Drives scientific methodology and workforce capability (Dutch universities 1600; British mechanics 1800) |
| 2. Innovation & Tech | Breakthrough inventions and engineering productivity | Leading Indicator | Generates technological edge (Dutch Fluyt vessels; British steam engines; American microprocessors) |
| 3. Competitiveness | Global productivity and export price advantage | Rising Indicator | Maximizes trade efficiency and captures market share across international sea lanes |
| 4. Economic Output | Total gross national product and industrial volume | Peak Indicator | Nation scales to become the dominant share of world economic production |
| 5. Share of World Trade | Percentage of global maritime and overland merchant flow | Peak Indicator | Transports imperial production globally; demands military protection of merchant trade routes |
| 6. Military Strength | Forward power projection and blue-water naval fleets | Lagging Indicator | Expands to secure global trade routes, overseas ports, and foreign imperial dominions |
| 7. Financial Center | Dominant global capital market and exchange hub | Lagging Indicator | Capital pools in the imperial metropolis (Amsterdam Bourse; City of London; Wall Street) |
| 8. Reserve Currency | Global pricing unit for foreign exchange reserves and debt | Ultimate Lagging Indicator | Enables sovereign debt monetization and exorbitant privilege; persists decades after competitive peak |"""

    if old_box2 in text2:
        text2 = text2.replace(old_box2, new_table2)
        f2.write_text(text2, encoding='utf-8')
        print("Updated Foundations Deep Dive.md")
    else:
        print("Could not find exact old_box2 in f2, searching lines...")

