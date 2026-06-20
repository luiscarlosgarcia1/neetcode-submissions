class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(string, start, end):
            if start == n and end == n:
                res.append(string)
                return

            if start < n:
                string += "("
                dfs(string, start + 1, end)
                string = string[:-1]

            if end < start:
                string += ")"
                dfs(string, start, end + 1)
                string = string[:-1]

        dfs("", 0, 0)
        return res