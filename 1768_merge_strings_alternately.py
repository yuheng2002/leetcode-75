"""
LeetCode 1768: Merge Strings Alternately
Link: https://leetcode.com/problems/merge-strings-alternately/
Approach 1: for-loop simulation
Time: O(n), Space: O(1)
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_word = ""
        first_loop = min(len(word1), len(word2))
        for i in range(first_loop):
            new_word += word1[i]
            new_word += word2[i]
        if len(word1) > len(word2):
            for j in range(len(word1) - first_loop):
                new_word += word1[j + first_loop]
        if len(word2) > len(word1):
            for k in range(len(word2) - first_loop):
                new_word += word2[k + first_loop]
        return new_word
      
"""
Approach 2: putting ordered letters in a list then join 
Time: O(n), Space: O(1)
"""
# the i < w1 and i < w2 condition guarantees that the letter will be added sequently at each index with the order of letters in word1 first then of letters in word2 second.
# since len() retrieves the length of the string, for example, if a string is "word", then the length is 4, but since index starts at 0, so 0, 1, 2, 3 -> the last index is 3 with 'd' as the corresponding letter
# thus, i < len() will ultimately go up to the last index of either word1 or word2 without exceeding the bound
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1, w2 = len(word1), len(word2)
        lst = []
        for i in range(max(w1, w2)):
            if i < w1:
                lst.append(word1[i])
            if i < w2:
                lst.append(word2[i])
        return ''.join(lst)
