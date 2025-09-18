"""
Leetcode 1456: Maximum Number of Vowels in a Substring of Given Length
Link: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

Sliding window (fixed length k).
- Count vowels in the first window s[:k].
- Then slide the window 1 step at a time:
  drop the left char if it's a vowel, add the new right char if it's a vowel.
  Track the best seen count.
- Two independent `if` checks so both "drop" and "add" can happen in the same step.

Same idea as the cleaner version below; this one uses a list for vowels
and builds the initial slice `s[:k]` to seed the count.

Time: O(n)  Space: O(1)
"""
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a','e','i','o','u']

        window = s[0:0+k]
        count = 0
        for char in window:
            if char in vowels:
                count += 1

        max_count = count

        i = 0
        while i + k < len(s):
            if s[i] in vowels:
                count -= 1
            
            i += 1
            if s[i+k-1] in vowels:
                count += 1
            
            if count > max_count:
                max_count = count

        return max_count

"""
Same sliding-window idea, written tighter for a small speedup.
What changed and why it helps:
- Use a set for membership checks (O(1) and faster in Python).
- Avoid building the slice `s[:k]` every time; use indexes and a single loop:
  for j in range(k, n), update with the entering char s[j] and the leaving char s[j-k].
- Early exit when best == k (can't beat that).
- Still keep two independent `if` checks so both updates can happen in one step.

Functionally identical to the version above; just fewer allocations and lighter checks.

Time: O(n)  Space: O(1)
"""
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        Vowels = set("aeiou")

        count = 0
        for i in range(k):
            if s[i] in Vowels:
                count += 1
        
        best = count

        if best == k:
            return best

        n = len(s)
        for j in range(k,n):
            # can be put together -> count += (s[j] in Vowels) - (s[j-k] in vowels)
            if s[j] in Vowels:
                count += 1
            
            if s[j-k] in Vowels:
                count -= 1
            
            if count > best:
                best = count
                if best == k:
                    return best
        
        return best
