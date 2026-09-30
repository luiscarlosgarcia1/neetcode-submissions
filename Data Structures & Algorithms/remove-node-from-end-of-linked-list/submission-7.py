# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = cur = ListNode(0, head)
        buffer = head

        for _ in range(n):
            buffer = buffer.next

        while buffer:
            cur = cur.next
            buffer = buffer.next

        cur.next = cur.next.next

        return dummy.next