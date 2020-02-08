# Plan de campagne

This is the source code for the plan de campagne of my 2020 internship at
Liferay.

Run `make` to compile the source code into `plan.pdf`. You will need
[Pandoc](https://pandoc.org/),
[pandoc-citeproc](https://github.com/jgm/pandoc-citeproc), and some version of
LaTeX.

If that sounds like too much effort, you can also simply go to
<https://github.com/carmenbianca/plan-de-campagne/actions> and download the
`plan.pdf` artifact generated from any given commit.

The most interesting file in this repository is `plan.md`, which contains all of
the actual text in Markdown format. The rest is annoying scaffolding. The
scaffolding is worth it, because the alternative is dealing with LaTeX syntax.
