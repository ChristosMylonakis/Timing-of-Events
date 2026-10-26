#!/usr/bin/env bash
# Build the slides and the slides-with-notes study version.
set -euo pipefail
cd "$(dirname "$0")"
for i in 1 2; do pdflatex -interaction=nonstopmode -halt-on-error slides.tex > /dev/null; done
for i in 1 2; do pdflatex -interaction=nonstopmode -halt-on-error -jobname=slides_with_notes "\def\withnotes{1}\input{slides.tex}" > /dev/null; done
rm -f ./*.aux ./*.log ./*.nav ./*.out ./*.snm ./*.toc ./*.vrb
echo "Built slides.pdf and slides_with_notes.pdf"
