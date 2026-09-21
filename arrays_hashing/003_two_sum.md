# Two Sum

**Problem, in my own words:** given a list of numbers and a target, find the two
numbers that add up to the target and return their positions (indices).

**Brute force:** nested loop — for each number, check every other number to see if
they add up to target.
Time: O(n²) — Space: O(1)

**Optimal:** single pass with a `dict` mapping number → index. For each number,
compute its `complement` (`target - num`) and check if that complement is already a
key in the dict *before* adding the current number. If it's there, its stored index
plus the current index is the answer.
Time: O(n) — Space: O(n)
**Insight:** a plain `set()` (used for Contains Duplicate) only remembers *that* a
number was seen. Two Sum also needs *where* — so a `dict` is the right structure,
since it attaches an extra piece of data (the index) to each key.

**What I got wrong first attempt:**
- Initially planned a nested loop even after building the dict — completely missed
  that the dict's whole purpose was to eliminate the second loop, not sit alongside it.
- Wrote `seen[num] == complement` — a comparison, not a lookup, and using the wrong
  key (`num` instead of `complement`). Retrieval is just `seen[complement]`, no `==`.
- Indentation bug: the loop body was dedented to the same level as `def twoSum`,
  which put it outside the method entirely — Python's `return outside function` error
  was pointing at exactly that.
