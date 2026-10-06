class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * n
        dp[-1] = 1
        def dfs(i):
            if i > n:
                return 0 
            if i == n:
                return 1

            if dp[i] != -1:
                return dp[i]

            res = 0
            res += dfs(i + 1)
            res += dfs(i + 2)

            dp[i] = res
            return res


        return dfs(0)