# Forecast Audit: Step 14 Reassessment

**Review date:** 2026-11-01
**Scope:** the 2026-2035 cross-domain convergence thesis, forecast claims about AI capability and AGI/ASI, and the fiscal, reserve, productivity, gold and tokenized-asset indicators used to support the thesis.
**Method:** re-read the current repository forecast register and forecast audit, then checked cited public-source definitions and the latest available official releases or live forecast pages. The current structured register is `review/FORECAST_REGISTER.csv`. The former register and audit are retained under `*_LEGACY_2026-10-14` for traceability and are not the current scored record.

## Question and scope

Do the repository's current observations and forecasts support a single, synchronized 2026-2035 convergence event, and are the AGI/ASI timelines comparable enough to support one? This review tests source definitions, dates, units, conditionality and sensitivity. It does not produce a new probability for convergence, AGI or ASI.

## Executive summary

The repository's earlier register did not define one measurable convergence event. It combined fiscal, institutional, reserve, tokenization and AI claims with different units and horizons. Several quantitative cells in the legacy CSV are incomplete, and its 65%, 70%, 75% and 45% confidence entries have no elicitation or calculation record in that file. Those values are therefore not carried forward as calibrated estimates.

The refreshed evidence supports separate observations: AI capability is measured on a narrow benchmark distribution; IMF reserve shares changed quarter to quarter; reported central-bank gold purchases are incomplete for 2026; tokenized asset values depend on whether the metric is distributed or represented; BLS productivity is an aggregate measure without an AI causal attribution; and CBO fiscal projections include explicit interest-rate sensitivities. None of these facts alone establishes synchronized convergence or its causal links.

The 2026-2035 convergence thesis remains a plausible research scenario, but it is unsupported as a single dated forecast until its domains, joint-event rule, quantitative thresholds, lags and scoring procedure are pre-registered. The refreshed register keeps delayed, partial, non-convergent and rapid-coupling scenarios side by side and assigns no probabilities to them.

## Method and register changes

The former register is preserved, not silently overwritten, as `review/FORECAST_REGISTER_LEGACY_2026-10-14.csv`. The former narrative audit is preserved as `review/FORECAST_AUDIT_LEGACY_2026-10-14.md`. The active files now separate observed measurements, external forecasters' estimates and analyst-defined scenarios.

Each active entry records its claim, horizon, source and date, whether it is an external observation or estimate, assumptions, proposed mechanism, quantitative basis and units, uncertainty or sensitivity, invalidating conditions and one of the requested confidence labels. The confidence label describes the evidential status of the stated claim; it is not a probability. Probabilities reported below are only those explicitly elicited and published by an external forecasting source.

## Reassessment of the convergence thesis

The old register groups indicators that are not on a common scale. It does not define how much change in one domain is needed, how many domains must move together, which leads or lags count, or how to distinguish a common cause from coincident movement. That prevents a reproducible score, sensitivity analysis or retrospective hit/miss decision.

The current evidence does show distinct signals, but their scope is narrower than the thesis often implies:

- CBO's October 8, 2026 Monthly Budget Review estimates a $2.0 trillion federal deficit for FY2026. Its separate October 8 analysis places debt held by the public at 100.6% of GDP in 2026 and 120.2% in 2036 under the February baseline. CBO also models interest-rate scenarios 50 and 150 basis points above that baseline. These are conditional projections, not a forecast of Federal Reserve yield-curve control or debt monetization.
- IMF COFER's September 30, 2026 release reports a 56.70% U.S.-dollar share of allocated foreign-exchange reserves in 2026Q2, down from 57.18% in 2026Q1. One quarter does not establish a persistent break or an abandonment of the dollar.
- The World Gold Council's October 6 report records 170 tonnes of reported central-bank net purchases year to date through August 2026, including 39 tonnes in August. This is a partial-year measure; it cannot confirm or refute a full-year threshold before the year ends.
- RWA.xyz displayed $39.17B in distributed asset value and $398.06B in represented asset value on November 1, 2026, with stablecoins listed separately at $286.62B. The two RWA totals are differently defined; represented value is not interchangeable with distributed value, market liquidity or institutional settlement volume.
- BLS's revised Q2 2026 release reports nonfarm business productivity growth of 1.4% at a seasonally adjusted annualized quarterly rate and 2.2% year over year. It does not identify AI as the cause. The next preliminary release was scheduled for November 5, 2026.

These observations are compatible with change, but they do not demonstrate that the domains are causally coupled or synchronized. CBO's own rate sensitivity illustrates why assumptions matter: its 150-basis-point scenario is materially different from the baseline, but it is a stress scenario rather than a probability-weighted outcome.

## AI capability, deployment and impact

METR defines time horizon as the human-expert task duration at which an agent is predicted to succeed at a stated reliability. Its page, last updated September 8, 2026, says it is no longer actively updated and that measurements above 16 hours are unreliable with the current task suite. Its tasks are mainly software engineering, machine learning and cybersecurity, often self-contained and automatically scored. METR explicitly says that time horizon is not the duration an AI can work independently and that an eight-hour horizon does not imply automation of all jobs.

LEAP's Wave 8 report says that, during its April-May 2026 survey, the median expert forecast assigned a 50% chance that an AI would reach 80% success on METR software tasks requiring at least eight hours of human-expert effort by 2030; the corresponding median years were 2028 for superforecasters and 2037 for the public. LEAP also reports that METR's May 8 estimate for Claude Mythos Preview was a 3-hour-6-minute 80%-time horizon, with a 95% interval from 1 hour 37 minutes to 6 hours 39 minutes. These are a benchmark observation and a survey of forecasts, respectively; neither is a measurement of economy-wide adoption or productivity.

The clean separation is: measured task capability, deployed use and realized economic or social impact are distinct outcomes. Adoption, workflow redesign, reliability, infrastructure, regulation and measurement can delay or limit impact. The available metrics do not identify their causal contribution to productivity.

## AGI and ASI timelines

AGI is not operationalized consistently across the sources. LEAP defines its survey event as a commercially available system outperforming the 90th-percentile professional employee in every primarily non-physical occupation on at least 90% of economically useful non-physical tasks, at an inference cost no more than five times equivalent human labor. Conditional on a majority of the LEAP panel agreeing that AGI exists before 2100, the expert median year is 2050, with the 25th and 75th percentile years at 2039 and 2065. These are conditional survey judgments, not an unconditional probability that AGI will exist by 2050.

Metaculus Question 5121 is a separate community forecast. Its live page displayed 23 September 2030 as the current estimate on November 1, 2026, alongside a displayed range from March 22, 2028 to July 2036. The extracted page did not expose the full resolution criteria or label the statistical meaning of that displayed range. The old register's paraphrase of the question is not treated as verified, and the Metaculus date is not pooled with the LEAP distribution.

The August 30, 2026 version of Genewein et al.'s AGI-to-ASI report characterizes AGI and ASI informally relative to human-level and broadly superhuman capability, then discusses possible pathways and bottlenecks. It is not a dated ASI forecast. This review assigns no ASI arrival year or probability.

## Scenarios and indicators

The active register retains four alternatives without probability weights:

1. Delayed impact: benchmark capability gains continue, while deployment and measured productivity effects lag. Track sector-level use, task reliability, infrastructure constraints and revised output-per-hour series.
2. Partial convergence: rapid change occurs in selected digital tasks or financial rails, while physical deployment, reserve composition and institutions follow different paths. Report each series separately and preserve units.
3. Non-convergence: capability growth plateaus or diffusion remains limited, while fiscal, reserve and institutional indicators adjust through separate mechanisms. Review benchmark updates and the same official series at each observation date.
4. Rapid coupling: capabilities, adoption and fiscal or institutional pressures reinforce each other. Treat this as a conditional research scenario until thresholds, time lags, causal links and a reproducible joint model are specified.

These scenarios are not mutually exclusive forecasts with calibrated weights. No probability is assigned. A future scoring pass should preregister each domain's series, threshold, date, lag, source, revision policy and cross-domain link before counting outcomes.

## Data provenance, units and sensitivity

Values are retained in their source units: dollars and percentages for CBO, reserve-share percentages for COFER, tonnes for gold, percentage growth rates for BLS, dollar asset values for RWA.xyz, human-equivalent task duration for METR, and calendar years for forecast distributions. No metric is converted into a common convergence score because no defensible weighting rule is available.

CBO's higher-interest analysis provides an explicit sensitivity design: it compares the 2026-2036 baseline against cases 50 and 150 basis points higher. The IMF release notes limited exchange-rate valuation effects in 2026Q2 and attributes the dollar-share change largely to other price changes and/or portfolio reallocations. WGC's year-to-date gold figure is reported activity through August, not an annualized projection. BLS reports a revised quarterly series and a separate year-over-year rate. RWA.xyz separates distributed from represented values and stablecoins. METR warns that its longer time-horizon measurements exceed the current suite's reliable range.

Reproduction path: use the dated provider release or live page linked in the register, record retrieval date and the exact metric definition, preserve provider revisions, and recalculate only within the same unit and definition. A composite sensitivity calculation is not reproducible until weights, lags and thresholds are specified.

## Competing views and counterarguments

A rapid-convergence interpretation can point to measurable benchmark progress, a large fiscal deficit, declining quarterly dollar-share readings, continuing central-bank gold purchases, and expanding tokenized asset values. These are real signals in their own respective measures.

A slower or non-convergent interpretation notes that a benchmark's task distribution is narrow; one quarter of reserve-share changes is not a structural regime shift; gold data for 2026 are incomplete; tokenized asset values are not equivalent to liquid settlement volume; and current aggregate productivity figures do not isolate AI. CBO explicitly separates baseline projections from alternative interest-rate assumptions. The evidence supports maintaining both interpretations until a reproducible coupling test distinguishes them.

## Limitations

This is a bounded step review of the current register and the linked public releases, not a full line-by-line audit of every forecast claim in every source dossier. Some pages are live and mutable. Metaculus resolution criteria were not visible in the extracted page text, so its date is reported only as the displayed estimate. METR's public time-horizon page is no longer actively updated. Macro releases are revised, and the gold report records only activity reported through August. The available sources do not provide a common causal model or a calibrated joint distribution.

## Conclusion

The evidence supports separately reported capability, fiscal, reserve, gold, productivity and tokenized-asset observations. It does not establish one synchronized convergence event in 2026-2035. Keep convergence as a plausible scenario, not a scored or probability-weighted forecast. Keep AGI timelines separate by operational definition, and keep ASI timing unquantified unless a source supplies a resolvable definition and an elicited forecast.

## References

- METR, Task-Completion Time Horizons of Frontier AI Models, last updated September 8, 2026: https://metr.org/time-horizons
- Thomas Kwa, Clarifying limitations of time horizon, January 22, 2026: https://metr.org/notes/2026-01-22-time-horizon-limitations
- LEAP, Wave 8: Timelines, published June 1, 2026: https://leap.forecastingresearch.org/reports/wave8
- Metaculus, Question 5121, live page observed November 1, 2026: https://www.metaculus.com/questions/5121/when-will-the-first-general-ai-system-be-devised-tested-and-publicly-announced
- Tim Genewein et al., From AGI to ASI, arXiv:2606.12683v2, August 30, 2026: https://arxiv.org/html/2606.12683
- Congressional Budget Office, Monthly Budget Review: September 2026, October 8, 2026: https://www.cbo.gov/publication/61985
- Congressional Budget Office, Projections of Deficits and Debt Under Two Scenarios With Higher Interest Rates, October 8, 2026: https://www.cbo.gov/publication/62809
- IMF, COFER Data Brief for 2026Q2, September 30, 2026: https://data.imf.org/en/news/imf%20data%20brief%20september%2030
- World Gold Council, Central Bank Gold Statistics: Central banks continue summer spree in August, October 6, 2026: https://www.gold.org/goldhub/gold-focus/2026/10/central-bank-gold-statistics-central-banks-continue-summer-spree-august
- World Gold Council, Gold Demand Trends: Q4 and Full Year 2025, January 29, 2026: https://www.gold.org/goldhub/research/gold-demand-trends/gold-demand-trends-full-year-2025
- U.S. Bureau of Labor Statistics, Productivity and Costs, Second Quarter 2026, Revised, September 3, 2026: https://www.bls.gov/news.release/prod2.nr0.htm
- RWA.xyz, Global Market Overview, observed November 1, 2026: https://app.rwa.xyz/
