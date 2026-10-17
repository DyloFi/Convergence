# LoAR: What Can Be Said, With Bounds, About 2026-2035

*Rewritten from the evidence up in Step 13 (2026-10-17). The previous version, which extrapolated a double-exponential formula to "10²⁷+ FLOP" clusters and Kardashev-scale energy without bounds or sources, is preserved at `archive/step13_originals/LoAR/Future_Implications/Future Implications Deep Dive.md.orig`.*

## Executive Summary

This report replaces open-ended extrapolation with projections that each carry a source, a range and a condition that would invalidate them. Three things can be said with reasonable confidence about the next decade. **Compute:** training compute for frontier AI models grew 4-5x per year from 2010 to May 2024 (Epoch AI). Epoch judges training runs of about 2×10²⁹ FLOP "likely feasible by 2030", about 10,000 times its estimate for GPT-4 (about 2×10²⁵ FLOP), with power the constraint "likely to bind first". **Electricity:** US data centres used 176 TWh in 2023 (4.4% of US electricity), and Lawrence Berkeley National Laboratory projects 325-580 TWh (6.7-12%) by 2028. The IEA projects global data-centre demand more than doubling to around 945 TWh by 2030. **Economy:** there is no evidence yet of the economy-wide acceleration LoAR predicts (see `Critiques/Critiques Deep Dive.md`). Feasibility is not destiny. Whether these scales are reached depends on investment returns, chip supply and power build-out, and each projection below names its failure conditions.

## Question and scope

**Question.** Which implications of continued exponential growth in computing for 2026-2035 can be stated with evidence-based bounds, and what would invalidate them?

**Scope.** Three domains with credible published projections: frontier AI training compute, data-centre electricity demand, and macroeconomic effects. Each claim is labelled as an *observed trend*, an *external projection* (by a named body) or *own arithmetic*. Not covered: AGI timelines (Technological Singularity pillar), labour-market impacts and geopolitics. The forecast register in Step 14 will handle these.

## Methodology

1. Use only projections from named, methodologically transparent sources (Epoch AI, LBNL, IEA), with their ranges.
2. Keep observed trends and projections apart, and never extend a trend past its source's own horizon without saying so.
3. For each projection, state the main assumption and what would show it to be wrong.
4. Show any arithmetic done here.

## Empirical Evidence

### 1. Frontier training compute

- *Observed trend.* Epoch AI's database shows that "the compute used to train recent models grew 4-5x yearly from 2010 to May 2024".
- *External projection.* Epoch's analysis of power, chip manufacturing, data and latency concludes that "training runs of 2e29 FLOP will likely be feasible by the end of this decade". Data-centre campuses of 1-5 GW, already under discussion, would support runs of about 10²⁸ to 3×10²⁹ FLOP. A geographically distributed US network of 2-45 GW could support 2×10²⁸ to 2×10³⁰ FLOP.
- *Own arithmetic.* 2×10²⁹ / 2×10²⁵ = 10⁴. Spread over the seven years from GPT-4 (2023) to 2030, that is about 3.7x per year (10^(4/7) ≈ 3.7), slightly below the 2010-2024 trend. So "feasible by 2030" is consistent with the trend slowing modestly, not with it accelerating.
- *Invalidated if:* frontier training runs stop growing for two or more years, through weak returns on investment, chip export limits or power shortfalls.

### 2. Electricity demand

| Measure | Value | Type and source |
| :--- | :--- | :--- |
| US data-centre electricity, 2014 | 58 TWh | Observed (LBNL) |
| US data-centre electricity, 2023 | 176 TWh, about 4.4% of US electricity | Observed (LBNL) |
| US data-centre electricity, 2028 | 325-580 TWh, about 6.7-12% of US electricity | External projection (LBNL) |
| Global data-centre electricity, 2030 | more than double today's, to about 945 TWh | External projection (IEA, *Energy and AI*, April 2025) |
| AI-optimised data centres, 2030 | demand more than quadruples | External projection (IEA) |
| US data centres' share of US electricity demand growth to 2030 | almost half | External projection (IEA) |

Epoch puts all US data-centre power use at "around 20 GW" in 2024, against 1-5 GW for a single frontier training campus by 2030. One training site would then draw a quarter or more of what all US data centres drew in 2024. The IEA stresses "significant uncertainties", including how capable and productive AI becomes, how fast efficiency improves, and whether energy-sector bottlenecks can be resolved.

- *Invalidated if:* efficiency gains outpace demand, or AI demand disappoints. LBNL attributes the doubling of US data-centre demand between 2017 and 2023 "largely" to growth in AI servers, so this projection depends directly on AI build-out.

### 3. Macroeconomic effects

No published evidence yet shows AI or computing raising aggregate productivity growth to the degree LoAR implies. Nordhaus's tests found the "Singularity is not near", and Bloom et al. found research productivity falling (see the Critiques report). For 2026-2035 the defensible statement is conditional. *If* AI substantially raises the productivity of research and of knowledge work, measured total factor productivity growth should rise above its post-2005 pace. That is the indicator to watch.

## Competing views and counterarguments

- **Faster than projected.** Acceleration advocates argue that the 4-5x trend may speed up if AI systems help design chips, write software and do research, and that power constraints will be solved with dedicated generation. Epoch's own distributed-training range (up to 2×10³⁰ FLOP) shows that higher outcomes are physically possible.
- **Slower than projected.** Sceptics point to the large and rising capital costs of frontier training, uncertain revenue, and possible limits on high-quality training data. Epoch lists data scarcity as one of its four constraints. A financial correction (see the Kondratiev Case Studies report on technology booms) could pause the build-out even if the technology keeps improving.
- **Efficiency could flatten the energy curve.** The width of LBNL's 2028 range (325-580 TWh) and the IEA's caveats both reflect uncertainty about how fast efficiency improves relative to demand.

## Limitations

- Every projection here comes from a single source per domain. They are not independent confirmations of one another.
- Epoch's analysis is US-focused and assumes companies can secure 10-40% of available power for distributed training. LBNL's range depends on how fast the rest of the economy grows. The IEA's global figure carries uncertainty the press release does not quantify.
- These are feasibility and demand projections. They say nothing about what the resulting models will be able to do.
- The global 2024 baseline behind the IEA's "more than double" is not stated in the press release used here, so no growth rate is computed from it.

## Conclusion

For 2026-2035, LoAR's implications can be stated with bounds in place of slogans. Frontier training compute could plausibly rise about 10,000-fold from GPT-4 by 2030 if power and chips allow. US data-centre electricity could rise from 4.4% to 6.7-12% of US demand by 2028. Neither projection requires double-exponential growth, and neither guarantees economic acceleration. The Convergence model should carry these as ranged, conditional projections, labelled by source, alongside the indicators that would confirm or overturn them: annual frontier training compute, data-centre electricity use, and measured productivity growth.

## References

- Epoch AI (2024). Training compute of frontier AI models grows by 4-5x per year (May 28, 2024). https://epoch.ai/blog/training-compute-of-frontier-ai-models-grows-by-4-5x-per-year
- Sevilla, J., Besiroglu, T., Cottier, B., You, J., Roldán, E., Villalobos, P., & Erdil, E. (2024). Can AI scaling continue through 2030? Epoch AI (August 20, 2024). https://epoch.ai/blog/can-ai-scaling-continue-through-2030
- Lawrence Berkeley National Laboratory (2025, January 15). Berkeley Lab Report Evaluates Increase in Electricity Demand from Data Centers. https://newscenter.lbl.gov/2025/01/15/berkeley-lab-report-evaluates-increase-in-electricity-demand-from-data-centers/
- International Energy Agency (2025, April 10). AI is set to drive surging electricity demand from data centres while offering the potential to transform how the energy sector works (*Energy and AI* report release). https://www.iea.org/news/ai-is-set-to-drive-surging-electricity-demand-from-data-centres-while-offering-the-potential-to-transform-how-the-energy-sector-works
- Nordhaus, W. D. (2021). Are We Approaching an Economic Singularity? *American Economic Journal: Macroeconomics*, 13(1), 299-332. https://doi.org/10.1257/mac.20170105
- Bloom, N., Jones, C. I., Van Reenen, J., & Webb, M. (2020). Are Ideas Getting Harder to Find? *American Economic Review*, 110(4), 1104-1144. https://doi.org/10.1257/aer.20180338
