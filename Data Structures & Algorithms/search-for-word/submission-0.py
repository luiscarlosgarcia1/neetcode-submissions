class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        res = False

        rows, cols = len(board), len(board[0])
        visited = [[False] * cols for _ in range(rows)]

        def dfs(i, j, pos):
            if pos == len(word):
                return True

            if (i < 0 or j < 0 or
                i >= rows or j >= cols or
                word[pos] != board[i][j] or 
                visited[i][j]):
                return False

            visited[i][j] = True
            res = (dfs(i - 1, j, pos + 1) or
                   dfs(i + 1, j, pos + 1) or 
                   dfs(i, j - 1, pos + 1) or 
                   dfs(i, j + 1, pos + 1))
            visited[i][j] = False

            return res
            
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j ,0): 
                    return True

        return False
