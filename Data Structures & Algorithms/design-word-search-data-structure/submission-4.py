class node:
    def __init__ (self):
        self.children = [None] * 26
        self.marked = False

class WordDictionary:

    def __init__(self):
        self.root = node()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            c = ord(c) - ord('a')

            if not cur.children[c]:
                cur.children[c] = node()

            cur = cur.children[c]

        cur.marked = True

    def search(self, word: str) -> bool:
        def dfs(i, node):
            if not node:
                return False

            if i == len(word):
                return node.marked

            if word[i] == ".":
                for child in node.children:
                    if child and dfs(i + 1, child):
                        return True
            else:
                c = ord(word[i]) - ord('a')
                return dfs(i + 1, node.children[c])

            return False

        return dfs(0, self.root)


