# Timing-of-Events

A repo for analyzing Abbring and Van den Berg (2003) - Econometrica, creating a presentation for the reading group and thinking of extensions/uses of it.

## Contents

| Path | What |
|---|---|
| `notes/01_understanding_the_paper.md` | Study guide: the argument rebuilt step by step, with derivations, an assumption ledger, critiques and modern connections |
| `notes/02_presentation_outline.md` | Proposed slide-by-slide outline with timing |
| `figures/make_figures.py` | Script that produces the teaching figures (`python3 figures/make_figures.py`) |
| `figures/*.png` | Dynamic selection, the anticipation example from Section 2.4, local vs. global dependence |

## How we work with GitHub here

- **`main`** is the "clean" version of the project.
- Work happens on a **branch** (currently `claude/busy-galileo-zhsiqs`). Each change is a **commit** with a message saying what changed.
- To see the work on github.com: open the repo, click the branch dropdown (it says `main`), and pick the working branch. Markdown files, including the maths, render directly in the browser.
- When a piece of work is ready, we open a **pull request** (PR) to merge the branch into `main`. On the PR page you can read the changes, leave comments on specific lines, and click "Merge" when you are happy.
