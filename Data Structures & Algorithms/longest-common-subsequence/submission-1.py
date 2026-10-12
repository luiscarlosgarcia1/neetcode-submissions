class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = [[None] * m for _ in range(n)]

        def dfs(i, j):
            if i >= n or j >= m:
                return 0
            if dp[i][j] is not None:
                return dp[i][j]

            res = 0
            if text1[i] == text2[j]:
                res += 1 + dfs(i + 1, j + 1)
            else:
                res += max(dfs(i + 1, j), dfs(i, j + 1))

            dp[i][j] = res
            return res

        return dfs(0, 0)