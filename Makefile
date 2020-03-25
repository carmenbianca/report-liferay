.DEFAULT_GOAL := all

all: gantt.svg
	pandoc --filter pandoc-citeproc --listings --pdf-engine=xelatex report.md -o report.pdf

gantt.svg:
	python3 create_gantt.py
