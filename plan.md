---
title: Plan de campagne TODO catchy title
author: Carmen Bianca Bakker, NHL Stenden Hogeschool
date: February 2020

documentclass: report
papersize: a4
lang: en-GB

toc: true
numbersections: true

filters:
    - pandoc-citeproc
bibliography: plan.bib
csl: apa.csl
link-citations: true
---

# Introduction

This is the *plan de campagne* (plan of action, Dutch: plan van aanpak) for my
end-of-study internship. I am Carmen Bianca Bakker, and follow a bachelor in
software engineering (Dutch: informatica) at NHL Stenden University of Applied
Sciences. My internship is at Liferay International Ltd. in Dublin, a daughter
company of Liferay Inc. in the United States. The companies will henceforth be
referred to as simply "Liferay". The internship lasts approximately 5 months
between 3 February 2020 and 30 June 2020. My job title at Liferay is "Paralegal
Engineering Intern".

The plan de campagne will detail the context of the internship, the problem that
I was brought in to solve, the research that will be conducted to TODO, the
project that will be undertaken, and the planning to bind everything together.

TODO: The shortest possible summary of the internship here.

TODO: Summarise each chapter individually.

# Context

This chapter details the context in which the internship takes place. It also
describes the problem that the internship is supposed to tackle, why this
problem is important, and therefore the motivation for the internship project.

## Liferay

Liferay Inc. is an international enterprise that is chiefly responsible for the
Liferay Digital Experience Platform (DXP), TODO describe DXP here. Liferay's
mission statement is "By building a vibrant business, making technology useful,
and investing in communities, we make it possible for people to reach their full
potential to serve others." Its slogan is "Enterprise. Open Source. For Life."
[@liferay-about]

## Legal

The "Open Source" aspect of Liferay involves Free and Open Source Software
(FOSS) licensing. Licensing involves Legal. This internship takes place within
the context of Liferay's Legal department. I will be working under Matija
Šuklje, Senior Counsel at Liferay. Matija is chiefly responsible for Liferay's
Intellectual Property (IP), specifically anything that involves the "©" symbol
and software copyright and licensing. The "™" symbol is managed by Kirstin
Huniar, and is not relevant to this internship. [@suklje-2019]

Beside FOSS licensing, Legal is also responsible for all other matters of law.
Like trademarks, these are not relevant to the internship, but mentioned for
completeness' sake.

## Engineering

Though this internship does not take place within the context of Liferay's
Engineering department, it is nevertheless important. Engineering is responsible
for creating Liferay's products. As part of creating Liferay's products, they
almost always interact with FOSS---either Liferay's, or a dependency's.

## Dublin office

Liferay has offices all over the globe. Its global headquarters are in Los
Angeles. The international office is Dublin, which is the site of this
internship. The Dublin office hosts approximately twenty employees working on
Human Resources, Legal, finances, sales, consulting, and other. Remote workers
are also registered as working for the Dublin office.

## The problem

### What

Liferay has a lot of software under various licenses. Liferay gives legal
assurances to its customers about its Intellectual Property, and therefore needs
to make sure that all code is correctly licensed. However, the current methods
of assuring the correctness of its licensing are manual. This does not scale in
an economically viable way.

### Who

Legal is responsible for verifying the licensing of Liferay's products.
Engineering interacts with licensed products, and may be affected by steps taken
to address the problem.

Matija Šuklje is the instigator of the project to tackle this problem.

### When

"When" is not strictly applicable, although the issue started being more
apparent as the product became too big to audit manually on a commercially
reasonable scale.

### Why

The work on licensing compliance is important for several reasons:

- Potential copyright violations provide legal and reputational risks, and
  potential loss of revenue and business.
- Copyright violations would also affect customers, who would be in breach of
  copyright law.
- Crudely put, breaking copyright law is illegal. [@berne-1886]

The manual work is a problem because:

- Manual verification of licensing takes up a lot of (expensive) time by legal
  experts.
- When a problem is identified, the feedback loop between Legal and Engineering
  is inefficient, and creates a bottleneck.

### Where

"Where" is not strictly applicable. The problem is in the codebase.

### The cause

The main cause of the problem is the quantity of files that need to be checked
for compliance. A small amount of files can be verified by hand, but thousands
cannot. Alternatively, there would be no need to verify compliance if all
engineers were completely diligent in introducing copyrighted code. However,
human error is unavoidable, so verification is mandatory.

## History

There is some tangent history to the problem, but the exact lines are blurry.
Liferay has an inbound and outbound licensing policy [@liferay-inbound;
@liferay-outbound], but they do not scale.

Liferay's internal *Source Formatter* tool [@liferay-source-formatter] also
checks some licensing compliance aspects, but it is not thorough enough. Source
Formatter is run as a linter in Liferay's Continuous Integration (CI) system.

Liferay also uses FOSSology and FOSSID as tools that reduce the workload of
Legal, but they are not automated.

## The project

The project of this internship is---in the simplest of terms---to make the
problem as described above go away. Chapter \ref{ch:project-definition}
describes the project in full. This section TODO

# Project definition {#ch:project-definition}

# Research

# Project activities

# Project boundaries

# Quality assurance

# Planning

# References {-}

<div id="refs"></div>

# Appendix {-}
