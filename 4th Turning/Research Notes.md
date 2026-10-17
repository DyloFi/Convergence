# 4th Turning Research Notes: How to Test a Generational Claim

*Rewritten from the evidence up in Step 13 (2026-10-17). The previous version, a set of loose notes padded with template text, is preserved at `archive/step13_originals/4th Turning/Research Notes.md.orig`.*

## Executive Summary

Most reports in the 4th Turning pillar make claims of the form "this generation is X" or "this turning brings Y". This note sets the minimum standard such claims must meet before the pillar or the Convergence synthesis relies on them. The core problem is well understood. Age, period and cohort are perfectly collinear: a person's birth year equals the survey year minus their age. Differences seen in one survey can therefore never be assigned to "generation" on their own. Pew Research Center calls this the identification problem and, after a 2022-2023 review, now does generational analysis only where long-run data and explicit age-period-cohort (APC) models allow it. The National Academies (2020) reached a similar conclusion about generational research in the workforce. Below are seven rules, each with a reason and an example from this pillar. The rewrites of `Demographic Trends`, `Public Perception` and `Neutral Analyses` follow them.

## Question and scope

**Question.** What evidence is needed before a 4th Turning report may attribute an observed pattern to a generation or a turning, rather than to age, period, composition or chance?

**Scope.** Method only. This note does not judge the Strauss-Howe theory (see `Neutral Analyses/Neutral Analyses Deep Dive.md`). It applies to every report in `4th Turning/` and to any claim the master synthesis takes from them.

## Methodology

The rules draw on Pew's published approach to generational research and its worked APC examples, the National Academies review, and the defects the Step 10-12 audits found in this pillar: invented tables, unsourced percentages and turning dates fitted after the fact.

## Empirical Evidence

### Why one survey cannot show a generational effect

Pew's methods team sets out the arithmetic: if someone was 50 in 2016, they were born around 1966, so knowing any two of age, period and cohort fixes the third. With data from one point in time, "it's not possible to identify conclusively whether apparent differences between generations are not just due to how old the respondents were." Pew's preferred fix is a multilevel model that places cohort and period at a different level from age and controls for traits such as sex and race. It uses long-running, consistently collected data such as the Census Bureau's Current Population Survey. In its worked examples, a generational gap in marriage rates survived the model, but an apparent gap in moving rates was explained by other factors.

### What independent reviews concluded

- Pew (2023) will only compare generations "at similar stages of life", will control for period effects and changing demographics, and will often drop the standard labels. It notes that a typical generation spans 15 to 18 years and that there is "great diversity of thought, experience and behavior within generations."
- The National Academies (2020) found that variation in workers' values and behaviour "more likely reflect[s] differences in their ages, career stages, job experiences, and general changes in society", and that people of the same generation are as likely to differ from one another as from people of other generations.

### The rules

| # | Rule | Why | Example in this pillar |
| :--- | :--- | :--- | :--- |
| 1 | No generational claim from a single cross-section | Age and cohort cannot be separated | "Millennials are less married" from one survey year is an age effect until shown otherwise |
| 2 | Compare cohorts at the same age, using long-run, consistently collected data | Only then can cohort differ from age | Census CPS series; NCHS birth records |
| 3 | Check for period effects before claiming a cohort effect | Events such as Watergate moved all ages | Trust in government fell for everyone after 1964 (Public Perception) |
| 4 | Fix turning and generation dates before looking at the outcome data, and use the theory's published dates | Dates chosen after seeing the data guarantee a fit | Demographic Trends uses the published Strauss-Howe dates, not dates fitted to fertility |
| 5 | State what result would count against the claim | Otherwise the claim cannot be tested | "If cross-party trust has not risen by the end of the dated Crisis, the rebuilding prediction failed" |
| 6 | Every number needs a source a reader can open, or a script in `scripts/` that reproduces it | Step 10-12 audits found invented tables in this pillar | `scripts/step13_demography_check.py` and the NCHS CSV under `Demographic Trends/data/` |
| 7 | Report the uncertainty and the alternative explanations next to the finding, not in a later section | Readers take the headline and skip caveats | Each rewritten report gives "supported / not supported / not testable" next to the evidence |

## Competing views and counterarguments

- **"Generations are real; ask anyone."** Shared formative events can leave lasting marks, and APC models sometimes find genuine cohort effects (Pew's marriage example). The rules do not rule generational claims out. They require the evidence to separate cohort from age and period.
- **"APC models just move the assumption somewhere else."** That is fair. Any APC method needs an identifying assumption, such as treating period and cohort as random effects. Results should be checked under more than one specification and the assumption stated. This is a reason for modesty, not a reason to skip the analysis.
- **"Qualitative history does not need regression."** Narrative history is valuable. But when a report presents numbers or forecasts, the numbers must meet these rules.

## Limitations

- These rules are a floor, not a full methods textbook. They do not cover sampling design, weighting or measurement error in historical sources, all of which also matter for older data.
- APC models need long, consistent series. For most attitudes these exist only from the 1970s (for example the General Social Survey), so claims about earlier generations will usually stay untestable.
- The examples cite US data only. The same rules apply to other countries, but data availability differs.
- Pew's and the National Academies' reviews focus on attitudes and workforce behaviour. Applying them to macro-historical cycles is my extension and is labelled as such.

## Conclusion

A 4th Turning report may attribute a pattern to a generation or turning only if it compares cohorts at the same age with long-run data, rules out period effects, uses dates fixed in advance, names what would refute it, and sources every number. Claims that cannot meet this standard can stay in the pillar as hypotheses, labelled as such, but should not feed the Convergence synthesis as evidence.

## References

- Pew Research Center (2023). Assessing the effects of generation using age-period-cohort analysis (Decoded). https://www.pewresearch.org/decoded/2023/05/22/assessing-the-effects-of-generation-using-age-period-cohort-analysis/
- Parker, K. (2023). How Pew Research Center will report on generations moving forward. https://www.pewresearch.org/short-reads/2023/05/22/how-pew-research-center-will-report-on-generations-moving-forward/
- National Academies of Sciences, Engineering, and Medicine (2020). *Are Generational Categories Meaningful Distinctions for Workforce Management?* doi:10.17226/25796. https://www.nationalacademies.org/news/categorizing-workers-needs-by-generation-such-as-baby-boomers-or-millennials-is-not-supported-by-research-or-useful-for-workforce-management
- CDC National Center for Health Statistics. Births and General Fertility Rates: United States, 1909-2018. https://data.cdc.gov/api/views/e6fc-ccez/rows.csv?accessType=DOWNLOAD
