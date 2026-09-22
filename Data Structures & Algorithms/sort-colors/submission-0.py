class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = defaultdict(int)

        for n in nums:
            count[n] += 1

        idx = 0
        for c in range(3):
            for _ in range(count[c]):
                nums[idx] = c
                idx += 1