class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        dq = collections.deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    dq.append((r, c))

        def bfs():
            dist = 0

            while dq:
                for _ in range(len(dq)):
                    i, j = dq.popleft()

                    if (i < 0 or i >= rows or
                        j < 0 or j >= cols or
                        grid[i][j] == -1 or
                        visited[i][j]):
                        continue

                    visited[i][j] = True
                    grid[i][j] = dist

                    dq.append((i + 1, j))
                    dq.append((i - 1, j))
                    dq.append((i, j + 1))
                    dq.append((i, j - 1))

                dist += 1

        bfs()