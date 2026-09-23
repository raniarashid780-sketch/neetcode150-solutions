# Group Anagrams

**Problem, in my own words:** given a list of strings, put every string that's an
anagram of another into the same group, and return all the groups.

**Brute force:** compare every string to every other string with a nested loop,
checking `sorted(a) == sorted(b)` each time, and merge matches into groups.
Time: O(n² · k log k) (n strings, each comparison costs a sort of length-k strings)
Space: O(n · k)

**Optimal:** one pass, using a hash map (`dict`) keyed by each string's sorted form.
For each string: compute `key = tuple(sorted(word))`, check if that key already exists
in the map — if not, create an empty list for it — then append the original word to
that key's list. Return `list(groups.values())` at the end.
Time: O(n · k log k) — Space: O(n · k)
**Insight:** anagrams share an identical sorted form, so that sorted form works as a
grouping key — same trick as Valid Anagram, but used to *bucket* many strings instead
of comparing just two.

**What I got wrong first attempt:**
- Initially thought of the problem as sorting/comparing **pairs**, which breaks the
  moment a group has 1 string (no pair) or 3+ strings (not a pair at all).
- Referenced `key` and `word` in the check-and-append logic before either variable was
  ever defined or assigned — `key` needed `tuple(sorted(i))` computed first; `word`
  was never a real variable at all, meant to be `i`.
- Forgot the `class Solution` / `def groupAnagrams` wrapper on a first pass — just
  submitted the loop body on its own.
- Returned `groups.values()` directly (a `dict_values` object) instead of
  `list(groups.values())`. LeetCode's judge accepted it anyway (likely compares
  elements rather than exact type), but `isinstance(result, list)` was actually
  `False` — not correct to the stated return type, just lucky the grader didn't check.
- Named the fixed variable `list`, shadowing Python's built-in `list` type for the
  rest of the function's scope — harmless here only because `list()` was never called
  again afterward, but a real landmine in general.
