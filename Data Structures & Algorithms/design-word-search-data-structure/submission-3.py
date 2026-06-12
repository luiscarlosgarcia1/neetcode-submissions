class Node:
    def __init__ (self):
        self.children = {}
        self.marked = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        
        cur.marked = True

    def search(self, word: str) -> bool:
        def dfs(i, root):
            cur = root

            if i == len(word):
                return cur.marked

            c = word[i]
            if c == '.':
                for child in cur.children.values():
                    if dfs(i + 1, child):
                        return True
                return False
            else:
                if c not in cur.children:
                    return False
                return dfs(i + 1, cur.children[c])

            

        return dfs(0, self.root)