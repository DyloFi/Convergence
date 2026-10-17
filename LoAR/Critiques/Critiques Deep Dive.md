# LoAR: Which Critiques of the Law of Accelerating Returns Hold Up?

*Rewritten from the evidence up in Step 13 (2026-10-17). The previous version, which framed critiques generically and stated physical limits with garbled units, is preserved at `archive/step13_originals/LoAR/Critiques/Critiques Deep Dive.md.orig`.*

## Executive Summary

Ray Kurzweil's 2001 essay states the Law of Accelerating Returns (LoAR): technological progress, and computing price-performance in particular, grows not just exponentially but "double" exponentially, so the 21st century will bring "more like 20,000 years of progress (at today's rate)". This report tests four lines of criticism against primary evidence. **Physics:** Landauer's limit is real and has been confirmed experimentally (Bérut et al., 2012), but the most efficient supercomputer in June 2025 still used about 5 billion times the Landauer energy per 64-bit operation. Thermodynamics is not the binding constraint this decade. **Architecture:** Hennessy and Patterson document that Dennard scaling faded between 2007 and 2012, cutting general-purpose processor gains to a few percent a year. Progress continued through specialised hardware. **Economics of innovation:** Bloom, Jones, Van Reenen and Webb (2020) find that sustaining Moore's Law now takes more than 18 times as many researchers as in the early 1970s, so the exponential holds only because effort grows exponentially. **Macroeconomics:** Nordhaus's tests (2015/2021) "suggest that the Singularity is not near". The verdict: the physics critique is overstated, while the economic critiques hold. Exponential trends in computing are real but bought with rising effort, and they have not produced the economy-wide acceleration LoAR predicts.

## Question and scope

**Question.** Which critiques of LoAR are supported by evidence: physical limits, the end of classical transistor scaling, falling research productivity, or the absence of macroeconomic acceleration?

**Scope.** LoAR as stated in Kurzweil's 2001 essay. Four critiques, each tested on primary or peer-reviewed sources. Logistic (S-curve) saturation (Modis 2002) is discussed as a competing model. Not covered: AI-specific capability forecasts (see the Technological Singularity pillar) and the energy outlook (see `Future_Implications/Future Implications Deep Dive.md`).

## Methodology

For each critique I state the claim, the strongest evidence for it, and whether the evidence bears on LoAR's core claim (sustained, accelerating exponential progress) or only on one technology. Where a number can be checked by arithmetic (the Landauer comparison), the calculation is shown.

## Empirical Evidence

### 1. Thermodynamic limits (Landauer)

Landauer (1961) showed that erasing one bit of information must dissipate at least kT ln 2 of energy. At 300 K this is 1.380649 × 10⁻²³ J/K × 300 K × 0.693 ≈ 2.87 × 10⁻²¹ J. Bérut et al. (2012) confirmed the bound experimentally with a colloidal particle in an optical trap.

How close is practical computing? The top system on the June 2025 Green500 list, JEDI (EuroHPC/FZJ), achieved 72.73 GFlops per watt. That is 1/(72.73 × 10⁹) ≈ 1.37 × 10⁻¹¹ J per 64-bit floating-point operation, about 4.8 × 10⁹ times the Landauer energy for one bit. Even if an operation erases a few hundred bits, practical hardware is still millions of times above the limit. The Landauer critique is correct in principle but irrelevant to 2026-2035.

### 2. The end of Dennard scaling

Hennessy and Patterson (2019) report that Moore's Law "began to slow sometime around 2000" and that by 2018 there was "a roughly 15-fold gap" between Moore's prediction and actual capability. Dennard scaling (near-constant power per mm² as transistors shrink) "began to slow significantly in 2007 and faded to almost nothing by 2012". Together with Amdahl's Law, this limits general-purpose processor gains "to only a few percent per year". Their answer is domain-specific architectures. Google's first TPU, for example, was 29 times faster than a contemporary CPU on Google's inference workloads and more than 80 times more energy-efficient. This critique hits general-purpose CPUs hard. It hits LoAR less, because LoAR's claim is about computation per dollar across paradigms, and specialised accelerators continued the trend for the workloads that matter most for AI.

### 3. Rising cost of progress (research productivity)

Bloom et al. (2020) find, across industries, products and firms, that research effort is rising substantially while research productivity is falling sharply. Their headline example: the number of researchers needed to double chip density is more than 18 times larger than in the early 1970s. "Ideas, and the exponential growth they imply, are getting harder to find." This is the strongest critique. It shows that the exponential in chips is not self-sustaining, as LoAR's feedback story implies. It depends on exponentially growing inputs, which cannot continue forever.

### 4. No macroeconomic acceleration (yet)

Nordhaus builds a growth model in which a "Singularity" occurs if information can substitute well enough for conventional inputs. He tests it on the macro data. His conclusion is direct: "The tests suggest that the Singularity is not near." The key question, he writes, "is the substitutability between information and conventional inputs."

### Summary

| Critique | Evidence | Does it refute LoAR's core claim? |
| :--- | :--- | :--- |
| Thermodynamic (Landauer) | Limit confirmed; best 2025 hardware is ~10⁹ times above it per bit | No, not on any relevant horizon |
| End of Dennard scaling | General-purpose CPU gains slowed after the mid-2000s | Partly: one paradigm saturated; specialised hardware continued |
| Research productivity | 18× more researchers needed for Moore's Law than in the early 1970s | Yes, for the "self-reinforcing" mechanism: progress depends on rising inputs |
| Macro acceleration | Nordhaus: Singularity "not near" | Yes, for the claim that computing gains are already accelerating overall growth |

## Competing views and counterarguments

- **Kurzweil's reply: paradigm shifts.** LoAR expects each technology to follow an S-curve and the overall trend to continue as new paradigms take over. Dennard's end followed by GPUs and AI accelerators fits this story. The question is whether paradigm shifts keep arriving on schedule, and LoAR assumes rather than demonstrates that.
- **Logistic saturation (Modis 2002).** Modis models complexity and change as following logistic curves, implying that the rate of change eventually peaks and declines. On this reading, apparent double-exponential growth is the steep middle of an S-curve.
- **AI may change the research-productivity picture.** If AI systems become effective researchers, the "harder to find ideas" constraint could loosen, since the research labour force could grow much faster than the human population. This is the central hope of acceleration advocates. It is a hypothesis to watch, not an observed trend (see the Technological Singularity pillar).
- **Measurement.** Some economists argue that GDP undercounts digital goods, which would make the lack of macro acceleration partly a measurement problem. That cuts both ways for Nordhaus's tests.

## Limitations

- The Landauer comparison uses an HPL (64-bit) benchmark. AI workloads at lower precision are more energy-efficient per operation, but still far above the limit.
- Bloom et al. measure research inputs through deflated R&D spending. Different deflators change the size of the decline, but the authors report the pattern across many settings.
- Nordhaus's tests use data up to the mid-2010s, before the large-language-model boom. They should be re-run on recent data before treating the conclusion as current.
- The TPU comparison is Google's own measurement on its own workloads, as reported by Hennessy and Patterson.

## Conclusion

The physical critique of LoAR is weak for any near-term horizon. The architectural critique shows that individual paradigms saturate, which LoAR itself allows. The economic critiques are strong. Exponential progress in computing has needed exponentially rising research effort, and through the mid-2010s it had not produced the economy-wide acceleration LoAR predicts. For the Convergence model, the defensible claim is "computing price-performance has improved exponentially at rising cost". The claim "progress is double-exponential and self-sustaining" is not defensible. What would change this verdict: evidence that AI is raising measured research productivity or total factor productivity growth.

## References

- Kurzweil, R. (2001). The Law of Accelerating Returns. KurzweilAI essay (archived copy). https://web.archive.org/web/2018/http://www.kurzweilai.net/the-law-of-accelerating-returns
- Landauer, R. (1961). Irreversibility and Heat Generation in the Computing Process. *IBM Journal of Research and Development*, 5(3), 183-191. https://doi.org/10.1147/rd.53.0183
- Bérut, A., Arakelyan, A., Petrosyan, A., Ciliberto, S., Dillenschneider, R., & Lutz, E. (2012). Experimental verification of Landauer's principle linking information and thermodynamics. *Nature*, 483(7388), 187-189. https://doi.org/10.1038/nature10872
- TOP500 (2025). Green500, June 2025. https://www.top500.org/lists/green500/2025/06/
- Hennessy, J. L., & Patterson, D. A. (2019). A new golden age for computer architecture. *Communications of the ACM*, 62(2), 48-60. https://doi.org/10.1145/3282307
- Bloom, N., Jones, C. I., Van Reenen, J., & Webb, M. (2020). Are Ideas Getting Harder to Find? *American Economic Review*, 110(4), 1104-1144. https://doi.org/10.1257/aer.20180338
- Nordhaus, W. D. (2021). Are We Approaching an Economic Singularity? Information Technology and the Future of Economic Growth. *American Economic Journal: Macroeconomics*, 13(1), 299-332. https://doi.org/10.1257/mac.20170105 (working paper: https://www.nber.org/papers/w21547)
- Modis, T. (2002). Forecasting the growth of complexity and change. *Technological Forecasting and Social Change*, 69(4), 377-404. https://doi.org/10.1016/S0040-1625(01)00172-X
