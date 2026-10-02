from functools import cache

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        @cache
        def dfs(i, cur):
            if cur > amount:
                return 0
            print(cur)
            if cur == amount:
                return 1

            count = 0
            for j in range(i, len(coins)):
                count += dfs(j, cur + coins[j])
            return count

        return dfs(0, 0)