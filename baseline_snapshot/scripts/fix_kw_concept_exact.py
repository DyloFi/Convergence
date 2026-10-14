import pathlib

p = pathlib.Path("Kondratiev Waves/Concept/01_Structural_Mechanisms_of_Long_Waves.md")
lines = p.read_text(encoding="utf-8").splitlines()

# 1. Replace the ASCII box diagram around lines 77-95
# Find start: "```text" or "STRUCTURAL PHASES OF THE LONG WAVE CYCLE"
start_idx = None
end_idx = None
for i, l in enumerate(lines):
    if "STRUCTURAL PHASES OF THE LONG WAVE CYCLE" in l:
        start_idx = i - 1 if i > 0 and "```" in lines[i-1] else i
    if start_idx is not None and i > start_idx and "```" in l:
        end_idx = i + 1
        break

new_diagram_text = """### Quantitative Architecture of Long Wave Structural Phases

The 50-to-60 year Kondratiev cycle unfolds across four distinct structural macroeconomic phases characterized by capital formation, depreciation dynamics, and real return differentials:

1. **Phase 1: Prosperity and Deployment Wave (Years 0 to 25)**
   - Initial conditions: New core technology paradigm diffusion (steam, rail, electricity, petrochemistry, microelectronics).
   - Capital behavior: Massive long-wave capital investment ($K_L$), surging fixed asset accumulation, and elevated marginal product of capital ($r_K > r^*$).
   - Macro indicators: Robust real output growth ($g > 3.5\\%$), moderate non-monetary disinflation, rising real wages, and rapid infrastructure expansion.

2. **Phase 2: Prosperity Crest and Saturation Plateau (Years 25 to 35)**
   - Initial conditions: Diminishing marginal returns on pervasive paradigm infrastructure; market saturation of core manufacturing products.
   - Capital behavior: Excess capacity emerges in capital goods sectors; capital redirection toward financial speculative assets.
   - Macro indicators: Speculative asset price bubbles, plateauing productivity growth ($g \\sim 2.0\\%$), tightening credit spreads, and latent debt fragility.

3. **Phase 3: Structural Crisis and Downswing Recessional Adjustment (Years 35 to 48)**
   - Initial conditions: Financial market rupture, rapid debt deflation, and institutional regime friction.
   - Capital behavior: Widespread capital liquidation, systemic write-downs of obsolete fixed physical assets ($D_L$), and structural unemployment.
   - Macro indicators: Severe economic contraction, structural deflation, trade protectionism, geopolitical tension, and falling interest rates ($r \\to 0$).

4. **Phase 4: Depression Valley and Latent Incubation (Years 48 to 60)**
   - Initial conditions: Exhaustion of debt overhang; radical technological breakthroughs incubating in laboratory and pilot scales.
   - Capital behavior: Idle liquid balances seeking yield; formation of next-generation techno-economic paradigm capital clusters.
   - Macro indicators: Low interest rate equilibrium, base stabilization, institutional restructuring, and emergence of foundational innovations."""

if start_idx is not None and end_idx is not None:
    lines = lines[:start_idx] + new_diagram_text.splitlines() + lines[end_idx:]

text = "\n".join(lines)

# 2. Fix concatenated header and split LaTeX fraction
text = text.replace("## Phase Transitions in Long-Wave Structural Regimes### Dynamic Multi-Scale Wavelet Decomposition", "## Phase Transitions in Long-Wave Structural Regimes\n\n### Dynamic Multi-Scale Wavelet Decomposition")
text = text.replace("\\nrac{1}{\\lambda}", "\\frac{1}{\\lambda}")
text = text.replace("W(s, \\tau) = \\nrac", "W(s, \\tau) = \\frac")

p.write_text(text, encoding="utf-8")
print(f"Concept/01_Structural_Mechanisms updated: {len(p.read_text().splitlines())} lines")
