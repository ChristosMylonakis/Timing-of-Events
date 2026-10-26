# Timing-of-Events

A repo for analyzing Abbring and Van den Berg (2003) - Econometrica, creating a presentation for the reading group and thinking of extensions/uses of it.

## Contents

| Path | What |
|---|---|
| `presentation/slides.pdf` | The talk (Beamer, ~20 slides + appendix) |
| `presentation/slides_with_notes.pdf` | Same slides, each followed by a note page explaining how the step emerges. This is the study document |
| `presentation/slides.tex` | Single source for both PDFs. Edit this |
| `presentation/build.sh` | Rebuilds both PDFs (`./presentation/build.sh`, needs a LaTeX installation) |
| `figures/make_figures.py` | Produces the figures (`python3 figures/make_figures.py`) |

## How we work with GitHub here

- **`main`** is the clean version of the project.
- Work happens on a **branch** (currently `claude/busy-galileo-zhsiqs`). Each change is a **commit** with a message saying what changed.
- To see the work on github.com: open the repo, switch the branch dropdown from `main` to the working branch, and click on a PDF to view it in the browser.
- When a stage is ready, we open a **pull request** to merge the branch into `main`. There you can review changes, comment on lines, and click "Merge".
