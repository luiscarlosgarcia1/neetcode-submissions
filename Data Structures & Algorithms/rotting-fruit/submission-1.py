class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        res = 0
        dq = collections.deque()
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]

        def append(i, j):
            if (i < 0 or i >= rows or j < 0 or j >= cols or
                    grid[i][j] == 0 or visited[i][j]):
                    return

            dq.append((i, j))
            visited[i][j] = True
            
        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    append(r, c)

        if fresh == 0:
            return 0

        time = -1
        while dq:
            for _ in range(len(dq)):
                i, j = dq.popleft()

                if grid[i][j] == 1:
                    fresh -= 1

                append(i + 1, j)
                append(i - 1, j)
                append(i, j + 1)
                append(i, j - 1)

            time += 1

        return -1 if fresh else time
