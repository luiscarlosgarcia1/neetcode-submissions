class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
            
        ref = defaultdict(list)
        for par, child in edges:
            ref[par].append(child)
            ref[child].append(par)

        seen = set()

        def dfs(node, par):
            if node in seen:
                return False

            seen.add(node)
            for nbr in ref[node]:
                if nbr == par:
                    continue
                if not dfs(nbr, node):
                    return False

            return True

        return dfs(0, -1) and len(seen) == n