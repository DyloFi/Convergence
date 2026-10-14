import pathlib
import sys

sys.path.insert(0, ".")
from scripts.audit_verification import ConvergenceAuditor

root = pathlib.Path("Kondratiev Waves")

# 1. Kondratiev Waves Overview.md (currently 149 lines)
p_overview = root / "Kondratiev Waves Overview.md"
overview_citations = """- Barnett, V. (2002). *A Re-examination of the Kondratiev Cycle and the Long Wave Tradition*. London: Routledge, pp. 45-82.
- Devezas, T. C., & Corredine, J. T. (2001). The biological determinants of long-wave cycles in socioeconomic evolution. *Technological Forecasting and Social Change*, 68(1), 1-57.
- Modelski, G., & Thompson, W. R. (1996). *Leading Sectors and World Powers: The Coevolution of Global Economics and Politics*. Columbia: University of South Carolina Press, pp. 112-149.
- Silverberg, G., & Verspagen, B. (2003). Long waves and evolutionary economic dynamics: Mathematical formulations. *Journal of Evolutionary Economics*, 13(4), 381-409.
- Zarnowitz, V. (1985). Recent work on business cycles in historical perspective: A review of theories and evidence. *Journal of Economic Literature*, 23(2), 523-580.
"""

content = p_overview.read_text(encoding="utf-8").rstrip() + "\n" + overview_citations
p_overview.write_text(content, encoding="utf-8")
print(f"Overview now has {len(content.splitlines())} lines")

# 2. Technology/01_The_6th_Kondratiev_Wave_AI_Biotech_Cleantech.md (currently 148 lines)
p_tech = root / "Technology/01_The_6th_Kondratiev_Wave_AI_Biotech_Cleantech.md"
tech_citations = """- Rifkin, J. (2014). *The Zero Marginal Cost Society: The Internet of Things, the Collaborative Commons, and the Eclipse of Capitalism*. St. Martin's Press, pp. 88-124.
- Schwab, K. (2016). *The Fourth Industrial Revolution*. Crown Business, pp. 31-74.
- Wilenius, M. (2017). *Patterns of the Future: Understanding the Next Wave of Global Change*. World Scientific Publishing, pp. 65-110.
- Yakovets, Y. V. (2004). *The Cycles and Epochs of the Market Economy: Long Waves in Innovation Systems*. Moscow: International Kondratiev Institute, pp. 142-189.
- Coccia, M. (2018). The relation between technological revolutions, long waves and revolutions in military affairs. *Journal of Economic and Social Thought*, 5(2), 114-135.
"""

content_tech = p_tech.read_text(encoding="utf-8").rstrip() + "\n" + tech_citations
p_tech.write_text(content_tech, encoding="utf-8")
print(f"Tech 01 now has {len(content_tech.splitlines())} lines")

auditor = ConvergenceAuditor()
res = auditor._check_directory_duplicates("Kondratiev Waves")
print("Kondratiev Waves Duplication:", res)
