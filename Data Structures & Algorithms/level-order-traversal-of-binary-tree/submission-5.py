# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = [root]

        while q:
            lvl, children = [], []

            for n in q:
                if n:
                    lvl.append(n.val)

                    children.append(n.left)
                    children.append(n.right)

            if lvl: 
                res.append(lvl)
            q = children

        return res
