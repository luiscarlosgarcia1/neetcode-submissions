# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        else:
            if head.next is None:
                return head
                
            former = head
            cur = former.next
            latter = cur.next

            head.next = None
            while True:
                cur.next = former
                if latter == None:
                    break
                former = cur
                cur = latter
                latter = cur.next
            
            head = cur
            return head