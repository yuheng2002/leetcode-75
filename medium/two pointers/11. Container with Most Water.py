"""
LeetCode 11: Container With Most Water
Link: https://leetcode.com/problems/container-with-most-water/

Approach: Two pointers + pruning.
- Start with LHS at 0 and RHS at n-1. Area = min(height[LHS], height[RHS]) * (RHS - LHS).
- Each step:
  1) Update the best area with the current pair.
  2) Move the **shorter** side inward. While moving, **skip** all bars that are
     ≤ the current short bar (they can’t beat the last area since width shrinks
     and the short side wouldn’t increase).
- Repeat until LHS meets RHS.

Why it works (short version):
- Area = short_side * width. Moving the taller side can’t help; only raising the
  short side might. Bars ≤ old short are safe to skip.

Time: O(n)   Space: O(1)
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        LHS = 0
        RHS = len(height) - 1
        area = min(height[LHS], height[RHS]) * (RHS - LHS)

        while LHS < RHS:
            # Redundant work here:
            # Compute the same area twice—once in the if-condition and again in the body.
            # This can be written as a single line like the cleaner version below:
            #   area = max(area, min(height[LHS], height[RHS]) * (RHS - LHS))
            if min(height[LHS], height[RHS]) * (RHS - LHS) > area:
                area = min(height[LHS], height[RHS]) * (RHS - LHS)

            # Move ONLY the shorter side inward.
            # While moving, skip all bars <= the current short bar (“old”).
            # Reason: width shrinks and the short side wouldn’t increase,
            # so those states cannot beat the last computed area.
            if height[LHS] <= height[RHS]:
                old = height[LHS]
                while LHS < RHS and height[LHS] <= old:
                    LHS += 1
            else:
                old = height[RHS]
                while LHS < RHS and height[RHS] <= old:
                    RHS -= 1

        return area

'''
Same Approach, but Cleaner code

Time: O(n)   Space: O(1)
'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        LHS = 0
        RHS = len(height) - 1
        area = 0

        while LHS < RHS:
            # Single computation per step (avoids the redundancy above).
            area = max(area, min(height[LHS], height[RHS]) * (RHS - LHS))

            # Move the shorter side in. While moving, skip bars that are the same or lower
            # than the current short one — they can’t give a bigger area anyway.
            if height[LHS] <= height[RHS]:
                old = height[LHS]
                # This skip helps a lot on long flat or downhill stretches: you jump over many
                # bars at once instead of computing the new area one by one.
                while LHS < RHS and height[LHS] <= old:
                    LHS += 1
            else:
                old = height[RHS]
                while LHS < RHS and height[RHS] <= old:
                    RHS -= 1

        return area

