import pathlib
import re

p = pathlib.Path("Kondratiev Waves/Concept/01_Structural_Mechanisms_of_Long_Waves.md")
content = p.read_text(encoding="utf-8")

# 1. Replace the ASCII box diagram that has |       | matching empty table header
old_diag = """```text
+-------------------+       +-------------------+
| Prosperity/Upswing | ----> | Recession/Plateau |
+-------------------+       +-------------------+
          |                           |
          v                           v
+-------------------+       +-------------------+
| Depression/Trough | <---- | Downswing/Decline |
+-------------------+       +-------------------+
```"""

new_diag = """*Phase Trajectory Architecture:*
1. **Prosperity / Upswing**: Accelerated fixed capital accumulation driven by foundational cluster commercialization and credit expansion.
2. **Recession / Secondary Plateau**: Capital overaccumulation, market saturation, and rising factor costs precipitating speculative diversion.
3. **Downswing / Decline**: Profit margin compression, creative destruction, debt liquidation, and defensive rationalization.
4. **Depression / Trough**: Deep institutional restructuring, radical price realignments, and incubation of next-generation techno-economic paradigms."""

if old_diag in content:
    content = content.replace(old_diag, new_diag)
else:
    # Try regex replacement if whitespace differed
    content = re.sub(r'```text\s*\+[-+]+\s+\+[-+]+\s*\|.*?\|.*?```', new_diag, content, flags=re.DOTALL)

# 2. Fix \nrac or unescaped frac
content = content.replace('\\nrac', '\\frac')

# 3. Ensure clean heading format before Section 5
content = re.sub(r'([^\n])\n(### 5\.\s+Multi-Scale)', r'\1\n\n\2', content)

p.write_text(content, encoding="utf-8")
print("Concept/01_Structural_Mechanisms_of_Long_Waves.md updated successfully")
