class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = {}
        res = []

        for word in words:
            cur = root
            for char in word:
                cur = cur.setdefault(char, {})
            cur["*"] = word

        n, m = len(board), len(board[0])
        def dfs(i, j, cur, visited):
            # three base cases
            if i < 0 or i >= n or \
               j < 0 or j >= m:
                return

            if (i, j) in visited:
                return   

            char = board[i][j]
            if char not in cur:
                return

            # traverse
            cur = cur[char]

            # append to res if the word exists
            nonlocal res
            if "*" in cur and cur["*"]:
                res.append(cur["*"])
                cur["*"] = False # dedupe

            visited.add((i, j))

            dfs(i - 1, j, cur, visited)
            dfs(i + 1, j, cur, visited)
            dfs(i, j - 1, cur, visited)
            dfs(i, j + 1, cur, visited)

            visited.remove((i, j))


        for i in range(n):
            for j in range(m):
                dfs(i, j, root, set())
        return res

        