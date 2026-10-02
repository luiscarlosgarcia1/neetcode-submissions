# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = ""

        def dfs(node):
            nonlocal res
            if not node:
                res += "n#"
                return

            res += str(node.val) + "#"
            dfs(node.left)
            dfs(node.right)

            return

        dfs(root)
        return res
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        i = 0

        def dfs():
            nonlocal i

            value = ""
            while data[i] != "#":
                value += data[i]
                i += 1
            i += 1

            if value == "n":
                return None

            int(value)
            node = TreeNode(value, dfs(), dfs())

            return node

        return dfs()