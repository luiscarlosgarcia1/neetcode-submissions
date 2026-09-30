# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def checkTree(self, root, interval) -> bool:
            if root is None:
                return True

            return interval[0] < root.val and root.val < interval[1] and \
                checkTree(self, root.left, (interval[0], root.val)) and \
                checkTree(self, root.right, (root.val, interval[1]))
            
        tup = (float('-inf'), float('inf'))
        return checkTree(self, root, tup)