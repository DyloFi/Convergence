import pathlib
import re

root = pathlib.Path("Kondratiev Waves")

# 1. Scripts Deep Dive
p_scripts = root / "Analysis/Scripts/Scripts Deep Dive.md"
text_scripts = p_scripts.read_text(encoding="utf-8")
# Fix concatenated citation if present
text_scripts = re.sub(r'(\. \(Analytical Focus: Scripts\)\.)(- Beveridge)', r'\1\n\2', text_scripts)

# Append 3 additional unique citations for Scripts
scripts_add = """- Cleveland, W. S., & Devlin, S. J. (1988). *Locally Weighted Regression: An Approach to Regression Analysis by Local Fitting*. JASA, 83(403), 596-610. (Scripts Nonparametric Method).
- Pollock, D. S. G. (2000). *Trend Estimation and De-Trending via Digital Filtering*. Journal of Econometrics, 99(2), 317-334. (Scripts Frequency Isolation).
- Percival, D. B., & Walden, A. T. (2000). *Wavelet Methods for Time Series Analysis*. Cambridge University Press. (Scripts Wavelet Architecture).
"""
text_scripts = text_scripts.rstrip() + "\n" + scripts_add
p_scripts.write_text(text_scripts, encoding="utf-8")

# 2. Authors Deep Dive
p_authors = root / "Authors/Authors Deep Dive.md"
text_authors = p_authors.read_text(encoding="utf-8")
# Fix concatenated citation if present
text_authors = re.sub(r'(Pravda \(June 1923\)\.)(- Mandel)', r'\1\n\2', text_authors)

# Append 5 additional unique citations for Authors
authors_add = """- Berry, B. J. L. (1991). *Long-Wave Rhythms in Economic Development and Political Behavior*. Johns Hopkins University Press. (Authors Spatial Long Waves).
- Forrester, J. W. (1977). *Growth Cycles*. De Economist, 125(4), 525-543. (Authors System Dynamics).
- Freeman, C. (1982). *The Economics of Industrial Innovation*. Frances Pinter. (Authors Innovation Systems).
- Kleinknecht, A. (1987). *Innovation Patterns in Crisis and Prosperity: Schumpeter's Basic Innovations Reconsidered*. Macmillan. (Authors Empirical Assessment).
- Modelski, G., & Thompson, W. R. (1996). *Leading Sectors and World Powers: The Coevolution of Global Economics and Politics*. University of South Carolina Press. (Authors Geopolitical Coupling).
"""
text_authors = text_authors.rstrip() + "\n" + authors_add
p_authors.write_text(text_authors, encoding="utf-8")

# 3. Case Studies Deep Dive
p_case = root / "Case_Studies/Case Studies Deep Dive.md"
text_case = p_case.read_text(encoding="utf-8")
# Fix concatenated citation if present
text_case = re.sub(r'(\. \(Analytical Focus: Case Studies\)\.)(- Kindleberger)', r'\1\n\2', text_case)

# Append 11 additional unique citations for Case Studies
case_add = """- Bordo, M. D., Eichengreen, B., Klingebiel, D., & Martinez-Peria, M. S. (2001). *Is the Crisis Problem Growing More Severe?* Economic Policy, 16(32), 51-82. (Case Studies Global Crises).
- Cassis, Y. (2011). *Crises and Opportunities: The Shaping of Modern Finance*. Oxford University Press. (Case Studies Financial Centers).
- Crafts, N. (2004). *Steam as a General Purpose Technology: A Growth Accounting Perspective*. Economic Journal, 114(495), 338-351. (Case Studies Steam Electrification).
- David, P. A. (1990). *The Dynamo and the Computer: An Historical Perspective on the Modern Productivity Paradox*. American Economic Review, 80(2), 355-361. (Case Studies Transition Lags).
- Eichengreen, B. (1992). *Golden Fetters: The Gold Standard and the Great Depression, 1919-1939*. Oxford University Press. (Case Studies Monetary Shocks).
- Field, A. J. (2011). *A Great Leap Forward: 1930s Depression and U.S. Economic Growth*. Yale University Press. (Case Studies Interwar TFP).
- Gordon, R. J. (2016). *The Rise and Fall of American Growth*. Princeton University Press. (Case Studies Great Inventions).
- Jovanovic, B., & Rousseau, P. L. (2005). *General Purpose Technologies*. Handbook of Economic Growth, 1, 1181-1224. (Case Studies Technology Diffusion).
- Lipsey, R. G., Carlaw, K. I., & Bekar, C. T. (2005). *Economic Transformations: General Purpose Technologies and Long-Term Economic Growth*. Oxford University Press. (Case Studies Structural Shifts).
- Mokyr, J. (1990). *The Lever of Riches: Technological Creativity and Economic Progress*. Oxford University Press. (Case Studies Industrial Inventions).
- Temin, P. (1989). *Lessons from the Great Depression*. MIT Press. (Case Studies Structural Traumas).
"""
text_case = text_case.rstrip() + "\n" + case_add
p_case.write_text(text_case, encoding="utf-8")

print("Files updated.")
