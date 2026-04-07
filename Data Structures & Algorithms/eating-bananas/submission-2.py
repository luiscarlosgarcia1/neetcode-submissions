from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = max(piles)

        low, high = 1, res
        while low <= high:
            k = (low + high) // 2
            time = 0

            for p in piles:
                time += ceil(p / k)

            if time <= h:
                res = min(k, res)
                high = k - 1
            elif time > h:
                low = k + 1

        return res