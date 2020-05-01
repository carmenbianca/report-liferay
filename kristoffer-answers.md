Pseudo-code that explains steps.

Send pseudo-code to Peter and create issue together.

Dependency jar names/versions are changed.

Determine acceptable score.

Mark validated jars as approved.

First design step, go through it manually.


- What CI system does Liferay use?

Jenkins.

- How much CPU time is a licensing solution entitled to? Real time?

No limits on CPU time; always looking to run quickly as possible. Don't add
hours and hours. Tests are run very frequently; even a little bit adds up.

At most five minutes.

- How often can/should the licensing solution run? When (in the development
  process) should it run?

Matija can answer this? Ideally as part of every PR. Soonest intervention moment
is PR.

Integrating with SourceFormatter is probably out of scope.

Earlier you run, more often it's run -> Adds up time.

Should there be manual review for PRs?

1/100 or 1/1000 contains dependency change.

- If problems are detected, is it possible to do automated interaction with the
  ticket system? Would manual interaction be preferable?

Currently not done, but maybe possible. Could do, but don't yet. 

Typically e-mail or Slack notification.

- Depending on how Legal answers: When a REUSE check fails, should the entire
  test fail?

Yes.

- What language or framework ought to be used for a solution?

Most likely: Bash, ant, Java combination.

All test logic in Ant, not Jenkins.

Proof-of-concept in different language is okay but not preferrable.

- Can a CI step make calls to a third-party internet API? Does this violate
  reproducibility?

Can, but try to avoid it. Because might overwhelm.

