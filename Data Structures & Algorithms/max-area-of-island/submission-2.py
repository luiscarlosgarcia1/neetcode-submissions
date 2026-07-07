class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]

        for row in grid:
            print(", ".join(str(item) for item in row))


        def dfs(r, c):
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                grid[r][c] == 0 or
                visited[r][c]):
                return 0

            visited[r][c] = True

            area = 1
            area += dfs(r + 1, c)
            area += dfs(r - 1, c)
            area += dfs(r, c + 1)
            area += dfs(r, c - 1)

            return area
        

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    visited[i][j] = True
                    continue
                
                if not visited[i][j]:
                    res = max(res, dfs(i, j))

        return res