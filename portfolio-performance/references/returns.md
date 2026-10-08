# Calculating portfolio returns (Chapter 2)

Notation: V_S = start value, V_E = end value, C = net external cash flow (in = positive), C_t = flow on day t, W_t = fraction of the period the flow was invested = (TD − D_t)/TD, TD = days in period, D_t = days elapsed since the start (including weekends and holidays).

**External cash flow** is new money added or withdrawn, in cash or in kind. Dividends, coupons, purchases and sales funded from within the portfolio are **not** external flows.

**Valuation basis:** economic value, which means trade-date (unsettled trades count) plus accrued interest and declared-but-unpaid dividends. A change in valuation policy can create spurious performance, so keep it consistent.

## Core definitions

| Concept | Formula |
|---|---|
| Wealth ratio | V_E / V_S |
| Simple return | r = V_E/V_S − 1 |
| Chain (geometric) linking | (1+r) = Π(1+r_t) |
| Continuously compounded | r̃ = ln(1+r). Additive over time: ln(1+r) = Σ ln(1+r_t). Unbiased, so use it for statistics |
| Arithmetic average | r_A = (f/n) Σ r_i (biased upward) |
| Annualised (geometric) | r_G = [Π(1+r_i)]^{f/n} − 1, where f = periods per year |
| Effective rate from nominal, n compoundings | (1 + r/n)^n − 1 |

Example: +20% then −20% has an arithmetic mean of 0%, but the annualised return is −2.02% (100 → 96). **Never annualise periods under a year.**

## Money-weighted methods (approximations of IRR)

| Method | Formula | Notes |
|---|---|---|
| Simple IRR | V_E = V_S(1+r) + C(1+r)^{0.5} | Assumes flows at mid-period |
| (Modified) IRR | V_E = V_S(1+r) + Σ C_t(1+r)^{W_t} | Single constant rate. Can't be split by component. Multi-year form: V_E = V_S(1+r)^Y + Σ C_t(1+r)^{Y−Y_t} |
| Simple (original) Dietz | r = (V_E − V_S − C) / (V_S + C/2) | First-order approximation of IRR. Can be split by component. The denominator is average capital, **not** the average of start and end values |
| ICAA | r = (V_E′ − V_S − C′ + I) / (V_S + C′/2) | I = income; C′ and V_E′ include reinvested income |
| Income unavailable | r = (V_E − V_S − C + I) / (V_S + (C − I)/2) | Income treated as an outflow, which leverages the return. Use only if income really is swept away (common for sector returns) |
| Modified Dietz | r = (V_E − V_S − C) / (V_S + Σ C_t·W_t) | Day-weighted. Set a firm-wide **start-of-day vs end-of-day** policy |

Day weighting: a flow on day 14 of a 31-day month is weighted (31−13)/31 at the start of the day and (31−14)/31 at the end.

## Time-weighted methods

- **True TWR:** revalue at every external flow and chain-link the sub-period wealth ratios.
  - End-of-day flow: Π (V_t − C_t)/V_{t−1}.
  - Start-of-day flow: Π V_t/(V_{t−1} + C_t).
  - Mid-day: Π (V_t − C_t/2)/(V_{t−1} + C_t/2). This is a hybrid, not a pure TWR.
- **Unit price (NAV) method:** units are issued or cancelled at the current NAV when flows occur. r = NAV_E/NAV_S − 1. It gives the same answer as true TWR and makes it easy to get the return between any two dates.
- **Approximations** (no valuation on the flow date):
  - Index substitution: estimate the value at the flow using the benchmark return.
  - Regression (β) method: index return × β.
  - **Analyst's test** (SIA 1972): TWA ≈ [V_A − (C_T − C_W)] / [V_N − (C_T − C_W)] × (1+TWN) − 1, where V_N is a notional fund that applies the portfolio's flows to the index, C_T is total flows and C_W is day-weighted flows. This is the most accurate of the three.

  All three share a problem: changing the index changes the portfolio's return, which is hard to explain. GIPS doesn't accept them.
- **Hybrids:** linked monthly Modified Dietz (the industry standard) and BAI (linked IRRs, mostly in the US). Both weight each month equally but are money-weighted within the month.

## Worked comparison (book's standard example)

Start $74.2m (31 Dec), end $104.4m (31 Jan), inflow $37.1m on 14 Jan. Value just before the flow is $66.0m (end of day) or $67.0m (start of day). The benchmark returned −10.68% to the flow date and +3.09% after it.

| Method | Return |
|---|---|
| Simple Dietz | −7.44% |
| Modified Dietz (end of day / start of day) | −7.30% / −7.21% |
| Simple IRR / IRR | −7.41% / −7.27% |
| True TWR (end of day / start of day) | −9.93% / −9.44% (book table shows −9.63% for start of day, which conflicts with its own exhibit) |
| Mid-day TWR | −9.63% |
| Index substitution / Regression (β 1.05) / Analyst's test | −9.80% / −9.18% / −9.49% |

The spread comes entirely from cash-flow assumptions in the denominator. It's large here only because the flow is big relative to assets. A valuation error at the flow date (e.g. 101.1 instead of 103.1) permanently distorts the TWR (−10.94%), so a true TWR needs a daily-valuation mindset.

**TWR vs MWR paradox (Exhibit 2.14):** £100 → £200, then +£1,000 in, then £1,200 → £700. The TWR is +16.67% but the client lost £400, and the MWR is −66.7%. (The book prints −33.3%, which is an arithmetic error.) TWR measures the manager. MWR measures the client's money.

## GIPS 2020 minimums (see `gips-2020.md`)
- TWR is the default. Composites need monthly valuation at month end, revaluation at every firm-defined **large cash flow**, and **daily-weighted** flows otherwise. Link geometrically.
- MWR (annualised since inception, daily flows) is allowed only when the firm controls external flows and the strategy is closed-end, fixed-life, fixed-commitment or illiquid.
- Approximations (index substitution, regression, analyst's test) are not acceptable.
- Net-of-fee returns may use a model fee only if it gives returns equal to or lower than actual fees.

## Choosing a method

| Situation | Use |
|---|---|
| Comparing managers or against indexes | Time-weighted (true TWR ideally) |
| Only accurate monthly valuations available | Linked monthly Modified Dietz, with forced revaluation above a threshold (10% is common, applied to a single flow or the period total) |
| Illiquid or hard-to-value assets | MWR or monthly Dietz. A true TWR's precision would be spurious |
| Private equity / VC (manager controls flows) | IRR |
| Private clients who would be confused by "lost money, positive return" | MWR, or show both with an explanation |

Bacon's ranking (10 = best): true TWR 10, linked Modified Dietz 9, Modified Dietz 8, ICAA 7, BAI 6, IRR 5, simple Dietz 4, simple IRR 3, analyst's test 2, index substitution 1, regression 0.

**Self-selection:** computing several methods and reporting the best is unethical. A subtler version: re-examining only the cash-flow distortions that hurt the return (e.g. when the manager complains about −0.2%) and never the ones that helped. Apply policy symmetrically.

**Mutual-fund dilution:** issuing units at a stale price (backdating, late trading) dilutes existing holders. Correct it by issuing at the current price and having the administrator make up the difference.

## Fees

- **Transaction costs:** always deducted (the manager controls them). Valuations already reflect them.
- **Management fee:** gross-of-fee return = treat the fee as an external outflow. Net-of-fee = don't. Gross is usually right for comparing institutional managers, since fees are negotiable. Regulators usually require net for funds.
- **Custody and administration fees:** outside the manager's control, so exclude them from the evaluation return. The client return after all fees is what the client actually received.
- **Bundled fees:** if trading costs can't be separated, deduct the whole fee for the investment return.
- **Estimation:** gross ≈ (1+net)(1+f) − 1 and net ≈ (1+gross)/(1+f) − 1, using the per-period fee rate f. Compare gross and net geometrically, not by subtraction.
- **Performance fees:** accrue them in net returns. Bacon is sceptical of them: they reward clients for choosing badly, they encourage changes to risk-taking (adding risk to earn the fee, or locking in gains by cutting it), and they're often badly drafted and disputed. If used, base them on risk-adjusted measures.

## Components, sectors and currency

- **Component (sector) returns** use the same method as the total. Flows between sectors are external flows to each sector. Income is moved to the cash sector if cash is a separate sector.
- **Modified Dietz component weight:** w_i = (V_S,i + Σ C_t,i·W_t,i) / (V_S + Σ C_t·W_t). Then Σ w_i·r_i = r. That identity is required for attribution.
- **Component TWRs** need valuations at internal flows too, which in practice means daily.
- **Zero-weight edge case** (e.g. a purchase into an empty sector under the end-of-day convention): use the flow as the weight, with an offsetting cash flow.
- **Cash** is measured like any other asset. Its standalone return may look odd, but weight × return reproduces its contribution.
- **Timing across periods:** the total return can be below every component's return (e.g. 90% equities in a −15.7% quarter). Allocation timing matters.
- **Currency:** (1 + r_base) = (1 + r_local)(1 + r_currency). Convert to another presentation currency with (1+r)(1+c) − 1. The portfolio's local return is Σ w_i·r_Li, an intermediate quantity only. The currency effect is the ratio of the base-currency return to the local return.
