# Performance attribution (Chapter 5, Appendices A and B)

**Definition:** quantifying the portfolio's excess return over its benchmark in terms of the active decisions in the investment process.

**First principle:** the analyst must understand the actual decision process and quantify *those* decisions. Factors outside the process add nothing. Common blind spots for managers: stocks in the index that *aren't* held are often large bets. Senior management uses attribution to spot outliers and check consistency, and it's the best opening for client dialogue, including proactively explaining underperformance.

Notation: w_i, W_i = portfolio and benchmark weights (each summing to 1). r_i, b_i = portfolio and benchmark sector returns. r = Σw_i r_i, b = ΣW_i b_i.
- **Semi-notional (allocation) fund** b_S = Σ w_i b_i
- **Selection notional fund** r_S = Σ W_i r_i

## Worked data (Table 5.1)

| | w | W | r | b |
|---|---|---|---|---|
| UK | 40% | 40% | 20% | 10% |
| Japan | 30% | 20% | −5% | −4% |
| US | 30% | 40% | 6% | 8% |
| Total | | | 8.3% | 6.4% |

This gives b_S = 5.2% and r_S = 9.4%.

## Arithmetic: Brinson, Hood and Beebower (1986)

| Effect | Category formula | Total | Example |
|---|---|---|---|
| Allocation | (w_i − W_i)·b_i | b_S − b | −1.2% (UK 0, Japan −0.4, US −0.8) |
| Selection | W_i·(r_i − b_i) | r_S − b | +3.0% (4.0, −0.2, −0.8) |
| Interaction | (w_i − W_i)(r_i − b_i) | r − r_S − b_S + b | +0.1% (0, −0.1, +0.2) |

The flaw: every overweight in a *positive* market scores positive even if that market lagged the overall benchmark. (BHB's paper didn't intend sector-level use, but practitioners apply it that way.)

## Arithmetic: Brinson and Fachler (1985)

Allocation is measured against the overall benchmark: A_i = (w_i − W_i)(b_i − b). It has the same total, because Σ(w_i − W_i)·b = 0.

Example: Japan −1.04% (an overweight in a market that underperformed the 6.4% total), US −0.16%, total −1.2%.

**Interaction is not a decision.** Nobody is responsible for it, so it gets ignored, split 50:50, or hidden. If allocation comes first, fold interaction into selection:
- S_i = w_i(r_i − b_i), with total r − b_S
- Example: +3.1% (4.0, −0.3, −0.6)

Judge stock pickers on their within-sector performance, not their contribution to the total. Think of it as three steps: benchmark → semi-notional (allocation) → portfolio (selection).

## Geometric attribution (Bacon, Burnie et al., Bain, Allen)

The target is the geometric excess return g = (1+r)/(1+b) − 1.

- **Allocation**
  - A_i^G = (w_i − W_i)·[(1+b_i)/(1+b) − 1]
  - Total: (1+b_S)/(1+b) − 1
  - Example: −1.13% (Japan −0.98%, US −0.15%)
- **Selection**
  - S_i^G = w_i·[(1+r_i)/(1+b_i) − 1]·(1+b_i)/(1+b_S), which simplifies to w_i(r_i − b_i)/(1+b_S)
  - Total: (1+r)/(1+b_S) − 1
  - Example: +2.95% (UK 3.80%, Japan −0.29%, US −0.57%)
  - The (1+b_i)/(1+b_S) term exists because outperforming in a strong market adds more value geometrically.
- **The two compound exactly:** (1+S^G)(1+A^G) − 1 = g, with no interaction and no residual. That's proved in Appendix A.

## Sector weights and data integrity

- Weights × returns must reproduce the total return. Sector returns must use the same method as the total.
- IRR isn't usable (it assumes a single constant rate).
- Dietz-type returns reconcile, but intra-period flows can **shift effects between allocation and selection**. In the book's example, simple Dietz shows the US underperforming (6.0% vs 8.0%), while the true TWR shows it outperforming (9.48%). Calculating before and after the flow moves Japan's selection to −2.5% and the US to +0.5%. Attribute as often as possible, ideally daily.
- **Illmer and Marty (2003):** decompose the money-weighted return by computing a money-weighted benchmark with the portfolio's flows, isolating the effect of client-directed flows as "timing".
- **Buy-and-hold (holdings-based) attribution:** start-of-period weights × returns from another source. It's easy, but it **won't reconcile**, and the residual grows with:
  - turnover
  - IPOs (it captures the close price, not the float price)
  - large flows
  - illiquid assets
  - longer periods

  It also hides trading value and operational errors. Bacon won't compromise here: use **transaction-based** attribution for clients, because reconciliation exposes back-office errors. (Spaulding 2003 gives a more balanced view.)
- **Security-level (bottom-up) attribution:** no allocation effect. Over- or underweighting a stock is the decision, and "selection" within a stock measures trade timing.

## Multi-period arithmetic linking (smoothing)

Arithmetic effects don't add up across periods, because Σ(r_t − b_t) ≠ r − b. All the fixes below rescale each period's effects so they sum to r − b. The book's four-quarter data: r = 3.86%, b = −9.41%, excess 13.27%.

| Method | Factor applied to period-t effects | 4-quarter totals (allocation / selection) | Notes |
|---|---|---|---|
| **Carino (1999)** | k_t/k, where k_t = [ln(1+r_t) − ln(1+b_t)]/(r_t − b_t) (or 1/(1+r_t) if r_t = b_t) and k is the same for the full period | 1.20 / 12.07 | Every period is restated whenever the horizon extends |
| **Menchero (2000)** | M + α_t, where M = [(r−b)/T]/[(1+r)^{1/T} − (1+b)^{1/T}] and α_t = [(r−b − M·Σ(r_t−b_t))/Σ(r_t−b_t)²]·(r_t−b_t) | 0.92 / 12.34 | Optimised to keep the factors as even as possible. Complex, and also restated |
| **GRAP (1997)** | Π_{s<t}(1+r_s) · Π_{s>t}(1+b_s) | 1.24 / 12.03 | The excess return compounds with the actual return up to t and is reinvested in the benchmark afterwards. Bacon's preferred arithmetic method |
| **Frongello (2002)** | f_T = a_T·Π_{t<T}(1+r_t) + b_T·Σ_{t<T} f_t | 1.24 / 12.03 (same as GRAP) | Period-1 effects never change. Later periods change as the horizon extends |
| **Davies and Laker (2001)** | Compound the notional funds: allocation Π(1+b_S,t) − Π(1+b_t), selection Π(1+r_S,t) − Π(1+b_t), interaction = the remainder | 1.16 / 13.18 / −1.07 | Totals only (sectors need smoothing). It makes interaction *less* meaningful, so better to define selection as Π(1+r_t) − Π(1+b_S,t) |

**Multi-period geometric needs no smoothing:** Π(1+S_t^G)·Π(1+A_t^G) − 1 = g. In the example, selection 13.19% and allocation 1.29% compound to 14.64%. These are the geometric counterpart of Davies and Laker.

Sector effects within a period sum (not compound) to the period total. To make sector effects compound to the total, apply the adjustment:

Ŝ_i = (1+S_i)·[(1+S)/Π(1+S_i)]^{|S_i|/Σ|S_j|} − 1

The adjustments are tiny and stay stable as the period extends.

Bacon's verdict: the linking method rarely changes the conclusions. Use geometric linking for geometric excess returns, and GRAP for arithmetic.

## Risk-adjusted attribution (Brinson, Singer and Beebower 1991)

Use this only if beta (or duration) is genuinely a decision lever.

- Risk-adjusted benchmark per sector: b′_i = x_i + β_i(b_i − x_i), where x_i is the local risk-free rate.
- Notional fund: b′_S = Σw_i·b′_i.
- The total splits into three compounding factors:

  1+g = [(1+r)/(1+b′_S)] **selectivity** × [(1+b′_S)/(1+b_S)] **systematic risk** × [(1+b_S)/(1+b)] **allocation**

- Sector formulas:
  - Selectivity: w_i·[(1+r_i)/(1+b′_i) − 1]·(1+b′_i)/(1+b′_S)
  - Systematic risk: w_i·[(1+b′_i)/(1+b_i) − 1]·(1+b_i)/(1+b_S)
- Example: UK β 1.3 in a rising market shifts +1.03% from "selection" to systematic risk. Selectivity is 2.35%, systematic risk 0.58%, allocation −1.13%.
- Rarely used for equities.

## Multi-currency attribution

Currency decomposition: c_i = S^{t+1}/S^t − 1 = e_i (currency surprise, (S^{t+1} − F)/S^t) + d_i (forward premium, F/S^t − 1). The forward-contract return is f_i = S^{t+1}/F − 1 = e_i/(1 + d_i).

### Ankrim and Hensel (1992), arithmetic

- l_i = b_i − c_i
- k_i = r_i − c_i
- l = ΣW_i·l_i

| Effect | Formula |
|---|---|
| Allocation | (w_i − W_i)(l_i − l) |
| Selection | W_i(k_i − l_i), or w_i(k_i − l_i) with interaction folded in |
| Interaction | (w_i − W_i)(k_i − l_i) |
| Currency | (w_i − W_i)(e_i − ē) + (w̃_i − W̃_i)(f_i − ē), where ē = ΣW_i·e_i and tildes are forward weights |
| Forward premium | (w_i − W_i)(d_i − d̄) |

Problems:
- The arithmetic premium spreads the market × currency compounding across the other effects.
- It isolates the forward premium, which actually results from allocation decisions and should sit with allocation.
- ē doesn't respond to benchmark hedging.

### Karnosky and Singer (1994), continuously compounded

- Return premium over local cash: r = Σw_i(r_Li − x_i) + Σ(w_i + w̃_i)(c_i + x_i). Benchmark likewise.
- Local premiums: l′_i = b_Li − x_i, k′_i = r_Li − x_i, l′ = ΣW_i·l′_i.
- Allocation: (w_i − W_i)(l′_i − l′). The forward premium is embedded here.
- Selection: w_i(k′_i − l′_i).
- Currency: (w_i − W_i)(c_i + x_i − c′) + (w̃_i − W̃_i)(c_i + x_i − c′), where c′ is the benchmark currency-plus-cash return.
- Because it uses log returns, this is effectively geometric.
- Bacon's disagreement: it treats *every* foreign position as earning the return premium (implicitly hedged). Only *deviations* from the benchmark should be exposed to interest differentials, since the client already priced the benchmark.

### Geometric multi-currency (Bacon; Appendix B)

Quantities:
- r_L = Σw_i·r_Li (portfolio local return)
- b_L = ΣW_i·b_Li (benchmark local return)
- b_SL = Σw_i·b_Li (local semi-notional)
- b_SH = ΣW_i·b_Li + Σ(w_i − W_i)·b_Hi (semi-notional with country bets **hedged to neutral**, using hedged index returns b_Hi = (1+b_Li)(1+d_i) − 1)
- r′_C = (1+r)/(1+r_L) − 1 and b′_C = (1+b)/(1+b_L) − 1 (implied currency returns)

**Naive currency attribution** = (1+r′_C)/(1+b′_C) − 1. It's quick and correct in total, but blind to hedging costs and compounding.

Full decomposition, which compounds exactly to g:

1+g = [(1+r_L)/(1+b_SL)] **stock selection** × [(1+b_SH)/(1+b_L)] **country allocation (incl. cost of hedging bets)** × [(1+b_SL)/(1+b_SH)] **hedging cost transferred** × [(1+r)/(1+r_L)]·[(1+b_L)/(1+b)] **naive currency**

- Sector allocation: (w_i − W_i)[(1+b_Hi)/(1+b_L) − 1]
- Sector selection: w_i[(1+r_Li)/(1+b_Li) − 1](1+b_Li)/(1+b_SL)

**Currency, from the currency-overlay manager's view.** A currency manager can only bet through forwards, so measure bets at forward returns, not spot.

Measured currency returns:
- Benchmark: b_C = ΣW_i·c_i + ΣW̃_i·f_i
- Portfolio: r_C = Σw_i·c′_i + Σw̃_i·f′_i (actual rates)

Semi-notional currency returns:
- c_S = Σw_i·c_i + Σw̃_i·f_i
- c_SH = ΣW_i·c_i + Σ(w_i − W_i + w̃_i)·f_i

Effects:
- **Currency allocation** = (1+c_SH)/(1+b_C) − 1. Per currency: (w_i + w̃_i − W_i − W̃_i)[(1+f_i)/(1+b_C) − 1].
- **Currency timing (selection)** = (1+r_C)/(1+c_S) − 1. Per currency: w_i[(1+c′_i)/(1+c_i) − 1](1+c_i)/(1+c_S), plus the forward analogue. It captures trading at rates other than the index fix (WM/Reuters 4pm).
- **Compounding** = [(1+r′_C)/(1+r_C)]·[(1+b_C)/(1+b′_C)] − 1. This is the market × currency interaction that an overlay manager can't see. It's usually a few basis points and smaller with daily measurement.
- **Hedging mismatch** = [(1+b_SL)/(1+b_SH)]·[(1+c_S)/(1+c_SH)] − 1. This is the difference between the overlay manager's and the allocator's view of hedging costs. It's tiny.

Currency overlay total = timing × allocation. Total currency = overlay × hedging mismatch × compounding.

Book example: stock selection 2.95%, allocation −1.22% (it cost 0.09% to hedge the bets), currency allocation 1.26%, timing 0.22%, other −0.50%. These compound to 2.69%.

**Other currency issues:**
- Unrealised gains or losses on forwards create a net position that damps or gears returns. This is an attributable factor in its own right.
- The currency a security is denominated in may not be its economic exposure. For example, US$-denominated Japanese warrants are really yen exposure.

## Fixed income: weighted duration attribution (van Breukelen 2000)

The approximation is r_Li ≈ x_i + D_i·(−Δy_i). Weight × duration is the exposure lever.

Notional funds:
- Duration notional: b_D = Σ Dβ·D_bi·W_i·(−Δy_bi) + c′, where Dβ = D_portfolio/D_benchmark
- Duration-adjusted semi-notional: r_S = ΣD_i·w_i·(−Δy_bi) + c′

| Effect | Formula |
|---|---|
| Overall duration (only if it's a decision) | b_D − b = Σ D_bi·W_i·(Dβ − 1)·(−Δy_b) |
| Market (yield-curve) allocation | (D_i·w_i − Dβ·D_bi·W_i)(−Δy_bi + Δy_b). Drop Dβ if duration isn't separately managed |
| Issue selection | D_i·w_i·(−Δy_ri + Δy_bi) |
| Currency (Karnosky-Singer) | (w_i − W_i)(c_i + x_i − c′) |

- Implied yield changes come from returns: Δy = −(r − x)/D.
- Book example: duration 0.87%, market allocation −0.17%, issue selection 0.17%, currency/interest allocation −0.01%. Overall excess 0.86%.
- Suitable for global bond and balanced portfolios. The risk factor is weight for equities and weighted duration for bonds. Single-currency bond books need yield-curve and credit-spread attribution instead (Campisi 2000).

## Practical rulings (EIPC questions 14 and 15)

- **Investing outside the benchmark:**
  - If it's a security decision, measure it against the *overall* benchmark as selection.
  - If it's a country or sector overweight, it's allocation measured against a chosen representative index, followed by selection against that index.
- **Transaction costs:** they land in selection by default. But costs caused by *allocation* decisions (especially in illiquid or emerging markets) should be charged to the asset allocator.

## Standards and lineage

Bacon opposed formal attribution standards in 2004, because the methods were still evolving and products need to differ. He preferred guidance for users (EIPC; see `standards.md`).

Key steps in the lineage: Brinson-Fachler (1985) → Karnosky-Singer (1994) → independent geometric methods (Burnie, Knowles and Teder; Bain; Bacon) → multi-currency geometric. He considers the arithmetic smoothing methods interesting but ultimately unnecessary.
