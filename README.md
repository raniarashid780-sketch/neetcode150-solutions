# NeetCode150 Solutions

Solutions to the [NeetCode150](https://neetcode.io/practice) problem set, worked through as part of DSA prep. Each solution is my own implementation after a timed cold attempt — approach notes are in the file, not copy-pasted from an editorial.

**Process:** attempt cold (timed) → if stuck past the timer, watch the NeetCode video for that problem → re-implement myself → submit on LeetCode → copy the accepted solution here.

## Progress

| Category | Solved / Total | Priority | Status |
|---|---|---|---|
| Arrays & Hashing | 4 / 9 | Tier 1 | In progress |
| Two Pointers | 0 / 5 | Tier 1 | Not started |
| Sliding Window | 0 / 6 | Tier 1 | Not started |
| Stack | 0 / 6 | Tier 1 | Not started |
| Binary Search | 0 / 7 | Tier 1 | Not started |
| Linked List | 0 / 11 | Tier 1 | Not started |
| Trees | 0 / 15 | Tier 1 | Not started |
| Heap / Priority Queue | 0 / 7 | Tier 1 | Not started |
| Tries | 0 / 3 | Tier 2 | Not started |
| Backtracking | 0 / 10 | Tier 2 | Not started |
| Graphs | 0 / 13 | Tier 2 | Not started |
| Greedy | 0 / 8 | Tier 2 | Not started |
| Intervals | 0 / 6 | Tier 2 | Not started |
| 1-D Dynamic Programming | 0 / 12 | Tier 2 | Not started |
| 2-D Dynamic Programming | 0 / 11 | Tier 3 | Not started |
| Advanced Graphs | 0 / 6 | Tier 3 | Not started |
| Math & Geometry | 0 / 8 | Tier 3 | Not started |
| Bit Manipulation | 0 / 7 | Tier 3 | Not started |
| **Total** | **4 / 150** | | |

*28 Easy · 101 Medium · 21 Hard.*

## Repo structure

Each category is a flat folder — no per-problem subfolders. Each problem is a pair:
`problem-name.py` (solution) and `problem-name.md` (full write-up: problem restated in
my own words, brute force + complexity, optimal + complexity + the actual insight, and
what I got wrong on the first attempt). No write-up, no commit.

Each category folder also has its own `README.md` — **not** a per-problem write-up,
just a scannable index table (problem, one-line pattern insight, link to its `.md`).
GitHub auto-renders it when the folder is opened. This table is updated in the *same
commit* as the problem it documents — never a separate "update the index" commit, or
it silently drifts out of sync with what's actually solved.

Example: `arrays_hashing/README.md` (index) + `arrays_hashing/two-sum.py` +
`arrays_hashing/two-sum.md`

## Order followed

Arrays & Hashing → Two Pointers → Sliding Window → Stack → Binary Search → Linked List → Trees → Tries → Heap/PQ → Backtracking → Graphs → Advanced Graphs → 1-D DP → 2-D DP → Greedy → Intervals → Math & Geometry → Bit Manipulation