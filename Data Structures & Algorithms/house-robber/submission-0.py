class Solution:
    def rob(self, nums: List[int]) -> int:
        h1, h2 = 0, 0

        for n in nums:
            h1, h2 = h2, max(n + h1, h2)

        return h2