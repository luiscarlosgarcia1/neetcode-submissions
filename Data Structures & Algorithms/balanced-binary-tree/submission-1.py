# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        else:
            leftBalance = self.isBalanced(root.left)
            rightBalance = self.isBalanced(root.right)

            leftHeight = self.getHeight(root.left)
            rightHeight = self.getHeight(root.right)
            diff = abs(leftHeight - rightHeight)

            if leftBalance and rightBalance and diff <= 1:
                return True
            return False

    def getHeight(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            return 1 + max(self.getHeight(root.left), self.getHeight(root.right))