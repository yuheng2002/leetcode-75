"""
LeetCode 1004: Max Consecutive Ones III
Link: https://leetcode.com/problems/max-consecutive-ones-iii/

Idea (sliding window, “at most k zeros”):
- Grow a window [left, right]. Track how many zeros are inside it.
- When the zero count goes over k, shrink from the left until the window
  is valid again (and remember to decrement the zero counter only when
  the element leaving is a zero).
- Every time the window is valid (zeros <= k), its length is a candidate
  answer: right - left + 1.

Note vs. 1493:
- 1493 requires deleting one element, so the length is (right - left).
- Here we *flip* up to k zeros, so we count the whole window:
  (right - left + 1).

Complexity: Time O(n), Space O(1).
"""
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros = 0
        left = 0
        res = 0

        for right, value in enumerate(nums):
            if value == 0:
                zeros += 1
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            res = max(res, right - left + 1)
        return res
