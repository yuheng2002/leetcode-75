'''
LeetCode 328: Odd Even Linked List — iterative
Link: https://leetcode.com/problems/odd-even-linked-list/

Goal:
- Reorder the list so that all nodes at odd indices come first, followed by
  all nodes at even indices. Indices are 1-based: head is index 1 (odd),
  head.next is index 2 (even), and so on.
- Keep the original relative order inside the odd group and inside the even group.
- Use O(1) extra space and O(n) time.

Idea:
- Maintain three pointers:
    odd       -> the tail of the growing odd list
    even      -> the tail of the growing even list
    even_head -> the fixed head of the even list (needed to stitch at the end)
- In each loop:
    1) Link odd to the next odd node (which is currently even.next), then advance odd.
    2) Link even to the next even node (which is now odd.next), then advance even.
- When we finish, connect the odd tail to even_head.

Loop invariant:
- All nodes up to 'odd' form a correct odd-index chain.
- All nodes up to 'even' form a correct even-index chain starting at 'even_head'.
- The unprocessed suffix begins at 'odd.next' (if any).
- Because 'even' always stays one step ahead of 'odd', checking 'even' and
  'even.next' is sufficient to know whether another full iteration is possible.

Edge cases:
- Empty list or single node: already satisfies the order, just return head.
- Final node can be odd or even; stitching 'odd.next = even_head' works in both cases.

Complexity:
- Time: O(n) — each node is relinked once.
- Space: O(1) — only a few pointers are used.

Common pitfalls:
- Forgetting to save 'even_head' before re-linking (you lose the even list head).
- Advancing pointers in the wrong order (always rewire first, then move).
- Overly strict loop condition; 'while even and even.next' is enough, but the
  longer condition is also correct and safe.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Special cases: empty list or single node → nothing to reorder.
        if head is None or head.next is None:
            return head

        odd = head                           # tail of the odd chain
        even_head = head.next                # fixed head of the even chain (needed at the end)
        even = head.next                     # tail of the even chain

        # In principle, checking only `even` and `even.next` is enough because
        # `even` always stays one step ahead of `odd`. The longer condition below is fine too.
        while odd and odd.next and even and even.next:
            # Link current odd to the next odd (which is `even.next`), then advance odd.
            odd.next = even.next
            odd = even.next

            # Now update the even side: link current even to the next even
            # (which is `odd.next` after the odd move), then advance even.
            # Order matters: rewire before moving pointers, or risk losing nodes.
            even.next = odd.next
            even = odd.next

        # Stitch the two chains: odd block first, then the even block we saved.
        odd.next = even_head
        return head
