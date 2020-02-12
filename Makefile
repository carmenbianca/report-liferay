.DEFAULT_GOAL := all

all:
	pandoc --filter pandoc-citeproc --listings plan.md -o plan.pdf
