"""
LeetCode 392: Is Subsequence
Link: https://leetcode.com/problems/is-subsequence/
Approach: Two pointers. Scan t once, advance i when s[i] matches t[j].
Time: O(|t|), Space: O(1)
"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0

        while i < len(s) and j < len(t):
            ch = s[i]

            # Both branches advance j; only the match branch also advances i.
            # So this can be simplified by always doing j += 1 and
            # incrementing i only when ch == t[j].
            if ch == t[j]:
                i += 1
                j += 1
            elif ch != t[j]:
                j += 1

        # This can be simplified to `return i == len(s)`.
        # The loop exits only when we've matched all of s (i == len(s))
        # or exhausted t (j == len(t)). Success ⇔ all of s was matched.
        if i < len(s) and j >= len(t):
            return False
        else:
            return True


'''
Simplified Version
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0

        while i < len(s) and j < len(t):
            ch = s[i]
            if ch == t[j]:
                i += 1
            j += 1

        return i == len(s)
