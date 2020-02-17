---
title: "Plan de campagne: Automated Copyright And Licensing Compliance"
author: Carmen Bianca Bakker, NHL Stenden Hogeschool
date: February 2020

pdf-engine: xelatex

documentclass: report
papersize: a4
lang: en-GB

toc: true
toc-depth: 1
numbersections: true

filters:
    - pandoc-citeproc
bibliography: plan.bib
csl: apa.csl
link-citations: true

header-includes:
    - \usepackage[section=chapter,toc]{glossaries}
    - \makenoidxglossaries
    - \input{glossary}
    - \lstset{breaklines=true,breakatwhitespace=true,frame=single,numbers=left}
---

# Introduction {-}

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

The "\gls{open-source}" aspect of Liferay involves \gls{foss} licensing.
Licensing involves Legal. This internship takes place within the context of
Liferay's Legal department. I will be working under Matija Šuklje, Senior
Counsel at Liferay. Matija is chiefly responsible for Liferay's \gls{ip},
specifically anything that involves the "©" symbol and software \gls{copyright}
and licensing. The "™" symbol is managed by Kirstin Huniar, and is not relevant
to this internship. [@suklje-2019]

Beside \gls{foss} licensing, Legal is also responsible for all other matters of law.
Like trademarks, these are not relevant to the internship, but mentioned for
completeness' sake.

## Engineering

Though this internship does not take place within the context of Liferay's
Engineering department, it is nevertheless important. Engineering is responsible
for creating Liferay's products. As part of creating Liferay's products, they
almost always interact with \gls{foss}---either Liferay's, or a dependency's.

## Dublin office

Liferay has offices all over the globe. Its global headquarters are in Los
Angeles. The international office is Dublin, which is the site of this
internship. The Dublin office hosts approximately twenty employees working on
Human Resources, Legal, finances, sales, consulting, and other. Remote workers
are also registered as working for the Dublin office.

(For posterity's sake---although the manual says otherwise---the office is
described *after* the departments because departments span offices.)

## The problem {#the-problem}

This section describes the problem curtly using the 6W method. [@verhoeven-2018,
chap. 3, sec. 3.2] The questions were posed to Matija Šuklje, and paraphrased
here.

#### What {-}

Liferay has a lot of software under various \glspl{license}. Liferay gives legal
assurances to its customers about its \gls{ip}, and therefore needs
to make sure that all code is correctly licensed. However, the current methods
of assuring the correctness of its licensing are manual. This does not scale in
an economically viable way.

#### Who {-}

Legal is responsible for verifying the licensing of Liferay's products.
Engineering interacts with licensed products, and may be affected by steps taken
to address the problem.

Matija Šuklje is the instigator of the project to tackle this problem.

#### When {-}

"When" is not strictly applicable, although the issue started being more
apparent as the product became too big to audit manually on a commercially
reasonable scale.

#### Why {-}

The work on licensing compliance is important for several reasons:

- Potential \gls{copyright} violations provide legal and reputational risks, and
  potential loss of revenue and business.
- \Gls{copyright} violations would also affect customers, who would be in breach
  of \gls{copyright} law.
- Crudely put, breaking \gls{copyright} law is illegal. [@berne-1886]

The manual work is a problem because:

- manual verification of licensing takes up a lot of (expensive) time by legal
  experts;
- when a problem is identified, the feedback loop between Legal and Engineering
  is inefficient, and creates a bottleneck.

#### Where {-}

"Where" is not strictly applicable. The problem is in the codebase.

#### The cause {-}

The main cause of the problem is the quantity of files that need to be checked
for compliance. A small amount of files can be verified by hand, but thousands
cannot. Alternatively, there would be no need to verify compliance if all
engineers were completely diligent in introducing copyrighted code. However,
human error is unavoidable, so verification is mandatory.

## Gap analysis of the problem

This section aims to simplify the fractured description in section
\ref{the-problem} with a gap analysis. The gap analysis is explicitly
as-short-as-possible to capture the essence of the problem.

> The current process of licensing compliance is manual. This takes a lot of
> time.
>
> The desired process of licensing compliance is automated. This saves a lot of
> time, and improves accuracy.

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
describes the project in full. This section details the context of the project.

Liferay is the *ordering party* (client, Dutch: opdrachtgever) of the project.
Matija Šuklje is the ordering party personified. The ordering party:

- describes the problem;
- provides resources to investigate the problem;
- describes further requirements and limitations;
- provides continuous feedback on the direction of the project;
- provides a working environment;
- provides assistance where needed.

I (Carmen Bianca Bakker) am the *delivering party* (contractor, Dutch:
opdrachtnemer) of the project. The delivering party:

- investigates the problem;
- performs research to form the basis of a requirements analysis;
- creates a requirements analysis;
- acts as project lead on the project to tackle the problem;
- creates a product to solve the problem;
- tests the product;
- writes a report on the process;
- performs evaluation at the end of the process to provide recommendations going
  forward.

These items are performed to the best of my abilities considering the
educational context within which the internship takes place.

## Detailed problem context

Section \ref{the-problem} gave the bare minimal problem description. Anything
more would have muddied the essence of the problem. However, more context is
needed to understand some things in chapter \ref{ch:project-definition}.

Notice to the reader: Feel free to skip this section or briefly skim over it. It
exists solely as reference material for chapter \ref{ch:project-definition}.

### Liferay Portal Community Edition

Liferay Portal Community Edition (henceforth: Liferay Portal) is the main
product of Liferay. It is the community version of Liferay DXP. It is licensed
under the terms of the GNU Lesser General Public License as published by the
Free Software Foundation, either version 2.1 of the \gls{license}, or any later
version. It consists of approximately 80,000[^liferay-source-files] files, out
of which ±32,000[^liferay-java-files] are Java code files. [@liferay-portal]

[^liferay-source-files]: `find . type -f | wc -l`

[^liferay-java-files]: `find . type -f -name "*.java" | wc -l`

### License headers {#license-headers}

By and large, the \gls{copyright} and licensing of a file is defined in its
comment header. In Liferay Portal, the Java files have a standardised header as
shown in listing \ref{lst:java-header}.

```{#lst:java-header caption="Comment header that contains Liferay's licensing blurb."}
/**
 * Copyright (c) 2000-present Liferay, Inc. All rights reserved.
 *
 * This library is free software; you can redistribute it and/or modify it under
 * the terms of the GNU Lesser General Public License as published by the Free
 * Software Foundation; either version 2.1 of the License, or (at your option)
 * any later version.
 *
 * This library is distributed in the hope that it will be useful, but WITHOUT
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
 * FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
 * details.
 */

```

@liferay-policy-marking-code identifies several problem with the current comment
headers: "[N]o coherent policy applied to all projects; years not updated; the
use of 'present' in the year span, which is useless at best and misleading at
worst; use of obsolete 'All rights reserved', which is neither needed nor true,
as the very next line gives rights through a FOSS license; does not include a
contact point to the copyright holder."

### Copyright assignment

Liferay uses a policy of \gls{copyright} assignment. This means that all
third-party contributors to Liferay must sign an agreement wherein they transfer
("assign") their \gls{copyright} to Liferay. If the agreement is not signed,
then the contributions are not accepted. [@liferay-cla]

Employee contributions always assign their copyright to the employer (Liferay).

The logical consequence of this policy is that all code inside of Liferay's
repositories is exclusively copyrighted by Liferay.

# Project definition {#ch:project-definition}

In this chapter, we define the parameters of the project. Specifically, this
chapter defines the end result of the project.

## Ideal situation

In order to give some context for the goals in section \ref{goals}, these are
some qualities of the ideal situation:

- Licensing problems get addressed much earlier during the development cycle.
- The feedback loop between Legal and Engineering is shortened.
- Total time spent working on this by Legal and Engineering is reduced to a
  minimum.
- Quality of licensing compliance improves.

Licensing problems get addressed much earlier during the development cycle.
Feedback loop gets shortened. Total time spent working on this by Legal and
Engineering is reduced to a minimum. Quality of licensing compliance improves

## Goals {#goals}

In coming up with a goal, it was quickly evident that it would be difficult to
formulate the main goal into a SMART goal. So instead of doing that, a broader
goal was chosen, with the implicit understanding that the goal would be met if
all SMART sub-goals are completed.

The main goal of the project is:

> Improve and automate \gls{inbound} and \gls{outbound} licensing compliance.

The sub-goals of the project are informed by the desires of Liferay.

### Follow industry best-practices by providing unified and unambiguous licensing information in all source code files

This resolves the problem mentioned in section \ref{license-headers}.
@liferay-outbound now mandates the use of a different header, but it has not
been implemented yet. The new header can be seen in listing
\ref{lst:reuse-header}.

```{#lst:reuse-header caption="TODO"}
/**
 * SPDX-FileCopyrightText: © {year_of_creation} Liferay, Inc. <https://liferay.com>
 * SPDX-License-Identifier: {spdx_license_short_identifier}
 */
```

TODO: This is informed by the REUSE project of the Free Software Foundation
Europe (TODO: Fix citing).

Optional goal TODO: Same header for open source and corporate thingamajig.

### Automatically check licensing of all inbound third-party code, and flag Legal if a problem is detected

All code that enters the project must have its licensing checked. More often
than not, it will be a contribution authored by an employee, which means that
the \gls{inbound} licensing is not a concern. If the employee commits code that
was authored by somebody else, however, the licensing must be double-checked.

The method of implementation is not yet certain, and will require research.
Preliminary research suggests that the code could be verified against a
"plagiarism checker" and a decision tree. The complexity of such a plagiarism
checker is much greater, however, because not only must one check for duplicity,
but also for the licensing of the original code. The decision tree is as complex
as the licensing policy that informs it.

Therefore, it would be fair to split this sub-goal up into a few more sub-goals:

- Automatically check whether inbound code is first-party or third-party

- Automatically check the licensing of inbound third-party code

- Verify whether the licensing of inbound third-party code is compatible

- Flag Legal if a problem is detected

### Produce a bill of materials that covers all outbound licensing

TODO: Are we doing this?

# Research



# Project activities

# Project boundaries

# Quality assurance

# Planning

\appendix

# Crash course in copyright and licensing

This appendix aims to provide a crash course in \gls{copyright} and licensing.
It is designed to be comprehensive-but-concise.

## What is copyright?

According to @cc-faq: "\Gls{copyright} law grants exclusive rights to creators
of original works of authorship, [...] prohibiting the making of copies without
the rights holder’s permission, among other things. [...] \Gls{copyright} in
most jurisdictions attaches automatically without need for any formality once a
creative work is fixed in tangible form. [...] In some jurisdictions, creators
may be required to register with a national agency in order to enforce
\gls{copyright} in court."

The Berne Convention [-@berne-1886] is an international agreement between
nations that forms the basis of much of \gls{copyright} law. It grants foreign
works the same protections as native works, and sets some minimum standards of
protection that all signatories must meet. The Berlin Act [-@berlin-1908]
introduces the concept that \gls{copyright} is enjoyed without being "subject to
any formality". In effect, this means that \gls{copyright} is granted as soon as
one's metaphorical pen is put to paper.

In order for a work to be eligible for \gls{copyright}, it must be original. In
this context, "'[o]riginal' means a work created through the 'fruits of
intellectual labor.' 'Originality' therefore requires not only that the
\gls{author} has not copied the work from another, but also that there is 'at
least some minimal degree of creativity.'" [@uslegal-originality]

There is no international threshold for originality. Countries create their own
thresholds for \gls{copyright} eligibility. In the Netherlands, in order for a
work to be copyrightable, the work must be perceivable by human senses; it must
have its own, original character and carry the mark of its maker; and the work
may not be solely necessary for the obtaining of a technical effect. Software is
an exception to this last item. [@auteursrecht-waarop]

The duration of \gls{copyright} differs across jurisdictions. In the European
Union, the Copyright Term Directive standardises \gls{copyright} duration to the
life of the \gls{author} and 70 years after their death, or 70 years after the
first lawful publication in case the \gls{author} is anonymous/pseudonymous.
[@copyright-term-directive]

The Berne Convention [-@berne-1886] and many other sources use the word
"\gls{author}" to refer to the person or organisation that holds the rights over
a certain work. In this document, "\gls{copyright-holder}" is consistently used
instead. The reason for this is that the \gls{author} is not always the
\gls{copyright-holder}---an \gls{author} may transfer their \gls{copyright} to
another party, such as when in the course of employment.
[@uk-ownership-copyright]

## What are licenses?

@reuse-faq says that "a \gls{license} defines the terms under which the
\gls{copyright-holder} allows the recipient of the \gls{license} to use the
software".

@choosealicense-no-license reasons that: "When you make a creative work (which
includes code), the work is under exclusive \gls{copyright} by default. Unless
you include a \gls{license} that specifies otherwise, nobody else can copy,
distribute, or modify your work without being at risk of take-downs,
shake-downs, or litigation. Once the work has other contributors (each a
\gls{copyright-holder}), 'nobody' starts including you", and adds that
"[d]isallowing use of your code might not be what you intend by 'no
\gls{license}.' An \gls{open-source} \gls{license} allows reuse of your code
while retaining \gls{copyright}."

A \gls{foss} \gls{license} grants certain rights to the recipient of the
\gls{license}. @fsf-free-sw says that a \gls{license} is a \gls{foss}
\gls{license} if it provides the user with four essential freedoms:

- “The freedom to run the program as you wish, for any purpose (freedom 0).
- The freedom to study how the program works, and change it so it does your
  computing as you wish (freedom 1). Access to the source code is a precondition
  for this.
- The freedom to redistribute copies so you can help others (freedom 2).
- The freedom to distribute copies of your modified versions to others (freedom
  3). By doing this you can give the whole community a chance to benefit from
  your changes. Access to the source code is a precondition for this.”

\Glspl{license} that do not provide the user with these freedoms, then, are
"\gls{proprietary}" or "\gls{non-free}" \glspl{license}.

@osi-osd has a similar requirement for a license to be identified as a
\gls{foss} \gls{license}. It says that a \gls{license} must abide by the Open
Source Definition.

These two definitions often---but not always---result in the same
\glspl{license} being identified as \gls{foss} \glspl{license}.
[@spdx-license-list]

@choosealicense-no-license, @osi-faq, and @stallman-license-compatibility
identify two types of \glspl{license}: \Gls{permissive} and \gls{copyleft}.
@osi-faq says that a \gls{permissive} \gls{license} is "simply a
non-\gls{copyleft} \gls{open-source} \gls{license} --- one that guarantees the
freedoms to use, modify, and redistribute, but that permits \gls{proprietary}
derivative works." @fsf-copyleft says that \gls{copyleft} "is a general method
for making a program (or other work) free (in the sense of freedom, not 'zero
price'), and requiring all modified and extended versions of the program to be
free as well." This last requirement is the defining feature of \gls{copyleft}
\glspl{license}.

The GNU General Public License family of \glspl{license} and the Creative
Commons Attribution-ShareAlike family of \glspl{license} are some of the most
widely used \gls{copyleft} \glspl{license}. [@fsf-copyleft;@cc-licenses]

## A word on FOSS

This document uses \acrshort{foss} (\acrlong{foss}) as a catch-all name for both
\gls{open-source} and \gls{free-software}. Furthermore, this document regards
\gls{open-source} and \gls{free-software} to be synonyms for simplicity's sake.
This is in the understanding that they are incredibly similar. [@schiessle-2012]

## Outbound licenses

An \gls{outbound} \gls{license} is effectively the \gls{license} under which a
first party distributes their code. The word "\gls{outbound}" is only added to
contrast against \gls{inbound} \glspl{license}.

## Inbound licenses

According to @liferay-internal-faq, "an \gls{inbound} \gls{license} is one that
is coming into the project or product, [of which there are generally] two types:
[1] code you copied from an \gls{upstream} project --- which is the same as that
upstream project's \gls{outbound} \gls{license}; and [2] code that was
contributed to one of our projects/products from an external party --- typically
by signing Liferay's CLA."

To paraphrase, all code and works that *enter* a project are covered by an
*\gls{inbound}* \gls{license}. The \gls{inbound} \gls{license} that a first
party receives is the \gls{outbound} \gls{license} of a third party.

\printnoidxglossary[sort=word]

# References {-}

<div id="refs"></div>
