# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(self, root: TreeNode, val: int) -> int:
            if root is None:
                return 0
            else:
                count = 0
                if root.val >= val:
                    count += 1
                    val = root.val

                return count + dfs(self, root.left, val) + dfs(self, root.right, val)

        return dfs(self, root, root.val)
