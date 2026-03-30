class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers, res = set(nums), 0

        for n in nums:
            if n - 1 not in numbers:
                res = max(res, self.findSeqLen(n, numbers))
        return res

    def findSeqLen(self, num, numbers) -> int:
        num += 1;
        seqLen = 1;
        while True:
            if num in numbers:
                num += 1
                seqLen += 1
            else: return seqLen
