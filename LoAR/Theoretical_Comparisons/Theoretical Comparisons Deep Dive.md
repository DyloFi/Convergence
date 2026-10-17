# LoAR: Kurzweil Compared With Growth Economics

*Rewritten from the evidence up in Step 13 (2026-10-17). The previous version, padded with ASCII boxes and a stylised "matrix" of theories, is preserved at `archive/step13_originals/LoAR/Theoretical_Comparisons/Theoretical Comparisons Deep Dive.md.orig`.*

## Executive Summary

Kurzweil's Law of Accelerating Returns and mainstream growth economics agree that technology drives long-run growth. They disagree about the shape of that growth. Solow's 1957 growth accounting attributed 87.5% of the doubling in US output per hour between 1909 and 1949 to "technical change". Modern endogenous-growth models (Romer 1990; Jones 1995) make technical change depend on research effort, which implies steady, not accelerating, growth unless research inputs keep rising. Kurzweil predicts double-exponential acceleration. The measured record does not show it. US nonfarm labour productivity grew 2.8% a year in 1948-1973, 1.4% in 1973-1995, 3.1% in 1995-2004 during the IT boom, 1.5% in 2004-2019 and 2.2% in 2019-2025. That is a pattern of surges and slowdowns around a fairly stable average, much as Solow noticed in 1987 when he said "You can see the computer age everywhere but in the productivity statistics." Aghion, Jones and Jones (2017) give a reason why fast progress in some sectors need not raise aggregate growth: Baumol's cost disease. Growth may be held back by "what is essential and yet hard to improve." Comparing the frameworks helps locate the gap: LoAR describes inputs (computation per dollar), and growth theory explains why those inputs have not yet produced accelerating output.

## Question and scope

**Question.** How do Kurzweil's LoAR, neoclassical growth accounting (Solow) and endogenous growth theory (Romer, Jones) differ in what they predict for the link between technology and economic growth, and which predictions does the US productivity record support?

**Scope.** Three frameworks and one test: the long-run US labour-productivity series (BLS, via FRED), 1948-2025. Perez's techno-economic paradigms are covered in the Kondratiev Waves pillar and are mentioned here only for comparison. Not covered: country comparisons and sector-level studies.

## Methodology

1. State each framework's core mechanism and what it predicts for aggregate growth over decades.
2. Compute compound annual growth of US nonfarm business output per hour between annual averages for standard sub-periods (`scripts/step13_productivity_check.py`; the data file is under `data/`).
3. Ask which framework's prediction the record matches.

## Empirical Evidence

### Core mechanisms compared

| Framework | Engine of growth | Predicted shape of long-run growth |
| :--- | :--- | :--- |
| Kurzweil, LoAR (2001) | Each technology generation is used to build the next; returns feed back | Double-exponential: "exponential growth in the rate of exponential growth" |
| Solow growth accounting (1957) | Capital per worker plus an unexplained "technical change" residual | Steady growth from technical change, which the model takes as given |
| Romer (1990) | Deliberate investment in new ideas, which are non-rival | Sustained growth that rises with the size of the research sector |
| Jones (1995) | Ideas, with research productivity falling as ideas get harder to find | Steady growth tied to growth in research inputs (ultimately population), not to their level |
| Aghion, Jones & Jones (2017) | AI as the latest stage of automation, with Baumol's cost disease | Growth may be held back by essential sectors that are hard to automate; "singularities" only under strong conditions |

### What growth accounting found

Solow's 1957 paper concluded that from 1909 to 1949 "gross output per man hour doubled over the interval, with 87½ per cent of the increase attributable to technical change and the remaining 12½ per cent to increased use of capital." He also found the shift in the production function ran at about 1% a year in the first half of the period and 2% in the second. Technology dominates growth. That is common ground with Kurzweil.

### What the productivity record shows

| Period | Output per hour, compound annual growth (US nonfarm business) |
| :--- | :---: |
| 1948-1973 | 2.8% |
| 1973-1995 | 1.4% |
| 1995-2004 | 3.1% |
| 2004-2019 | 1.5% |
| 2019-2025 | 2.2% |

Source: BLS series OPHNFB via FRED, downloaded 2026-10-17; calculations in `scripts/step13_productivity_check.py`.

Over a period in which computing price-performance improved by many orders of magnitude, US productivity growth did not trend upwards. It rose with the 1995-2004 IT boom, fell back, and has picked up since 2019. Solow's 1987 quip about the computer age and the productivity statistics led Brynjolfsson (1993) to name the "productivity paradox". The paradox has eased at times but has never turned into acceleration.

### Which predictions hold

- **LoAR's double-exponential prediction for the economy:** not supported over 1948-2025.
- **Steady growth driven by ideas (Romer/Jones):** broadly consistent with growth fluctuating around a stable average. Jones's prediction that growth depends on growing research inputs fits Bloom et al.'s (2020) finding that research effort keeps rising while research productivity falls (see `Critiques/Critiques Deep Dive.md`).
- **Bottlenecks (Aghion-Jones-Jones):** consistent with fast progress in computing coexisting with ordinary aggregate growth.

## Competing views and counterarguments

- **Kurzweil's defence.** LoAR is mainly about information technologies' price-performance, which has grown exponentially. On this view the economy-wide effect arrives later, when information technology absorbs other sectors. The 1995-2004 surge and the post-2019 pickup could be early signs. A sceptic's answer is that the record so far shows surges, as in 1995-2004, not sustained acceleration.
- **Measurement.** If GDP undercounts free digital services, measured productivity understates true gains. Studies disagree on how large this effect is, and the question is not settled here.
- **AI as automated research.** Aghion, Jones and Jones discuss conditions under which automating idea production could produce explosive growth. This is the strongest theoretical bridge between growth economics and LoAR. It requires AI to substitute for human researchers across essential tasks, which has not yet been observed.
- **Perez's framing.** Techno-economic paradigms predict surges tied to the deployment of each revolution, which fits the 1995-2004 pattern better than either smooth acceleration or smooth steady growth.

## Limitations

- US data only, and labour productivity only. Total factor productivity, which is closer to Solow's residual, is not computed here.
- Period boundaries change the averages. The ones used are conventional (peak-to-peak business-cycle years and the IT boom), but alternatives are defensible.
- The 2019-2025 rate includes pandemic distortions to hours and output composition.
- The frameworks are summarised in a sentence each. Their technical conditions, such as Jones's parameter restrictions, are simplified.

## Conclusion

Growth economics and LoAR share the premise that technology drives growth. They differ on whether that growth accelerates. Seventy-five years of US productivity data fit growth theory's picture of idea-driven growth fluctuating around a stable rate better than Kurzweil's double-exponential. The productive way to use LoAR in the Convergence model is as a claim about technological inputs, which is well supported for computing. Whether those inputs produce accelerating output is a separate empirical question, and the indicator for it is measured productivity growth.

## References

- Kurzweil, R. (2001). The Law of Accelerating Returns. KurzweilAI essay (archived copy). https://web.archive.org/web/2018/http://www.kurzweilai.net/the-law-of-accelerating-returns
- Solow, R. M. (1957). Technical Change and the Aggregate Production Function. *The Review of Economics and Statistics*, 39(3), 312-320. https://doi.org/10.2307/1926047 (copy: http://www.piketty.pse.ens.fr/files/Solow1957.pdf)
- Romer, P. M. (1990). Endogenous Technological Change. *Journal of Political Economy*, 98(5, Part 2), S71-S102. https://doi.org/10.1086/261725
- Jones, C. I. (1995). R&D-Based Models of Economic Growth. *Journal of Political Economy*, 103(4), 759-784. https://doi.org/10.1086/262002
- Aghion, P., Jones, B. F., & Jones, C. I. (2017). Artificial Intelligence and Economic Growth. NBER Working Paper 23928. https://www.nber.org/papers/w23928
- Brynjolfsson, E. (1993). The productivity paradox of information technology. *Communications of the ACM*, 36(12), 66-77. https://doi.org/10.1145/163298.163309
- U.S. Bureau of Labor Statistics. Nonfarm Business Sector: Labor Productivity (Output per Hour of All Persons), series OPHNFB, via FRED. https://fred.stlouisfed.org/series/OPHNFB
- Bloom, N., Jones, C. I., Van Reenen, J., & Webb, M. (2020). Are Ideas Getting Harder to Find? *American Economic Review*, 110(4), 1104-1144. https://doi.org/10.1257/aer.20180338
- Productivity paradox (source of the Solow 1987 quotation, *New York Times Book Review*, July 12, 1987, p. 36). Wikipedia, accessed 2026-10-17. https://en.wikipedia.org/wiki/Productivity_paradox
