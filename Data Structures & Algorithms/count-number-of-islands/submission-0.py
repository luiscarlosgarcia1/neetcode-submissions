class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]

        def dfs(i, j):
            if (i < 0 or j < 0 or
                i >= rows or j >= cols or
                visited[i][j] or
                grid[i][j] == "0"):
                return

            visited[i][j] = True
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "0":
                    visited[i][j] = True
                    continue

                if not visited[i][j]:
                    res += 1
                    dfs(i,j)

        return res