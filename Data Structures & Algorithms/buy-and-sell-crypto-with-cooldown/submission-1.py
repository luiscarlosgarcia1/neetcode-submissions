class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        def dfs(i, cur):
            if i >= len(prices):
                return 0

            if (i, cur) in dp:
                return dp[(i, cur)]

            skip = dfs(i + 1, cur)

            if cur == -1:
                buy = dfs(i + 1, prices[i])
                dp[(i, cur)] = max(skip, buy)
            else:
                sell = prices[i] - cur + dfs(i + 2, -1)
                dp[(i, cur)] = max(skip, sell)

            return dp[(i, cur)]

        return dfs(0, -1)