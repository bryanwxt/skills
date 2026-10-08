---
name: portfolio-performance
description: 'Use when calculating, checking, or explaining investment portfolio returns (time-weighted, money-weighted/IRR, Modified Dietz, unit price, annualized, gross/net of fees, multi-currency); choosing or building a benchmark (custom, blended, hedged, peer group) or excess return (arithmetic vs geometric); computing or interpreting risk-adjusted measures (Sharpe, M², Treynor, Jensen alpha, information ratio, tracking error, Sortino, VaR, duration); building or reviewing performance attribution (Brinson-Fachler, geometric, multi-period linking, multi-currency, fixed income); or preparing/reviewing GIPS performance presentations, GIPS 2020 compliance, composites, pooled fund reports or GIPS advertisements. Based on Carl Bacon''s "Practical Portfolio Performance Measurement and Attribution" (2004).'
---

# Portfolio Performance Measurement and Attribution

**The book's frame.** Performance measurement follows five steps, in this order:
1. **Calculate the return.** Use total return (income plus realised and unrealised gains), time-weighted, at economic (trade-date, accrued) value.
2. **Compare against a benchmark.** It must be appropriate, investable, accessible, independent and unambiguous, and agreed in advance.
3. **Assess the reward for the risk taken.** Use risk-adjusted measures that fit the mandate.
4. **Attribute the excess return** to the manager's actual investment decisions.
5. **Present the results** fairly, with full disclosure (GIPS).

Performance measurers are independent risk controllers, not back office. Their test is always: does the number fairly represent what the manager did and what the client got?

## Bacon's defaults (his stated preferences; disclose if you deviate)

| Decision | Default | Why |
|---|---|---|
| Return method | True time-weighted (revalue at every external cash flow). Otherwise monthly Modified Dietz, chain-linked, with forced revaluation for large flows (≥10%) | Removes the effect of cash-flow timing the manager didn't control |
| Money-weighted (IRR) | Private equity/VC, private clients, or when the manager controls flows | Reflects the client's actual money experience |
| Excess return | **Geometric** (1+r)/(1+b)−1 | Proportionate, the same in any currency, compounds over time |
| Attribution | Brinson-Fachler allocation (vs overall benchmark), interaction folded into selection, geometric version for multi-period | Follows the decision process, no residual |
| Multi-period arithmetic linking | GRAP (or Frongello) if you must stay arithmetic | Intuitive. Carino and Menchero are acceptable but cumbersome |
| Attribution data | Transaction-based, reconciling to the official return, ideally daily | Buy-and-hold leaves residuals that hide errors |
| Multi-currency | Geometric, with forward rates for currency bets and the cost of hedging charged to the asset allocator | The currency manager can only bet through forwards |
| Risk-adjusted headline | M² (and M² excess), information ratio | A real return, comparable across portfolios |
| Standard deviation | Population (divide by n), annualised by √periods | Consistency across analysts |

## Quick rules (no references needed)

- **Never annualise periods shorter than a year.** Use geometric averages for multi-year returns. Arithmetic averages are biased upward.
- **Never pick the most flattering method** (self-selection). Fix a written policy (cash-flow timing, revaluation threshold, fee treatment) and apply it whatever the result.
- **Never change a benchmark retrospectively.** Splice (chain-link) the old and new benchmarks.
- **IRR cannot be split into components**, so don't use it for sector returns or attribution.
- **The sum of weight × component return must equal the total return**, or the attribution is wrong.
- Every number needs its method disclosed: arithmetic or geometric, data frequency, period, n or n−1, ex post or ex ante.
- Interaction and residuals aren't investment decisions. Fold interaction into selection and investigate residuals. Never hide them.
- With low R² (well below 0.8), ignore alpha, beta and the measures derived from them.

## References

- `references/returns.md`: every return method, with formulas, worked results and when to use each. Covers fees, components, currency and carve-outs.
- `references/benchmarks.md`: benchmark attributes, index construction (turnover, hedged, custom, fixed-weight vs floating-weight, capped, spliced), peer groups, notional funds, and arithmetic vs geometric excess returns.
- `references/risk.md`: all risk and risk-adjusted measures (variability, Sharpe, M², regression, CAPM, Treynor, appraisal, Fama decomposition, tracking error, information ratio, distribution shape, downside risk, VaR, Hurst, duration and convexity), how to choose among them, and the risk-control structure.
- `references/attribution.md`: Brinson-Hood-Beebower, Brinson-Fachler, geometric, sector weights, buy-and-hold vs transaction-based, smoothing (Carino, Menchero, GRAP, Frongello, Davies-Laker), risk-adjusted, multi-currency (Ankrim-Hensel, Karnosky-Singer, geometric), and fixed income (weighted duration).
- `references/gips-2020.md`: **current GIPS** (2020 edition plus guidance statements on Benchmarks, revised 2023, and OCIO, effective 31 Dec 2025). Covers fundamentals, calculation minimums, composites, report contents, MWR rules, advertising, and what changed since the book. Use this for any compliance question.
- `references/standards.md`: GIPS as described in 2004 (historical rationale only), verification, carve-outs, portability, firm definition, the EIPC's 22 questions to ask about an attribution report, and the attribution disclosure checklist.
- `references/playbooks.md`: step-by-step procedures (calculating a return series, building a custom benchmark, a risk report, attribution end to end, reviewing someone else's attribution, a GIPS readiness check, reconciliation debugging).
- `scripts/perf.py`: tested reference implementations (Dietz, IRR, TWR, linking, excess returns, Sharpe, M², tracking error, Sortino, Brinson, geometric attribution, Carino and GRAP factors). Run `python3 scripts/perf.py` for self-tests against the book's examples.

## Limits (say these when they apply)

- **The book's GIPS content is from 2004.** Use `references/gips-2020.md` for current requirements (summarised from CFA Institute's 2020 standards, checked October 2026). Check gipsstandards.org for newer guidance statements or Q&As before giving compliance advice. Copy required wording (compliance statements) exactly from the official text.
- **Known errata in the book** (corrected in these references):
  - Exhibit 2.14: the money-weighted return is −66.7%, not −33.3%.
  - Table 4.4: M² for portfolio B is 8.89%, not 8.74%.
  - Equation 4.38: the printed σP·√(1−ρ²) is specific risk, not tracking error (they match only when β ≈ 1). The general formula is √(σP² + σM² − 2ρσPσM).
  - The modified Treynor ratio should use σS (= β·σM) in the denominator.
  - Some exhibits contain small typos. Recompute rather than copy.
- **Author preferences aren't industry law.** Arithmetic excess returns and BHB-style reports remain common, especially in the US. State which one you're using rather than calling the other wrong.
- **Formulas are tools, not judgments.** Bacon's own advice is to compute a few measures consistent with the mandate and watch how they change over time, rather than chasing precision in any single one.

*Condensed and paraphrased from Carl R. Bacon, "Practical Portfolio Performance Measurement and Attribution" (Wiley Finance, 2004). Formulas restated in standard notation. Errors in the source are noted where found.*
