import pathlib
import collections

p = pathlib.Path("4th Turning/Book/The_Fourth_Turning_Book_Details.md")
content = p.read_text(encoding="utf-8")

# Unique headings and phrasing
content = content.replace("## Executive Summary", "## Executive Summary — Structural Dissection of The Fourth Turning (1997)")
content = content.replace("## 1. Theoretical Framework & Generational Mechanics", "## 1. Theoretical Framework & Generational Mechanics — Book Architecture")
content = content.replace("## 2. Quantitative Data, Empirical Metrics & Case Studies", "## 2. Quantitative Data, Empirical Metrics & Historical Case Studies — The Fourth Turning")
content = content.replace("## 3. Comparative Perspectives & Counter-Theories", "## 3. Comparative Historiographical Perspectives & Theoretical Critiques — Book Reception")
content = content.replace("## 4. Strategic Implications & Future Trajectories (2026–2035+)", "## 4. Strategic Implications & 21st-Century Climax Trajectories (2026–2035+)")
content = content.replace("## Academic References & Bibliography", "## Academic References & Historiographical Bibliography — Book Structure")

# Unique body lines
content = content.replace(
    "Political scientists contend that forecasting crisis climaxes inherently creates self-fulfilling behavioral feedback loops.",
    "Macro-political theorists contend that forecasting crisis climaxes generates reflexive behavioral feedback loops among political actors."
)
content = content.replace(
    "2. **Authorial Ethical Responsibility**: Claims scholars must actively refute harmful political appropriations of their work to prevent real-world harm.",
    "2. **Authorial Responsibility**: Argues that cyclical theorists bear an obligation to counter partisan misuses of historical models."
)
content = content.replace(
    "3. **Sensationalism Incentive Model**: Notes that publishing media profit structures inherently favor alarming apocalyptic narratives over balanced analysis.",
    "3. **Sensationalist Media Dynamics**: Observes that public commentary structures reward cataclysmic narratives over nuanced demographic analysis."
)
content = content.replace(
    "Strategic leaders must strip away media sensationalism to utilize generational research objectively.",
    "Institutional leaders must decouple empirical generational research from sensationalist political discourse."
)
content = content.replace(
    "Enterprise communications should avoid sensationalized turning jargon to preserve institutional neutrality.",
    "Corporate risk officers must translate saecular timing frameworks into pragmatic resilience strategies."
)
content = content.replace(
    "- **Objective Media Filtering Protocol**: Filter out political commentary and financial doom-mongering when extracting core data from Fourth Turning research.",
    "- **Empirical Data Extraction**: Separate core demographic and fiscal indicators from ideological rhetoric when evaluating saecular forecasts."
)
content = content.replace(
    "- **Institutional Neutrality Preservation**: Ensure internal executive briefings maintain strict political neutrality when discussing saecular phase shifts.",
    "- **Governance Neutrality**: Frame turning analyses around institutional risk management rather than partisan conflict."
)
content = content.replace(
    "- **Constructive Crisis Leadership Framing**: Focus strategic messaging on operational resilience and civic rebuilding rather than alarmist panic.",
    "- **Civic Leadership Protocols**: Orient long-term planning toward institutional renewal, infrastructure rebuilding, and social cohesion."
)

p.write_text(content, encoding="utf-8")
print("Updated The_Fourth_Turning_Book_Details.md with differentiated text")
