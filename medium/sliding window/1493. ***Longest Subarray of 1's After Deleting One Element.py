"""
LeetCode 1493: Longest Subarray of 1's After Deleting One Element
Link: https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

Approach 1 — Two run lengths (prev_cnt & curr_cnt), single pass.
- curr_cnt = length of the current run of 1s (to the right of the last 0).
- prev_cnt = length of the run of 1s immediately to the left of the last 0.
- When we see a 0: we can “bridge” across that single 0, so update
  res with prev_cnt + curr_cnt, then shift the split:
      prev_cnt = curr_cnt
      curr_cnt = 0
- Also update res after each step so the trailing run is considered.

Important note (two consecutive zeros):
- If we see 0 twice in a row, the second 0 does `prev_cnt = curr_cnt (== 0)`
  and `curr_cnt = 0`, so both become 0. That’s correct: we are allowed to
  delete at most one 0, so we cannot bridge across two zeros.

Edge case: all 1s → we must delete one element, return n - 1.

Time: O(n)   Space: O(1)
"""
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        curr_cnt = 0
        prev_cnt = 0
        
        i = 0
        n = len(nums)

        res = 0

        if 0 not in nums:          # all ones ⇒ must delete one
            return len(nums) - 1
          
        while i < n:
            if nums[i] == 1:
                curr_cnt += 1
            elif nums[i] == 0:
                # bridge across this single 0, then shift the split
                prev_cnt = curr_cnt
                curr_cnt = 0
            i += 1
            # best by bridging one 0 between prev run and current run
            res = max(res, prev_cnt + curr_cnt)
        return res
      
"""
Approach 1.1 — Same idea as Approach 1, but cleaner for-loop.
- Same prev_cnt / curr_cnt mechanics; no separate pre-scan.
- Use a seen_zero flag instead of `0 not in nums` to handle the all-ones case.

Why this version:
- Same O(n)/O(1) behavior, fewer moving parts (no manual index i).

Time: O(n)   Space: O(1)
"""
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        curr_cnt = 0
        prev_cnt = 0
        seen_zero = False
        res = 0

        for num in nums:
            if num == 1:
                curr_cnt += 1
            else:
                # hit a 0: bridge once, then shift the split to the right side
                prev_cnt = curr_cnt
                curr_cnt = 0
                seen_zero = True
            res = max(res, prev_cnt + curr_cnt)
            
        # all ones ⇒ must delete one
        if seen_zero:
            return res
        else:
            return len(nums) - 1

"""
Approach 2 — Sliding window with at most one 0 (two pointers).
- Maintain a window [left, right] that contains at most one 0.
- Expand right each step; if zeros > 1, shrink from the left until zeros <= 1.
- Answer is window length minus one (we must delete exactly one element):
      res = max(res, right - left)     # not right - left + 1

Key details:
- When shrinking, only decrement the zero-counter if the leaving element is 0.
  Otherwise you’d “pretend” a zero left the window when it didn’t.
- This template is the standard “at most K bad elements” window; here K=1.
  It generalizes well to “delete up to K zeros”.

Time: O(n)   Space: O(1)
"""
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        zeros = 0
        res = 0

        for right, value in enumerate(nums):
            if value == 0:
                zeros += 1
            # keep at most one zero in the window
            while zeros > 1:
                if nums[left] == 0:           # only decrement when a zero leaves
                    zeros -= 1
                left += 1
            # delete one element ⇒ window size minus 1
            res = max(res, right - left)      # not right - left + 1
            # (normal count would be right-left+1, but we must delete one element)
        
        return res
