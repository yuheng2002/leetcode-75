"""
LeetCode 338: Counting Bits
Link: https://leetcode.com/problems/counting-bits/

What this solves:
Given n, return an array res where res[i] is the number of 1-bits in i (0 ≤ i ≤ n).

What’s new here (beyond basic base conversion I saw in CSE20):
- Bitwise operations: especially the AND operator `&` working on binary digits.
- Kernighan’s trick: `x & (x - 1)` clears the lowest set bit of `x`.
- DP-style recurrence: reuse a smaller already-computed subproblem
  via `res[i] = res[i & (i - 1)] + 1`.

Why this is neat:
Once you accept that `i & (i - 1)` removes exactly one 1-bit, you get
an O(n) bottom-up fill with O(1) work per i.

Complexity:
- Time: O(n)
- Space: O(n) for the output array

Sanity check:
n=5 → res = [0,1,1,2,1,2]
"""

class Solution:
    def countBits(self, n: int) -> List[int]:

        res = []
        res.append(0)

        for i in range(1, n + 1):
            res.append(res[i & (i-1)] + 1)
        
        return res

# when '&' is used between two integers, here is what happens:
# it compares the corresponding bits (binary digits) of both numbers.
# If both bits are 1, the result is 1; otherwise it is 0.
# Example: 3 = (11) in binary, 4 = (100).
# Pad 3 with a leading zero: 3 = (011).
# Now compare each digit with 4 = (100):
#   011
# & 100
# -----
#   000
# The result is (000) in binary, which is decimal 0.

# Now let’s apply Kernighan’s algorithm:
# The key property is with n and (n-1).
# Subtracting 1 from n flips all the bits at and after the rightmost 1.
# This means:
#   - the rightmost 1 itself becomes 0
#   - everything to its right changes (0s turn into 1s)
#
# Example: n = 8 = (1000), n-1 = 7 = (0111).
# You can see the rightmost 1 of 8 was cleared, and all bits to the right flipped.

# But here’s the important part: when we do n & (n-1),
# all those "new 1s" in (n-1) will be ANDed with the original n,
# and since n already had 0s in those positions, they cancel out.
# The only net effect is: the lowest set bit of n gets removed.
#
# Example: n = 40 = (101000)
#          n-1   = (100111)
#   n & (n-1)   = (100000)
# See? The lowest 1 in n got cleared, everything to the right became 0.

# So we have this simple but powerful fact:
#   popcount(n) = popcount(n & (n-1)) + 1
# Because n & (n-1) is just n with its lowest 1 removed,
# so it has exactly one fewer 1 than n.

# With this observation, we can use dynamic programming:
# - Start from 0 (which has 0 ones).
# - For each i, reuse the result of i & (i-1) (a smaller number we already computed),
#   then just add 1.
# This way we build up the answers for all numbers from 0 to n step by step.
