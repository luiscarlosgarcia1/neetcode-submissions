class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        combo = ""
        ref = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(i):
            nonlocal combo

            if i >= len(digits):
                res.append(combo)
                return

            for c in ref[digits[i]]:
                combo += c
                dfs(i + 1)
                combo = combo[:-1]
        
        if digits:
            dfs(0)
        return res