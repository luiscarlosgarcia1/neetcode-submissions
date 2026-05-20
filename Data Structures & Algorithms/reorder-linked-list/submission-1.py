# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return head

        slow, fast = head, head.next

        # split list into halves
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # break the link
        first, second = head, slow.next
        slow.next = None

        # reverse second
        prev, curr = None, second
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        second = prev

        curr = head
        while first and second:
            first = first.next
            curr.next = second
            curr = second
            second = second.next
            curr.next = first
            curr = first

        return None