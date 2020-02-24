.DEFAULT_GOAL := all

all: gantt.svg
	pandoc --filter pandoc-citeproc --listings --pdf-engine=xelatex plan.md -o plan.pdf

gantt.svg:
	python3 create_gantt.py
