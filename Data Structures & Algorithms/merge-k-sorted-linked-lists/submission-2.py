# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        while len(lists) > 1:
            mergedLists = []

            while len(lists) > 1:
                list1, list2 = lists.pop(), lists.pop()
                mergedLL = self.mergeLists(list1, list2)
                mergedLists.append(mergedLL)

            if lists:
                mergedLists.append(lists[0])

            lists = mergedLists
        
        return lists[0] if lists else None

    def mergeLists(self, list1, list2) -> ListNode:
        dummy = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        node.next = list1 or list2

        return dummy.next