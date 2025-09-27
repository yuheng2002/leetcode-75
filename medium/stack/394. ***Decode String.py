"""
LeetCode 394 - Decode String
Link: https://leetcode.com/problems/decode-string/

Idea:
  - Scan the string once.
  - Keep two stacks: num_stack (repeat counts) and str_stack (partial strings).
  - Keep curr_num and curr_str for the current layer.
    * digit -> build curr_num (multi-digit friendly): curr_num = curr_num*10 + int(ch)
    * '['   -> push (curr_num, curr_str) to stacks, then reset both
    * letter-> append to curr_str
    * ']'   -> pop k and prev; curr_str = prev + curr_str * k  (close one layer)

Complexity:
  Time: O(n)
  Space: O(n)
"""

class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = [] 
        str_stack = [] 

        cur_num = 0   # multiplier k before each '['
        cur_str = ""  # string collected between the last '[' and its matching ']'

        digits = set('0123456789')

        for ch in s:
            if ch in digits:
                # build multi-digit k
                cur_num = cur_num * 10 + int(ch) 
                # e.g. "321" -> (((0*10+3)*10+2)*10+1) = 321

            elif ch == '[':
                # push current state, then reset for new layer
                num_stack.append(cur_num)   # multiplier for this layer
                str_stack.append(cur_str)   # outer string before this layer
                cur_num = 0
                cur_str = "" 

            elif ch == ']':
                # pop one layer
                prev = str_stack.pop()      # string from outer layer
                multiplier = num_stack.pop()# k for this layer
                # combine: outer string + repeated inner string
                cur_str = prev + (cur_str * multiplier) 

            else:
                # add normal chars
                # case 1: right after '[', collect chars for current layer
                # case 2: right after ']', add leftover chars without multiplier
                cur_str += ch

        return cur_str
