"""
LeetCode 1657: Determine if Two Strings Are Close
Link: https://leetcode.com/problems/determine-if-two-strings-are-close/

Approach 1 — Manual counts + set check:
- First, lengths must match.
- The two words must use the same set of characters (you can’t create a
  new letter by swapping/relabeling).
- Compare the *multiset* of frequencies: take the counts of each letter
  from both words, sort those counts, and check they’re equal. We don’t
  care which letter owns which count, only the bag of counts.

Why it works:
- Allowed operations let you reorder letters arbitrarily and “swap
  counts” between letters, but you cannot introduce new letters or lose
  existing ones. Same char set + same bag of counts is exactly the
  necessary and sufficient condition.

Complexity: Time O(n + σ log σ), Space O(σ)
(σ = number of distinct letters; for lowercase a–z, σ ≤ 26)
"""
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        S1 = set(word1)
        S2 = set(word2)

        dictionary1 = {}
        dictionary2 = {}

        for char1, char2 in zip(word1, word2):
            dictionary1[char1] = dictionary1.get(char1, 0) + 1
            dictionary2[char2] = dictionary2.get(char2, 0) + 1

        dictionary1 = list(dictionary1.values())
        dictionary2 = list(dictionary2.values())

        return S1 == S2 and sorted(dictionary1) == sorted(dictionary2)
      
"""
Approach 2 — Counter-based (same logic, cleaner code):
- Count letters with Counter (C-optimized).
- Keys (the letter set) must match: c1.keys() == c2.keys().
- Bag of counts must match: sorted(c1.values()) == sorted(c2.values()).

Notes:
- Comparing keys enforces “no new/missing letters”.
- Sorting the values compares frequency bags (which letter owns which
  count doesn’t matter).
- You can also do Counter(c1.values()) == Counter(c2.values()) to avoid
  sorting; both are fine here.

Complexity: Time O(n + σ log σ), Space O(σ)
"""
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2]):
            return False
        
        # Counter creates a dict-like mapping: letter -> frequency
        c1 = Counter(word1)
        c2 = Counter(word2)

        # Keys are unordered sets of letters; they must match exactly.
        if c1.keys() != c2.keys():  # equivalent to: set(c1) != set(c2)
            return False

        return sorted(c1.values()) == sorted(c2.values())
