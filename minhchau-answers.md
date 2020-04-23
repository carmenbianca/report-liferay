Technical support lead. Tasks get escalated to Minhchau. Help with data
engineering. Automated translation work.

- When during the development process do you test/lint?

At the end, just before sending a pull request.

- How do you test/lint? Locally or via CI?

Linting locally. All other tests via CI.

- How do you make the decision to use third-party code/libraries? Does licensing
  factor into this decision?

Technical support can't bring in new libraries. Only upgrade existing ones. New
libraries must be justified. Unless plan to distribute---don't look at
licensing, only pricing.

Don't know how engineering chooses new libraries.

- During which stage of development do you see yourself using a compliance tool?

Header test before PR. Dependency check during CI. It would be nice to do the
dependency check locally for sanity's sake. Specific CI command.

- During which stage of development do you NOT see yourself using a compliance
  tool?

Only at the start, or at the end, but not in the middle.

- How quickly do you need feedback about whether you can use third-party code or
  not?

Ideally within a week.
