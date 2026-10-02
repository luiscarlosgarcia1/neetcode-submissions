class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()

        n, m = len(board), len(board[0])
        def dfs(i, j, cur):
            # out of bounds
            if i < 0 or i >= n or \
                j < 0 or j >= m:
                return False

            # stop exploration on bad branch
            if len(cur) > len(word) or cur != word[:len(cur)]:
                return

            # cannot use the same cell twice
            if (i, j) in visited:
                return False

            cur += board[i][j]

            # word found
            if cur == word:
                return True

            visited.add((i, j))

            res = dfs(i - 1, j, cur) or dfs(i + 1, j, cur) or \
                  dfs(i, j - 1, cur) or dfs(i, j + 1, cur)

            visited.remove((i, j))

            return res

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0] and dfs(i, j, ""):
                    return True

        return False