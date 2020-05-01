# ClearlyDefined

Upfronting this information because it's important for understanding everything
else.

ClearlyDefined API has two/three relevant calls
<https://api.clearlydefined.io/api-docs>:

## GET /definitions/{type}/{provider}/{namespace}/{name}/{revision}

Returns a JSON with information about a revision of a package with name
{name}. Example output:
<https://api.clearlydefined.io/definitions/pypi/pypi/-/black/19.10b0>

Specifically, the output contains licensing information about the given package,
and gives a score at the end. The score depends on a load of factors that aren't
relevant in this document. Safe to say that Matija/Legal determined that a score
of 87% is sufficient.

## POST /harvest

Tell the server behind the API to schedule a harvesting job. Example POST
body:

```
[
  {
    "tool": "package",
    "coordinates": "npm/npmjs/-/redie/0.3.0"
  },
  {
    "tool": "source",
    "coordinates": "git/github/microsoft/redie/194269b5b7010ad6f8dc4ef608c88128615031ca"
  }
]
```

## GET /harvest/{type}/{provider}/{namespace}/{name}/{revision}

Frankly not really sure what this does. "Get all the harvested data for a
component revision." Sounds relevant.

# The plan

1. When new library is introduced to codebase, look up that specific revision
   using ClearlyDefined.
2. Check the API result against certain criteria:
  + Score is above a threshold (87%, as per Inbound Licensing Policy)
  + All licenses used by the package are in a pre-approved list.
  + The package+revision is internally whitelisted (or blacklisted?).
3. If the criteria are met, all is well. If not, all is not well: post the link
   <https://issues.liferay.com/browse/FOSS> in the output to suggest that the
   user make an issue.

## Problems

1. ClearlyDefined has scans for *a lot* of packages, but some revisions simply
   haven't been harvested yet. Harvesting a revision takes time, and I am not
   aware of any way to be notified of whether the harvesting job got through
   other than doing `GET definitions` every once in a while.

2. I understand that sometimes, jars are renamed downstream within Portal, or
   that the version number is not preserved. The exact upstream name *must* be
   preserved for this to work. The version number *should* be preserved, but can
   be worked around:

   Do a checksum of the jar, and check the checksum against the checksums the
   checksums of all versions of a package. You have now identified the exact
   revision.

# The pseudocode

```python
def files_changed_between_current_branch_and_master() -> List[str]:
  """Functionality speaks for itself. I believe Ant exposes this functionality,
  but it's introduced here as a function for completeness' sake.
  """
  pass

def is_whitelisted(file: str) -> bool:
  """Figure out whether a file has been manually whitelisted by Legal. The
  information about whether a file is whitelisted or not is probably stored
  adjacent to the file, or in a central configuration file.
  """
  pass

def extract_name_and_version(file: str) -> Tuple[str, Optional[str]]:
  """Inspect the file name and divine the name and version number from it.
  The version number can be empty, but the name cannot be.
  
  :raises ValueError: could not identify name.
  """
  pass

def divine_version_from_checksum(name: str, checksum: str) -> str:
  """Do API calls to servers to figure out the version number. Compare 
  *checksum* to checksums of all released revisions. If there's a match, then
  that's the version.

  :raises ValueError: could not divine version.
  """
  pass

def clearlydefined_definitions(name: str, version: str) -> json:
  """Do an API call to ClearlyDefined with the name and version.

  The {type}, {provider}, and {namespace} will probably need to be guessed? Not
  sure where to get this information from a file name. Fortunately {type} and
  {provider} are finite.
  """

def extract_json(clearlydefined_json: json) -> Result:
  """Extract information from the json and put it in a result."""
  
  result = Result()

  result.score = clearlydefined_json[...]
  result.licenses = clearlydefined_json[...]
  # etc etc etc

  return result

def check(file: str) -> Result:
  """Kind of a super-function that handles all the bells and whistles to check a
  single file.

  This should PROBABLY be extracted into multiple functions. But putting all of
  this in a single pseudocode function gives a decent overview.
  """
  if is_whitelisted(file):
    return Result(...) # good result, whitelisted.

  try:
    name, version = extract_name_and_version(file)
  except ValueError:
    return Result(...) # bad result, couldn't find name
  if version is None:
    try:
      version = divine_version_from_checksum(name, checksum(file))
    except ValueError:
      return Result(...) # bad result, couldn't find version
  
  clearlydefined_json = clearlydefined_definitions(name, version)

  if not clearlydefined_json:
    return Result (...) # bad result, was not harvested by clearlydefined

  result = extract_json(clearlydefined_json)

  if result.score < 87:
    result.approved = False
  for license in result.licenses:
    if license not in PREAPPROVED_LICENSES:
      result.approved = False
      break
  # Probably some more criteria? Not sure.

  return result

def main() -> bool:
  results = []
  for file in files_changed_between_current_branch_and_master():
    results.append(check(file))

  approved = True
  for result in results:
    if not result.approved:
      approved = False
      print("Information about why the check failed goes here.")
      print("Create issue at <https://issues.liferay.com/browse/FOSS>.")
    else:
      print(f"{result.file} is approved.")

  return approved
```
