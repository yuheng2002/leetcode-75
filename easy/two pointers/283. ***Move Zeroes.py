"""
Approach 1 — Shift-left per zero

Idea:
- Scan from left to right with index `i` and track a shrinking "effective length" `n`.
- When nums[i] == 0, shift the segment [i..n-2] left by one, write a 0 at position n-1,
then do n -= 1. Do NOT advance `i` so the newly shifted-in element at `i` is rechecked.
- When nums[i] != 0, simply i += 1.

Properties:
- Stable: relative order of non-zero elements is preserved.
- In-place: O(1) extra space.
- Many writes: each zero may trigger shifting a whole segment.

Complexity:
- Time: O(n^2) in the worst case (e.g., many zeros). (runtime is slow)
- Space: O(1).

Examples:
    # [0, 0, 1] -> # [1, 0, 0]

    # [0, 1, 0, 3, 12] -> # [1, 0, 3, 12, 0] -> # [1, 3, 12, 0, 0]
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        n = len(nums)

        while i < n:
            if nums[i] == 0:
                for j in range(i, n - 1):
                    nums[j] = nums[j + 1]
                nums[n - 1] = 0
                n -= 1
            else:
                i += 1

"""
Approach 2 — Stable compaction (write non-zeros, then fill zeros)

Idea:
- Use two pointers (read/write). Iterate once; whenever nums[i] != 0,
  write it to nums[write] and advance `write`. After the pass, fill
  positions [write..end] with zeros.
- This is the standard "stable compaction" pattern.

Properties:
- Stable: preserves order of non-zero elements.
- In-place: O(1) extra space.
- Simple and readable; may rewrite each non-zero once.

Complexity:
- Time: O(n) (one pass + tail zero fill).
- Space: O(1).

Example:
    [0, 1, 0, 3, 12] -> [1, 3, 12, 0, 0]
"""

class Solution:
    def moveZeroes(self, nums):
        write = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[write] = nums[i]
                write += 1
        while write < len(nums):
            nums[write] = 0
            write += 1

"""
Approach 3 — Swap step by step

Idea:
- Maintain `base` as the next position where a non-zero should go.
- Iterate i from 0..n-1; when nums[i] != 0, swap nums[base] and nums[i],
  then base += 1. Zeros naturally accumulate at the end.

Why stable?
- Each non-zero moves to the earliest "zero slot" in front without
  reordering non-zeros relative to each other.

Python tip:
- Use parallel assignment `nums[base], nums[i] = nums[i], nums[base]`
  to avoid overwriting when swapping (splitting into two lines can duplicate values).

Properties:
- Stable, in-place, and usually fewer writes than Approach 2 (each non-zero
  participates in at most one swap).

Complexity:
- Time: O(n)
- Space: O(1)

Example:
    [0, 1, 0, 3, 12] -> [1, 3, 12, 0, 0]
"""
class Solution:
    def moveZeroes(self, nums):
        base = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[base], nums[i] = nums[i], nums[base]
                base += 1


