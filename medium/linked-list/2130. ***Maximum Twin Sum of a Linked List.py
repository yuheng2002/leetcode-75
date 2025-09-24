''' 
LeetCode 2130: Maximum Twin Sum of a Linked List — length count + in-place reverse
Link: https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

-------------------Approach following intuition--------------------
Plan:
1) First pass: count nodes to get n.
2) Walk n//2 steps to reach the start of the second half.
3) Reverse the second half in place.
4) Walk from the original head and the reversed second half in lockstep; track max pair sum.

Notes & pitfalls:
- After the reverse loop, the cursor is None; the new head of the reversed half is `prev`,
  so reset `second_head = prev` before pairing.
- Problem guarantees even length; both halves advance together and finish at the same time.

Complexity: O(n) time, O(1) extra space.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        best = 0
        count = 0 
        
        cur = head
        while cur:
            cur = cur.next
            count += 1
        
        second_head = head
        for i in range(count // 2):
            second_head = second_head.next
        
        prev = None
        while second_head:
            after = second_head.next
            second_head.next = prev

            prev = second_head
            second_head = after
        
        second_head = prev # without this line, second_head just went beyond the last node
        # prev now sits at the last node

        while head and second_head:
            best = max(best, head.val + second_head.val)
            head = head.next
            second_head = second_head.next
        
        return best

'''
--------------------Same General Approach + Cleaned Up Version--------------------
Why this version:
- This is a tightened version of the length-count approach. It uses the 2095
  "Delete the Middle Node" pattern (fast/slow pointers) to reach the midpoint
  in a single traversal, so we avoid an extra full pass and reduce constant factors.
- Fewer branches/variables while keeping O(n) time and O(1) extra space.

Core steps (high-level only):
1) Use fast/slow so that `slow` lands at the first node of the second half (even length).
2) Reverse the second half in place starting at `slow`.
3) Walk the first half and the reversed second half in lockstep; track the max twin sum.

Characteristics / pitfalls:
- After reversing, the head of the reversed half is `prev`; reset `second_head = prev`
  before pairing.
- Start the reverse at `slow` (not at `head`) to avoid misalignment.
- Even length guarantee means both pointers finish at the same time.

Complexity: O(n) time, O(1) extra space; usually faster in practice thanks to one less full pass.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # 1) find middle: slow at start of second half
        # technique used in 2095. Delete the Middle Node of a Linked List
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 2) reverse the second half (starting at slow)
        prev = None
        second_head = slow
        while second_head:
            after = second_head.next
            second_head.next = prev
            prev = second_head
            second_head = after

        second_head = prev  # prev now sits at the old tail (new head of reversed half)

        # 3) compute maximum twin sum
        best = 0
        while head and second_head:
            best = max(best, head.val + second_head.val)
            head = head.next
            second_head = second_head.next
        
        return best
        
