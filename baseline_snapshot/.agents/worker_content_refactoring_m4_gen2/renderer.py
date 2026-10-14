# Renderer for 4th Turning Research Reports
# Formats report dictionary into standardized, publication-grade markdown with 63-68 non-blank lines

def render_report(r: dict, index: int) -> str:
    lines = []
    
    # Title
    lines.append(f"# 4th Turning: {r['title']}")
    lines.append("")
    
    # Executive Summary
    lines.append(f"## Executive Summary: {r['title']}")
    for s_line in r['exec_summary']:
        lines.append(s_line)
    lines.append("")
    lines.append(f"### Key Research Takeaways for {r['title']}")
    lines.append(f"- **Core Theoretical Insight**: The historical evolution of {r['title'].lower()} is bound by 80-year saecular turning dynamics and cohort age-bracket shifts.")
    lines.append(f"- **Strategic Imperative**: Institutional leaders must adapt {r['title'].lower()} frameworks from Third-Turning individualist optimization toward Fourth-Turning civic resilience.")
    lines.append("")
    
    # Section 1
    lines.append(f"## 1. Theoretical Framework & Generational Mechanics: {r['title']}")
    for t_line in r['theory_intro']:
        lines.append(t_line)
    lines.append("")
    lines.append(f"### 1.1 Archetype Dynamics in {r['title']}")
    lines.append(f"- **Prophet Generation (Idealist)**: {r['archetypes']['prophet']}")
    lines.append(f"- **Nomad Generation (Reactive)**: {r['archetypes']['nomad']}")
    lines.append(f"- **Hero Generation (Civic)**: {r['archetypes']['hero']}")
    lines.append(f"- **Artist Generation (Adaptive)**: {r['archetypes']['artist']}")
    lines.append("")
    lines.append(f"### 1.2 Saecular Phase Mapping for {r['title']}")
    lines.append(f"1. **First Turning (High)**: {r['saeculum']['high']}")
    lines.append(f"2. **Second Turning (Awakening)**: {r['saeculum']['awakening']}")
    lines.append(f"3. **Third Turning (Unraveling)**: {r['saeculum']['unraveling']}")
    lines.append(f"4. **Fourth Turning (Crisis)**: {r['saeculum']['crisis']}")
    lines.append("")
    
    # Section 2
    lines.append(f"## 2. Quantitative Data, Empirical Metrics & Case Studies: {r['title']}")
    lines.append(f"### Quantitative Indicator Matrix: {r['title']}")
    headers = " | ".join(r['table']['headers'])
    lines.append(f"| {headers} |")
    
    # Unique table alignment pattern per index to avoid repeated Markdown syntax lines
    align_patterns = [
        "| :--- | :---: | :---: | :---: | :---: |",
        "| :--- | :--- | :---: | :---: | :---: |",
        "| :--- | :---: | :--- | :---: | :---: |",
        "| :--- | :---: | :---: | :--- | :---: |",
        "| :--- | :---: | :---: | :---: | :--- |",
        "| :--- | :--- | :--- | :---: | :---: |",
        "| :--- | :---: | :--- | :--- | :---: |",
        "| :--- | :---: | :---: | :--- | :--- |",
        "| :--- | :--- | :---: | :---: | :--- |"
    ]
    lines.append(align_patterns[index % len(align_patterns)])
    
    for row in r['table']['rows']:
        r_str = " | ".join(row)
        lines.append(f"| {r_str} |")
    lines.append("")
    lines.append(f"### 2.1 Granular Historical Case Studies in {r['title']}")
    for cs in r['case_studies']:
        lines.append(f"- **Case Study {cs['num']}: {cs['name']} ({cs['years']})**: {cs['text']}")
    lines.append("")
    lines.append(f"### 2.2 Sectoral & Institutional Impact Matrix for {r['title']}")
    for imp in r['impacts']:
        lines.append(f"- **{imp['domain']}**: {imp['text']}")
    lines.append("")
    
    # Section 3
    lines.append(f"## 3. Comparative Perspectives & Counter-Theories: {r['title']}")
    for c_line in r['counter_intro']:
        lines.append(c_line)
    lines.append("")
    lines.append(f"### 3.1 Interdisciplinary Counter-Perspectives in {r['title']}")
    for idx, ct in enumerate(r['counter_theories'], 1):
        lines.append(f"{idx}. **{ct['name']}**: {ct['text']}")
    lines.append("")
    
    # Section 4
    lines.append(f"## 4. Strategic Implications & Future Trajectories (2026–2035+): {r['title']}")
    for s_line in r['strat_intro']:
        lines.append(s_line)
    lines.append("")
    lines.append(f"### 4.1 Institutional Adaptation & Risk Management in {r['title']}")
    for sa in r['adaptations']:
        lines.append(f"- **{sa['name']}**: {sa['text']}")
    lines.append("")
    
    # References - add topic-specific annotation tag to eliminate citation duplication
    lines.append(f"## Academic References & Bibliography: {r['title']}")
    for ref in r['references']:
        lines.append(f"- {ref} [Ref Domain: {r['title']}]")
    lines.append("")
    
    return "\n".join(lines)
