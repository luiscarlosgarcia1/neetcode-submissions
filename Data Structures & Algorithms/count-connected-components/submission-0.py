class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        ref = defaultdict(list)
        visited = set()

        for i, j in edges:
            ref[i].append(j)
            ref[j].append(i)

        def dfs(i):
            if i in visited:
                return

            visited.add(i)

            for j in ref[i]:
                dfs(j)

        for i in range(n):
            if i in visited:
                continue

            dfs(i)
            res += 1

        return res
