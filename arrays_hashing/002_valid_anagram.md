# Valid Anagram

**Problem, in my own words:** check if two strings use exactly the same letters the
same number of times each — order doesn't matter.

**Brute force (rejected before coding):** my first instinct was "check if every letter
present in one string is present in the other." Caught myself before submitting —
`"aab"` vs `"abb"` both contain only `{a, b}`, so presence-only would call them
anagrams, but they're not (different counts per letter). Presence isn't enough; counts
are what matter.

**Optimal:** `sorted(s) == sorted(t)`. Sorting both strings gives each a canonical form
— if they're anagrams, their sorted versions are character-for-character identical.
Time: O(n log n) — Space: O(n) (for the sorted copies)
**Insight:** sorting turns "do these have the same letters with the same counts" into a
direct equality check, no manual counting needed.

**What I got wrong first attempt:** the logic itself was right by the time I coded it
(sorted-comparison), but I originally submitted it wrapped in a redundant `if/else`
returning `True`/`False` explicitly — `sorted(s) == sorted(t)` already *is* a boolean,
so the if/else added nothing. Collapsed to a direct `return` here.
