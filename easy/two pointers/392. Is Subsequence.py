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

''' 
Approach 2 (for-loop version):
- Just walk through `t` once with a pointer `i` on `s`.
- Every time the current char in `t` equals `s[i]`, increment `i`.
- Because a for-loop moves forward through `t`, any next match for `s[i]`
  must come from later in `t` — so order is naturally preserved.
- At the end, if we matched all chars in `s` (`i == len(s)`), return True.

Why a for-loop works here:
- We only need `t` to move forward one step at a time.
- `i` only moves when we see a match, so it never gets ahead.
- Super readable and O(|t|) time, O(1) space.
- (Optional) Add an early break when `i == len(s)` to shave a few cycles.

Time: O(|t|)   Space: O(1)
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for ch in t:
            if i < len(s) and ch == s[i]:
                i += 1
        return i == len(s)
