"""
LeetCode 345: Reverse Vowels of a String
Link: https://leetcode.com/problems/reverse-vowels-of-a-string/
Approach 1: Collect indices of vowels, reverse the vowel list, then put back
Time: O(n)
"""
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel_lst = []
        index_lst = []
        s_lst = list(s)

        for i in range (len(s)):
            if s[i] in "aeiouAEIOU":
                vowel_lst.append(s[i])
                index_lst.append(i)

        if vowel_lst == []:
            return s

        for j in range (len(vowel_lst) // 2):
            temp = vowel_lst[j]
            vowel_lst[j] = vowel_lst[len(vowel_lst) - 1 - j]
            vowel_lst[len(vowel_lst) - 1 - j] = temp
        
        for index, vowel in zip(index_lst, vowel_lst):
            s_lst[index] = vowel
        return "".join(s_lst)
