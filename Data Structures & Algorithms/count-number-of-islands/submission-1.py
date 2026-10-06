class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        seen = set()
        n, m = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= n or \
                j < 0 or j >= m:
                return

            if grid[i][j] == "0" or (i,j) in seen:
                return

            if grid[i][j] == "1":
                seen.add((i, j))

            dfs(i - 1, j)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)            

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and (i, j) not in seen:
                    dfs(i, j)
                    res += 1

        return res