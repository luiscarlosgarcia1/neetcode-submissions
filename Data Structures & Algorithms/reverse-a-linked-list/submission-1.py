# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        prev, nxt = None, head.next
        while head:
            head.next = prev
            prev = head
            head = nxt
            nxt = head.next if head else None

        return prev