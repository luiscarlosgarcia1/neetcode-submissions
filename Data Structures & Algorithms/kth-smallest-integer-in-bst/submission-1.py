# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []

        def dfs(self, node):
            if node is None:
                return

            dfs(self, node.left)
            res.append(node.val)
            dfs(self, node.right)

        dfs(self, root)
        return res[k - 1]