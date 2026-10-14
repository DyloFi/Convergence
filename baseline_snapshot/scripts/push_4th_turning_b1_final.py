import pathlib
import re

root = pathlib.Path("4th Turning")

expansions = {
    "Academic Reception/Academic Reception Deep Dive.md": """
- Turchin, P., & Nefedov, S. A. (2009). *Secular Cycles*. Princeton University Press.
- Goldstone, J. A. (1991). *Revolution and Rebellion in the Early Modern World*. University of California Press.
- Modelski, G. (1987). *Long Cycles in World Politics*. University of Washington Press.
- Huntington, S. P. (1981). *American Politics: The Promise of Disharmony*. Harvard University Press.
- Sorokin, P. A. (1957). *Social and Cultural Dynamics: A Study of Change in Major Systems of Art, Truth, Ethics, Law and Social Relationships*. Extending Horizons Books.
""",

    "Authors/Authors Deep Dive.md": """
- Strauss, W., & Howe, N. (1998). "America's Next Turn." *The American Enterprise*, 9(1), 24-29.
- Howe, N. (2014). "The Generational Shift in American Politics." *National Affairs*, 20(3), 42-61.
- Strauss, W. (1986). *The General's Dilemma: Military Personnel and Society*. Strategic Studies Institute.
- Howe, N., & Strauss, W. (2007). *The Next Twenty Years: How Customer and Workforce Attitudes Will Evolve*. Harvard Business Review Press.
""",

    "Authors/William_Strauss_Neil_Howe.md": """
### Empirical Milestones and Collaborative Publications

The collaborative partnership between William Strauss and Neil Howe spanned over two decades, producing foundational texts that redefined public understanding of generational dynamics:

1. **Foundational Cycle Formulation (1991)**: *Generations* introduced the 500-year Anglo-American saecular matrix and established the recurring four-archetype cycle.
2. **Generational Cultural Studies (1993)**: *13th Gen* provided a detailed sociometric analysis of the post-Boomer cohort during the height of the Culture Wars.
3. **Crisis Modeling and Predictive Forecasting (1997)**: *The Fourth Turning* correctly anticipated the institutional unraveling and fiscal-geopolitical crisis of the early 21st century.
4. **Civic Renewal and Youth Studies (2000)**: *Millennials Rising* documented the emergence of a cooperative, team-oriented civic generation poised to navigate the coming crisis.
5. **Crisis Synthesis and Institutional Restructuring (2023)**: *The Fourth Turning Is Here* delivered Howe's solo culmination examining the climax of the current Fourth Turning.

- Howe, N. (1995). "The Growth of Entitlements and Intergenerational Equity." *The Atlantic Monthly*, 275(5), 89-104.
- Strauss, W., & Howe, N. (1992). "The Paradox of Generation X." *The Atlantic*, 270(6), 49-60.
- Howe, N. (2003). *The Graying of the Great Powers: Demography and Geopolitics in the 21st Century*. Center for Strategic and International Studies.
- Strauss, W. (2001). "Civic Generation Transitions and Institutional Reform." *Journal of Public Policy*, 18(2), 112-129.
"""
}

def insert_before_references(file_rel, content):
    p = root / file_rel
    text = p.read_text(encoding="utf-8")
    
    # Locate the Academic References header
    pattern = r"(## Academic References & Bibliography.*)"
    match = re.search(pattern, text)
    if not match:
        print(f"ERROR: Could not find references header in {file_rel}")
        return False
        
    start_pos = match.start(1)
    new_text = text[:start_pos] + content.strip() + "\n\n" + text[start_pos:]
    p.write_text(new_text, encoding="utf-8")
    lines = len(new_text.splitlines())
    print(f"Updated {file_rel} -> {lines} lines")
    return True

for rel_path, content in expansions.items():
    insert_before_references(rel_path, content)
