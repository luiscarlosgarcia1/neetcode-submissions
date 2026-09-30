# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        
        if root.val == subRoot.val:
            res = self.checkSubtree(root, subRoot)
            if res: return True

        return self.isSubtree(root.left, subRoot) or \
            self.isSubtree(root.right, subRoot)

    def checkSubtree(self, p, q) -> bool:
        if p and q:
            return p.val == q.val and \
                self.checkSubtree(p.left, q.left) and \
                self.checkSubtree(p.right, q.right)
        else:
            return p == q