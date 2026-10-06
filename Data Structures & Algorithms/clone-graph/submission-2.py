"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        ref = {}

        def dfs(node):
            if node is None:
                return
                
            if node in ref:
                return ref[node]

            clone = Node(node.val)
            ref[node] = clone

            for nbr in node.neighbors:
                clone.neighbors.append(dfs(nbr))

            return clone 

        return dfs(node)