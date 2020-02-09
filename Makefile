.DEFAULT_GOAL := all

all:
	pandoc --filter pandoc-citeproc plan.md -o plan.pdf
