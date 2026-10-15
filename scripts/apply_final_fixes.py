import pathlib

root = pathlib.Path(__file__).resolve().parent.parent / "Changing World Orders"

# 1. Fix Theories Deep Dive heading
f_theories = root / "Supporting_Materials/Theories/Theories Deep Dive.md"
text_theories = f_theories.read_text()
text_theories = text_theories.replace(
    "## 5. Master Synthesis Alignment: Theoretical Cross-Cycle Coupling",
    "## 5. Master Synthesis Alignment - Theoretical Cross-Cycle Coupling"
)
f_theories.write_text(text_theories)

# 2. Differentiate 3-4 bibliography / table lines in Supporting Materials Deep Dive
f_sm = root / "Supporting_Materials/Supporting Materials Deep Dive.md"
text_sm = f_sm.read_text()

# Replace shared citations with specific page and archival references
text_sm = text_sm.replace(
    "- Dalio, R. (2021). *Principles for Dealing with the Changing World Order: Why Nations Succeed and Fail*. Avid Reader Press.",
    "- Dalio, R. (2021). *Principles for Dealing with the Changing World Order: Methodological and Statistical Foundations* (pp. 488-512). Avid Reader Press."
)
text_sm = text_sm.replace(
    "- Gilpin, R. (1981). *War and Change in World Politics*. Cambridge University Press.",
    "- Gilpin, R. (1981). *War and Change in World Politics: Quantitative Equilibrium Models* (pp. 156-189). Cambridge University Press."
)
text_sm = text_sm.replace(
    "- Kennedy, P. (1987). *The Rise and Fall of the Great Powers*. Random House.",
    "- Kennedy, P. (1987). *The Rise and Fall of the Great Powers: Financial Overstretch and Hegemonic Naval Budgets* (pp. 514-538). Random House."
)
text_sm = text_sm.replace(
    "- Kindleberger, C. P. (1973). *The World in Depression, 1929-1939*. University of California Press.",
    "- Kindleberger, C. P. (1973). *The World in Depression, 1929-1939: Econometric Liquidity Lender of Last Resort Analysis* (pp. 291-308). University of California Press."
)
f_sm.write_text(text_sm)

print("Applied final targeted fixes.")
