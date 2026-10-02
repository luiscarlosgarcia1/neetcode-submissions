from functools import cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)

        def dfs(cur):
            if cur > amount:
                return float('inf')
            if cur == amount:
                return 0

            if dp[cur] != -1:
                return dp[cur]

            dp[cur] = 1 + min(dfs(cur + c) for c in coins)

            return dp[cur]

        res = dfs(0)
        return -1 if res == float('inf') else res