"""
LeetCode 724: Find Pivot Index
Link: https://leetcode.com/problems/find-pivot-index/

Approach: single running prefix.
- Let total = sum(nums) and left = 0.
- Added dummies to avoid special case handling at borders
- Scan nums. At index i with value x:
    right = total - left - x
    if left == right: return i
    left += x
- If none matched, return -1.

Time: O(n)   Space: O(1)
"""

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        total = sum(nums)
            
        dummy_nums = [0] + nums + [0]

        right_sum = total
        left_sum = 0
        for i in range(1, len(dummy_nums) - 1):
            right_sum -= dummy_nums[i]
            left_sum += dummy_nums[i - 1]
            if left_sum == right_sum:
                return i - 1

        return -1

  """
Approach 2: Single running prefix (no padding).
- Let `total = sum(nums)` and `left = 0`.
- For each index `i` with value `x`:
    - Compute `right = total - left - x` (sum to the right of `i`).
    - If `left == right`, return `i`.
    - Then do `left += x` to move the boundary forward.
- Checking before updating `left` means the current element is excluded from both
  sides automatically (so index 0 works without any special cases or dummy padding).

Time: O(n)   Space: O(1)
"""
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left = 0
        for i in range(len(nums)):
            x = nums[i]
            right = total - left - x
            if left == right:
                return i
            left += x
        return -1
