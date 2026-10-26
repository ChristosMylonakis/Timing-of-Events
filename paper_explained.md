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
- $T \ge 0$: time spent in a state (e.g. unemployment duration).
- Usual descriptions: density $f(t)$, CDF $F(t)$.
- **Survival function**: $S(t) = \Pr(T > t) = 1 - F(t)$.
  - Share still in the state at $t$.

**Hazard rate**
- $\theta(t) = \lim_{dt \downarrow 0} \dfrac{\Pr(t \le T < t+dt \mid T \ge t)}{dt} = \dfrac{f(t)}{S(t)}$
- Meaning: exit rate *among those still in the state* at $t$.
- $\theta(t)\,dt \approx$ probability of leaving in the next instant, given you are still there.
- Not a probability: it is a rate, and can exceed 1.

**Integrated hazard**
- $\Lambda(t) = \int_0^t \theta(u)\,du$
- Since $\theta(t) = f(t)/S(t) = -\frac{d}{dt}\log S(t)$:
  - $S(t) = \exp\big(-\Lambda(t)\big)$
- So hazard, survival and density are three descriptions of the same distribution.

**Examples**
- Constant hazard $\theta(t) = c$:
  - $S(t) = e^{-ct}$, i.e. exponential.
  - Memoryless: the chance of leaving tomorrow does not depend on how long you have been unemployed.
- $\theta(t)$ decreasing: **negative duration dependence** (the longer unemployed, the harder to leave).
- $\theta(t)$ increasing: **positive duration dependence** (e.g. benefits running out).

**Why economists model hazards rather than $T$ directly**
- Theory delivers rates: in job search, exit rate $=$ offer arrival rate $\times$ Pr(accept).
- Things that happen *during* the spell enter naturally:
  - e.g. a sanction at time $s$ changes the hazard from $s$ onward.
- Spells cut off by the end of the data (censoring) are easy to handle.

**One technical fact (used by the paper)**
- $\Lambda(T) \sim \text{Exp}(1)$, i.e. a unit exponential.
- Equivalently, $T = \Lambda^{-1}(E)$ with $E \sim \text{Exp}(1)$.
- Reading: the hazard is the model; $E$ is pure "luck".
