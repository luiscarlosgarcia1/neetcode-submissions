class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        cMax, cMin = 1, 1

        for n in nums:
            if n == 0:
                cMax, cMin = 1, 1
                continue

            nMax, nMin = n * cMax, n * cMin

            cMax = max(nMax, nMin, n)
            cMin = min(nMax, nMin, n)

            res = max(res, cMax)

        return res