'''
LeetCode 2095: Delete the Middle Node of a Linked List — two-pointer
Link: https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

Idea:
- Use slow/fast pointers to locate the middle in one pass.
  `slow` moves 1 step, `fast` moves 2 steps; `prev` trails `slow`.
  When the loop stops, `slow` is the middle (the floor(n/2)-th, 0-indexed).
  Delete it by linking `prev.next = slow.next`.

Edge cases:
- List of length 1 → return None (deleting the only node yields an empty list).

Complexity:
- Time: O(n) (single traversal)
- Space: O(1) (constant extra pointers)

Pitfalls:
- Forgetting to advance `prev` with `slow` (you need it to relink).
- Off-by-one loop condition that picks the wrong middle on even lengths.
- Handling length-1 lists (must return None).
'''
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        prev = None  # previous node of `slow` (needed to relink around the middle)

        # Length-1 list: deleting the only node leaves an empty list.
        if head.next == None:
            return None
          
        # Loop guard:
        # `while fast is not None and fast.next is not None:` ensures we stop when
        # `fast` reaches the end or steps past it, which gives the required middle
        # for both odd and even lengths per the problem definition.
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            prev = slow
            slow = slow.next

        # Delete the middle node (`slow`) by skipping it.
        prev.next = slow.next
        return head
