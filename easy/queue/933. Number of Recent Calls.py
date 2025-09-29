"""
LeetCode 933 - Number of Recent Calls
Link: https://leetcode.com/problems/number-of-recent-calls/

Idea:
  - Keep track of all ping times in increasing order.
  - Each time ping(t) is called:
      * Add t to the end.
      * Remove from the front any times < t-3000.
      * The number of valid times left is the answer.
  - This is basically a "sliding time window" problem,
    but implemented with a "queue" idea.

Implementation detail:
  - In Python, list slicing or pop(0) is costly (O(n)).
  - To avoid that, keep a head index that points to the
    start of the valid window. We only move the head
    forward when old times expire.
  - No need to physically delete old elements.

Complexity:
  Time: Amortized O(1) per ping (each time is added once and removed once)
  Space: O(n), where n is the number of calls within the last 3000 ms
"""
class RecentCounter:

    def __init__(self):
        self.arr = []
        self.head = 0

    def ping(self, t: int) -> int:
        self.arr.append(t)
        # Queue idea with a list:
        # - Python list is dynamic; we just append new timestamps.
        # - We do NOT delete from the front (slice/pop(0) would copy/shift and be slow).
        # - Instead, keep a 'head' index that marks the start of the valid window.
        # - Elements before 'head' are logically discarded; we just skip them.

        while self.head < len(self.arr) and self.arr[self.head] < t - 3000:
            self.head += 1

        # size of the current window
        return len(self.arr) - self.head
      
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

"""
Approach:
  - Use a 'deque' as a queue of timestamps in increasing order.
  - On ping(t):
      * push t to the back
      * while the front < t-3000, pop from the front
      * the deque now holds exactly the times in [t-3000, t]
      * return its length
      
Benefits:
  - deque allows removing an element at O(1) cost
  - unlike pop(0) or slicing in a list, which costs O(n) due to 
    the nature to shift elements
  - deque is generally a better approach when solving sliding window
    or queue-type problems
  
Why this works:
  - t is strictly increasing, so expired times are always at the front.
  - deque supports O(1) append and O(1) popleft.

Complexity:
  - Time: Amortized O(1) per ping (each time is added once and removed once).
  - Space: O(k), where k is the number of pings in the last 3000 ms.
"""
from collections import deque

class RecentCounter:
    def __init__(self):
        # Use a deque = double-ended queue.
        # - append(x): push to the BACK (O(1))
        # - popleft(): pop from the FRONT (O(1))
        # It’s not a list; we use it because we need fast head removals.
        self.q = deque()

    def ping(self, t: int) -> int:
        # Times arrive in nondecreasing order, so the deque stays sorted by time.
        # Always record the new ping at the BACK.
        self.q.append(t)

        # Keep only times in the window [t-3000, t].
        # `while self.q` ensures the deque is non-empty before checking self.q[0].
        # self.q[0] is the FRONT (the oldest time). If it’s too old, drop it.
        while self.q and self.q[0] < t - 3000:
            self.q.popleft()

        # Now the deque holds exactly the recent calls within [t-3000, t].
        # Its length is the answer.
        return len(self.q)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
