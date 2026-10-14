import pathlib
import re

p = pathlib.Path("4th Turning/Book/The_Fourth_Turning_Book_Details.md")
content = p.read_text(encoding="utf-8")

content = content.replace("### Key Research Takeaways", "### Key Research Takeaways — Formal Architecture of The Fourth Turning (1997)")
content = content.replace("### 1.2 Saecular Phase Mapping", "### 1.2 Saecular Phase Mapping Across Analytical Chapters")
content = content.replace("### Quantitative Indicator Matrix", "### Quantitative Structural Breakdown of Book Volumes and Themes")
content = content.replace("### 2.2 Sectoral & Institutional Impact Matrix", "### 2.2 Analytical Utility and Historiographical Impact Matrix")

# Replace ASCII box with markdown table
box_pattern = r"```\n\+[-+]+\n\|[^\n]+\n\+[-+]+\n\|[^\n]+\n\+[-+]+\n(?:\|[^\n]+\n)+\+[-+]+\n```"
new_table = """| Chapter Segment & Scope | Formal Theoretical Specification | Empirical Analytical Focus |
| :--- | :--- | :--- |
| Generational Horizon (Ch. 1-3) | 20-22 Year Lifecycle Epoch | Shifting cohort peer personality dynamics |
| Saecular Cycle Horizon (Ch. 4-6) | 80-90 Year Historical Arc | Recurrent Anglo-American social mood realignment |
| Four Turning Quadrants (Ch. 7-9) | High, Awakening, Unraveling, Crisis | Institutional strength vs. individualist expression |
| Climax Catalyst Window (Ch. 10-13) | 3-5 Year Critical Climax | Sovereign restructuring and institutional rebirth |"""

content = re.sub(box_pattern, new_table, content)
p.write_text(content, encoding="utf-8")
print("Successfully fixed The_Fourth_Turning_Book_Details.md")
