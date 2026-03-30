class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        for i, low in enumerate(prices):
            if i != len(prices)-1:
                high = max(prices[i::1])
                prof = high - low
                if prof > best:
                    best = prof

        return best