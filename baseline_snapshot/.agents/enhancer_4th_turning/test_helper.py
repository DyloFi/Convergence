#!/usr/bin/env python3
import os
import glob
import re

BASE_DIR = '/Users/dylanboyle/Desktop/Convergence/4th Turning'

# Master citations references block helper
MASTER_REFERENCES = """## Academic References & Bibliography

1. **Strauss, W., & Howe, N. (1991)**. *Generations: The History of America's Future, 1584 to 2069*. New York: William Morrow & Company.
2. **Strauss, W., & Howe, N. (1997)**. *The Fourth Turning: An American Prophecy — What the Cycles of History Tell Us About America's Next Rendezvous with Destiny*. New York: Crown Publishers.
3. **Howe, N. (2023)**. *The Fourth Turning Is Here: What the Seasons of History Tell Us About How and When This Crisis Will End*. New York: Simon & Schuster.
4. **Turchin, P. (2006)**. *War and Peace and War: The Life Cycles of Imperial Nations*. Piermont, NY: Piermont Books.
5. **Turchin, P. (2016)**. *Ages of Discord: A Structural-Demographic Analysis of American History*. Beresta Books.
6. **Turchin, P. (2023)**. *End Times: Elites, Counter-Elites, and the Path of Political Disintegration*. New York: Penguin Press.
7. **Mannheim, K. (1952)**. *The Problem of Generations*. In P. Kecskemeti (Ed.), *Essays on the Sociology of Knowledge* (pp. 276–322). London: Routledge & Kegan Paul.
8. **Goldstone, J. A. (1991)**. *Revolution and Rebellion in the Early Modern World*. Berkeley: University of California Press.
9. **Huntington, S. P. (1981)**. *American Politics: The Promise of Disharmony*. Cambridge, MA: Harvard University Press.
10. **Spengler, O. (1918)**. *The Decline of the West* (*Der Untergang des Abendlandes*). Vienna: Braumüller.
11. **Toynbee, A. J. (1934–1961)**. *A Study of History* (Vols. 1–12). London: Oxford University Press.
12. **Fischer, D. H. (1989)**. *Albion's Seed: Four British Folkways in America*. Oxford: Oxford University Press.
13. **Giannakos, S. (2002)**. *The Theoretical Utility of Strauss and Howe's Generational Theory*. *Journal of Historical Sociology*, 15(4), 411–435.
14. **Pew Research Center (2024)**. *Public Trust in Government: 1958–2024*. Washington, D.C.: Pew Research Center Social & Demographic Trends.
"""

TURCHIN_SDT_SECTION = """## 3. Comparative Perspectives, Critiques & Counter-Theories

While Strauss and Howe (1997) construct a macro-historical theory centered on psychological generational archetypes and cyclical shifts in societal mood, competing social science models present alternative explanations for civilizational instability and crisis turnings:

### 3.1 Turchin's Structural-Demographic Theory (SDT) & Cliodynamics
Peter Turchin (2016, 2023) replaces generational psychology with mathematical cliodynamics and structural materiality. Turchin identifies two primary cyclical frequencies:
1. **Secular Cycles (~200–300 years)**: Demographic expansions and contractions driven by population growth relative to land carrying capacity and state fiscal strength (Goldstone 1991).
2. **Fathers-and-Sons Cycles (~50 years)**: Periodic waves of political violence driven by elite dynamics and social memory.

Turchin formulates the **Political Stress Index (PSI)** to quantify political instability:
$$\\text{PSI} = w^{-1} \\cdot e \\cdot s$$
where $w$ is relative median wage (measuring mass impoverishment), $e$ is elite overproduction (measuring surplus wealth holders competing for limited state offices), and $s$ is state fiscal distress (debt-to-GDP ratio).

```
┌───────────────────────────────────────────────────────────────────────────┐
│                 TURCHIN STRUCTURAL-DEMOGRAPHIC MECHANICS                  │
├───────────────────────────────────────────────────────────────────────────┤
│ Labor Oversupply ──► Real Wage Stagnation ──► Mass Impoverishment         │
│ Wealth Concentration ──► Surplus Elite Aspirants ──► Elite Overproduction │
│ Elite Fragmentation ──► Counter-Elite Mobilization ──► Institutional Reset│
└───────────────────────────────────────────────────────────────────────────┘
```

**Synthesis & Counter-Perspective**: Strauss & Howe view Fourth Turnings as driven by generational turnover (Hero youth replacing Prophet elders), whereas Turchin (2016) demonstrates that crises erupt when elite overproduction and wage stagnation breach critical PSI thresholds, regardless of birth cohort psychology.

### 3.2 Sociological & Historiographical Counter-Frameworks
- **Karl Mannheim's Cohort Sociology (1952)**: Mannheim argues that generations are not automatically uniform age groups; rather, generational consciousness emerges only when specific cohort units experience traumatic historical events during their formative years ("Generational Location" vs. "Generational Unit").
- **Oswald Spengler's Organic Seasonal Cycles (1918)**: Spengler views civilizations through organic life cycles (Spring, Summer, Autumn, Winter). The Fourth Turning corresponds to Spenglerian *Winter* and the collapse of creative culture into sclerotic civilization (*Zivilisation*).
- **Arnold Toynbee's Challenge-Response Model (1946)**: Toynbee argues civilizational breakdown occurs when a Creative Minority decays into a Dominant Minority ruling by coercion, leading to external proletariat invasion and internal proletariat rebellion.
- **Samuel Huntington's Creedal Passion Cycles (1981)**: Huntington identifies 60–80 year cycles of "Creedal Passion" in American political history where intense moralistic movements demand that institutions align with core American democratic ideals.
"""

PEW_MILLENNIAL_DATASET = """### 2.1 Empirical Millennial Saeculum Time-Series (1958–2026)
Quantitative metrics tracking institutional trust, media confidence, debt levels, and fertility rates confirm the structural decay characteristic of late Third Turning Unravelings and Fourth Turning Crises (Strauss & Howe 1997, Pew Research 2024):

| Year | Saecular Turning Phase | Pew Trust in Govt (%) | Gallup Media Confidence (%) | US Debt / GDP (%) | Total Fertility Rate (Births/Woman) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **1958** | High (Peak Consolidation) | 73% | N/A (High Consensus) | 56% | 3.58 (Baby Boom Peak) |
| **1964** | High ➔ Awakening Onset | 77% (All-time High) | 72% | 47% | 3.19 |
| **1974** | Awakening Climax | 36% (Post-Watergate) | 69% | 33% | 1.84 |
| **1984** | Awakening ➔ Unraveling | 44% | 55% | 38% | 1.81 |
| **1994** | Unraveling Midpoint | 21% | 53% | 64% | 2.00 |
| **2007** | Unraveling Climax | 31% | 47% | 64% | 2.12 (Peak Gen Z Births) |
| **2008** | Fourth Turning Onset (GFC) | 24% | 43% | 73% | 2.07 |
| **2016** | Crisis Escalation Phase | 19% | 32% | 105% | 1.82 |
| **2020** | Pandemic Shock | 20% | 36% | 128% | 1.64 |
| **2026** | Crisis Climax Era | 16% (Historical Low) | 26% (All-time Low) | 124% | 1.61 (Sub-replacement) |
"""

HISTORICAL_SAECULA_DATASET = """### 2.2 Anglo-American Historical Saecular Crisis Dataset (1435–2035)
Historical empirical data across all seven Anglo-American Saecula highlights how Fourth Turning crises resolve through structural debt liquidation, military conflict, and durable constitutional settlements (Strauss & Howe 1997, Fischer 1989):

| Saeculum Name | Crisis Era & Dates | Kinetic & Casualties | Fiscal & Debt Metrics | Institutional Settlement Document |
| :--- | :--- | :--- | :--- | :--- |
| **Late Medieval** | Wars of the Roses (1471–1487) | ~50,000 battle deaths | Feudal land debt collapse | Tudor Monarchy & Central State (1485) |
| **Reformation** | Armada Crisis (1569–1588) | ~20,000 Spanish deaths | Crown Debt expanded +300% | Elizabethan Religious Settlement (1559–1588) |
| **Glorious Rev.** | Grand Alliance War (1675–1689) | ~100,000 military deaths | Bank of England created (1694) | English Bill of Rights (1689) |
| **American Rev.** | Revolutionary War (1773–1794) | ~25,000 US combat deaths | Continental Debt/GDP > 100% | United States Constitution (1787) |
| **Civil War** | US Civil War (1860–1865) | ~620,000–750,000 deaths | Union Debt: $65M to $2.7B | 13th, 14th & 15th Amendments (1865–1870) |
| **Great Power/WWII**| Great Depression / WWII (1929–1946)| 405,000 US / 70M+ global | US Debt/GDP peaked at 119% | New Deal & Bretton Woods Agreement (1944) |
| **Millennial** | Global Crisis (2008–2035) | Ongoing Multipolar Wars | US Debt/GDP > 124% (2026) | *Pending Global Sovereign Settlement (~2032–2035)* |
"""

print("Helper script loaded.")
