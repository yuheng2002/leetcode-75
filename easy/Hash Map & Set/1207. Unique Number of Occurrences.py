"""
LeetCode 1207: Unique Number of Occurrences
Link: https://leetcode.com/problems/unique-number-of-occurrences/

Approach 1: Count -> list counts -> compare with set
- Count each value with a dict: value -> frequency.
- Put all frequencies into a list, then compare:
  if len(list_of_freq) == len(set(list_of_freq)), all counts are unique.
Why it works: a set does not allow reptitions, so it removes duplicates; equality of sizes means no frequency was repeated.
Time: O(n) to count + O(u) to build/set where u is #distinct values  (overall O(n))
Space: O(u) for the frequency map and the list/set of counts
"""
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dictionary = {}
        for x in arr:
            dictionary[x] = dictionary.get(x, 0) + 1

        lst = []
        for key in dictionary:
            lst.append(dictionary[key])

        n = len(lst)
        lst = set(lst)
        m = len(lst)

        return m == n

"""
Approach 2: Count -> use set(dict.values()) directly
- Same idea as Approach 1, but skip building an intermediate list.
- Compare len(dict.values()) with len(set(dict.values())).
  (Careful: set(dictionary) would take the *keys*; use .values() to take counts.)
Why it works: if any frequency repeats, the set of frequencies gets smaller.
Time: O(n) overall
Space: O(u)
"""
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dictionary = {}
        for x in arr:
            dictionary[x] = dictionary.get(x, 0) + 1

        n = len(dictionary)

        m = len(set(dictionary.values())) 
        # note set(dictionary) will only extract the keys
        # make sure to call .values() to extract the values

        return m == n
