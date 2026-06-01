# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        Q = collections.deque([root])
        res = []

        while Q:
            for i in range(len(Q)):
                cur = Q.popleft()

                if cur.left:
                    Q.append(cur.left)
                if cur.right:
                    Q.append(cur.right)

            res.append(cur.val)

        return res