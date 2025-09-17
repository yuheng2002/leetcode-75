"""
LeetCode 1679: Max Number of K-Sum Pairs
Approach 1 — Frequency map (hashmap).

Idea:
- Count how many times each number appears: count[x].
- For each distinct x, its partner must be y = k - x.
  * If x < y and y exists, we can form min(count[x], count[y]) pairs.
  * If x == y, the pairs come from self-matching: count[x] // 2.
  (The x < y check prevents double-counting the same pair in both orders.)

Pros:
- Linear time on average, no sorting, doesn’t rely on element order.
- Simple to reason about duplicates.

Cons:
- Uses extra memory proportional to the number of distinct values.

Complexity:
- Time: O(n) to build the map + O(d) to sweep distinct keys (d ≤ n).
- Space: O(d).
"""

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        pairs = 0
        for x in count:
            y = k - x
            if x < y and y in count:
                pairs += min(count[x], count[y])
            elif x == y:
                pairs += count[x] // 2
        
        return pairs

"""
Idea:
- Sort nums ascending, then use two pointers i (left) and j (right).
- Let s = nums[i] + nums[j]:
  * If s == k: we found a pair; move both pointers inward.
  * If s < k: sum is too small; move left pointer (need a bigger number).
  * If s > k: sum is too big; move right pointer (need a smaller number).
- Sorting guarantees we never miss a valid pair: once s < k, the current
  left value can’t pair with any element to its left of j, so it’s safe to move i.

Pros:
- Constant extra space, very clean loop.

Cons:
- Requires sorting, which is O(n log n) and mutates the input order.
- Usually slower than the hashmap approach when n is large and memory is not tight.

Complexity:
- Time: O(n log n) from sorting (the two-pointer scan is O(n)).
- Space: O(1) extra (in-place sort).
"""
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0 
        j = len(nums) - 1
        pairs = 0

        while i < j: 
            s = nums[i] + nums[j]
            if s == k:
                pairs += 1
                i += 1
                j -= 1
            elif s < k: # sum is not big enough, increment left pointer
                i += 1
            else:
                j -= 1
        
        return pairs
