"""
LeetCode 443: String Compression
Link: https://leetcode.com/problems/string-compression/
Approach 1: Two pointers (read/write), group consecutive chars and write char + count digits in-place
Time: O(n), Space: O(1)
"""

class Solution:
    def compress(self, chars: List[str]) -> int:
        # special case, saves a little runtime
        if len(chars) == 1:
            return 1

        i = 0 # to keep track of index of chars
        n = len(chars)
        write = 0 # keep track of both where to write next and how many have been written

        while i < n: 
            ch = chars[i] # set the current character to be whatever at index i
            j = i

            # advance j to the first index where chars[j] != ch
            while j < n and chars[j] == ch:
                j += 1
                count = j - i # length of the current run

            # override the element at the index to write next and then increment write
            chars[write] = ch
            write += 1

            if count > 1:
                for digit in str(count):
                    # Write the decimal digits of `count` into `chars`, one by one (e.g., 12 -> '1','2').
                    chars[write] = digit 
                    write += 1
            # because j sits at the index after a series of the same characters, so update i to j, then repeat the same process for the next character
            i = j

        return write
        
