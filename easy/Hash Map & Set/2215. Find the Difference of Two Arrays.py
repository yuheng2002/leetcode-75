"""
LeetCode 2215: Find the Difference of Two Arrays
Link: https://leetcode.com/problems/find-the-difference-of-two-arrays/

Approach 1: List scan with on-the-fly dedup (intuitive)
- Walk nums1; for each value, if it is NOT in nums2 and NOT already in lst1, append it.
- Walk nums2; for each value, if it is NOT in nums1 and NOT already in lst2, append it.
- This keeps only values unique to each side and removes duplicates by checking the
  growing answer lists.

Cost notes:
- `x in <list>` is O(n), so doing it for every element makes this O(n*m) overall
  (worst-case ~O(n^2)).
- Space: O(n + m) for the two output lists.
"""
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        lst1 = []
        lst2 = []

        for num in nums1:
            if num not in nums2 and num not in lst1:
                lst1.append(num)

        for num in nums2:
            if num not in nums1 and num not in lst2:
                lst2.append(num)

        output = []
        output.append(lst1)
        output.append(lst2)

        return output

"""
Approach 2: Use sets for O(1) membership and set difference
- Convert to sets: s1 = set(nums1), s2 = set(nums2) to deduplicate and enable
  average O(1) lookups.
- The answers are simply: list(s1 - s2) and list(s2 - s1).

Why it’s better:
- Set difference computes “in A but not in B” in linear time after the conversion.
- Time: O(n + m). Space: O(n + m) for the sets (order is unspecified, which is OK here).
"""
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1, set2 = set(nums1), set(nums2)
        nums1_distinct = list(set1 - set2)
        nums2_distinct = list(set2 - set1)
        output = [nums1_distinct, nums2_distinct]

        return output
