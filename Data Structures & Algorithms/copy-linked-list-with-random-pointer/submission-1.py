"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        copy = Node(head.val)
        old, new = head.next, copy
        ref = {head: copy}

        while old:
            node = Node(old.val)
            ref[old] = node
            new.next = node
            old, new = old.next, new.next

        old, new = head, copy
        while old:
            new.random = ref[old.random] if old.random else None
            old, new = old.next, new.next

        return copy