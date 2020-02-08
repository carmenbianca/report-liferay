.DEFAULT_GOAL := all

all:
	pandoc --filter pandoc-citeproc meta.yaml plan.md -o plan.pdf
