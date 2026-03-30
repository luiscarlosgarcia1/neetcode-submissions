# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        que = deque([root])

        while que:
            prevLen = len(que)
            for i in range(prevLen):
                if que[i] is None:
                    continue
                if que[i].val == subRoot.val:
                    if self.checkStack(que[i], subRoot):
                        return True
                
                que.append(que[i].left)
                que.append(que[i].right)

            for i in range(prevLen):
                que.popleft()
        return False

    def checkStack(self, root, subRoot) -> bool:
        stack = [(root, subRoot)]
        while stack:
            p, q = stack.pop()

            if not p and not q:
                continue
            if not p or not q or p.val != q.val:
                return False
            
            stack.append((p.left, q.left))
            stack.append((p.right, q.right))
        
        return True