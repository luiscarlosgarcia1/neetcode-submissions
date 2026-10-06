class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        seen = set()

        ref = defaultdict(list)
        for par, child in edges:
            ref[par].append(child)
            ref[child].append(par)

        def dfs(node):
            if node in seen:
                return

            seen.add(node)
            for nbr in ref[node]:
                dfs(nbr)

        for node in range(n):
            if node in seen:
                continue
            else:
                res += 1
                dfs(node)

        return res
