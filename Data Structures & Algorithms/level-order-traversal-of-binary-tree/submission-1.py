# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        Q = collections.deque([root])
        res = []

        while Q:
            lvl = []

            for i in range(len(Q)):
                cur = Q.popleft()
                if cur is None:
                    continue
                
                if cur.left:
                    Q.append(cur.left)
                if cur.right:
                    Q.append(cur.right)

                lvl.append(cur.val)

            res.append(lvl)

        return res