from functools import cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        @cache
        def dfs(cur):
            if cur > amount:
                return float('inf')
            if cur == amount:
                return 0

            return 1 + min(dfs(cur + c) for c in coins)

        res = dfs(0)
        return -1 if res == float('inf') else res