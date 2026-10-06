class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        n, m = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(i, j, ocean, prev):
            if i < 0 or i >= n or \
               j < 0 or j >= m:
                return

            if heights[i][j] < prev:
                return

            if (i ,j) in ocean:
                return

            ocean.add((i, j))

            for x, y in dirs:
                dfs(i + x, j + y, ocean, heights[i][j])

        # left, right
        for i in range(n):
            dfs(i, 0, pac, heights[i][0])
            dfs(i, m - 1, atl, heights[i][m - 1])

        # top, bottom
        for j in range(m):
            dfs(0, j, pac, heights[0][j])
            dfs(n - 1, j, atl, heights[n - 1][j])


        res = []
        for i in range(n):
            for j in range(m):
                if (i, j) in pac and (i, j) in atl:
                    res.append([i, j])

        return res