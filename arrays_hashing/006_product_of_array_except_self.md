# Product of Array Except Self

## Problem, in my words
Given a list of numbers, return a new list where each position holds the product of every other number in the list (everything except the number at that position). Division is not allowed, and it must run in O(n).

## Brute force
For each index i, loop over the whole array with a nested loop and multiply every number except `nums[i]`.
- Time: O(n^2)
- Space: O(1) extra (output not counted)
- Result: correct, but Time Limit Exceeded on large inputs, so it could not be submitted.

## Optimal approach
The answer at index i is (product of everything to the left of i) x (product of everything to the right of i). Instead of recomputing those products for every index, carry them as running values.
- Pass 1 (left to right): keep `running_prefix`. At each index write it into `res[i]` FIRST, then multiply `nums[i]` into it. Writing before updating is what keeps `nums[i]` out of its own answer. After this pass `res[i]` = product of everything left of i (index 0 is always 1: nothing to its left).
- Pass 2 (right to left): keep `running_suffix`. At each index multiply it into the existing `res[i]` (left product x right product), then multiply `nums[i]` into the suffix.
- Time: O(n), two passes
- Space: O(1) extra, the output array is reused for both passes
- Insight: reuse one array for both directions and always write before updating the running value. Works with zeros because there is no division.

## What I got wrong on first attempt
- Went straight to nested loops and hit the time limit.
- Found the "before and after" idea only after the brute force failed.
- Wrote the prefix/suffix code but could not explain why `res[i] *= running_suffix` works in place, or what `res[2]` holds after pass 1 (answer for [1,2,3,4]: 2, which is 1 x 2, the left side only).
