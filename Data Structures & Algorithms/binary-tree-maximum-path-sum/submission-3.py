# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')

        def dfs(node):
            nonlocal res

            if node is None:
                return 0

            left = node.val + dfs(node.left)
            right = node.val + dfs(node.right)
            full = left + right - node.val

            res = max(res, node.val, left, right, full)
            return max(node.val, left, right)

        dfs(root)
        return res