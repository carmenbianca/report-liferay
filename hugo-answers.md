- What CI system does Liferay use?

Jenkins.

Tests for SourceFormatter: Regular tests, and if all files are changed, all
Liferay tests.

- How much CPU time is a licensing solution entitled to? Real time?

No idea.

- How often can/should the licensing solution run? When (in the development
  process) should it run?
- If problems are detected, is it possible to do automated interaction with the
  ticket system? Would manual interaction be preferable?
- Depending on how Legal answers: When a REUSE check fails, should the entire
  test fail?
- What language or framework ought to be used for a solution?

Chiefly Java and JS. Little bit of Python.

- Can a CI step make calls to a third-party internet API? Does this violate
  reproducibility?

Yes it can.

"Would say so" that it violates reproducibility.

- When during the development process do you test/lint?

After making changes.

- How do you test/lint? Locally or via CI?

Small tests locally, big tests over CI.

- How do you make the decision to use third-party code/libraries? Does licensing
  factor into this decision?

Depends on what you need.

Can usually see that Liferay is already using it in another module; naively
assume it's fine.

Go to website and check if open source or not. Don't check licence.

- During which stage of development do you see yourself using a compliance tool?

SourceFormatter before commit. If a pull request is sent to Brian without
SourceFormatter, tests will fail.

SourceFormatter before every pull request. (Usually, last commit of PR is
SourceFormatter).

- During which stage of development do you NOT see yourself using a compliance
  tool?

N/A. Any time.

- How quickly do you need feedback about whether you can use third-party code or
  not?

If it takes a couple of days, it's fine. But it's in the context of a
non-customer-facing thing.

---

SourceFormatter blacklists third-party files somehow.

Generated tags are ignored.

`copyright.txt` overwrites a thingamajig.

All files in PR are new; allows to check the current year.

Deal moved/renamed files somehow.
