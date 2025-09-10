"""
LeetCode 605: Can Place Flowers
Link: https://leetcode.com/problems/can-place-flowers/
Approach 1: greedy scan with boundary checks (simulate planting)
Time: O(n), Space: O(1)
"""

# this approach is generated from my initial intuition. Although it has a good runtime, it is a little complicated than it has to be 
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed_length = len(flowerbed)
        # Edge case 1: when n == 0, always True
        if n == 0:  return True

        # Edge case 2: when flowerbed has only one element in it
        if flowerbed_length == 1 and flowerbed[0] == 0 and n <= 1:
            return True

        # Deal with the head (first two elements)
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            n -= 1
            flowerbed[0] = 1
            if n == 0:
                return True

        # Deal with the middle (except for head and the tail)
        for i in range (2, flowerbed_length - 1):
            if flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed [i+1] == 0:
                n -= 1
                flowerbed[i] = 1
                if n == 0:
                    return True

        # Deal with the tail (last two elements)
        if flowerbed[flowerbed_length - 1] == 0 and flowerbed[flowerbed_length - 2] == 0:
            n -= 1
            flowerbed[flowerbed_length - 1] = 1
            if n == 0:
                return True

        # if none of the above conditions are satisfied, then it is not possible to plant n more plants
        return False 

"""
Approach 2: adding sentinel (dummy) elements to the head and tail of the list to generalize them, so that I won't have to deal with them separately
Time: O(n)
"""
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed_with_sentinels = [0] + flowerbed + [0]
        for i in range (1, len(flowerbed_with_sentinels) -1):
            if (
                flowerbed_with_sentinels[i-1] == 0 
                and flowerbed_with_sentinels[i] == 0 
                and flowerbed_with_sentinels[i+1] == 0
            ):
                flowerbed_with_sentinels[i] = 1
                n -= 1
        return n <= 0
