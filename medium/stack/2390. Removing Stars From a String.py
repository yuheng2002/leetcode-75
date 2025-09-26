"""
LeetCode 2390 - Removing Stars From a String
Link: https://leetcode.com/problems/removing-stars-from-a-string/

Approach 1: intuitive approach
    - since strings are immutable, convert 's' to a list and traverse it
    - any time there is a star '*', delete it and the element before it
    - decrement the index tracker i so it goes back to index 'i-1' to check
      the element that just got shifted to the left
    - repeat this process until reaching the end of the list

Problem with this version:
    time complexity is worst-case O(n²), and it may time out
    on large input sizes

Complexity:
    Time: O(n²)
    Space: O(n)
"""
class Solution:
    def removeStars(self, s: str) -> str:
        # strings are immutable
        s = list(s)

        i = 0 

        while i < len(s):
            if s[i] == '*':
                del s[i]
                del s[i-1]
                i -= 1
            else:
                i += 1
            
        return ''.join(s)

"""
Approach 2: using a stack
    - similar to checking for balanced parentheses
    - think of '*' as the only type of closing parenthesis:
      it matches any character other than itself
    - push all non-'*' characters onto the stack;
      any time there is a '*', pop the last item on the stack
    - in Python, use a list to implement a stack
        - append() ≈ push()
        - pop()    ≈ pop()

Complexity:
    Time: O(n)
    Space: O(n)
"""
class Solution:
    def removeStars(self, s: str) -> str:
        n = len(s)

        stack = []

        for i in range(n):
            if s[i] is not '*':
                stack.append(s[i])
            else:
                stack.pop(-1)
        
        return ''.join(stack)
