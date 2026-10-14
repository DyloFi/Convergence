import pathlib, re

files = [
    "Changing World Orders/Current_Geopolitical/01_US_China_Competition_and_Multipolarity.md",
    "Changing World Orders/Current_Geopolitical/Current Geopolitical Deep Dive.md",
    "Changing World Orders/Expert_Perspectives/Expert Perspectives Deep Dive.md",
    "Changing World Orders/Foundations/01_Big_Cycle_Framework_Ray_Dalio.md",
    "Changing World Orders/Future_Scenarios/Future Scenarios Deep Dive.md"
]

for fp in files:
    path = pathlib.Path(fp)
    text = path.read_text()
    
    # 1. 01_US_China_Competition_and_Multipolarity.md
    text = text.replace("## Theoretical Foundations: Hegemonic Transition and Structural Rivalry", "## Theoretical Foundations of Hegemonic Transition and Structural Rivalry")
    
    # 2. Current Geopolitical Deep Dive.md
    text = text.replace("### Table 1: Multi-Decadal Macroeconomic & Geopolitical Distribution Matrix", "### Table 1. Multi-Decadal Macroeconomic & Geopolitical Distribution Breakdown")
    text = text.replace("### 1. The Republic of India: Strategic Autonomy and Multi-Vector Engagement", "### 1. The Republic of India and Strategic Autonomy")
    text = text.replace("### Table 3: Sovereign Structural Resilience and Stress-Absorption Matrix", "### Table 3. Sovereign Structural Resilience and Stress-Absorption Audit")
    
    # 3. Expert Perspectives Deep Dive.md
    text = text.replace("### 2. Graham Allison: The Thucydides Trap Framework", "### 2. Graham Allison on the Thucydides Trap Dynamics")
    text = text.replace("### Table 3: Cross-Scholar Comparative Assessment & Projection Matrix", "### Table 3. Cross-Scholar Comparative Assessment & Projection Audit")
    
    # 4. Foundations/01_Big_Cycle_Framework_Ray_Dalio.md
    text = text.replace("## 4. Empirical Historical Application: The Three Precedent Cycles", "## 4. Empirical Historical Application across Three Precedent Cycles")
    
    # 5. Future Scenarios Deep Dive.md
    text = text.replace("### Table 1: Comprehensive Scenario Definition and Structural Boundary Matrix", "### Table 1. Comprehensive Scenario Definition and Structural Boundaries")
    text = text.replace("### Table 2: Quantitative Macroeconomic and Financial Stress-Test Matrix", "### Table 2. Quantitative Macroeconomic and Financial Stress-Test System")
    text = text.replace("### Table 3: Strategic Interaction Game-Theoretic Payoff Matrix", "### Table 3. Strategic Interaction Game-Theoretic Payoffs")
    text = text.replace("### Table 4: Institutional Asset Allocation Matrix", "### Table 4. Institutional Asset Allocation Audit")
    
    path.write_text(text)
    print(f"Updated headings in {fp}")

