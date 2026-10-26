# Understanding Abbring & Van den Berg (2003)

*"The Nonparametric Identification of Treatment Effects in Duration Models", Econometrica 71(5), 1491–1517.*

These notes rebuild the paper's argument in the order you need to understand it, which differs from the order the paper presents it. The aim at each step is to say **what is assumed, what it buys, and where identification comes from**.

---

## 0. The paper in one paragraph

An unemployed person may get a treatment, such as a benefit sanction, at some random time $S$ during their spell. We want the causal effect of the treatment on the exit rate from unemployment ($Y$ is the unemployment duration). The paper does three things:

1. It shows that, **without more structure, the data cannot distinguish a causal effect from selection, nor "no anticipation" from anticipation** (Proposition 1).
2. It assumes no anticipation and that all selection runs through time-invariant observed and unobserved characteristics $(X,V)$. It puts **mixed proportional hazard (MPH)** structure on both the treatment hazard and the outcome hazard. Then the treatment effect is **identified from a single spell per person, without an exclusion restriction / instrument and without a conditional-independence (selection-on-observables) assumption** (Propositions 2–4).
3. With **two spells per person** (or per "stratum" sharing the same $V$), much of that structure can be dropped. This is the duration analogue of panel fixed effects (Propositions 5–6).

The slogan is **"the timing of events carries information"**. A causal effect shows up as a *local* change in the exit hazard *right after* treatment, wherever treatment falls. Selection shows up as a *global* correlation between $S$ and $Y$.

---

## 1. A duration-models primer (what the audience needs first)

### 1.1 Hazard, survival, integrated hazard

For a duration $T \ge 0$:

- **Hazard**: $\theta(t) = \lim_{dt\downarrow 0} \Pr(T\in[t,t+dt) \mid T\ge t)/dt$. It is the instantaneous exit rate *among those still in the state*.
- **Integrated hazard**: $\Theta(t) = \int_0^t \theta(u)\,du$.
- **Survival**: $\Pr(T>t) = \exp(-\Theta(t))$.

The useful fact the paper uses in Section 2.2 is that **$\Theta(T)$ is unit exponential**. So we can always write $T = \Theta^{-1}(E)$ with $E\sim\text{Exp}(1)$. The hazard is the model, and the randomness is a standard exponential "clock". This is how the paper builds potential outcomes: $Y^*(s) = \Theta_{Y^*(s)}^{-1}(E)$.

**Why economists model hazards rather than durations.** Search theory delivers exit *rates*. Treatment can arrive mid-spell, so it is natural to let it *shift the rate from that moment on*. Censoring is also handled naturally.

### 1.2 Unobserved heterogeneity and *dynamic selection*

This is the key idea for the whole paper, and the audience will not have seen it.

Suppose people differ in an unobserved multiplicative "frailty" $V$, with individual hazard $\theta(t\mid V) = \lambda(t)\, V$. Then the **observed** (population) hazard is

$$
\bar\theta(t) = \lambda(t)\, \mathbb{E}[V \mid T \ge t],
$$

and $\mathbb{E}[V\mid T\ge t]$ **falls over time**, because high-$V$ people leave first. See `figures/fig1_dynamic_selection.png`: two types with *constant* hazards produce a *declining* population hazard.

Consequences:

- Observed duration dependence mixes true duration dependence ($\lambda$) with sorting ($V$).
- **The composition of the risk set changes over time.** People still unemployed and untreated at month 6 are a selected group. Comparing the "treated at 6" with the "not yet treated at 6" is only valid if we know how both groups were selected up to 6.

### 1.3 The MPH model and the Laplace transform

The **mixed proportional hazard** model is

$$
\theta(t\mid x, V) = \lambda(t)\,\phi(x)\,V, \qquad V \sim G,\ V\perp X .
$$

Integrating out $V$ gives

$$
\Pr(T>t\mid x) = \mathbb{E}\big[e^{-V\phi(x)\Lambda(t)}\big] = \mathcal{L}_G\big(\phi(x)\Lambda(t)\big),
$$

where $\mathcal{L}_G(z) = \mathbb{E}[e^{-zV}]$ is the **Laplace transform** of $G$. The data give one known function of the **single index** $\phi(x)\Lambda(t)$.

**How the MPH model is identified (Elbers & Ridder 1982).** This is the template the paper reuses.

1. Take the ratio of hazards for two values of $x$ as $t\downarrow 0$. Selection has not acted yet, so $\mathbb{E}[V\mid T\ge t]\to\mathbb{E}[V]$, which is finite by assumption. The ratio tends to $\phi(x_1)/\phi(x_2)$, so **$\phi$ is identified** (up to the normalization $\phi(x^*)=1$).
2. With $\phi$ known, variation in $x$ moves the index, so **$\Lambda$ is identified** (normalize $\Lambda(t^*)=1$).
3. With the index known, we know $\mathcal{L}_G$ on an interval. The Laplace transform is real-analytic and determines the distribution uniquely, so **$G$ is identified**.

Things to notice:
- Covariate variation does the work. It needs to move the hazard but does *not* have to be excluded from anything.
- The finite-mean assumption $\mathbb{E}[V]<\infty$ is needed for the $t\downarrow0$ argument.
- **Identification leans on behaviour near $t=0$** (short durations), where data are thin. This matters for the critique later.

### 1.4 Competing risks

With two durations $Y$ and $S$ we only see whichever ends first (the "identified minimum"). Cox (1959) and Tsiatis (1975) showed that **any** competing-risks data can be generated by *independent* latent durations. So dependence between risks is not identified without structure. Heckman & Honoré (1989) and Abbring & Van den Berg (2003, JRSSB) showed that **MPH structure with covariates** restores identification. This is the engine of Proposition 2.

---

## 2. The causal framework (Section 2)

### 2.1 Potential outcomes indexed by treatment time

The binary treatment is dynamically assigned. The paper turns it into a **continuum of mutually exclusive treatments** indexed by the treatment time $s\in[0,\infty]$, with $s=\infty$ meaning "never treated".

- Potential outcomes: $\{Y^*(s): s\ge0\}$. $Y^*(s)$ is the unemployment duration if we intervened to treat at $s$.
- Assignment: the random treatment time $S$.
- Observed: $Y = Y^*(S)$.

Each $Y^*(s)$ has its own hazard $\theta_{Y^*(s)}(y)$. *(Today this is exactly the staggered-adoption DiD set-up, where potential outcomes are indexed by adoption cohort $g$. See §7.)*

### 2.2 What is observed: the treatment is censored

Treatment is only observed if it happens **before** exit. If someone finds a job at month 3 and would have been sanctioned at month 5, we never see the 5. The data are therefore two **sub-survival functions**:

$$
Q_S(y,s) = \Pr(Y>y,\ S>s,\ Y>S), \qquad Q_Y(y) = \Pr(Y>y,\ Y<S).
$$

- $Q_Y$ describes people who exit *untreated*. Their $S$ is censored.
- $Q_S$ describes people treated *before* exit. We see both $S$ and the subsequent $Y$.

In words: the pre-treatment part of the data is **competing-risks** data ("exit" vs "get treated"), plus **post-treatment** durations for those treated.

### 2.3 Assumption 1: No anticipation

$$
\Theta_{Y^*(s)}(y) = \Theta_{Y^*(t)}(y) \quad \text{for all } y \le \min\{s,t\}.
$$

**The hazard path cannot depend on the *future* treatment date.** Before $s$, being "scheduled for treatment at $s$" and "scheduled for $t$" are indistinguishable in outcomes.

- In biostatistics this is a harmless "consistency"/"cause precedes effect" condition.
- **In economics it is a substantive behavioural and informational assumption.** Forward-looking agents act on information. If people know their sanction date (or learn it some time in advance), they change search effort *before* $s$, and the assumption fails.
- **What it does *not* rule out:** agents may know and react to the *process* (e.g. the sanction *rate*). That reaction is just part of every $Y^*(s)$. So the estimated effect contrasts *realized treatment times under a given policy regime*. It is **not** the effect of having the programme versus a world without it. That ex-ante effect is not identified here. This point is important and easy to miss.
- **Reinterpretation:** if information arrives before the treatment, the "real" treatment is the *information shock*. Then the assumption means "the econometrician observes the moment people learn about the treatment".

### 2.4 Proposition 1: the basic non-identification result

> For every causal model $(\{Y^*\},S)$ there is an observationally equivalent one that satisfies **no anticipation** *and* **randomized assignment** $\{Y^*\}\perp S$.

**Proof idea (Appendix), in two steps:**

1. *Pre-treatment part.* The data before treatment are competing-risks data. By Tsiatis/Miller, there is an **independent** pair $(\hat Y,\hat S)$ that reproduces the identified minimum. Use $\hat S$ as the treatment time, and use $\hat Y$'s hazard as the common pre-treatment hazard for every $Y^*(s)$. That gives no anticipation, and $\hat S$ is independent by construction.
2. *Post-treatment part.* For $y>s$, simply **define** the post-treatment hazard to match $\Pr(Y>y\mid Y>s, S=s)$ from the data.

So any data can be rationalised by "no anticipation + random assignment". Two lessons:

- **(a) Selection vs causality.** Without structure we cannot tell whether treated people exit fast because of the treatment or because fast leavers get treated. This is the usual selection problem.
- **(b) Anticipation.** We cannot tell a model *with* anticipation from one *without*. **No anticipation is untestable.** It is a maintained assumption, and the paper simply keeps it.

### 2.5 The job-search example (Section 2.4)

This is a concrete instance of (b). See `figures/fig2_anticipation_equivalence.png`.

- **Model A (perfect foresight):** the worker knows the sanction date $s$. Search effort, and therefore the exit hazard, *rises* as $s$ approaches (eq. 3), then is 1 after $s$.
- **Model B (no anticipation):** the worker only knows that sanctions arrive at a constant rate. The hazard is flat at 0.581 before $s$ and jumps to 1 at $s$.

With suitably chosen parameters (discount rates 5% vs 1.23%, a different sanction distribution), **both produce exactly the same $(Q_S,Q_Y)$**. The data only show the *mixture* hazard among those not yet treated, which is $0.581$ in both (footnote 11). The individual pre-treatment hazards $\theta_{Y^*(s)}(y)$ for $y<s$ are never observed at the $s$ that applies, because $S$ is unobserved for anyone who leaves before $s$.

**Teaching point:** one model has rich anticipation and the other has a pure jump at treatment, yet the data cannot tell them apart. That is why no anticipation has to be *assumed*.

---

## 3. What structure is added, and why each piece is there

### 3.1 Assumption 2: selection only through $(X,V)$

$$
\{Y^\dagger\} \perp \{S^\dagger\} \mid (X,V),
$$

plus absolute continuity (no ties: $\Pr(Y=S)=0$, and covariates don't determine $S$ or $Y$ exactly).

- It looks like conditional independence, **but conditions on unobservables $V$ too**. It allows selection on unobservables, provided that selection is *time-invariant* and captured by one random vector.
- $V$ must contain **everything** jointly driving treatment and outcome, including information that triggers behavioural responses.
- Time-varying unobservables are excluded in the single-spell case. They are partly allowed in Section 4.

### 3.2 Model 1a

$$
\theta_Y(t\mid S,x,V) = \begin{cases} \lambda_Y(t)\,\phi_Y(x)\,V_Y & t\le S\\ \lambda_Y(t)\,\phi_Y(x)\,\delta(t\mid S,x)\,V_Y & t>S\end{cases}
\qquad
\theta_S(t\mid x,V) = \lambda_S(t)\,\phi_S(x)\,V_S,
$$

with $V=(V_Y,V_S)\sim G$ **arbitrarily correlated**, $V\perp X$.

- **Two MPH hazards linked only through correlated frailties.** That correlation is the selection on unobservables.
- **$\delta(t\mid s,x)$ is the treatment effect**: a multiplicative shift in the exit hazard *after* treatment. It may vary with elapsed duration $t$, treatment time $s$ (and hence time since treatment $t-s$), and $x$. It is homogeneous in $V$.
- Because $\delta$ only multiplies for $t>S$, **no anticipation holds by construction**.
- Same $x$ can enter both hazards. **There is no exclusion restriction.**
- Everything is nonparametric: $\lambda_Y,\lambda_S,\phi_Y,\phi_S,\delta,G$. Mass points at 0 or $\infty$ are allowed (some never treated, some never exit).

### 3.3 The remaining regularity assumptions

- **Assumption 3**: $\{(\phi_Y(x),\phi_S(x)) : x\in\mathcal X\}$ contains a non-empty **open set in $\mathbb{R}^2$**.
  - This is *not* an exclusion restriction, but it is not free either. Covariates must move the two hazards **in non-proportional ways**. With $\phi_j(x)=e^{x'\beta_j}$ you need at least **two continuous covariates** and $(\beta_Y\ \beta_S)$ of full rank. This is a weaker relative of an exclusion restriction, and a fair point to raise in the discussion.
- **Assumption 4**: $\mathbb{E}[V_Y]<\infty$, $\mathbb{E}[V_S]<\infty$. Needed for the Elbers–Ridder "$t\downarrow0$" argument.

---

## 4. Identification in the single-spell case: where it comes from

### 4.1 The intuition, before any maths

There are three ingredients.

1. **Conditional on $(x,V)$, treatment timing is random.** Because treatment is assigned through a *hazard*, in each instant $[t,t+dt)$ a not-yet-treated person gets treated with probability $\theta_S(t\mid x,V)\,dt$. That is a coin flip (footnote 15). Equivalently, $\Lambda_S(S)\phi_S(x)V_S$ is unit exponential, independent of $(x,V)$. **This is the "randomization" the paper exploits, and no instrument is needed.**
2. **But the comparison groups at $s$ differ in their $V$ distribution.** Among people still unemployed and untreated at $s$, those treated *at* $s$ are tilted toward high $V_S$ (treated with probability $\propto V_S$), and so toward whatever $V_Y$ correlates with. This is dynamic selection again.
3. **That tilt is learnable from the pre-treatment (competing-risks) part of the data.** Before anyone is treated, $\delta$ plays no role. So the pre-treatment data identify $G$ and both baseline hazards (Proposition 2). Once we know $G$, we know *exactly* how the treated-at-$s$ group is selected, and we can strip that out of their post-treatment survival (Proposition 3).

**The "timing-of-events" picture** (`figures/fig3_local_vs_global.png`):
- A **causal effect** makes exits **bunch right after treatment, at every treatment time**. Points hug the diagonal $Y=S$ all the way along. This is *local* dependence.
- **Selection** produces a *global* correlation: early-treated people exit early. Bunching near the diagonal only happens where high types are concentrated (small $S$).
- Treatment can only act *after* it occurs, but $V$ acts *throughout*. That asymmetry is what separates them.

**Contrast with static selection models.** In a latent-index binary treatment model (Heckman-type), identification of the treatment effect requires an **exclusion restriction**. Here, timing replaces the instrument.

### 4.2 Step 1, Proposition 2: the competing-risks part

Before treatment, the data $\{Q_S^0, Q_Y\}$ come from two MPH hazards with correlated frailties. That is an **MPH competing-risks model**, and $\delta$ does not enter. By Abbring & Van den Berg (2003, JRSSB), under Assumptions 3–4:

$$
\Lambda_Y,\ \Lambda_S,\ \phi_Y,\ \phi_S,\ G \quad \text{are identified.}
$$

Logic: it is the bivariate version of Elbers–Ridder. The joint "latent" survival is $\mathcal L_G\big(\phi_Y(x)\Lambda_Y(y),\ \phi_S(x)\Lambda_S(s)\big)$. The open-set Assumption 3 lets you trace the **bivariate** Laplace transform on an open set of $\mathbb{R}^2$, and analyticity pins down all of $G$, *including the correlation between $V_Y$ and $V_S$*. This is why Assumption 3 needs two-dimensional variation.

### 4.3 Step 2, Proposition 3: recovering $\delta$ (derivation of eq. 10)

Define the integrated post-treatment hazard $\Upsilon(y\mid s,x) = \int_s^y \lambda_Y(\tau)\,\delta(\tau\mid s,x)\,d\tau$. Take $s<y$.

The density of being treated at $s$ *and still unemployed at* $y$ is $-\partial Q_S(y,s\mid x)/\partial s$. Conditional on $V$:

- density of treatment at $s$: $\lambda_S(s)\phi_S(x)V_S\, e^{-\phi_S(x)\Lambda_S(s)V_S}$
- survival to $y$ given treatment at $s$: $e^{-\phi_Y(x)V_Y[\Lambda_Y(s)+\Upsilon(y\mid s,x)]}$
- by Assumption 2 these multiply.

Integrate over $G$:

$$
-\frac{\partial Q_S(y,s\mid x)}{\partial s} = \lambda_S(s)\phi_S(x)\,\mathbb{E}\Big[V_S\, e^{-V_Y\phi_Y(x)[\Lambda_Y(s)+\Upsilon(y\mid s,x)] - V_S\phi_S(x)\Lambda_S(s)}\Big].
$$

Writing $\mathcal L_G^{(S)}(z_1,z_2)=\partial\mathcal L_G/\partial z_2 = -\mathbb{E}[V_S e^{-z_1V_Y-z_2V_S}]$ gives the paper's eq. (10):

$$
\frac{\partial Q_S(y,s\mid x)}{\partial s} = \phi_S(x)\lambda_S(s)\,\mathcal L_G^{(S)}\Big(\phi_Y(x)\big[\Lambda_Y(s)+\Upsilon(y\mid s,x)\big],\ \phi_S(x)\Lambda_S(s)\Big).
$$

- The **left side is data**.
- On the right, **everything except $\Upsilon$ is known from Step 1**.
- $\mathcal L_G^{(S)}$ is strictly increasing in its first argument, so **invert to get $\Upsilon(y\mid s,x)$**. Then $\delta(y\mid s,x) = \frac{\partial\Upsilon(y\mid s,x)/\partial y}{\lambda_Y(y)}$.

The weighting by $V_S$ inside the expectation *is* the dynamic selection of who gets treated at $s$. Knowing $G$ undoes it.

### 4.4 Heterogeneous effects: Model 1b and Proposition 4

Model 1a has $\delta$ homogeneous in unobservables. Model 1b instead lets the post-treatment hazard have its own frailty:

$$
\theta_Y(t\mid S,x,V)=\lambda_\Delta(t)\phi_\Delta(x)V_\Delta \ \ (t>S), \qquad
\delta(t\mid x,V_Y,V_\Delta) = \frac{\lambda_\Delta(t)\phi_\Delta(x)V_\Delta}{\lambda_Y(t)\phi_Y(x)V_Y},
$$

with $(V_Y,V_\Delta,V_S)$ jointly distributed.

- **Gained:** the effect varies with unobservables, and $V_\Delta$ may correlate with $V_S$. So **selection on gains** is allowed: people who benefit more may get treated earlier.
- **Lost:** $\delta$ can no longer depend on the treatment time $s$.
- **Extra assumptions:** Assumption 5 (variation in $\phi_\Delta$) and Assumption 6 ($\mathbb{E}[V_\Delta V_S]<\infty$). The finite mean is of the *product* because conditioning on being treated at $s$ reweights by $V_S$.
- **Idea of proof:** given $S$ and $Y>S$, the residual duration is again an MPH model, so Elbers–Ridder applies to it. Second derivatives of $Q_S$ in $(y,s)$, with limits $y,s\downarrow0$, identify $\phi_\Delta$, then $\Lambda_\Delta$, then the trivariate Laplace transform.

---

## 5. Multiple spells (Section 4): the panel-data analogue

**Data:** each "stratum" (an individual with two unemployment spells, siblings, twins, …) contributes two spells $(Y_1,S_1),(Y_2,S_2)$ that **share the same $V$**.

### 5.1 Models 2a/2b (Proposition 5)
These are MPH-type, with spell-specific baselines and effects. The common $V$ links the spells. Compared with single spells:
- **No covariates are needed** (no Assumption 3).
- **No finite-mean** assumption is needed.
- Covariates may correlate with $V$ (fixed-effects style).

This mirrors Honoré (1993) for MPH models with multiple spells.

### 5.2 Model 2c and the stratified partial likelihood (Proposition 6)
This is the "within estimator".

$$
\theta_{Y_k}(t\mid S_k,V)=\lambda_{Y_k}(t)\,V_Y(t)\,\delta_k(t\mid S_k)^{\mathbf 1(t>S_k)},\quad k=1,2,\ \ \lambda_{Y_1}\equiv1.
$$

- $V_Y(t)$ can be **any (time-varying) stochastic process**, as long as it is **common to both spells**.
- **No model for $S$ at all.** Treatment can depend on $V$ arbitrarily.

**Derivation (eq. 9).** Let $Y_{(1)}=\min(Y_1,Y_2)$. Given that one spell ends at $t=Y_{(1)}$, the chance that it is spell 1 is the ratio of hazards at $t$. **$V_Y(t)$ cancels** because it multiplies both:

$$
\Pr(Y_1=Y_{(1)}\mid Y_{(1)}=t,\text{histories},V) = \frac{\delta_1(t\mid S_1)^{N_{S_1}(t-)}}{\delta_1(t\mid S_1)^{N_{S_1}(t-)}+\lambda_{Y_2}(t)\,\delta_2(t\mid S_2)^{N_{S_2}(t-)}} .
$$

Four cases:
| at time $t$ | probability spell 1 ends first | identifies |
|---|---|---|
| neither treated | $1/(1+\lambda_{Y_2}(t))$ | baseline difference $\lambda_{Y_2}$ |
| only spell 1 treated | $\delta_1/(\delta_1+\lambda_{Y_2})$ | $\delta_1$ |
| only spell 2 treated | $1/(1+\lambda_{Y_2}\delta_2)$ | $\delta_2$ |
| both treated | $\delta_1/(\delta_1+\lambda_{Y_2}\delta_2)$ | (extra info) |

This is Cox's partial likelihood / conditional logit: **condition on the stratum and difference out the fixed effect**.

**What it costs:** $V$ must be identical across spells, and there must be **no causal links across spells** (no lagged duration dependence, no effect of spell-1 treatment on spell 2). Whether two unemployment spells of the same person really share the same $V$ is debatable.

---

## 6. The assumption ledger

| | Single spell (Models 1a/1b) | Multiple spells (2a/2b) | Multiple spells (2c, partial likelihood) |
|---|---|---|---|
| No anticipation | **required, untestable** | required | required |
| Exclusion restriction / IV | not needed | not needed | not needed |
| Selection on observables (CIA) | not needed | not needed | not needed |
| Parametric forms | not needed | not needed | not needed |
| Selection through time-invariant $V$ | required | required (common across spells) | $V_Y(t)$ may vary in $t$, but common across spells |
| Proportional (MPH) separability | required | required | only in $V$ vs rest |
| $V\perp X$ | required | not needed | not needed |
| Covariate variation (Assn 3) | required (2-dim) | not needed | not needed |
| Finite means of $V$ | required | not needed | not needed |
| Model for treatment $S$ | required (MPH) | required | **not needed** |
| Effect heterogeneity in $V$ | 1a: no; 1b: yes, but not in $s$ | 2a: no; 2b: yes | no |
| No cross-spell causal effects | — | required | required |
| Continuous time, no ties | required | required | required |

**The trade in one sentence:** instead of an instrument or selection on observables, the paper uses **(i) the exact timing of treatment and outcome, (ii) multiplicative separability (MPH), (iii) time-invariant unobservables, and (iv) no anticipation**.

---

## 7. Critiques and things to discuss

1. **No anticipation is untestable** (Prop. 1), and economic agents often have advance notice (e.g. warnings before sanctions, caseworker meetings). The "information shock" reinterpretation needs data on when information arrives.
2. **Identification "at zero".** The Elbers–Ridder steps use limits as durations go to 0, where data are thin. In practice estimation leans on functional form, usually parametric baselines and discrete-mass-point $G$ (Heckman–Singer). Gaure, Røed & Zhang (2007, J. Econometrics) run Monte Carlo assessments of how well the timing-of-events approach works in practice.
3. **Proportionality is doing heavy lifting.** It is what lets the pre-treatment competing-risks data reveal $G$. Without MPH, Tsiatis non-identification bites again.
4. **Assumption 3 is a quasi-exclusion restriction.** You need covariates that shift the two hazards differently.
5. **Continuous time.** Real data are monthly or weekly. Ties ($Y$ and $S$ in the same interval) blur the "local" signal. The paper itself warns that time-aggregating to a binary treatment indicator throws away the identifying information.
6. **Interpretation of $\delta$.** It is a *hazard ratio conditional on $V$*, not an effect on mean duration or on the population hazard. Turning it into, e.g., the effect on expected duration requires $G$ and the baseline hazards.
7. **Policy-relevant vs. identified effect.** The identified effect is "treated at $s$ vs. later, under the current regime", not "programme vs. no programme" (ex-ante effects of the threat of treatment are not identified).

---

## 8. Connections to modern methods (for the last 1–2 slides)

*(Check exact citations before putting them on slides.)*

1. **Staggered-adoption DiD / event studies.** Potential outcomes indexed by adoption date $Y_t(g)$ are the discrete-time analogue of $Y^*(s)$. The **"no anticipation" assumption** in Callaway & Sant'Anna (2021), Sun & Abraham (2021), Borusyak, Jaravel & Spiess (2024) is *exactly* Assumption 1. Prop. 1 shows why it must be assumed and not tested. In DiD, pre-trend tests jointly test parallel trends *and* no anticipation. The difference is how selection is handled: **DiD uses parallel trends (additive, time-invariant unobservables in levels); ToE uses multiplicative, time-invariant frailty in hazards, plus random timing**. Prop. 6 *is* a fixed-effects estimator.
2. **"The hazards of hazard ratios".** In epidemiology, population hazard ratios are not causal even in an RCT, because of dynamic selection (Hernán 2010; Martinussen, Vansteelandt & Andersen 2020). Abbring & Van den Berg define the effect *conditional on the frailty $V$*, which is precisely the fix. The cost is the structure needed to recover $V$'s distribution. Related: Ham & LaLonde (1996) on RCTs with duration outcomes, and Abbring & Van den Berg (2005) on social experiments with durations.
3. **Dynamic treatment assignment under sequential unconfoundedness.** Robins' g-methods and marginal structural models, and in labour economics Sianesi (2004), Crépon et al. (2009), Vikström (2017), Kastoryano & Van der Klaauw (2022). These drop $V$ and assume **dynamic selection on observables**. ToE and dynamic CIA are the two main alternatives, and they trade different assumptions.
4. **Later structural work.** Abbring & Heckman (2007, Handbook of Econometrics ch. 72) and Heckman & Navarro (2007) on dynamic discrete choice and dynamic treatment effects, both building on the no-anticipation concept from this paper.
