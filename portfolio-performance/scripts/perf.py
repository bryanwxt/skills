"""Reference implementations of the core formulas in Bacon, "Practical Portfolio
Performance Measurement and Attribution" (2004). Pure Python, no dependencies.

Conventions: returns are decimals (0.05 = 5%). Weights sum to 1.
Run `python3 perf.py` to execute the self-tests, which reproduce the book's
worked examples.
"""
from __future__ import annotations

import math
from typing import Sequence

# ---------------------------------------------------------------- returns (ch 2)

def simple_return(v_start: float, v_end: float) -> float:
    return v_end / v_start - 1


def chain_link(returns: Sequence[float]) -> float:
    """Geometric (chain) linking of sub-period returns."""
    w = 1.0
    for r in returns:
        w *= 1 + r
    return w - 1


def simple_dietz(v_start: float, v_end: float, cash_flow: float) -> float:
    return (v_end - v_start - cash_flow) / (v_start + cash_flow / 2)


def modified_dietz(v_start: float, v_end: float, flows: Sequence[tuple[float, float]]) -> float:
    """flows: (amount, weight) where weight = fraction of period the flow was invested,
    e.g. (TD - Dt) / TD. End-of-day flow on day 14 of 31 -> (31-14)/31."""
    c = sum(a for a, _ in flows)
    return (v_end - v_start - c) / (v_start + sum(a * w for a, w in flows))


def irr(v_start: float, v_end: float, flows: Sequence[tuple[float, float]],
        lo: float = -0.99, hi: float = 10.0, tol: float = 1e-12) -> float:
    """Solve V_E = V_S(1+r) + sum C_t (1+r)^W_t by bisection (single period)."""
    def f(r: float) -> float:
        return v_start * (1 + r) + sum(a * (1 + r) ** w for a, w in flows) - v_end
    for _ in range(300):
        mid = (lo + hi) / 2
        if f(lo) * f(mid) <= 0:
            hi = mid
        else:
            lo = mid
        if hi - lo < tol:
            break
    return (lo + hi) / 2


def true_twr(segments: Sequence[tuple[float, float, float]]) -> float:
    """segments: (start_value, end_value_before_flow, flow_at_end).
    Each sub-period return = end_before_flow / start - 1, then chain-linked."""
    return chain_link([vb / vs - 1 for vs, vb, _ in segments])


def annualized(returns: Sequence[float], periods_per_year: int) -> float:
    n = len(returns)
    return (1 + chain_link(returns)) ** (periods_per_year / n) - 1


def gross_up(net: float, fee: float) -> float:
    return (1 + net) * (1 + fee) - 1


def net_down(gross: float, fee: float) -> float:
    return (1 + gross) / (1 + fee) - 1


# ------------------------------------------------------------ benchmarks (ch 3)

def arithmetic_excess(r: float, b: float) -> float:
    return r - b


def geometric_excess(r: float, b: float) -> float:
    return (1 + r) / (1 + b) - 1


def percentile_rank(rank: int, n: int) -> float:
    """0 = best, 1 = worst; median maps to 0.5."""
    return (rank - 1) / (n - 1)


# ------------------------------------------------------------------- risk (ch 4)

def mean(x: Sequence[float]) -> float:
    return sum(x) / len(x)


def stdev(x: Sequence[float]) -> float:
    """Population (n) standard deviation, the book's convention."""
    m = mean(x)
    return math.sqrt(sum((v - m) ** 2 for v in x) / len(x))


def annualize_sd(sd: float, periods_per_year: int) -> float:
    return sd * math.sqrt(periods_per_year)


def sharpe(rp: float, rf: float, sd_p: float) -> float:
    return (rp - rf) / sd_p


def m2(rp: float, rf: float, sd_p: float, sd_m: float) -> float:
    return rp + sharpe(rp, rf, sd_p) * (sd_m - sd_p)


def differential_return(rp: float, rf: float, b: float, sd_p: float, sd_m: float) -> float:
    return rp - rf - (b - rf) / sd_m * sd_p


def beta(rp: Sequence[float], rb: Sequence[float]) -> float:
    mp, mb = mean(rp), mean(rb)
    cov = sum((p - mp) * (q - mb) for p, q in zip(rp, rb))
    return cov / sum((q - mb) ** 2 for q in rb)


def correlation(rp: Sequence[float], rb: Sequence[float]) -> float:
    mp, mb = mean(rp), mean(rb)
    cov = sum((p - mp) * (q - mb) for p, q in zip(rp, rb)) / len(rp)
    return cov / (stdev(rp) * stdev(rb))


def jensen_alpha(rp: float, rf: float, b: float, beta_p: float) -> float:
    return rp - rf - beta_p * (b - rf)


def treynor(rp: float, rf: float, beta_p: float) -> float:
    return (rp - rf) / beta_p


def tracking_error(rp: Sequence[float], rb: Sequence[float], geometric: bool = False) -> float:
    ex = [geometric_excess(p, q) if geometric else p - q for p, q in zip(rp, rb)]
    return stdev(ex)


def information_ratio(ann_excess: float, ann_te: float) -> float:
    return ann_excess / ann_te


def downside_risk(r: Sequence[float], target: float) -> float:
    """Semi-standard deviation below target; divides by ALL n observations."""
    return math.sqrt(sum(min(v - target, 0.0) ** 2 for v in r) / len(r))


def sortino(rp: float, target: float, dd: float) -> float:
    return (rp - target) / dd


def upside_potential_ratio(r: Sequence[float], target: float) -> float:
    up = sum(max(v - target, 0.0) for v in r) / len(r)
    return up / downside_risk(r, target)


# ------------------------------------------------------------ attribution (ch 5)

def brinson(w: Sequence[float], W: Sequence[float], r: Sequence[float], b: Sequence[float],
            model: str = "BF", interaction: str = "selection") -> dict:
    """Single-period arithmetic Brinson attribution.
    model: "BHB" (allocation = (w-W)*b_i) or "BF" (allocation = (w-W)*(b_i - b)).
    interaction: "separate" (selection uses W, interaction shown) or
                 "selection" (selection uses w, interaction folded in)."""
    btot = sum(Wi * bi for Wi, bi in zip(W, b))
    alloc = [(wi - Wi) * (bi - (btot if model == "BF" else 0.0)) for wi, Wi, bi in zip(w, W, b)]
    if interaction == "separate":
        sel = [Wi * (ri - bi) for Wi, ri, bi in zip(W, r, b)]
        inter = [(wi - Wi) * (ri - bi) for wi, Wi, ri, bi in zip(w, W, r, b)]
    else:
        sel = [wi * (ri - bi) for wi, ri, bi in zip(w, r, b)]
        inter = [0.0] * len(w)
    return {"allocation": alloc, "selection": sel, "interaction": inter,
            "r": sum(wi * ri for wi, ri in zip(w, r)), "b": btot}


def geometric_attribution(w, W, r, b) -> dict:
    """Bacon/Burnie-style geometric attribution (no interaction, no residual).
    (1+S)(1+A) - 1 = (1+r)/(1+b) - 1."""
    rt = sum(wi * ri for wi, ri in zip(w, r))
    bt = sum(Wi * bi for Wi, bi in zip(W, b))
    bs = sum(wi * bi for wi, bi in zip(w, b))  # semi-notional
    alloc = [(wi - Wi) * ((1 + bi) / (1 + bt) - 1) for wi, Wi, bi in zip(w, W, b)]
    sel = [wi * ((1 + ri) / (1 + bi) - 1) * (1 + bi) / (1 + bs) for wi, ri, bi in zip(w, r, b)]
    return {"allocation": alloc, "selection": sel, "r": rt, "b": bt, "bs": bs}


def carino_factors(r_t: Sequence[float], b_t: Sequence[float]) -> list[float]:
    """Per-period scaling k_t / k so arithmetic effects sum to total r - b."""
    def k(r: float, b: float) -> float:
        return (math.log(1 + r) - math.log(1 + b)) / (r - b) if r != b else 1 / (1 + r)
    r, b = chain_link(r_t), chain_link(b_t)
    K = k(r, b)
    return [k(ri, bi) / K for ri, bi in zip(r_t, b_t)]


def grap_factors(r_t: Sequence[float], b_t: Sequence[float]) -> list[float]:
    """Effect in period T is scaled by prod_{t<T}(1+r_t) * prod_{t>T}(1+b_t)."""
    out = []
    for T in range(len(r_t)):
        f = 1.0
        for t in range(T):
            f *= 1 + r_t[t]
        for t in range(T + 1, len(b_t)):
            f *= 1 + b_t[t]
        out.append(f)
    return out


# ------------------------------------------------------------------ self-tests

def _close(a: float, b: float, tol: float = 5e-4) -> bool:
    return abs(a - b) <= tol


def _selftest() -> None:
    # Chapter 2 standard example: start 74.2, end 104.4, flow 37.1 on 14 Jan (31-day month)
    assert _close(simple_dietz(74.2, 104.4, 37.1), -0.0744)
    assert _close(modified_dietz(74.2, 104.4, [(37.1, 17 / 31)]), -0.0730)   # end of day
    assert _close(modified_dietz(74.2, 104.4, [(37.1, 18 / 31)]), -0.0721)   # start of day
    assert _close(irr(74.2, 104.4, [(37.1, 0.5)]), -0.0741)
    assert _close(irr(74.2, 104.4, [(37.1, 17 / 31)]), -0.0727)
    assert _close(true_twr([(74.2, 103.1 - 37.1, 37.1), (103.1, 104.4, 0)]), -0.0993)
    assert _close(chain_link([.12, 95 / 112 - 1, 99 / 95 - 1, 107 / 99 - 1, 115 / 107 - 1]), 0.15)
    assert _close(annualized([.105, -.056, .234, -.157, .086], 1), 0.033, 1e-3)
    # TWR vs MWR (Exhibit 2.14)
    assert _close(true_twr([(100, 200, 1000), (1200, 700, 0)]), 0.1667)
    assert _close(simple_dietz(100, 700, 1000), -0.6667)  # book prints -33.3% (erratum)
    # Chapter 3
    assert _close(geometric_excess(0.07, 0.05), 0.019)
    assert _close(geometric_excess(-0.5, -0.75), 1.0)
    assert percentile_rank(8, 15) == 0.5
    # Chapter 4 (Table 4.3/4.4)
    assert _close(sharpe(.079, .02, .055), 1.07, 5e-3)
    assert _close(m2(.079, .02, .055, .045), .0683, 5e-4)
    assert _close(m2(.069, .02, .032, .045), .0889, 5e-4)  # book prints 8.74% (erratum)
    assert _close(differential_return(.069, .02, .075, .032, .045), .010, 5e-4)
    # Chapter 5 Table 5.1
    w, W = [.4, .3, .3], [.4, .2, .4]
    r, b = [.20, -.05, .06], [.10, -.04, .08]
    bhb = brinson(w, W, r, b, "BHB", "separate")
    assert _close(sum(bhb["allocation"]), -.012) and _close(sum(bhb["selection"]), .030)
    assert _close(sum(bhb["interaction"]), .001)
    bf = brinson(w, W, r, b, "BF", "selection")
    assert _close(bf["allocation"][1], -.0104) and _close(sum(bf["selection"]), .031)
    g = geometric_attribution(w, W, r, b)
    assert _close(sum(g["allocation"]), -.0113) and _close(sum(g["selection"]), .0295)
    assert _close((1 + sum(g["allocation"])) * (1 + sum(g["selection"])) - 1,
                  geometric_excess(g["r"], g["b"]), 1e-9)
    # Multi-period linking (Table 5.8 quarterly totals)
    rq, bq = [.083, -.034, -.05, .045], [.064, -.046, -.125, .02]
    assert _close(chain_link(rq), .0386) and _close(chain_link(bq), -.0941)
    cf = carino_factors(rq, bq)
    assert _close(sum(f * (x - y) for f, x, y in zip(cf, rq, bq)), chain_link(rq) - chain_link(bq), 1e-12)
    gf = grap_factors(rq, bq)
    assert _close(sum(f * (x - y) for f, x, y in zip(gf, rq, bq)), chain_link(rq) - chain_link(bq), 1e-12)
    print("all self-tests passed")


if __name__ == "__main__":
    _selftest()
