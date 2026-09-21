# Contains Duplicate

**Problem, in my own words:** given a list of numbers, tell me if any number shows up more than once.

**Brute force:** compare every number to every other number with a nested loop.
Time: O(n²) — Space: O(1)

**Optimal:** walk the list once, keeping a `set()` of numbers already seen. For each
number, check the set *before* adding to it — if it's already there, it's a duplicate.
Time: O(n) — Space: O(n)
**Insight:** trade memory for time — remembering what you've seen turns "search the
whole list again" into a single O(1) lookup.

**What I got wrong first attempt:**
- Tried `seen += i` to add a number to the set — wrong tool entirely; `+=` on a set
  expects something iterable, not a single int. Sets add single items with `.add()`.
- First working draft had the check backwards: `if i not in seen: return True`. That
  returns `True` on the very first number (since `seen` starts empty), before the
  function ever gets a chance to find an actual duplicate. The check has to fire when
  the number **is** already in `seen`, not when it isn't.
