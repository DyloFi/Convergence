import pathlib

root = pathlib.Path(__file__).resolve().parent.parent
cwo = root / 'Changing World Orders/Foundations/02_Empirical_Macro_Debt_Reserves_and_Institutional_Decay.md'
txt = cwo.read_text(encoding='utf-8')

clean_section = """### US Sovereign Debt, Revenue, and Net Interest Carrying Costs (1960–2026+ CBO Data)

| Fiscal Year | Gross Federal Debt ($B) | Publicly Held Debt (% of GDP) | Total Federal Revenues ($B) | Net Interest Outlays ($B) | Net Interest as % of Federal Revenue (%) | Net Interest (% of GDP) | Average Effective Interest Rate (%) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1960** | $286B | 46.1% | $92.5B | $6.9B | 7.5% | 1.3% | 3.2% |
| **1970** | $371B | 28.0% | $192.8B | $14.4B | 7.5% | 1.4% | 5.3% |
| **1980** | $908B | 25.5% | $517.1B | $52.5B | 10.2% | 1.9% | 8.9% |
| **1990** | $3,233B | 40.8% | $1,032B | $184.3B | 17.9% | 3.1% | 8.4% |
| **1995** | $4,974B | 47.7% | $1,351B | $232.2B | 17.2% | 3.1% | 6.8% |
| **2000** | $5,674B | 34.7% | $2,025B | $223.0B | 11.0% | 2.2% | 6.4% |
| **2005** | $7,933B | 35.6% | $2,154B | $184.0B | 8.5% | 1.4% | 4.3% |
| **2010** | $13,562B | 60.6% | $2,163B | $196.9B | 9.1% | 1.3% | 2.4% |
| **2015** | $18,151B | 72.4% | $3,250B | $223.2B | 6.9% | 1.2% | 1.7% |
| **2020** | $27,748B | 99.7% | $3,420B | $345.5B | 10.1% | 1.6% | 1.6% |
| **2022** | $30,929B | 97.0% | $4,896B | $475.1B | 9.7% | 1.9% | 2.1% |
| **2024** | $35,465B | 122.4% | $4,919B | $882.0B | 17.9% | 3.1% | 3.3% |
| **2025 (Est.)** | $37,120B | 123.8% | $5,120B | $995.0B | 19.4% | 3.3% | 3.4% |
| **2026 (Est.)** | $38,980B | 125.2% | $5,310B | $1,110.0B | 20.9% | 3.5% | 3.5% |
| **2030 (Proj.)** | $46,500B | 131.5% | $6,150B | $1,420.0B | 23.1% | 3.9% | 3.6% |"""

start_needle = '### US Sovereign Debt, Revenue, and Net Interest Carrying Costs (1960–2026+ CBO Data)'
end_needle = '### The Compound Interest Trap and Fiscal Dominance'

idx_start = txt.find(start_needle)
idx_end = txt.find(end_needle)

if idx_start != -1 and idx_end != -1:
    txt = txt[:idx_start] + clean_section + '\n\n' + txt[idx_end:]
    cwo.write_text(txt, encoding='utf-8')
    print('Cleanly replaced CWO debt section.')
else:
    print('Could not find start or end needle!')
