class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ref = set(nums)
        res = 0

        for n in nums:
            if n - 1 in ref:
                continue
            
            tmp, seq = n + 1, 1
            while tmp in ref:
                seq += 1
                tmp += 1

            res = max(res, seq)

        return res
