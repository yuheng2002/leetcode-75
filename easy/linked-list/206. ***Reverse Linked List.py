"""
LeetCode 206: Reverse Linked List — iterative (my original version)
Link: https://leetcode.com/problems/reverse-linked-list/

-------- Version 1: my original iterative approach --------

Idea (what this version does):
- Start with two pointers at the front: prev=head, cur=head.next.
- Immediately cut prev.next to break the original forward edge.
- Then walk the list, flipping one edge at a time (cur.next = prev).
- Carry a third pointer `after` so we don’t lose the rest of the list.

Loop invariant:
- `prev` always points to the head of the already-reversed prefix.
- `cur` is the next node to process (the head of the remaining suffix).
- All nodes strictly before `prev` are now reversed and isolated.

Why the early `prev.next = None`:
- It disconnects the old head from its next node right away, so when we
  first flip `cur.next = prev`, we don’t accidentally create a 2-cycle.
- The final tail of the reversed list (which was the original head) must
  end in None anyway, so this line naturally sets that up.

Example [1,2,3,4,5]:
- Start: prev=1(None), cur=2
- Step1: 2→1, move to (prev=2, cur=3)
- Step2: 3→2, move to (prev=3, cur=4)
- ...
- End: prev=5 is the new head; return it.

Complexity:
- Time: O(n) — each edge flipped once
- Space: O(1) — constant extra pointers

Pitfalls this version avoids:
- Forgetting to cut the old head’s next (can cause a small cycle on step 1).
- Losing the rest of the list if you don’t save `after = cur.next` first.
"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        prev = head
        cur = head.next

        # Cut the old head’s forward link up front.
        prev.next = None

        while cur:
            after = cur.next       # Save next node
            cur.next = prev        # Flip edge

            prev = cur             # Advance both pointers
            cur = after

        # `prev` is now the new head (the old tail).
        head = prev
        return head

"""
-------- Version 2: simplified canonical iterative template --------

Idea (standard three-pointer loop):
- Use `prev`, `cur`, `after`:
    after = cur.next
    cur.next = prev
    prev = cur
    cur = after
- No special cases needed: empty or single-node lists fall out naturally.

Loop invariant:
- `prev` is the head of the reversed prefix.
- `cur` is the next node to reverse.
- `after` protects access to the remaining nodes.

Why this is simpler than Version 1:
- No need to pre-cut head.next or handle head specially.
- Fewer branches and symmetric updates each iteration.

Example [1,2,3,4,5]:
- Start: prev=None, cur=1
- Step1: 1→None, (prev=1, cur=2)
- Step2: 2→1,    (prev=2, cur=3)
- ...
- End: prev=5 is the new head.

Complexity:
- Time: O(n)
- Space: O(1)

Common mistakes to avoid:
- Not saving `after` before writing `cur.next`.
- Returning `head` instead of `prev` at the end.
"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head

        while cur:
            after = cur.next   # Save next
            cur.next = prev    # Flip edge

            prev = cur         # Advance
            cur = after

        # `prev` sits at the old tail, which is the new head.
        head = prev
        return head
"""
Idea in one line:
- Recursively reverse the suffix starting at head.next to get `new_head`, then
  point that next node back to `head` and cut `head`’s old forward link.

Base case — why this works:
- `if head is None or head.next is None: return head`
  * Empty list or single node is already “reversed”.
  * Note: `head` here is the local variable of the current frame (not a global).

What the call stack is doing (example: 1->2->3->4->5):
1) Go down: reverse(1) → reverse(2) → reverse(3) → reverse(4) → reverse(5)
2) At 5: base case hits, return 5. From now on every frame receives `new_head = 5`.
3) Unwind (each frame does only two pointer edits, then returns the same `new_head`):
   - `head.next.next = head`   # point “next” back to current (e.g., 5.next = 4)
   - `head.next = None`        # cut current’s old forward edge (e.g., 4.next = None)
   - `return new_head`         # keep bubbling up the same head (5)
   Result: 5 -> 4 -> 3 -> 2 -> 1 -> None

Why `head.next = None` matters:
- Middle nodes will soon have their `next` overwritten to point backward, so setting
  them to None first is harmless. The **original head (1)** won’t be overwritten later.
  If you forget `head.next = None` at that last unwind step, you leave `1 -> 2`
  intact and create a cycle: 5->4->3->2->1->2->1...

Why `new_head` stays 5:
- The deepest frame returns a reference to node 5. Upper frames never change that
  reference; they only rewire `next` pointers. So `new_head` is the same object
  in every return.

Complexity:
- Time: O(n) — each node is visited and its `next` is reassigned once.
- Extra space: O(n) — recursion stack. In Python, very long lists may hit the
  recursion limit; the iterative O(1)-space solution is safer for production.

Common pitfalls:
- Forgetting `self.` when calling recursively inside a class method.
- Forgetting `head.next = None`, causing a cycle.
- Not returning `new_head` on every frame.
- Confusing the local `head` (per frame) with the initial top-level head.
"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base cases:
        # - Empty list
        # - Single node
        # In both cases the list is already "reversed", so return head as-is.
        #
        # In the normal (multi-node) case, this base will eventually trigger
        # when recursion reaches the last node (the original tail).
        if head is None or head.next is None:
            return head

        # Call stack picture for [1,2,3,4,5]:
        #   new_head = reverse(1.next)  -> reverse(2)
        #   new_head = reverse(2.next)  -> reverse(3)
        #   new_head = reverse(3.next)  -> reverse(4)
        #   new_head = reverse(4.next)  -> reverse(5)
        # At reverse(5): head.next is None -> return head (i.e., return node 5)
        # So new_head becomes 5 at the deepest frame and stays 5 while we unwind.
        #
        # Important: the 'head' here is a local variable per frame; it is not the
        # "global" head. Each frame’s 'head' is just the current node for that frame.
        new_head = self.reverseList(head.next)

        # Unwinding step (do two pointer edits per frame):
        # 1) Point the next node back to current:
        #    head.next is the node we just reversed; make it point to 'head'.
        #    Example at head=4: head.next (5).next = 4   ->   5.next = 4
        head.next.next = head

        # 2) Cut current's old forward edge:
        #    This prevents cycles. For middle nodes this temporary None will be
        #    overwritten by their caller’s "point back" step, which is fine.
        #    For the original head (1), there is no caller to overwrite it, so
        #    setting 1.next = None is what terminates the final list:
        #    5 -> 4 -> 3 -> 2 -> 1 -> None
        #
        #    If we forget this line, the old edge (1 -> 2) remains and we get a cycle:
        #    5 -> 4 -> 3 -> 2 -> 1 -> 2 -> 1 -> ...
        head.next = None

        # Propagation:
        # Always return the same new_head (which is node 5 in the example).
        # We are not copying nodes—this is the same reference bubbling up.
        return new_head
