class trie:
    def __init__(self):
        self.root = {}
        self.marker = "*"

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            cur = cur.setdefault(char, {})
        cur[self.marker] = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = {}
        res = []

        for word in words:
            cur = root
            for char in word:
                cur = cur.setdefault(char, {})
            cur["*"] = True

        n, m = len(board), len(board[0])
        def dfs(i, j, word, cur, visited):
            if i < 0 or i >= n or \
               j < 0 or j >= m:
                return
            if (i, j) in visited:
                return           

            char = board[i][j]

            if char not in cur:
                return

            cur = cur[char]
            word += char

            nonlocal res
            if "*" in cur and cur["*"]:
                res.append(word)
                cur["*"] = False

            visited.add((i, j))

            dfs(i - 1, j, word, cur, visited)
            dfs(i + 1, j, word, cur, visited)
            dfs(i, j - 1, word, cur, visited)
            dfs(i, j + 1, word, cur, visited)

            visited.remove((i, j))


        for i in range(n):
            for j in range(m):
                dfs(i, j, "", root, set())
        return res

        