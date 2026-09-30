# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        q = deque([root])

        cur = None
        while q:
            cur = q.pop()

            if cur.val == subRoot.val:
                res = self.checkSubtree(cur, subRoot)
                if res:
                    return res

            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)

        return False

    def checkSubtree(self, p, q) -> bool:
        if p and q:
            return p.val == q.val and \
                self.checkSubtree(p.left, q.left) and \
                self.checkSubtree(p.right, q.right)
        else:
            return p == q