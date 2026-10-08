# Benchmarks and excess return (Chapter 3)

## Good benchmark attributes
1. **Appropriate:** matches the strategy and the client's requirements.
2. **Investable:** the manager can hold every constituent. Otherwise part of the relative performance is outside the manager's control.
3. **Accessible:** constituents and weights are known at the start of the period, not just the returns.
4. **Independent:** calculated by a third party.
5. **Unambiguous:** one benchmark, agreed in advance. Never measure against several, and never change one retrospectively.

## Commercial indexes
- Always use **total-return** indexes, not price indexes.
- Weighting can be cap-weighted, free-float adjusted, GDP-weighted by country, or equal-weighted. Choose by client need.
- **Coverage** = the index's market cap ÷ total market cap. **Concentration** = the weight of the top few names. High concentration means more specific risk.
- **Turnover** = market cap of (additions + deletions) ÷ (2 × average total market cap). Highest in mid-cap indexes. Indexes bear no trading costs, so high turnover is a structural handicap for managers.
- **Hedged indexes:**
  - Static method: one-month forwards that aren't rebalanced, leaving a residual currency exposure.
  - Or b_H = (1 + b_L)(1 + d) − 1, where d is the interest-rate differential. b_H > b_L when the foreign interest rate is below the base-currency rate.
  - Or b_H = (1 + b)/(1 + f) − 1, where f is the forward-contract return.
- **Licensing:** index providers increasingly charge for reuse and customisation. Check you're licensed.

## Custom (composite) benchmarks
- **Excluding a region:** reweight the remaining contributions by 1/(1 − excluded weight).
- **Changing base currency:** (1 + b_A)/(1 + c) − 1, where c is the currency return.
- **Fixed weights vs floating weights.** The rebalancing frequency must be part of the definition.
  - Fixed weights rebalanced quarterly produce a different annual return than applying the weights to annual returns. The book's example: 11.94% fixed vs 11.39% floating.
  - To make quarterly data reproduce "50/50 applied to annual returns", let the weights drift with market moves ("dynamised").
- **Capped indexes:** regulatory or client limits are set as fixed weights at the cap (or below it, to leave room for an overweight).
- **Blended (spliced):** when the benchmark changes, chain-link the old and new so the long-term series survives. Never restate history.

## Peer groups (universes)
- **Pros:** real alternatives for the client, and the returns include real costs.
- **Cons:** the compiler controls quality, loose entry criteria mix strategies, and **survivorship bias** inflates long-term results. The manager also has to guess competitors' positions (e.g. the average IBM weight), which is an extra skill.
- **Percentile rank** = (n − 1)/(N − 1), with 0% = best and the median = 50%. Grouped into quartiles, quintiles or deciles. Football-field charts show the quartile ranges by period, often trimming the top and bottom 5%.

## Other comparators
- **Notional fund:** the benchmark recomputed with the portfolio's actual cash flows (the basis of the analyst's test). More accurate for one portfolio, useless for comparing across portfolios.
- **Normal portfolio:** the manager's realistic universe (e.g. the in-house buy list). Relevant, but not independent.
- **Style indexes:** measure growth managers against growth indexes and value managers against value indexes.

## Excess return

| | Arithmetic a = r − b | Geometric g = (1+r)/(1+b) − 1 |
|---|---|---|
| Meaning | Added value relative to the **initial** investment | Added value relative to the **benchmark's ending value** ("how much bigger is my fund than if I'd bought the index?") |
| Link | g = (r − b)/(1 + b). In rising markets a > g, and in falling markets a < g | |
| Proportional | No: −50% vs −75% gives +25% | Yes: +100% (the portfolio is twice the size) |
| Same in any currency | No (2.0% in USD became 2.2% in EUR in the example) | Yes, because the currency factor cancels |
| Compounds over time | No: 2% each quarter ≠ 9.5% for the year | Yes: Π(1+g_t) = 1+g (1.9%/quarter → 7.8%) |

Bacon strongly prefers geometric excess returns: they're proportional, convertible and compoundable, and he argues they're *more* intuitive to trustees. Arithmetic remains common, especially in the US and Australia. Disclose which one you use.

## GIPS 2020 overlay (see `gips-2020.md`)
- Benchmarks in GIPS reports must be **total return**. Price-only benchmarks are prohibited (except as labelled supplemental information next to a total-return benchmark).
- Custom or blended benchmarks: disclose components, weights, rebalancing and method, and label the benchmark as custom. Never blend TWR and MWR series.
- MWR (private markets) composites: compare against a **PME** of a public index.
- Benchmark changes: GIPS *permits* retroactive changes if they're disclosed as retroactive, with the date and description, for at least a year. Bacon's stricter rule (never change retrospectively; splice forward) remains best practice.
