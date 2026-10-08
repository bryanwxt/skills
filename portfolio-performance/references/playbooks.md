# Playbooks

Each one lists inputs → steps → output. Before computing, state the conventions you're using (arithmetic or geometric, n or n−1, start-of-day or end-of-day flows, gross or net of fees). Use `scripts/perf.py` for the core formulas, and check new code against its self-tests.

---

## A. Calculate a portfolio return series
**Inputs:** valuations (trade-date, with accruals), external cash flows with dates and timing, income, fees.
1. Classify the flows. External means client money in or out. Income, trades and internal transfers aren't external. Decide whether fees are external flows (for gross returns) or not (for net).
2. Choose the method (table in `returns.md`): true TWR if you have valuations at every flow. Otherwise monthly Modified Dietz, with revaluation above the policy threshold (e.g. 10%).
3. Apply the written timing policy (start-of-day or end-of-day) consistently.
4. Compute the sub-period returns and chain-link them. For components, check that Σ w_i r_i = r.
5. Annualise only periods of a year or more, geometrically.
6. Sanity checks: compare against the benchmark. Large gaps on flow dates suggest a valuation error at the flow. Recompute with an alternative method only for diagnosis, never to choose which number to report.

**Output:** the return series plus a methodology note (method, timing, threshold, fee basis, valuation source).

---

## B. Build or review a custom benchmark
1. Check the five attributes: appropriate, investable, accessible, independent, unambiguous.
2. Specify the components (total-return indexes), weights, **rebalancing frequency** (fixed vs floating), caps, the currency basis (unhedged, local or hedged), and the data licence.
3. Compute it: Σ W_i·b_i each period, chain-linked. Recheck that the stated rebalancing rule reproduces the intended annual mix.
4. For changes, splice forward (chain-link) and never restate history. Record the date and reason.
5. For peer groups, record the entry criteria, survivorship handling, and percentile rank (n−1)/(N−1).

**Output:** the benchmark definition document and its return series.

---

## C. Risk and risk-adjusted performance report
1. Agree a few measures that match the mandate:
   - **Absolute:** σ, Sharpe, M²
   - **Relative:** TE, IR, M² excess
   - **Downside:** σ_D, Sortino
   - **Systematic:** β (only if R² ≥ about 0.8), Jensen's α, Treynor
   - **Bonds:** modified or effective duration, duration β
2. Use the same risk-free rate and the same frequency and period for the portfolio and benchmark. Annualise σ by √f.
3. Report ex post, and ex ante if available. Compute the **risk efficiency ratio** (ex post / ex ante TE).
4. Add distribution shape (skew, kurtosis) if tails matter. Remember that normal-based VaR and TE understate fat tails.
5. Show the **trend** over time and explain sudden changes (data error, model change, or a genuine change in risk).

**Output:** a table of measures with a disclosure footnote covering frequency, period, n or n−1, arithmetic or geometric, ex post or ex ante, r_F and target.

---

## D. Attribution end to end
1. **Map the decision process.** Top-down (allocation, then selection)? Bottom-up (security only)? Is currency managed separately? Is duration or beta a lever? Get the manager to confirm it.
2. **Choose the model to match:**
   - Single currency, arithmetic: Brinson-Fachler with interaction folded into selection.
   - Geometric: Bacon/Burnie.
   - Multi-currency: geometric with hedged-index allocation and forward-based currency allocation, or Karnosky-Singer.
   - Bonds: weighted-duration attribution.
   - Bottom-up: security-level, with no allocation effect.
3. **Data:** transaction-based. Sector returns use the same method as the total. Weights reproduce the total return. Run it at the highest feasible frequency (daily is best).
4. **Compute** the single-period effects, then link: geometric (compound) or arithmetic with GRAP, Frongello or Carino, disclosed.
5. **Reconcile:** sum of effects = excess return, and attribution returns = official returns. Investigate any residual.
6. **Edge cases:** off-benchmark positions (classify as allocation or selection per the process); allocation-driven transaction costs (charge to the allocator); cash (strategic or incidental, with a cash benchmark); leverage and derivatives (economic exposure); fees (gross or net against the benchmark).
7. **Present** with the EIPC disclosures (`standards.md`).

**Output:** an effects table by sector and factor, the linked totals, the reconciliation, and the disclosures.

---

## E. Review someone else's attribution report
Go through the **EIPC 22 questions** (`standards.md`). Red flags:
- a large or rising residual, or one relabelled as "timing" or "other"
- interaction split arbitrarily or dropped
- BHB-style allocation that credits overweights in positive-but-lagging markets
- buy-and-hold attribution that doesn't reconcile
- currency effects with no currency process behind them
- local returns treated as achievable
- a benchmark changed retrospectively
- an arithmetic total compared across currencies
- different periods or benchmarks for risk and return attribution

**Output:** a findings list (issue → impact on interpretation → fix), plus whether the conclusions still hold.

---

## F. GIPS readiness check
(Requirements are in `gips-2020.md`. Confirm against gipsstandards.org for newer guidance statements or Q&As.)
0. Choose TWR or MWR per composite (MWR only if the firm controls flows and the strategy is closed-end, fixed-life, fixed-commitment or illiquid). Classify pooled funds as broad or limited distribution. Check whether the OCIO guidance applies.
1. **Firm definition:** meaningful and fair. Prove completeness, for example from fee income.
2. **Composite list:** every fee-paying discretionary portfolio is included, terminated ones too. There are written definitions, inclusion and exclusion timing rules, and a creation date.
3. **Calculation policies:** TWR method (monthly valuation at month end, revaluation at firm-defined *large* cash flows, daily-weighted flows otherwise), fair-value hierarchy, trade-date and accrual accounting, fee basis (model fees no higher in return than actual), taxes, FX source, *significant* cash-flow policy (amount or percentage only).
4. **Presentation:** 5 years building to 10; annual returns; benchmark total returns (no price-only); portfolio count; composite and total firm assets; internal dispersion; 3-year annualised ex post SD for composite and benchmark; the exact compliance statement and trademark disclosure; all 4.C disclosures; no partial-year annualisation. Add the GIPS Compliance Notification Form (annual, by 30 June) and a process for distributing reports to all prospects.
5. **Controls:** an owner, quarterly review, annual verification, staff training (client-facing staff especially).
6. **Carve-outs and portability:** avoid carve-outs if possible. Check the conditions before linking prior-firm records.

**Output:** a gap list ranked by severity, and a project plan (allow a year or more for complex firms).

---

## G. Debug a reconciliation break
1. Does Σ w_i r_i equal the total? If not, check the weight definition, internal flows between sectors, and income sweeps to cash.
2. Do the portfolio returns match the official returns? Look for a different method or timing convention, a missing flow, a pricing or FX source mismatch, or fee treatment.
3. Do the benchmark returns match the published index? Check total return vs price, rebalancing rules, FX fix time, and withholding tax.
4. Is the residual concentrated on flow dates? Revalue at the flow or attribute more often.
5. Do multi-period totals fail to add up? Check that the linking method suits the excess-return definition, and that the arithmetic effects were smoothed.
6. Is the multi-currency residual about the size of the compounding effect? Show compounding explicitly.
