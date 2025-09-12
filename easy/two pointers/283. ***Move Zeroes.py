"""
LeetCode 283: Move Zeroes
Link: https://leetcode.com/problems/move-zeroes/

Approach 1 — Shift-left per zero

Idea:
- Scan from left to right with index `i` and track a shrinking "effective length" `n`.
- When nums[i] == 0, shift the segment [i..n-2] left by one, write a 0 at position n-1,
  then do n -= 1. Do NOT advance `i` so the newly shifted-in element at `i` is rechecked.
- When nums[i] != 0, simply i += 1.

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
        n = len(nums) # n marks the current effective end; zeros beyond n-1 are already settled.
        
        while i < n:
            if nums[i] == 0:
                # Shift [i..n-2] left by one and place a 0 at n-1.
                for j in range(i, n - 1):
                    nums[j] = nums[j + 1]
                nums[n - 1] = 0
                
                # Exclude the tail zero we just placed; it needs no further work.
                n -= 1

                # Do NOT advance i here: a new value just shifted into index i
                # (it may be another 0), so we must re-check this position.
            else:
                # Only advance when no shift happened.
                i += 1

"""
Approach 2 — Stable compaction (write non-zeros, then fill zeros)

Idea:
- This is the standard "stable compaction" pattern.
- Use 'write' to both keep track of how many 0s to write at the end of the list,
  and where to move the next non-zero number
- write only increments on non-zeros.
  So nums[:write] are exactly the non-zeros seen so far (in order).
  write is the next slot for a non-zero; whatever is at nums[write] gets overwritten.
  After the scan, fill nums[write:] with 0.

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
- Maintain 'base' as the next position where a non-zero should go.
- Iterate i from 0..n-1; when nums[i] != 0, swap nums[base] and nums[i],
  then base += 1. Zeros naturally accumulate at the end.

Why stable?
- Each non-zero moves to the earliest "zero slot" in front without
  reordering non-zeros relative to each other.

Python note:
- Use parallel assignment `nums[base], nums[i] = nums[i], nums[base]`
  to avoid overwriting when swapping (splitting into two lines can duplicate values).

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


