"""
LeetCode 151: Reverse Words in a String
Link: https://leetcode.com/problems/reverse-words-in-a-string/

Approach 1: manual parsing + reverse
- Iterate through string, manually build words while skipping spaces
- Collect words into list, then reverse list (either by loop or .reverse())
Time: O(n)
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        lst = []
        word = ""
        i = 0
        while i < len(s):
            if s[i] != ' ':
                word += s[i]
                i += 1
            elif s[i] == ' ':
                if word != "":
                    lst.append(word)
                    word = ""
                i += 1
        if word != "":
            lst.append(word)

        # this step can be done by using .reverse() instead
        # lst.reverse() 
        for j in range (len(lst)//2):
           temp = lst[j]
           lst[j] = lst[len(lst) - 1 - j]
           lst[len(lst) - 1 - j] = temp
      
        
        output = ' '.join(lst)
        return output

"""
Approach 2: reverse string + reverse each word
- Reverse the entire string s
- Split by spaces (removes extra spaces)
- Reverse each word back individually
- Join with single space
Time: O(n)
"""
class Solution:
    def reverseWords(self, s: str) -> str:
      
        reversed_word = s[::-1] # reverse the entire s string
      
        output = []

        # split the string by spaces and put each word in a list, removing all the addtional spaces as well   
        reversed_lst = reversed_word.split()  
      
        for word in reversed_lst:
            output.append(word[::-1]) # append the re-reversed words to the list we will use to output the string
        return " ".join(output)

"""
Approach 3: convert string into a list, then reverse the list
- Just a couple of lines of code (use Python built-in functions, such as .split() and .reverse()
- Reverse the list directly
- join back with spaces
Time: O(n)
"""
class Solution:
    def reverseWords(self, s: str) -> str:
      words = s.split()
      words.reverse()
      return " ".join(words)
