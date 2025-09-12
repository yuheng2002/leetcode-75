"""
LeetCode 238: Product of Array Except Self
Link: https://leetcode.com/problems/product-of-array-except-self/

Approach 1 (brute force with dummy padding):
- Add dummy 1’s at the start and end of nums to simplify boundary handling.  
- For each index i, compute the product of all elements to the left and all elements to the right, then multiply them together.  
- Append the result to output.

Time Complexity: O(n^2)  (because we loop through left and right subarrays for every index)  
Space Complexity: O(1) (excluding the output list)
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_with_dummy = [1] + nums + [1]
        i = 1
        output = []
        while i < len(nums)+1:
            n = 1
            for j in range(0, i):
                n = n * nums_with_dummy[j]
            for k in range(i + 1, len(nums_with_dummy)):
                n = n * nums_with_dummy[k]
            i += 1
            output.append(n)
        return output


'''
Approach 2: prefix + suffix (without using division)
- First compute prefix product for each element.
- Then compute suffix product in reverse order.
- Multiply prefix and suffix to get the final result.
- Initialize prefix and suffix with 1 because 1 is the identity element for multiplication.
Time Complexity: O(n)  
Space Complexity: O(1) (excluding the output list)
'''
class Solution:
    def productExceptSelf(self, nums):
        # this is the first time I ma introduced the prefix/suffix type of algorithm
        n = len(nums)
        output = [1] * n # creates an output list that has the same length as input list nums with all elements being 1

        # get the prefix for every element output[i]
        prefix = 1 

        # Note: I initialize prefix as 1 because 1 is the identity element in multiplication.  
        # For index 0, there are no elements on the left, but prefix = 1 ensures we don’t need  
        # any special case handling at the boundary.  
        # Since output is initialized as [1] * n, writing output[i] *= prefix also works  
        # (because 1 * prefix = prefix).  
        # However, the more general and safer way is output[i] = prefix,  
        # because if the operation changes (e.g., addition), the identity element wouldn’t be 1,  
        # and using *= could cause bugs.  
        for i in range(n):
            # output[i] *= prefix
            output[i] = prefix
            prefix *= nums[i]

        # get the suffix for every element output[i], the loop logic is exactly the same as getting the prefix
        # just in a reversed order
        suffix = 1
        for i in range(n - 1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]
        
        return output
