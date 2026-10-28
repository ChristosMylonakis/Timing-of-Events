"""Teaching figures for the Abbring & Van den Berg (2003) presentation.

Run from the repo root:  python3 figures/make_figures.py
Produces three PNGs in figures/.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

OUT = Path(__file__).resolve().parent
plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False})


# ---------------------------------------------------------------------------
# Figure 1: dynamic selection. Two types with constant individual hazards.
# The observed hazard falls over time even though nobody's hazard changes,
# because the high-hazard type leaves first.
# ---------------------------------------------------------------------------
def fig_dynamic_selection():
    y = np.linspace(0, 6, 400)
    v_lo, v_hi, p_hi = 0.3, 1.5, 0.5
    surv_lo, surv_hi = np.exp(-v_lo * y), np.exp(-v_hi * y)
    share_hi = p_hi * surv_hi / (p_hi * surv_hi + (1 - p_hi) * surv_lo)
    pop_hazard = share_hi * v_hi + (1 - share_hi) * v_lo
    pop_surv = p_hi * surv_hi + (1 - p_hi) * surv_lo

    # Right panel: the same observed survival is fitted exactly by ANY type
    # distribution G, with baseline Lambda_G = L_G^{-1}(S_bar). Each G (all with
    # E[V] = 1) implies a different baseline hazard lambda_G(y).
    def two_type_laplace(a, v1, v2):
        return 0.5 * np.exp(-a * v1) + 0.5 * np.exp(-a * v2)

    def invert(L, target, hi=200.0):
        lo, up = np.zeros_like(target), np.full_like(target, hi)
        for _ in range(200):
            mid = 0.5 * (lo + up)
            too_high = L(mid) > target  # L decreasing: need larger a
            lo = np.where(too_high, mid, lo)
            up = np.where(too_high, up, mid)
        return 0.5 * (lo + up)

    m = 0.5 * (v_lo + v_hi)
    specs = [
        ("no heterogeneity: all duration dependence", lambda a: np.exp(-a), "tab:gray"),
        ("some heterogeneity", lambda a: two_type_laplace(a, 0.6, 1.4), "tab:purple"),
        ("strong heterogeneity: no duration dependence",
         lambda a: two_type_laplace(a, v_lo / m, v_hi / m), "tab:green"),
    ]

    fig, ax = plt.subplots(1, 2, figsize=(10, 3.8))
    ax[0].plot(y, np.full_like(y, v_hi), "--", color="tab:red", label="high type: hazard 1.5")
    ax[0].plot(y, np.full_like(y, v_lo), "--", color="tab:blue", label="low type: hazard 0.3")
    ax[0].plot(y, pop_hazard, color="black", lw=2.5, label="observed hazard")
    ax[0].set(xlabel="elapsed duration y", ylabel="hazard rate", title="Individual vs. observed hazard")
    ax[0].legend(frameon=False, fontsize=9)
    for label, L, c in specs:
        Lam = invert(L, pop_surv)
        lam = np.gradient(Lam, y)
        ax[1].plot(y[1:], lam[1:], color=c, lw=2, label=label)
    ax[1].set(xlabel="elapsed duration y", ylabel=r"implied baseline $\lambda(y)$", ylim=(0, 1.1),
              title="Same data, different stories")
    ax[1].legend(frameon=False, fontsize=8, loc="lower left")
    fig.tight_layout()
    fig.savefig(OUT / "fig1_dynamic_selection.png", dpi=200)
    # single panels for slides
    for i, name in enumerate(["fig1a_observed_hazard.png", "fig1b_same_data.png"]):
        extent = ax[i].get_tightbbox(fig.canvas.get_renderer()).transformed(fig.dpi_scale_trans.inverted())
        fig.savefig(OUT / name, dpi=200, bbox_inches=extent.expanded(1.03, 1.03))
    plt.close(fig)


# ---------------------------------------------------------------------------
# Figure 2: the paper's Section 2.4 example (Proposition 1 in action).
# Model A: perfect foresight about the sanction date s (full anticipation).
# Model B: only the arrival rate of sanctions is known (no anticipation).
# Both models produce exactly the same observable data (Q_S, Q_Y).
# ---------------------------------------------------------------------------
def fig_anticipation_equivalence():
    rho = 0.05
    y = np.linspace(0, 6, 600)
    pooled = (4 * rho + 3) / (4 * rho**2 + 10 * rho + 5)  # = 0.581, observed hazard before treatment

    def hazard_A(y, s):  # equation (3)
        pre = 2 * rho / ((2 * rho + 1) * np.exp(rho * (s - y)) - 1)
        return np.where(y <= s, pre, 1.0)

    def hazard_B(y, s):  # constant 0.581 before s, 1 after
        return np.where(y <= s, pooled, 1.0)

    fig, ax = plt.subplots(1, 2, figsize=(10, 3.8), sharey=True)
    for s, c in zip([1, 2.5, 4], ["tab:blue", "tab:green", "tab:purple"]):
        ax[0].plot(y, hazard_A(y, s), color=c, label=f"treated at s = {s}")
        ax[1].plot(y, hazard_B(y, s), color=c, label=f"treated at s = {s}")
    for a, title in zip(ax, ["Model A: knows s in advance (anticipation)",
                             "Model B: only knows sanction rate (no anticipation)"]):
        a.axhline(pooled, color="black", ls=":", lw=1)
        a.set(xlabel="unemployment duration y", title=title, ylim=(0, 1.1))
        a.legend(frameon=False, fontsize=9, loc="lower right")
    ax[0].set_ylabel(r"potential hazard $\theta_{Y^*(s)}(y)$")
    ax[0].annotate("observed hazard among\nnot-yet-treated = 0.581\n(same in both models)",
                   xy=(0.3, pooled), xytext=(0.3, 0.2), fontsize=9,
                   arrowprops=dict(arrowstyle="->", lw=0.8))
    fig.tight_layout()
    fig.savefig(OUT / "fig2_anticipation_equivalence.png", dpi=200)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Figure 3: the "timing of events" intuition.
# World A: a causal effect (delta = 4), no selection (V_Y independent of V_S).
# World B: no causal effect (delta = 1), strong selection (V_Y = V_S).
# A causal effect makes exits bunch right after treatment, whenever treatment happens
# (local dependence). Selection makes S and Y correlated in general (global dependence).
# ---------------------------------------------------------------------------
def simulate(n, delta, correlated, rng):
    types = np.array([0.25, 2.0])
    v_s = types[rng.integers(0, 2, n)]
    v_y = v_s if correlated else types[rng.integers(0, 2, n)]
    S = rng.exponential(1 / (0.6 * v_s))
    Y0 = rng.exponential(1 / v_y)                      # exit time if never treated
    post = S + rng.exponential(1 / (delta * v_y))     # memoryless restart at S with hazard delta*V_Y
    Y = np.where(Y0 < S, Y0, post)
    return S, Y


def fig_local_vs_global():
    with plt.rc_context({"font.size": 15, "lines.linewidth": 3}):
        _fig_local_vs_global()


def _fig_local_vs_global():
    rng = np.random.default_rng(1)
    h = 0.25  # "soon after treatment"
    worlds = [("World A: causal effect, no selection\n" + r"$\delta=4$, $V_Y \perp V_D$", 4.0, False, "tab:blue"),
              ("World B: no effect, pure selection\n" + r"$\delta=1$, $V_Y = V_D$", 1.0, True, "tab:orange")]
    fig, ax = plt.subplots(1, 3, figsize=(15, 4.8))
    bins = np.array([0, 0.5, 1, 1.5, 2, 3, 4, 5])
    mids = 0.5 * (bins[:-1] + bins[1:])
    for k, (title, delta, corr, col) in enumerate(worlds):
        # scatter: treated only, quick exits highlighted
        D, Y = simulate(2500, delta, corr, rng)
        tr = D < Y
        quick = tr & (Y - D < h)
        ax[k].scatter(D[tr & ~quick], Y[tr & ~quick], s=10, color="lightgray", label="treated, later exit")
        ax[k].scatter(D[quick], Y[quick], s=18, color="crimson", label=f"exit within {h} of treatment")
        ax[k].plot([0, 6], [0, 6], color="black", lw=1)
        ax[k].set(xlim=(0, 5), ylim=(0, 6), xlabel="treatment time D", title=title)
        ax[k].legend(frameon=False, fontsize=12, loc="upper left", markerscale=2)
        # ratio: exit soon after treatment, treated at D vs. not yet treated at D
        D, Y = simulate(400000, delta, corr, rng)
        ratio = []
        for a, b, m in zip(bins[:-1], bins[1:], mids):
            treated = (D >= a) & (D < b) & (D < Y)
            at_risk = (Y > m) & (D > m)
            ratio.append(((Y - D) < h)[treated].mean() / ((Y < m + h) & (Y < D))[at_risk].mean())
        ax[2].plot(mids, ratio, "o-", color=col, lw=2.5, label=title.split(":")[0])
    ax[0].set_ylabel("outcome duration Y  (treated only)")
    ax[2].axhline(1, color="black", lw=1, ls=":")
    ax[2].axhline(4, color="tab:blue", lw=1, ls="--")
    ax[2].text(5.0, 4.1, r"$\delta=4$", color="tab:blue", ha="right")
    ax[2].set(xlabel="treatment time D", ylim=(0, 4.8),
              title="Exit soon after treatment:\ntreated vs. not yet treated (ratio)")
    ax[2].legend(frameon=False, fontsize=13)
    fig.tight_layout()
    fig.savefig(OUT / "fig3_local_vs_global.png", dpi=200)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Figure 4: why covariates identify the competing-risks model.
# The data reveal the Laplace transform L(a, b) = E[exp(-a V_Y - b V_S)] only at the
# points (a, b) = (phi_Y(x) Lambda_Y(t), phi_S(x) Lambda_S(t)).
# Without covariates these points form a curve (Tsiatis non-identification);
# with covariates that shift the two hazards non-proportionally they fill open sets.
# ---------------------------------------------------------------------------
def fig_competing_risks_geometry():
    t = np.linspace(0.01, 2.2, 300)
    lam_y, lam_s = t, t**1.6
    rng = np.random.default_rng(0)
    x = rng.uniform(-0.35, 0.35, size=(1500, 2))
    phi_y = np.exp(x[:, 0] + 0.3 * x[:, 1])
    phi_s = np.exp(0.3 * x[:, 0] + x[:, 1])

    fig, ax = plt.subplots(1, 2, figsize=(10, 4.2), sharex=True, sharey=True)
    ax[0].plot(lam_y, lam_s, color="black", lw=2.5)
    ax[0].set_title("No covariates: data reveal $L$ only on a curve")
    ax[1].plot(lam_y, lam_s, color="black", lw=1, ls=":")
    for tt, c in zip([0.5, 1.0, 1.6], ["tab:blue", "tab:green", "tab:purple"]):
        ax[1].scatter(phi_y * tt, phi_s * tt**1.6, s=2, alpha=0.4, color=c, label=f"t = {tt}")
    ax[1].set_title("Covariates: data reveal $L$ on open sets")
    ax[1].legend(frameon=False, fontsize=9, markerscale=5, loc="upper left")
    for a in ax:
        a.set(xlim=(0, 2.6), ylim=(0, 3.6),
              xlabel=r"$\Lambda_Y(t\mid x)$", ylabel=r"$\Lambda_D(t\mid x)$")
    fig.tight_layout()
    fig.savefig(OUT / "fig4_competing_risks_geometry.png", dpi=200)
    plt.close(fig)


if __name__ == "__main__":
    fig_dynamic_selection()
    fig_anticipation_equivalence()
    fig_local_vs_global()
    fig_competing_risks_geometry()
    print("figures written to", OUT)
