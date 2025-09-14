"""
LeetCode 1732: Find the Highest Altitude
Link: https://leetcode.com/problems/find-the-highest-altitude/

Approach1: Build the full altitude sequence (prefix sums), then take the max.
- Start with altitudes = [0] (starting point at altitude 0).
- For each delta g in gain, append altitudes[-1] + g.
- Return max(altitudes).

Time: O(n)       Space: O(n)  (stores all n+1 altitudes)
"""

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitudes = [0]
        for g in gain:
            altitudes.append(altitudes[-1]+g)
        return max(altitudes)

'''
Approach2: running prefix sum + rolling max (start from 0)
Time: O(n), Space: O(1)
Why this over building a full list: no extra list, one pass, O(1) space, same result.
'''

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        cur = 0 # running sum: current altitude (start at 0)
        highest = 0 # highest altitude seen so far
        for g in gain:
            cur += g
            if cur > highest: # update max on the fly; no need to store all altitudes
                highest = cur
        return highest
