# Timing-of-Events

A repo for analyzing Abbring and Van den Berg (2003) - Econometrica, creating a presentation for the reading group and thinking of extensions/uses of it.

## Contents

| Path | What |
|---|---|
| `presentation/talk.pdf` | The talk, "Duration Models and Treatment Effects" (Beamer). 24 numbered slides, then an appendix with a proof for every derivation, reachable through the Proof/Back buttons |
| `presentation/talk.tex` | Source of the talk. Build with `cd presentation && pdflatex talk.tex` (run twice) |
| `paper_explained.pdf` | Study document: the paper built up step by step, with derivations |
| `paper_explained.tex` | Source of the study document. Build with `pdflatex paper_explained.tex` (run twice) |
| `figures/make_figures.py` | Produces all figures (`python3 figures/make_figures.py`, needs numpy and matplotlib) |

## Notation

- `Y`: unemployment duration. `D`: time of treatment (the paper's `S`).
- Bars (`S̄`, `θ̄`) mark observed objects, i.e. averaged over the unobserved types `V`.
- `S̄₀`, `θ̄₀^Y`, `θ̄₀^D`: observed survival and cause-specific hazards before treatment. `S̄₁`: survival after treatment.
- `Λ_Y(t|x) = φ_Y(x)Λ_Y(t)`: integrated baseline with covariates. `Δ(y|d,x)`: integrated post-treatment hazard.
