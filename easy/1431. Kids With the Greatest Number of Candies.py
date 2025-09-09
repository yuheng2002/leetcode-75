"""
LeetCode 1431: Kids With the Greatest Number of Candies
Link: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
Approach 1: Calculate the candies each kid has after adding the extra candies and then compare it with all the others with a for loop (my original thought)
Time: O(n)^2
"""

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        lst = []
        for i in range(len(candies)):
            temp_candy = candies[i] + extraCandies
            max = temp_candy
            for j in range (len(candies)):
                if candies[j] > temp_candy:
                    max = candies[j]
            lst.append(temp_candy == max)
        return lst

"""
Approach 2: Precompute max candy and compare with each kid (faster runtime)
(essentially, because a kid after adding extraCandies does not have to compare with him/herself, each kid compares with the max of all kids)
Time: O(n)
"""

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        lst = []
        max_candy = max(candies)
        for i in range (len(candies)):
            lst.append(candies[i]+extraCandies >= max_candy)
        return lst
