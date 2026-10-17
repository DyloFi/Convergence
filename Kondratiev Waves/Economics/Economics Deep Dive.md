# Kondratiev Waves: How Strong Is the Macroeconomic Evidence?

*Rewritten from the evidence up in Step 13 (2026-10-17). The previous version, built from recycled Trotsky and Schumpeter passages and an unsourced "time-series matrix", is preserved at `archive/step13_originals/Kondratiev Waves/Economics/Economics Deep Dive.md.orig`.*

## Executive Summary

Nikolai Kondratiev's 1935 English-language article, "The Long Waves in Economic Life", claimed 50-60 year waves in prices, interest rates, wages, trade and output. Ninety years on, the evidence divides by indicator. Long waves in **prices** before World War II are widely accepted, but the pattern disappears from price indices after 1945. Evidence in **output** is contested. Kondratiev's own production series relied on fitting elaborate trend curves and smoothing the residuals, a method criticised since the 1940s because it can manufacture waves. As Slutsky showed in 1937, smoothing random shocks can produce cycles. The best recent support comes from Korotayev and Tsirel (2010). Their spectral analysis of world GDP growth from 1871 to 2007 found a 52-53 year component at a combined significance of 4-5%, on a series no longer than three cycles. Modern growth theory explains long-run growth through investment in ideas and creative destruction (Romer 1990; Aghion and Howitt 1992), and does not require a fixed-period wave. The fair verdict: long waves are a live, weakly supported hypothesis about output, and a description of pre-1945 prices. They are not an established macroeconomic regularity to forecast with.

## Question and scope

**Question.** For which macroeconomic indicators is there statistical evidence of 40-60 year Kondratiev waves, how strong is it, and how does modern growth theory treat long swings?

**Scope.** The indicators Kondratiev used (prices, interest rates, production) and world GDP growth. Evidence comes from Kondratiev's article, the review of the econometric literature in Korotayev and Tsirel (2010), and their spectral results. Not covered: wave datings and named waves (see `History/History Deep Dive.md`), and individual crises (see `Case_Studies/Case Studies Deep Dive.md`).

## Methodology

1. Separate the claim by indicator, because the evidence differs sharply between prices and output.
2. For each, record what the strongest supporting study found and what the main methodological objections are.
3. Note the statistical power problem: a 50-year cycle can appear at most two or three times in any reliable series.
4. Compare the long-wave claim with what modern growth models predict.

No new estimation is done here. The repository holds no long-run datasets (see `Kondratiev Waves/Data/README.md`). A replication would need, for example, the Bank of England's "A millennium of macroeconomic data" (version 3.1, to 2016) for the UK and Maddison-type world GDP estimates.

## Empirical Evidence

### Prices: strong before 1945, absent after

Korotayev and Tsirel summarise the literature: "The presence of K-waves in price dynamics (at least till the 2nd World War) has found a very wide empirical support". They add that "the K-wave pattern ceased to be traced in the price indices after the 2nd World War", citing Goldstein (1988). A likely reason is the change of monetary regime. Under the gold standard, price levels rose and fell over long periods. Under post-war fiat money, prices mostly rose. A wave that depends on the monetary regime is a weak basis for a law of capitalist development.

### Output: contested, with a method problem

Kondratiev also claimed long waves in world coal and pig-iron production. His method was to fit a long-term trend (often a cubic function), then smooth the residuals with moving averages. Critics from Garvy (1943) to Goldstein (1988) argued that this "casts doubt on the theoretical meaning and parsimony of the resulting long waves". The concern is sharpened by Slutsky's 1937 result that summing random disturbances can generate apparently regular cycles. Any long-wave finding that depends on detrending and smoothing has to rule out a filtering artefact.

### World GDP: the best recent support, and its limits

Korotayev and Tsirel ran a spectral analysis of annual world GDP growth rates for 1871-2007, built from Maddison and World Bank estimates. Their results:

| Component | Period found | Significance reported |
| :--- | :--- | :--- |
| Kondratiev wave (with its third harmonic) | about 52-53 years | combined 4-5% (0.04 < p < 0.05) |
| Juglar cycle | 7-9 years (reduced spectrum) | about 2-3% |
| Kitchin cycle | shorter | about 2-3% in one specification |

The authors note that this significance was reached "on the basis of series of observations that cover a period that does not exceed the length of three cycles". They also note that the "turbulent 2nd–4th decades of the 20th century", with two world wars and the Depression, dominate the variation in the series. A result at p of about 0.045, on fewer than three cycles, with much of the signal coming from 1914-1945, is suggestive but not robust.

### What modern growth theory says

Endogenous growth models explain sustained growth through deliberate investment in new ideas (Romer 1990). Schumpeterian models (Aghion and Howitt 1992) add creative destruction: each innovation makes earlier ones obsolete. These models can produce irregular swings when major innovations arrive in clusters or take decades to spread. They do not predict a fixed 50-year period. Long swings are compatible with modern theory. Clockwork waves are not required by it.

## Competing views and counterarguments

- **For long waves.** Supporters argue that each great surge has a clear technological core (steam, steel and electricity, oil and cars, ICT) and that the clustering of innovations, infrastructure investment and finance makes 40-60 year swings plausible. The Korotayev-Tsirel result shows a statistically detectable long component in world output, which earlier sceptics said did not exist.
- **Against.** Sceptics reply that the waves are irregular, that the post-1945 price wave vanished, that significance hinges on two world wars, and that filtering methods can create cycles from noise.
- **A middle reading.** "Long swings of variable length tied to technological revolutions" (closer to Perez) is better supported than "a 50-60 year cycle". The second implies forecastable turning points, and the evidence does not support that.

## Limitations

- This report reviews published evidence and does not re-estimate anything. Korotayev and Tsirel's numbers are taken as reported.
- World GDP before 1950 rests on reconstructed estimates (Maddison), with large uncertainty, especially for non-Western economies.
- Spectral analysis on series of roughly 140 years can resolve a 50-year component only loosely. Significance tests assume a noise model that may not fit series with structural breaks.
- Kondratiev's article (1935, translated by W. F. Stolper) is cited from its bibliographic record. Its contents are summarised through the secondary literature cited.

## Conclusion

The macroeconomic case for Kondratiev waves is strongest for pre-1945 prices and weakest for anything that would let us forecast. In output, the best evidence reaches borderline significance on fewer than three cycles, with heavy dependence on 1914-1945. For the Convergence model, long waves should be treated as a hypothesis that frames questions about technology-driven investment swings. It should not be used as a timing device for 2026-2035.

## References

- Kondratieff, N. D. (1935). The Long Waves in Economic Life (W. F. Stolper, trans.). *The Review of Economics and Statistics*, 17(6), 105-115. https://doi.org/10.2307/1928486
- Korotayev, A. V., & Tsirel, S. V. (2010). A Spectral Analysis of World GDP Dynamics: Kondratieff Waves, Kuznets Swings, Juglar and Kitchin Cycles in Global Economic Development, and the 2008-2009 Economic Crisis. *Structure and Dynamics*, 4(1), 3-57. https://escholarship.org/uc/item/9jv108xp
- Slutzky, E. (1937). The Summation of Random Causes as the Source of Cyclic Processes. *Econometrica*, 5(2), 105ff. https://doi.org/10.2307/1907241
- Romer, P. M. (1990). Endogenous Technological Change. *Journal of Political Economy*, 98(5, Part 2), S71-S102. https://doi.org/10.1086/261725
- Aghion, P., & Howitt, P. (1992). A Model of Growth Through Creative Destruction. *Econometrica*, 60(2), 323-351. https://doi.org/10.2307/2951599
- Bank of England. A millennium of macroeconomic data (version 3.1). https://www.bankofengland.co.uk/statistics/research-datasets
- Goldstein, J. S. (1988). *Long Cycles: Prosperity and War in the Modern Age*. Yale University Press. (Cited via Korotayev & Tsirel 2010.)
- Garvy, G. (1943). Kondratieff's Theory of Long Cycles. *The Review of Economics and Statistics*, 25(4), 203ff. https://doi.org/10.2307/1927337
