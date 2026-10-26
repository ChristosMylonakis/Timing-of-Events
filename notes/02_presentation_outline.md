# Proposed presentation outline (≈18 slides, 35–40 min)

Design principle: **build each result from the previous one**. The audience should always know (a) what problem we are stuck on, (b) which assumption we add to get unstuck, and (c) what that assumption costs. A running "assumption ledger" (a small box in the slide corner that grows) makes the trade visible.

Running example throughout: **benefit sanctions ($S$) and unemployment duration ($Y$)**.

| # | Slide | Content / derivation shown | Figure | Min |
|---|---|---|---|---|
| 1 | Title | | | 0.5 |
| 2 | The question | Sanction at random time $S$ during the spell; effect on exit rate. Four difficulties: treatment is dynamic, $S$ is censored if exit comes first, selection on unobservables, no credible instrument. | timeline sketch | 2 |
| 3 | Primer I: hazards | $\theta$, $\Theta$, survival $=e^{-\Theta}$; $Y=\Theta^{-1}(E)$. Why economists model rates. | | 2 |
| 4 | Primer II: dynamic selection | $\bar\theta(t)=\lambda(t)\,\mathbb E[V\mid T\ge t]$. Constant individual hazards → declining population hazard. The risk set at month 6 is selected. | fig1 | 2.5 |
| 5 | Primer III: MPH & how it is identified | $\Pr(T>t\mid x)=\mathcal L_G(\phi(x)\Lambda(t))$; 3-step Elbers–Ridder argument ($t\downarrow0$ ratio → $\phi$; → $\Lambda$; Laplace → $G$). Competing risks: Tsiatis non-identification, MPH fixes it. | | 3 |
| 6 | Potential outcomes indexed by time | $Y^*(s)$, $s\in[0,\infty]$; observed data $Q_S$, $Q_Y$, i.e. competing risks before treatment + post-treatment durations. | | 2 |
| 7 | No anticipation | Definition, biostat vs econ reading, what it does *not* rule out (reaction to the policy regime), information-shock reinterpretation. | | 2.5 |
| 8 | Prop 1: non-identification | Statement + 2-step proof idea (Tsiatis → independent pair; define post-treatment hazard from data). Two lessons: selection ≠ causality; anticipation untestable. | | 2.5 |
| 9 | Job-search example | Anticipation vs jump models, same data. | fig2 | 2 |
| 10 | Adding structure: Assumption 2 + Model 1a | Selection only via $(X,V)$; two MPH hazards, correlated frailties, effect $\delta(t\mid s,x)$. No exclusion restriction. | | 2.5 |
| 11 | Where identification comes from (intuition) | 3 ingredients: random timing given $V$; selected comparison groups; selection learnable pre-treatment. Local vs global dependence. | fig3 | 3 |
| 12 | Step 1 (Prop 2) | Pre-treatment = MPH competing risks → $\Lambda$'s, $\phi$'s, $G$. Why Assumption 3 needs 2-D variation (quasi-exclusion). | | 2 |
| 13 | Step 2 (Prop 3): derive eq. (10) | Build $-\partial Q_S/\partial s$ term by term, integrate over $G$, invert for $\Upsilon$, differentiate → $\delta$. The $V_S$ weight = dynamic selection. | | 3 |
| 14 | Heterogeneous effects (Model 1b) | Selection on gains allowed; cost: no dependence on $s$, extra finite-moment conditions. | | 1.5 |
| 15 | Multiple spells (Model 2c) | Derive eq. (9): $V_Y(t)$ cancels; 4-case table. "Within estimator". Cost: common $V$, no cross-spell effects. | | 3 |
| 16 | The assumption ledger | Full table: what's avoided vs what's bought. | | 1.5 |
| 17 | Critiques | Identification at zero, MPH, discrete time, untestable NA, meaning of $\delta$. | | 1.5 |
| 18 | Modern connections | Staggered DiD's no-anticipation, cohort-indexed POs; hazards of hazard ratios; dynamic CIA as the alternative. | | 2 |
| 19 | Takeaways | Three bullets. | | 0.5 |

Total ≈ 40 min. If short on time, merge 3–5 into two slides and drop 14.

## Open decisions
- Slide format: **Beamer (LaTeX)** is standard for econometrics reading groups. The alternative is an HTML deck.
- Which "modern" connection to emphasise depends on what *you* work on.
- Optional backup slides: the Proposition 4 proof sketch, and the Models 2a/2b statements.
