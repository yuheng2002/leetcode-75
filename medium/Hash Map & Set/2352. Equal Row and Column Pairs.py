"""
LeetCode 2352 — Equal Row and Column Pairs
Link: https://leetcode.com/problems/equal-row-and-column-pairs/

Idea in one line:
Count how many times each row pattern appears and how many times each
column pattern appears, then sum a*b over all shared patterns (Cartesian product).

Why this works:
- A “pair” is formed when a row equals a column element-by-element.
- If some pattern P appears a times among rows and b times among columns,
  it contributes a*b pairs (every row-P can pair with every col-P).
  This is a Cartesian product count, not max/min.

Implementation notes:
- Rows: `Counter(tuple(row) for row in grid)`
    * We convert each row (a list) to a tuple so it’s hashable and can
      be used as a Counter key. Lists are unhashable; tuples are fine.
- Cols: either
    * Pythonic: `Counter(zip(*grid))`  ← `zip(*grid)` transposes rows→cols,
      and each produced item is already a tuple; or
    * Manual: collect each column j via `[grid[i][j] for i in range(n)]`
      and `tuple(...)` it before counting (that’s what this solution does).
- Summation: iterate the intersection of keys and add
  `row_cnt[k] * col_cnt[k]` for each pattern k.

Pitfalls to avoid:
- Don’t do `Counter(grid)` or `Counter(tuple(grid))`: the inner lists
  are still unhashable. Convert each inner list (row/col) to a tuple.
- Don’t use `Counter &` (min-by-key) or `max(a,b)` for combining counts;
  the correct contribution is `a * b`.

Complexity:
- Time: O(n^2) to build both Counters + O(m) to aggregate, where m is
  the number of distinct row/col patterns (m ≤ n).
- Space: O(n^2) in the worst case for storing all unique patterns.

Python mini-tips:
- Generator form `Counter(tuple(row) for row in grid)` avoids a temp list.
- `zip(*grid)` means “unpack rows as separate iterables into zip”, which
  aligns same indices together and effectively transposes the matrix.
"""
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        #{[3,1,2,2]:1, [1,4,4,5]:1, [2,4,2,2]:2}
        #{[3,1,2,2]:1, [1,4,4,4]:1, [2,4,2,2]:1, [2,5,2,2]:1}

        row_cnt = Counter(tuple(row) for row in grid) # every row becomes tuple

        # equivalent to col_cnt = Counter(tuple(col) for col in zip(*grid))
        cols = []
        for j in range(len(grid)):
            col = []
            for i in range(len(grid)):
                col.append(grid[i][j])
            cols.append(tuple(col))
        
        col_cnt = Counter(cols)

        n = 0

        for key in row_cnt & col_cnt:
            # here calculate the cartesian product
            # not max(row_cnt[key], col_cnt[key]), this only works for (1,2)
            n += row_cnt[key] * col_cnt[key]
        
        return n
