class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        ref = defaultdict(list)
        visited = set()

        for i, j in edges:
            ref[i].append(j)
            ref[j].append(i)

        def dfs(i, prev):
            if i in visited:
                return False
            
            visited.add(i)

            for j in ref[i]:
                if j != prev and not dfs(j, i):
                    return False

            return True

        return dfs(0, 0) and n == len(visited)