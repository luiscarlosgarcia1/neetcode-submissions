class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ref = defaultdict(int)

        for n in nums:
            ref[n] += 1
            if ref[n] > 1:
                return n