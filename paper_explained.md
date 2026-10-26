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

**Why economists model hazards rather than $Y$ directly**
- Theory delivers rates.
  - Job search: exit rate $=$ job-offer arrival rate $\times$ Pr(accept offer).
- Treatment status can change *during* the spell.
  - Someone sanctioned at month 5 is untreated in months 0–5 and treated after.
  - A regression of $Y$ on "ever sanctioned" cannot express this.
    - It also has a built-in bias: people who leave early have no time to be sanctioned.
  - A hazard is defined moment by moment, so we can write
    - $\theta(y)$ = baseline for $y \le 5$; baseline $\times\,\delta$ for $y > 5$.
- Incomplete spells (censoring).
  - The data end at month 12, and someone is still unemployed then.
  - We only know $Y > 12$, not $Y$.
  - With hazards they still count: they were at risk at every month up to 12 and never left.
    - Their likelihood contribution is $S(12)$.

**A way to generate a duration (used in Section 5)**
- Draw a random "budget" $E \sim \text{Exp}(1)$, i.e. $\Pr(E > e) = e^{-e}$.
- The person accumulates hazard $\Theta(y)$ as time passes.
- They exit when the accumulated hazard uses up the budget: $Y = \Theta^{-1}(E)$.
- Check: $\Pr(Y > y) = \Pr(E > \Theta(y)) = e^{-\Theta(y)} = S(y)$. ✓
- Why useful:
  - It separates the **model** ($\Theta$, which can depend on treatment) from **luck** ($E$).
  - The paper builds potential outcomes this way:
    - change $\Theta$ (e.g. treat at $s$ or not), keep the same luck $E$.
