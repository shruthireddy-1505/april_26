# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        frst = dummy
        curr = dummy
        prev = None
        for i in range(left-1):
            frst = frst.next
            curr = curr.next
        curr = curr.next
        d = curr
        for i in range(right-left+1):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        frst.next = prev
        d.next = curr
        return dummy.next


        