# Abbring & Van den Berg (2003), built up step by step

## Plan (to be filled one section at a time)
1. One duration: survival, hazard, integrated hazard
2. People differ: unobserved heterogeneity and dynamic selection
3. The mixed proportional hazard (MPH) model
4. Two durations racing: competing risks
5. Adding a treatment: potential outcomes indexed by treatment time, no anticipation
6. What we actually observe
7. The model of the paper (Model 1a)
8. Identification, step by step
9. Extensions: heterogeneous effects, multiple spells
10. Connections: DiD with staggered adoption, sequential exogeneity, traps

---

## 1. One duration

**Object**
- $Y \ge 0$: time spent in a state (e.g. unemployment duration); $y$ a particular value.
- Usual descriptions: density $f(y)$, CDF $F(y)$.
- **Survival function**: $S(y) = \Pr(Y > y) = 1 - F(y)$.
  - Share still in the state at $y$.

**Hazard rate**
- $\theta(y) = \lim_{dy \downarrow 0} \dfrac{\Pr(y \le Y < y+dy \mid Y \ge y)}{dy} = \dfrac{f(y)}{S(y)}$
- Meaning: exit rate *among those still in the state* at $y$.
- $\theta(y)\,dy \approx$ probability of leaving in the next instant, given you are still there.
- Not a probability: it is a rate, and can exceed 1.

**Integrated hazard**
- $\Theta(y) = \int_0^y \theta(u)\,du$
- Since $\theta(y) = f(y)/S(y) = -\frac{d}{dy}\log S(y)$:
  - $S(y) = \exp\big(-\Theta(y)\big)$
- So hazard, survival and density are three descriptions of the same distribution.

**Examples**
- Constant hazard $\theta(y) = c$:
  - $S(y) = e^{-cy}$, i.e. exponential.
  - Memoryless: the chance of leaving tomorrow does not depend on how long you have been unemployed.
- $\theta(y)$ decreasing: **negative duration dependence** (the longer unemployed, the harder to leave).
- $\theta(y)$ increasing: **positive duration dependence** (e.g. benefits running out).

**Running example (the paper's)**
- Unemployed people receive unemployment benefits.
- The benefit agency can impose a **sanction**: a temporary cut in benefits.
  - Typically a punishment, e.g. for not applying to enough jobs.
- Question: does a sanction make people find a job faster?
- $Y$: unemployment duration. $S$: the moment the sanction is imposed.

**Why model hazards? Reason 1: treatment arrives *during* the spell**
- Textbook set-up: treatment $D \in \{0,1\}$ is fixed *before* the outcome. Compare $Y$ across $D=1$ and $D=0$.
- Here, a person is unsanctioned until $S$ and sanctioned afterwards.
- Tempting fix: $D = 1$ if "sanctioned before finding a job", i.e. $D = \mathbf 1\{S < Y\}$.
  - Problem: $D$ depends on the outcome $Y$ itself.
- Example with **zero effect**:
  - Rule: everyone still unemployed at month 5 gets sanctioned, so $S = 5$ for all.
  - Then $D = 1 \iff Y > 5$.
  - So the "sanctioned" all have $Y > 5$, and the "unsanctioned" all have $Y \le 5$.
  - $\mathbb E[Y \mid D=1] > \mathbb E[Y \mid D=0]$: sanctions *look* like they lengthen unemployment, purely by construction.
- Hazard formulation: the effect is a change in the exit rate *from the moment of treatment on*.
  - $\theta(y) = \theta_0(y)$ for $y \le S$, and $\theta(y) = \theta_0(y)\,\delta$ for $y > S$.
  - $\delta = 1$: no effect. $\delta > 1$: the sanction speeds up exit.
  - At each moment we only use who is treated *so far*, never the future.

**Why model hazards? Reason 2: incomplete spells (censoring)**
- The data stop at month 12. Some people are still unemployed then.
  - For them we only know $Y > 12$.
- Dropping them is biased: we drop exactly the long spells.
- Likelihood with $n$ people, where $d_i = 1$ if person $i$'s exit is observed:
  - exit observed at $y_i$: contributes $f(y_i)$;
  - still unemployed at 12: contributes $\Pr(Y > 12) = S(12)$.
  - $\mathcal L = \prod_i f(y_i)^{d_i}\, S(12)^{1-d_i}$
- Use $f = \theta S$ and $S = e^{-\Theta}$, and write $c_i = \min(y_i, 12)$ for the time person $i$ is observed:
  - $\log \mathcal L = \sum_i \big[\, d_i \log \theta(y_i) \;-\; \Theta(c_i) \,\big]$
- Reading:
  - Everyone contributes $-\Theta$ over the time they were observed at risk.
  - Only observed exits add $\log\theta$ at the exit moment.
  - Censored people are used, just without an exit term.
- In the paper the key censoring is of $S$: if someone finds a job before being sanctioned, we never see when the sanction would have come.

**A way to generate a duration (used in Section 5)**
- Goal: produce a random $Y$ with a given hazard $\theta(y)$.
- Recipe:
  1. Draw $E$ with $\Pr(E > e) = e^{-e}$ (a unit exponential): a random "budget".
  2. As time passes, the person accumulates hazard $\Theta(y)$, which increases in $y$.
  3. Exit happens when the accumulated hazard reaches the budget: $Y$ solves $\Theta(Y) = E$, i.e. $Y = \Theta^{-1}(E)$.
- Why $Y$ has the right distribution:
  - Still unemployed at $y$ $\iff$ budget not yet used up at $y$ $\iff$ $E > \Theta(y)$ (since $\Theta$ is increasing).
  - So $\Pr(Y > y) = \Pr(E > \Theta(y)) = e^{-\Theta(y)}$ (plug $e = \Theta(y)$ into step 1).
  - That is exactly $S(y)$ from above, so $Y$ has hazard $\theta$. ✓
- Example: constant hazard $c$, so $\Theta(y) = cy$ and $Y = E/c$.
  - Higher $c$ means the budget is used up faster, so $Y$ is shorter.
- Why it matters:
  - $Y$ = (model) applied to (luck).
  - $\Theta$ carries the economics and may depend on treatment.
  - $E$ is pure chance with the same distribution for everyone.
  - Section 5: "treated at $s$" vs "treated later" changes $\Theta$, not the luck.
