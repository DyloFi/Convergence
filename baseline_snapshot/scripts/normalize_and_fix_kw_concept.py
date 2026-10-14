import pathlib
import re

p = pathlib.Path("Kondratiev Waves/Concept/01_Structural_Mechanisms_of_Long_Waves.md")
content = p.read_text(encoding="utf-8")

# 1. Replace the ASCII box diagram that has |   | with clean markdown text
old_diagram_block = """```
+-------------------------------------------------------------+
|                PHASE 1: PROSPERITY / EXPANSION              |
| High innovation investment, rising capital goods production |
+------------------------------+------------------------------+
                               |
                               v
+------------------------------+------------------------------+
|                 PHASE 2: RECESSION / PLATEAU                |
| Overcapacity, falling profit rates, financial speculation    |
+------------------------------+------------------------------+
                               |
                               v
+------------------------------+------------------------------+
|                PHASE 3: DEPRESSION / DOWNTURN               |
| Liquidation, debt deflation, basic innovation gestation     |
+------------------------------+------------------------------+
                               |
                               v
+------------------------------+------------------------------+
|                PHASE 4: RECOVERY / REVIVAL                  |
| Deployment of new techno-economic paradigm, credit rebuild  |
+-------------------------------------------------------------+
```"""

new_diagram_block = """*Figure 1.1: Four-Phase Structural Cycle of Kondratiev Long Waves*

1. **Phase 1: Prosperity and Expansion (Upswing)**
   - Accelerated capital allocation into core infrastructure and basic innovations.
   - Rapid expansion of production goods sector outpacing aggregate consumption.
   - Rising employment, real wage stabilization, and high marginal efficiency of capital.

2. **Phase 2: Recession and Plateau (Upper Turning Point)**
   - Saturation of foundational markets and overcapacity in primary capital goods.
   - Declining marginal returns on technological deployment leading to falling profit rates.
   - Capital divergence from productive equipment toward speculative financial assets.

3. **Phase 3: Depression and Downswing (Downside Realignment)**
   - Balance-sheet liquidation, structural debt deflation, and institutional stress.
   - Creative destruction eliminating obsolescent techno-economic paradigm infrastructure.
   - Incubation and gestation of basic radical innovations in low-cost environments.

4. **Phase 4: Recovery and Revival (Lower Turning Point)**
   - Modernization of depreciated fixed capital stock across fundamental networks.
   - Institutional realignment facilitating diffusion of new general-purpose technologies.
   - Rebuilding of productive credit channels and initial commercial deployment phase."""

if old_diagram_block in content:
    content = content.replace(old_diagram_block, new_diagram_block)
    print("Replaced ASCII cycle diagram in Concept successfully.")
else:
    print("Warning: old_diagram_block not found exactly, attempting regex replacement...")
    # fallback regex for the diagram block
    content = re.sub(r'```\s*\+[-+]+\+.*?PHASE 1:.*?PHASE 4:.*?\+[-+]+\+\s*```', new_diagram_block, content, flags=re.DOTALL)

# 2. Fix lines 135-144: concatenated heading and LaTeX frac escape (\nrac)
# Let's inspect or replace the problematic section around line 135
content = re.sub(r'\\nrac\{', r'\\frac{', content)
content = re.sub(r'### Capital Goods Inertia Models### Phase Transition Dynamics', 
                 r'### Capital Goods Inertia Models\n\n### Phase Transition Dynamics', content)

p.write_text(content, encoding="utf-8")
print("Concept/01_Structural_Mechanisms normalized and saved. Line count:", len(content.splitlines()))
