class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums, res = set(nums), 0

        for n in nums:
            if n - 1 not in nums:
                res = max(res, self.findSeqLen(n, nums))
        return res

    def findSeqLen(self, i, nums) -> int:
        i += 1
        leng = 1
        while True:
            if i in nums:
                i += 1
                leng += 1
            else: return leng