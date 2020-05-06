- Does the automated solution need to do snippet-level scanning?

It would be nice to have. Probably not needed.

- Does the automated solution need to verify the licensing of third-party
  libraries that are introduced?

Yes

  + Only included libraries (e.g., *.jar* copied into the repository), or any
    dependencies?

Both would be nice. At a minimum the code that is actually included.

  + When should third-party libraries be verified? Only when introduced? Every
    time the tool is run?

Needs to run at least once. Must be synced with engineering. Should be enough to
check for real ones. Can do a full run every now and again (yearly, pre- or
post-release trigger).

  + What to do when the solution identifies a third-party library as being
    incompatible, but manual review says otherwise? Should there be a manual
    curation flag?

Override the tool somehow, probably through some kind of configuration file.
This already happens in the third-party software list.

Having a link to an issue would be nice to have.

  + When issues in licensing are discovered, should those issues be addressed
    upstream? How?

Not a requirement. Something Liferay would like to do. Hard to have a procedure
for this. Very manual process, and depends. There's a difference between
approaching a company and approaching "some kid" who uploaded some JavaScript.

- Does the codebase need to be fully REUSE-compliant? i.e., licensing headers in
  *every single file*.

That's what the policy says. Going to be very very difficult to get that done.
Ideally yes. Realistically only with source code Liferay owns.

  + If partial, which parts?

(Java and JavaScript) code. Strictly speaking code that is Copyright Liferay.

- Does the automated tool need to check for compatible licenses?

Nice to have. Probably need a decision tree.

  + Should this be a whitelist and a blacklist? A complex decision tree?

Could have a simple whitelist for the simple cases. Complex decision tree could
be added later. This is lazy, but a good start.


- In Liferay Portal, is any copyright statement other than "Copyright Liferay"
  permissible? Is it only permissible for non-\gls{copyleft} licenses?

Might make sense to have this be more freeform. It is currently very strict, and
not necessarily reflective of reality. e.g., there's some JS code that is
probably relicensed to LGPL upon inclusion in the Portal repo.

Some licenses other than LGPL might also make sense, probably a whitelist of a
limited amount of licenses.

Copyright Liferay + Copyright Jane Doe does not conflict with
SPDX-License-Identifier: LGPL. Matija doesn't see a practical use case of this
happening. Jane Doe has to agree with the dual-license relicensing.

Liferay currently does copyright assignment.
