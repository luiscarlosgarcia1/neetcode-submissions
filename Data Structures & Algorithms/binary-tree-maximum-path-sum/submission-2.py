# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')

        def dfs(root):
            nonlocal res

            if root is None:
                return 0

            s = root.val
            l = s + dfs(root.left)
            r = s + dfs(root.right)
            m = l + r - s

            res = max(res, s, l, r, m)
            return max(s, l , r)

        dfs(root)
        return res