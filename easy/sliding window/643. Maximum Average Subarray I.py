"""
LeetCode 643: Maximum Average Subarray I
Link: https://leetcode.com/problems/maximum-average-subarray-i/

Approach (raw version): fixed-size sliding window.
- Build the first window sum by hand in a for-loop.
- Slide the window one step at a time: subtract the leftmost, add the new rightmost.
- Track the best window sum and return best / k.

Notes:
- This works and is clear. It’s just a bit slower in Python because the initial
  k-step loop runs in Python space, and `len(nums)` is called each while-iteration.
Time: O(n)   Space: O(1)
"""
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window = 0
        # First window sum (Python loop; readable, slightly slower than sum(...))
        for i in range(k):
            window += nums[i]
        best = window
        
        j = 0
        # Each step: add nums[j + k], remove nums[j], move j forward
        while j + k < len(nums):  # calling len(...) each time is fine, just a tiny overhead
            window = window - nums[j] + nums[j + k]
            # Readable one-liner; in hot loops an if-branch can be a hair faster than max(...)
            best = max(best, window)
            j += 1
        
        return best / k
      
"""
Approach (cleaner version): fixed-size sliding window, small Python-friendly tweaks.
- Use sum(nums[:k]) to get the first window (fast, C-implemented).
- Cache n = len(nums) so the loop condition is cheap.
- Slide by doing: window += nums[j + k] - nums[j].
- Update best with a simple branch (tiny micro-opt), then return best / k.

Why this is a bit faster:
- Fewer Python-level operations in the hot loop (no repeated len(...), no k-step init loop).
Time: O(n)   Space: O(1)
"""
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # First window via built-in sum (fast path)
        window = sum(nums[:k])
        best = window

        n = len(nums)  # cache length once
        j = 0 
        while j + k < n:
            # Slide window: add the incoming element(right), remove the outgoing one(left)
            window += nums[j + k] - nums[j]
            # Slightly faster than best = max(best, window) in tight loops
            if window > best:
                best = window
            j += 1
        
        return best / k
