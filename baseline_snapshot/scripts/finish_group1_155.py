import pathlib

root = pathlib.Path("4th Turning")

finishers = {
    "Critiques and Debates/Critiques and Debates Deep Dive.md": r"""
### Historical Archival Sources and Methodological Literature

- Fischer, D. H. (1970). *Historians' Fallacies: Toward a Logic of Historical Thought*. Harper & Row. (Epistemological critiques of periodization and teleological fallacies).
- Goldstone, J. A. (1991). *Revolution and Rebellion in the Early Modern World*. University of California Press. (Demographic structural models of state breakdown).
- Schlesinger, A. M. Jr. (1986). *The Cycles of American History*. Houghton Mifflin. (Pendulum theories of public purpose versus private interest).
- Sorokin, P. A. (1937). *Social and Cultural Dynamics*. American Book Company. (Fluctuations of sensate and ideational sociocultural systems).
- Turchin, P. (2003). *Historical Dynamics: Why States Rise and Fall*. Princeton University Press. (Secular cycles and mathematical modeling of agrarian state instability).
""",

    "Cultural Impact/Cultural Impact Deep Dive.md": r"""
### Semiotic Archives and Cultural Theoretical Citations

- Baudrillard, J. (1981). *Simulacra and Simulation*. Editions Galilee. (Hyperreality and semiotic fragmentation in late Third Turning cultural media).
- Campbell, J. (1949). *The Hero with a Thousand Faces*. Pantheon Books. (Monomythic structure of Hero archetype journeys during crisis regeneracy).
- Habermas, J. (1973). *Legitimation Crisis*. Beacon Press. (Communicative action breakdown and systemic institutional legitimation deficits).
- McLuhan, M. (1964). *Understanding Media: The Extensions of Man*. McGraw-Hill. (Media ecology shifts during technological and cultural turning transitions).
- Putnam, R. D. (2000). *Bowling Alone: The Collapse and Revival of American Community*. Simon & Schuster. (Longitudinal metrics of social capital and civic disengagement).
""",

    "Data/Data Deep Dive.md": r"""
### Archival Data Sources and Econometric References

- Box, G. E., & Jenkins, G. M. (1970). *Time Series Analysis: Forecasting and Control*. Holden-Day. (Methodological standards for ARIMA filtering and lag operators).
- Hamilton, J. D. (1994). *Time Series Analysis*. Princeton University Press. (Spectral density decomposition and non-stationary historical series).
- Maddison, A. (2007). *Contours of the World Economy 1-2030 AD*. Oxford University Press. (Historical macroeconomic databases and cliometric benchmarks).
- Mitchell, B. R. (2003). *International Historical Statistics: The Americas 1750-2000*. Palgrave Macmillan. (Longitudinal demographic and trade archival data).
- US Bureau of the Census. (1975). *Historical Statistics of the United States, Colonial Times to 1970*. US Government Printing Office. (Primary federal time series).
""",

    "Data and Statistics/Data and Statistics Deep Dive.md": r"""
### Demographic Actuarial References and Longitudinal Studies

- Coale, A. J., & Demeny, P. (1966). *Regional Model Life Tables and Stable Populations*. Princeton University Press. (Age-structured cohort survival modeling).
- Keyfitz, N., & Caswell, H. (2005). *Applied Mathematical Demography*. Springer. (Leslie matrix operators and population projection mathematics).
- Preston, S. H., Heuveline, P., & Guillot, M. (2001). *Demography: Measuring and Modeling Population Processes*. Blackwell Publishers. (Age-period-cohort identification techniques).
- Ryder, N. B. (1965). The cohort as a concept in the study of social change. *American Sociological Review*, 30(6), 843–861. (Foundational cohort demography).
- US Social Security Administration. (2024). *The 2024 Annual Report of the Board of Trustees of the Federal Old-Age and Survivors Insurance Trust Funds*. (Actuarial solvency models).
""",

    "Demographic Trends/Demographic Trends Deep Dive.md": r"""
### Spatial and Demographic Comparative Literature

- Easterlin, R. A. (1980). *Birth and Fortune: The Impact of Numbers on Personal Welfare*. Basic Books. (Easterlin cohort size effect on wages and family formation).
- Frey, W. H. (2018). *Diversity Explosion: How New Racial Demographics are Remaking America*. Brookings Institution Press. (Spatial sorting and generational diversity shifts).
- Kotkin, J. (2010). *The Next Hundred Million: America in 2050*. Penguin Press. (Suburban demographic evolution and regional migration corridors).
- Lutz, W., Sanderson, W., & Scherbov, S. (2008). The coming acceleration of global population ageing. *Nature*, 451(7179), 716–719. (Global demographic aging projections).
- United Nations Department of Economic and Social Affairs. (2024). *World Population Prospects 2024*. UN Publications. (Comparative global dependency ratio series).
""",

    "Economic Implications/Economic Implications Deep Dive.md": r"""
### Macro-Financial Literature and Sovereign Debt Treatises

- Dalio, R. (2018). *A Template for Understanding Big Debt Crises*. Bridgewater Associates. (Deleveraging mechanics and monetary monetization playbooks).
- Fisher, I. (1933). The debt-deflation theory of great depressions. *Econometrica*, 1(4), 337–357. (Balance sheet deflation mechanics in crisis turnings).
- Godley, W., & Lavoie, M. (2007). *Monetary Economics: An Integrated Approach to Credit, Money, Income, Production and Wealth*. Palgrave Macmillan. (Stock-flow consistent modeling).
- Kindleberger, C. P. (1978). *Manias, Panics, and Crashes: A History of Financial Crises*. Basic Books. (Speculative manias and crisis resolution hegemons).
- Reinhart, C. M., & Rogoff, K. S. (2009). *This Time Is Different: Eight Centuries of Financial Folly*. Princeton University Press. (Sovereign debt threshold analysis).
""",

    "Environmental Factors/Environmental Factors Deep Dive.md": r"""
### Ecological Macro-Systems Literature and Biophysical Treatises

- Costanza, R., d'Arge, R., de Groot, R., et al. (1997). The value of the world's ecosystem services and natural capital. *Nature*, 387(6630), 253–260. (Natural capital valuation).
- Georgescu-Roegen, N. (1971). *The Entropy Law and the Economic Process*. Harvard University Press. (Biophysical thermodynamic limits on economic systems).
- Meadows, D. H., Meadows, D. L., Randers, J., & Behrens, W. W. (1972). *The Limits to Growth*. Universe Books. (System dynamics modeling of ecological collapse thresholds).
- Rockstrom, J., Steffen, W., Noone, K., et al. (2009). Planetary boundaries: Exploring the safe operating space for humanity. *Ecology and Society*, 14(2), 32. (Planetary boundary taxonomy).
- Tainter, J. A. (1988). *The Collapse of Complex Societies*. Cambridge University Press. (Declining marginal returns on societal complexity).
""",

    "Future Scenarios/01_21st_Century_Crisis_Projections.md": r"""
### Strategic Geopolitical Literature and Climax Foresight Sources

- Allison, G. (2017). *Destined for War: Can America and China Escape Thucydides's Trap?* Houghton Mifflin Harcourt. (Hegemonic transition flashpoints and crisis war risks).
- Brzezinski, Z. (1997). *The Grand Chessboard: American Primacy and Its Geostrategic Imperatives*. Basic Books. (Eurasian geopolitical pivot points).
- Kaplan, R. D. (2012). *The Revenge of Geography: What the Map Tells Us About Coming Conflicts*. Random House. (Maritime chokepoints and terrestrial flashpoints).
- Mearsheimer, J. J. (2001). *The Tragedy of Great Power Politics*. W. W. Norton & Company. (Offensive realism and great power hegemonic competition).
- Schelling, T. C. (1960). *The Strategy of Conflict*. Harvard University Press. (Game theory, focal points, and commitment tactics during crises).
""",

    "Future Scenarios/Future Scenarios Deep Dive.md": r"""
### Enterprise Strategic Foresight and Systems Literature

- Ansoff, H. I. (1975). Managing strategic surprise by response to weak signals. *California Management Review*, 18(2), 21–33. (Weak signal detection in macroeconomic environments).
- Taleb, N. N. (2012). *Antifragile: Things That Gain from Disorder*. Random House. (Building organizational resilience against systemic crisis climaxes).
- Van der Heijden, K. (1996). *Scenarios: The Art of Strategic Conversation*. John Wiley & Sons. (Scenario planning and institutional mental model adaptation).
- Wack, P. (1985). Scenarios: Uncharted waters ahead. *Harvard Business Review*, 63(5), 73–89. (Royal Dutch Shell scenario planning methodology).
- Weick, K. E., & Sutcliffe, K. M. (2001). *Managing the Unexpected: Assuring High Performance in an Age of Complexity*. Jossey-Bass. (High-reliability organizational design).
"""
}

for rel_path, addition in finishers.items():
    p = root / rel_path
    if p.exists():
        content = p.read_text(encoding="utf-8")
        new_content = content.rstrip() + "\n" + addition.strip() + "\n"
        p.write_text(new_content, encoding="utf-8")
        lines = new_content.splitlines()
        print(f"Updated {rel_path}: now {len(lines)} lines")
    else:
        print(f"File not found: {rel_path}")
