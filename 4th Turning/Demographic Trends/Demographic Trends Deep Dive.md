# 4th Turning: What US Birth Data Says About Generations and Turnings

*Rewritten from the evidence up in Step 13 (2026-10-17). The previous version, which relied on invented fertility tables, is preserved at `archive/step13_originals/4th Turning/Demographic Trends/Demographic Trends Deep Dive.md.orig`.*

## Executive Summary

Strauss and Howe divide American history into roughly 20-year turnings and assign each birth cohort to a generation. If those divisions describe something real in the population itself, it should show up in births and fertility. Using the National Center for Health Statistics (NCHS) annual series for 1909-2018, plus CDC figures for 2023-2024, the answer is mixed and mostly negative. The post-war baby boom is a real demographic event with sharp edges: births jumped 19.3% in 1946 and peaked at 4.3 million in 1957. It is the only generation the Census Bureau defines from birth data. None of the other generational boundaries shows up as a break in the series. Fertility has declined over the long run, from a general fertility rate of 126.8 per 1,000 women in 1909 to 59.1 in 2018, with one large interruption (the boom). Crisis turnings do have low fertility (1930s, post-2008), but the steepest decline came in an Awakening (1964-1984), and the lowest point of that decline (1976) sits in the middle of it. Birth data supports describing the boom as a cohort. It does not support the claim that fertility moves in step with turnings.

## Question and scope

**Question.** Do US birth counts and fertility rates show the breaks and phase pattern that the Strauss-Howe generational and turning boundaries imply?

**Scope.** United States only, 1909-2024. Births and the general fertility rate (GFR, births per 1,000 women aged 15-44) come from NCHS. The total fertility rate (TFR) comes from published CDC and Census figures. Generation and turning dates are Strauss and Howe's as currently used by Howe. Not covered: migration (which changes cohort size after birth), mortality, and other countries.

## Methodology

1. Load the NCHS series (`data/nchs_births_gfr_us_1909_2018.csv`, unchanged from data.cdc.gov dataset e6fc-ccez). NCHS adjusts births before 1959 for under-registration.
2. For each Strauss-Howe generation, compute mean births per year and mean GFR. Means are used because the generations differ in length (18 to 24 years).
3. For each turning, record GFR at its start and end, its mean and its low year.
4. List the largest one-year changes in births, to see whether any generational boundary coincides with a demographic break.

`scripts/step13_demography_check.py` reproduces every number in the two tables below.

## Empirical Evidence

### Births and fertility by generation

| Strauss-Howe generation (birth years) | Mean births per year | Mean GFR |
| :--- | ---: | ---: |
| G.I. (1901-1924; data from 1909) | 2.90 million | 120.5 |
| Silent (1925-1942) | 2.58 million | 85.8 |
| Boom (1943-1960) | 3.79 million | 110.2 |
| 13th / Gen X (1961-1981) | 3.58 million | 82.5 |
| Millennial (1982-2005) | 3.94 million | 66.3 |
| Homeland (2006-; data to 2018) | 4.03 million | 64.0 |

Two things stand out. First, birth counts and fertility point in different directions. The Millennial years produced more births per year than the Boom years even though fertility was 40% lower, because the Boom generation itself had become parents. The Homeland average is high partly because 2007 has the most births in the whole NCHS series (4,316,233). Second, the Boom is the only generation whose fertility clearly differs from its neighbours.

### Fertility by turning

| Turning (Strauss-Howe dates) | GFR, first year | GFR, last year | Mean | Low (year) |
| :--- | ---: | ---: | ---: | :--- |
| Unraveling 1908-1929 | 126.8 | 93.8 | 116.5 | 93.8 (1928) |
| Crisis 1929-1946 | 89.3 | 85.9 | 83.0 | 75.8 (1936) |
| High 1946-1964 | 101.9 | 108.3 | 114.0 | 101.9 (1946) |
| Awakening 1964-1984 | 104.7 | 65.7 | 76.4 | 65.0 (1976) |
| Unraveling 1984-2008 | 65.5 | 69.3 | 66.5 | 63.6 (1997) |
| Crisis 2008- (data to 2018) | 68.1 | 59.1 | 63.1 | 59.1 (2018) |

### Where the real breaks are

The three largest one-year rises in births were 1946 (+19.3%), 1947 (+11.9%) and 1942 (+10.6%). The three largest falls were 1972 (-8.4%), 1919 (-7.1%) and 1965 (-6.6%). The 1946 jump and the 1965 fall bracket the boom, matching the Census Bureau's 1946-1964 definition. Strauss and Howe date the Boom generation 1943-1960 instead, which puts their boundaries about three years earlier than the demographic edges. Pew Research Center notes that the Baby Boomers are "the only generation officially designated by the U.S. Census Bureau" and that "there are no comparably definitive thresholds" for later generations.

Published TFR figures tell the same story. TFR peaked at 3.77 births per woman in 1957, fell from 2.91 in 1965 to 1.84 in 1980, rose to 2.08 in 1990 and stayed roughly flat until 2007. It then declined to 1.73 in 2018. Except for 2006 and 2007 it has been below replacement (2.1) since 1971. The provisional 2024 figures are 3,622,673 births and a TFR of 1,626.5 per 1,000 women, slightly up on 2023. Births fell by an average of 2% a year from 2015 to 2020 and have fluctuated since.

### Reading the evidence against the claim

- **Supported:** the Boom is a real cohort defined by a demographic surge. Crisis periods (the 1930s and the post-2008 years) have below-trend fertility.
- **Not supported:** the idea that fertility rises and falls with the four turnings. Fertility fell fastest during an Awakening, stayed flat through an Unraveling, and reached its 20th-century low (1976) mid-Awakening. Over the whole period, the main pattern is a long decline interrupted once.
- **Not testable with this data:** whether the Boom's size *caused* any later turning. Cohort size is consistent with many causal stories.

## Competing views and counterarguments

- **Demographic transition and economics.** Mainstream demography explains the long decline through falling child mortality, urbanisation, women's education and paid work, contraception and the rising cost of children. The boom is usually explained by post-war prosperity, earlier marriage and a catch-up in births delayed by the Depression and the war. These accounts explain the data at least as well as a turning cycle, without assuming one.
- **The strongest case for Strauss and Howe.** One could argue that the theory is about generational *mood*, not birth volume, so a fertility test is beside the point. That is fair to the core theory. But earlier versions of this report, and other reports in this pillar, make explicit fertility claims ("Fourth Turning: TFR hits historical lows"), and those claims are what this file tests.
- **Coincidence of crises and low fertility.** Low fertility in crises is real, but both crises here also had recessions (1929-1933, 2007-2009). Economic downturns lower fertility directly, so the link does not need a generational cycle to explain it.

## Limitations

- One country with about 110 years of data covers only about one and a half saecula, so any test of an 80-year cycle has very little power.
- GFR and TFR measure period fertility. Completed cohort fertility would answer a slightly different question and is not used here.
- Pre-1959 births are NCHS estimates adjusted for under-registration.
- Cohort sizes change after birth through immigration and mortality. The Millennial generation, for example, is larger as adults than its births alone imply.
- Turning dates come from the theory itself, and Howe has adjusted them over time (the current crisis is dated from 2008). Testing a theory against boundaries it defines carries a risk of fitting after the fact.

## Conclusion

The birth record backs one generational boundary, the post-war boom, and gives no support to the others. Fertility does not move in step with the four turnings. The long decline since 1909 and the single boom-era interruption are better explained by standard demographic and economic accounts. The pillar should treat cohort size as context for the 2026-2035 discussion (an ageing population and below-replacement fertility are well measured), not as evidence that a Fourth Turning is underway.

## References

- Centers for Disease Control and Prevention, NCHS. Births and General Fertility Rates: United States, 1909-2018 (dataset e6fc-ccez). https://data.cdc.gov/api/views/e6fc-ccez/rows.csv?accessType=DOWNLOAD
- CDC (2020). QuickStats: Expected Number of Births over a Woman's Lifetime, United States, 1940-2018. *MMWR* 69(1):20. https://www.cdc.gov/mmwr/volumes/69/wr/mm6901a5.htm
- Hamilton, B. E., Martin, J. A., & Osterman, M. J. K. (2025). Births: Provisional data for 2024. *Vital Statistics Rapid Release* No. 38. https://www.cdc.gov/nchs/data/vsrr/vsrr038.pdf
- Colby, S. L., & Ortman, J. M. (2014). *The Baby Boom Cohort in the United States: 2012 to 2060* (P25-1141). U.S. Census Bureau. https://www.census.gov/content/dam/Census/library/publications/2014/demo/p25-1141.pdf
- Pew Research Center (2019). Defining generations: Where Millennials end and Generation Z begins. Pew Research Center. https://www.pewresearch.org/short-reads/2019/01/17/where-millennials-end-and-generation-z-begins/
- Strauss, W., & Howe, N. (1991). *Generations: The History of America's Future, 1584 to 2069*. William Morrow.
- Strauss–Howe generational theory (turning and generation dates as used by Howe). Wikipedia, accessed 2026-10-17. https://en.wikipedia.org/wiki/Strauss%E2%80%93Howe_generational_theory
