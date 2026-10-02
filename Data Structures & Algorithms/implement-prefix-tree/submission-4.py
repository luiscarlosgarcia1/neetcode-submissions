class node:
    def __init__(self, EOW=False):
        self.marked = EOW
        self.children = [None] * 26

class PrefixTree:

    def __init__(self):
        self.root = node()

    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            c = ord(c) - ord('a')

            if not cur.children[c]:
                cur.children[c] = node()

            cur = cur.children[c]

        cur.marked = True

    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            c = ord(c) - ord('a')

            if not cur.children[c]:
                return False
            
            cur = cur.children[c]

        return cur.marked

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            c = ord(c) - ord('a')

            if not cur.children[c]:
                return False
            
            cur = cur.children[c]

        return True

        