- What is the most common licensing compliance issue [in Liferay]?

Probably not fulfilling all formal obligations of certain licenses. e.g. not
including all artifacts. Apache require you to keep notice files.

For third-party software, not all information is 100% ideal. Customers aren't
happy about that.

- How and by whom are licensing compliance issues reported to Legal?

Through JIRA tickets ("FOSS Project" ticket type). Separate ticket types for
inbound and outbound. Anyone can make these tickets, but usually it's developers
themselves, or developer leads, or product managers.

- Does Legal search for licensing compliance issues? If so, how?

Matija follows several keywords (open source, IP-related).

Stuff is found during scans.

Search through JIRA.

- What are the steps that are taken when a licensing compliance issue pops up?

There's a process for that:

  + https://grow.liferay.com/group/guest/excellence/-/wiki/34277/foss+in+liferay#finding-and-reporting-a-licensingcopyrightpatent-issue

  + https://grow.liferay.com/excellence/FOSS+non-compliance+procedure

- Where in the process does Liferay lose the most time?

Two gaps:

  + Waiting for development to flag something.

  + The scanning itself takes a lot of time. Automated scanning has gone from days
  to hours. But then need to go through it manually. Code duplication: A lot of
  false positives.
