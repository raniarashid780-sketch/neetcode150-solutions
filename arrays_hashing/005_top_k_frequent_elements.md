# Top K Frequent Elements

**Problem, in my own words:** given a list of numbers and a number `k`, return the `k`
numbers that appear most often.

**Brute force:** count occurrences with a dict, then scan the dict `k` times, each time
picking out the current max and removing it.
Time: O(n·k) — Space: O(n)

**Optimal (what I implemented):** count occurrences with a dict, sort the
`(number, count)` pairs by count descending, take the first `k`, extract just the
numbers.
Time: O(n log n) — dominated by the sort — Space: O(n)
**Insight:** a dict is unordered by value — you can't "just look at it" and read off
the biggest counts, you have to explicitly sort `.items()` by the count
(`key=lambda pair: pair[1]`) to get them ranked. There's a better O(n) bucket-sort
approach (bucket index = frequency, since frequency is bounded by list length) that
avoids the sort entirely — not implemented yet, worth doing as a follow-up.

**What I got wrong first attempt — more than usual today, being honest about it:**
- Broke the cold-attempt rule itself: looked at LeetCode discussion before describing
  my own approach, which had held since Contains Duplicate. Correctly called out — I
  don't actually know if I'd have reached frequency-counting unaided.
- The discussion-sourced approach I proposed first was wrong for this problem — added
  tie-breaking rules (lexicographic/ascending order for equal counts) that don't exist
  in the actual constraints (LeetCode explicitly allows any order for ties).
- Proposed `.value_counts()` (pandas) as the counting mechanism — works conceptually,
  but pulls in a whole library for something a plain `dict`/`Counter` does natively;
  not how this gets solved in an interview setting.
- `return [k for pair in sorted_items[:k]]` — used `k` (the function's own parameter)
  instead of `pair[0]` inside the list comprehension. Ran without crashing and returned
  a list of the *correct length*, but full of copies of `k` itself, not the actual
  answer — the dangerous kind of bug, since it doesn't announce itself as a crash.
- Unclosed parenthesis on the `sorted(...)` call — plain syntax error, caught by
  Python immediately, not a logic issue.
- `items = counts.items()` computed and never used — dead code, harmless but sloppy.