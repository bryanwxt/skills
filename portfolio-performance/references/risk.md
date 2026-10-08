# Risk and risk-adjusted measures (Chapter 4)

**Risk** is the uncertainty of expected outcomes. Firm-level categories: compliance (breaching a regulatory, client or internal limit, which are treated as equal), operational (errors, fraud, systems, failed trades; track error frequency even when there's no loss), counterparty, and **portfolio risk**, which is the uncertainty of meeting client expectations. Reputational risk results from failures in any of these.

**Risk managers** (portfolio managers) are paid to take risk. **Risk controllers** are paid to monitor it. Their objectives conflict, which is resolved by asking: was the return sufficient for the risk taken?

**Ex post** (historical, realised) and **ex ante** (forecast from current holdings) measures differ materially. Always label which one you mean.

Conventions: population statistics (divide by n), annualise σ by √periods-per-year, and use the same risk-free rate for every portfolio being compared.

## Variability (total risk)
- Mean absolute deviation = Σ|r_i − r̄|/n
- Variance σ² = Σ(r_i − r̄)²/n, standard deviation σ = √variance. Annualised: σ_A = σ·√t.
- Book data: monthly σ 3.87% → 13.4% annualised (portfolio). 3.76% → 13.0% (benchmark).

## Total-risk-adjusted measures
- **Sharpe ratio** SR = (r_P − r_F)/σ_P. Higher is better. When returns are negative it perversely rewards *more* volatility.
- **M²** (Modigliani and Modigliani) = r_P + SR·(σ_M − σ_P) = (r_P − r_F)·σ_M/σ_P + r_F. It's the portfolio's return scaled to benchmark risk, so it's a real return you can rank and size. Bacon prefers it over Sharpe and differential return.
  - Book data: A (7.9%, σ 5.5%) gives 6.83%. B (6.9%, σ 3.2%) gives **8.89%** (the book prints 8.74%, an arithmetic error). r_F = 2%, σ_M = 4.5%.
- **M² excess:** geometric (1+M²)/(1+b) − 1 (preferred) or M² − b.
- **Differential return** = r_P − [r_F + (b − r_F)/σ_M · σ_P]. This adjusts the benchmark to the portfolio's risk, so every portfolio gets a different hurdle, making it less useful for comparisons.

## Regression and systematic risk
- Regression: r_P = α_R + β_R·b + ε. Here β_R = Σ(r−r̄)(b−b̄)/Σ(b−b̄)².
- CAPM form: r_P − r_F = α + β(b − r_F) + ε.
  - **Jensen's alpha** α = r_P − r_F − β(b − r_F) (the "selectivity").
  - Practitioners' "alpha" usually just means excess return.
- **Bull beta / bear beta:** regressions on up-market and down-market periods only. **Beta timing ratio** = β⁺/β⁻. Above 1 suggests good timing.
- **Covariance** = Σ(r−r̄)(b−b̄)/n. **Correlation** ρ = cov/(σ_P·σ_M). β = ρ·σ_P/σ_M.
- **R²** = ρ² = systematic variance/total variance. If R² is much below about 0.8, ignore α, β and everything derived from them.
- **Systematic risk** σ_S = β·σ_M. **Specific (residual) risk** σ_ε = standard deviation of the regression residuals. Total² = systematic² + specific².
- **Treynor ratio** = (r_P − r_F)/β. It ignores specific risk, and gives the same ranking as Sharpe for fully diversified portfolios.
- **Modified Treynor** = (r_P − r_F)/σ_S. (The book prints σ_M in the denominator, which is a typo.)
- **M² for beta** = r_F + Treynor ratio (the return at β = 1).
- **Appraisal ratio** = α/σ_ε, the systematic-risk-adjusted reward per unit of specific risk.
- **Modified Jensen** = α/β (Smith and Tito). Alternative: α/σ_S.
- **Fama decomposition:** r_P − r_F = selectivity (α) + systematic risk [β(b − r_F)].
  - Fama beta β_F = σ_P/σ_M.
  - Diversification cost d = (β_F − β)(b − r_F), always ≥ 0.
  - **Net selectivity** = α − d. If it's negative, the manager didn't justify giving up diversification.
  - Useful when only total-fund returns are available (e.g. mutual funds).

## Relative risk
- **Tracking error** (tracking risk, active risk) = σ of the excess returns, using arithmetic (a_i) or geometric (g_i) excess. Always label ex post vs ex ante.
  - Closed form: TE = √(σ_P² + σ_M² − 2ρσ_Pσ_M). On the book's data that gives √(13.4² + 13.0² − 2·0.97·13.4·13.0) ≈ 3.25%.
  - The book's equation 4.38 (printed as σ_P·√((1−ρ)²)) is really σ_P·√(1−ρ²). That is specific risk, which only approximates TE when β ≈ 1. The book's example has β ≈ 1, which is why it appears to work.
- **Information ratio** IR = annualised excess return / annualised tracking error.
  - Disclose: data frequency, period, arithmetic or geometric excess, arithmetic or geometric mean, n or n−1, ex post or ex ante.
  - Rough guide (Grinold and Kahn, which Bacon endorses if sustained for 3–5 years): 0.5 good, 0.75 very good, 1.0 exceptional. Goodwin finds above 0.5 hard to sustain.
  - With a negative IR, consistent underperformance (low TE) is worse than erratic underperformance.
  - An ex ante TE in the denominator can be window-dressed by cutting bets at the measurement date.
- Book data: annualised TE 3.28%, IR = (10.42% − 11.80%)/3.28% = −0.42.

## Distribution shape
- Normal distribution: about 68% of returns within ±1σ and about 95% within ±2σ.
- **Skewness** = Σ((r−r̄)/σ)³/n (normal = 0).
- **Kurtosis** = Σ((r−r̄)/σ)⁴/n. Normal = 3. Above 3 means fat tails. Equity markets have fat tails, so normal-based TE and VaR understate tail risk.
- **d ratio** = (n_d·Σ|negative returns|)/(n_u·Σ positive returns). 0 = no losses. Lower is better.
- **Volatility skewness** = upside variance / downside variance (above 1 means positively skewed).

## Downside risk
- **Downside deviation** σ_D = √[Σ min(r_i − r_T, 0)²/n] for a minimum target r_T (risk-free rate, benchmark or client hurdle). It divides by all n. Make sure there are enough observations below the target. Alternatively fit a distribution (Sortino and Satchell).
- **Sortino ratio** = (r_P − r_T)/σ_D. Use r_F instead of r_T if r_F is higher.
- **M² for Sortino** = r_P + Sortino·(σ_DM − σ_D).
- **Upside potential ratio** = [Σ max(r_i − r_T, 0)/n]/σ_D.
- **Omega excess return** = r_P − 3·β_S·σ²_MD, where β_S = σ_D/σ_MD (style beta) and the 3 is an arbitrary risk-aversion factor. Bacon prefers M² for Sortino.
- Book data (monthly target 0.5% = 6.17% a year): σ_D 8.84% annualised, Sortino 0.48, UPR 0.20, M²_S 10.36%.

## VaR, persistence and fixed income
- **VaR:** the worst expected loss over a horizon at a confidence level (95% or 99%) under normal markets. It's not the maximum loss. It's usually ex ante but worth calculating ex post too. **VaR ratio** = VaR/assets. A strategy change can lower TE while raising tail VaR, so choose by client preference.
- **Hurst index** H = log(m)/log(n), where m = (max r − min r)/σ.
  - 0 to 0.5: mean-reverting. 0.5: random. 0.5 to 1: persistent.
  - Equity markets are about 0.7 and Nile floods about 0.9.
- **Duration:**
  - Macaulay D = Σ F_i·t_i·d^{t_i}/P, where d = 1/(1+y).
  - Modified duration = d·D.
  - **Effective duration** (bonds with options) = (P₋ − P₊)/(2·P·Δy).
- **Convexity:**
  - Σ F_i·t_i(t_i+1)·d^{t_i}.
  - Modified convexity = d²·convexity/P.
  - **Effective convexity** = (P₋ + P₊ − 2P)/(P·Δy²).
- **Duration beta** = D_portfolio/D_benchmark, the bond equivalent of equity beta.

## GIPS note
GIPS 2020 requires the **3-year annualised ex post standard deviation** (36 monthly returns) of the composite *and* benchmark at each year end. Composite and benchmark must use the same periodicity and method. Gross-of-fees returns are recommended for risk measures, and any additional measure (with its risk-free rate) must be described. See `gips-2020.md`.

## Choosing measures
- Choose a **few** measures that fit the mandate and that every party understands. They often contradict each other.
- Track the **change** in a measure over time rather than fussing over its accuracy. A sudden change signals a data error, a model change, or an intentional or unintentional change in risk. Discuss it with the manager.
- **Risk efficiency ratio** = ex post TE / ex ante TE (or ex post VaR / ex ante VaR). About 1 means the forecasting is working. Well above 1 means the model underestimates risk.

## Risk-control structure (Bacon's recommended set-up)
- Performance, risk control, legal and internal audit report to the **head of middle office**. Never to the front office or marketing.
- **Essentials:** a written risk policy, front/middle/back-office independence, firm-wide risk awareness, clear risk limits in the investment management agreement, independent risk and return attribution, risk-adjusted measures suited to the strategy, and a review process for new products, instruments and strategies.
- **Four responses to an identified risk:** ignore it (if control costs more than failure would), mitigate it (e.g. insurance), control it (limits and monitoring), or eliminate it (stop the activity).
- **Committees:** a Risk Management Committee (reports to the board, chaired by the head of risk), with Portfolio Risk, Credit Risk and Operational Risk committees under it.
