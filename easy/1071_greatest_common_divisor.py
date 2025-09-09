"""
LeetCode 1071: Greatest Common Divisor of Strings
Link: https://leetcode.com/problems/greatest-common-divisor-of-strings/
Approach 1: gcd + string multiplication
Time: O(n), Space: O(1)
"""

import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # If both strings are built by repeating the same base string,
        # then str1 + str2 must equal str2 + str1.
        # e.g., "ABABAB" + "ABAB" == "ABAB" + "ABABAB" == "ABABABABAB"
        if (str1+str2) != (str2+str1):
            return ""
          
        # The length of the largest base must divide both lengths.
        g = math.gcd(len(str1), len(str2))

        # only need either str1[:g] or str2[:g] as the base, because the first step already makes sure the existence of a base string
        base = str1[:g]
      
        # Verify base indeed generates both strings by repetition.
        str1_length_factor = len(str1) // g
        str2_length_factor = len(str2) // g
        if (base * str1_length_factor == str1) and (base * str2_length_factor == str2):
            return str1_base

