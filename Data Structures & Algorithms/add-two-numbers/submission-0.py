# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s = l1.val + l2.val
        carry = s // 10
        head = ListNode(s % 10)
        cur, l1, l2 = head, l1.next, l2.next

        while l1 or l2:
            s = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = s // 10
            
            cur.next = ListNode(s % 10)
            cur, l1, l2 = cur.next, (l1.next if l1 else None), (l2.next if l2 else None)
        
        if carry:
            cur.next = ListNode(carry)

        return head