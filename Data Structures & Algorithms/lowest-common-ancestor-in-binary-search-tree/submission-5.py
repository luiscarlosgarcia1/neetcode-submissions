# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        while root:
            # root is less than both: p and q both on right
            if root.val < p.val and root.val < q.val:
                root = root.right
            # root is greater than both: both on left
            elif root.val > p.val and root.val > q.val:
                root = root.left
            else:
                # root is between both: one is on left one is on right
                break

        return root