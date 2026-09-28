# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return head

        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        temp = slow
        slow = slow.next
        temp.next = None

        prev, temp = None, None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        left, right = head, prev
        dummy = node = ListNode()
        while left and right:
            node.next = left
            left = left.next
            node = node.next

            node.next = right
            right = right.next
            node = node.next

        node.next = left