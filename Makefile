.DEFAULT_GOAL := all

all:
	pandoc --filter pandoc-citeproc --listings --pdf-engine=xelatex plan.md -o plan.pdf
