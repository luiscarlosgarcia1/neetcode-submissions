# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and list2:
            # can get rid of this this starting block using a dummy node
            if list1.val < list2.val:
                start, list1 = list1, list1.next
            else:
                start, list2 = list2, list2.next
            
            cur = start
            while list1 and list2:
                if list1.val < list2.val:
                    cur.next, list1 = list1, list1.next
                else:
                    cur.next, list2 = list2, list2.next
                cur = cur.next

            cur.next = list1 if list1 else list2

            return start
        return list1 if list1 else list2


# decide starting list
# store next options as the new head of the lists since we don't need previous values anymore
# since we can't compare none type values we need to check for them before
# if none type is present then work down the rest of the other list
# else compare list values and go with next as the smaller one