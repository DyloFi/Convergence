import pathlib, re

root = pathlib.Path('/Users/dylanboyle/Desktop/Convergence')

# 1. Clean Master Synthesis
synth = root / 'Convergence_Master_Synthesis.md'
txt = synth.read_text(encoding='utf-8')

# Fix line 103
txt = txt.replace(r'$$\f\frac{dI}{dt} = \alpha \cdot I(t)^\gamma \cdot C(t)^\beta$$', r'$$\frac{dI}{dt} = \alpha \cdot I(t)^\gamma \cdot C(t)^\beta$$')

# Fix lines 111-115
txt = txt.replace(r'((t) = I_0 e^{\alpha t}$)', r'($I(t) = I_0 e^{\alpha t}$)')
txt = re.sub(
    r'at \^\* = t_0 \+ \\+f?\\+frac\{I_0\^\{1-\\gamma\}\}\{\\alpha\(\\gamma - 1\)\}',
    r'at $t^* = t_0 + \\frac{I_0^{1-\\gamma}}{\\alpha(\\gamma - 1)}$',
    txt
)

# Section 4.1 in Master Synthesis
sec4_old = """1. **Algorithmic Cognitive Acceleration**:
41166\\f\\frac{dA}{dt} = \\kappa_A \\cdot A(t)^\\theta \\cdot \\left(\\f\\frac{E(t)}{E_0}\\right)^\\mu41166
Where (t)$ is algorithmic efficiency, (t)$ is dedicated compute energy (Gigawatts), and $\\theta > 1$ represents recursive algorithmic self-optimization. In the idealized model where $\\theta > 1$ and energy scaling remains unconstrained, this formulation produces finite-time divergence (^* = t_0 + \\f\\frac{A_0^{1-\\theta}}{\\kappa_A(\\theta-1)}$). In physical systems, however, thermal dissipation bounds (Landauer limit: {\\min} = k_B T \\ln 2$), von Neumann memory bandwidth walls, and grid interconnect latencies enforce logistic saturation.

2. **Societal Institutional Stress Index ({\\text{inst}}$)**:
41166\\f\\frac{dA}{dt} = \\kappa_A \\cdot A(t)^\\theta \\cdot \\left(\\f\\frac{E(t)}{E_0}\\right)^\\mu41166
Institutional stress accelerates proportionally to the rate of technological change (labor displacement and information epistemic fragmentation) and sovereign debt saturation, attenuated only by governance capacity $\\text{Cap}_{gov}(t)$.

3. **Macroeconomic Fragility Threshold**:
When {\\text{inst}}(t) > S_{\\text{crit}}$, formal institutional equilibrium becomes unstable, transitioning society from evolutionary adaptation to structural Fourth Turning restructuring and debt reorganization."""

sec4_new = r"""1. **Algorithmic Cognitive Acceleration**:
$$\frac{dA}{dt} = \kappa_A \cdot A(t)^\theta \cdot \left(\frac{E(t)}{E_0}\right)^\mu$$
Where $A(t)$ is algorithmic efficiency, $E(t)$ is dedicated compute energy (Gigawatts), and $\theta > 1$ represents recursive algorithmic self-optimization. In the idealized model where $\theta > 1$ and energy scaling remains unconstrained, this formulation produces finite-time divergence ($t^* = t_0 + \frac{A_0^{1-\theta}}{\kappa_A(\theta-1)}$). In physical systems, however, thermal dissipation bounds (Landauer limit: $E_{\min} = k_B T \ln 2$), von Neumann memory bandwidth walls, and grid interconnect latencies enforce logistic saturation.

2. **Societal Institutional Stress Index ($S_{\text{inst}}$)**:
$$\frac{dS_{\text{inst}}}{dt} = \lambda_1 \cdot \left|\frac{dA}{dt}\right| + \lambda_2 \cdot \left(\frac{\text{Debt}(t)}{\text{GDP}(t)}\right) - \delta \cdot \text{Cap}_{gov}(t)$$
Institutional stress accelerates proportionally to the rate of technological change (labor displacement and information epistemic fragmentation) and sovereign debt saturation, attenuated only by governance capacity $\text{Cap}_{gov}(t)$.

3. **Macroeconomic Fragility Threshold**:
When $S_{\text{inst}}(t) > S_{\text{crit}}$, formal institutional equilibrium becomes unstable, transitioning society from evolutionary adaptation to structural Fourth Turning restructuring and debt reorganization."""

if sec4_old in txt:
    txt = txt.replace(sec4_old, sec4_new)
    print("Replaced Section 4.1 in Master Synthesis successfully.")
else:
    # regex fallback
    txt = re.sub(
        r'1\. \*\*Algorithmic Cognitive Acceleration\*\*:\s*\d*\\+f?\\+frac\{dA\}\{dt\}.*?transitioning society from evolutionary adaptation to structural Fourth Turning restructuring and debt reorganization\.',
        sec4_new,
        txt,
        flags=re.DOTALL
    )
    print("Replaced Section 4.1 with regex.")

synth.write_text(txt, encoding='utf-8')

# 2. Fix all \f\frac, \x0c\frac, and \f\frac across all active markdown files
frac_cleaned = 0
for p in root.rglob('*.md'):
    if any(x in p.parts for x in ['.git', 'baseline_snapshot', 'audit']) or p.name.endswith('.bak.md'):
        continue
    txt = p.read_text(encoding='utf-8')
    orig = txt
    
    # Strip form feed character
    txt = txt.replace('\x0c', '')
    # Replace \f\frac with \frac
    txt = re.sub(r'\\f\\frac\{', r'\\frac{', txt)
    # Replace \f\frac without double backslash if literal
    txt = txt.replace(r'\f\frac{', r'\frac{')
    
    # Remove any stray PIDs (36646, 36689, 41166) in math expressions
    for pid in ['36646', '36689', '41166']:
        txt = re.sub(rf'{pid}\s*\\frac', r'$$\\frac', txt)
        txt = re.sub(rf'\\mu\s*{pid}', r'\\mu$$', txt)
        txt = re.sub(rf'{pid}', '', txt) if pid in ['36646', '36689', '41166'] and ('\\frac' in txt or 'dA/dt' in txt) else txt

    if txt != orig:
        p.write_text(txt, encoding='utf-8')
        frac_cleaned += 1

print(f'Cleaned \\f\\frac and PIDs across {frac_cleaned} files.')
