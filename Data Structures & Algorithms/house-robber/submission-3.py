class Solution:
    def rob(self, nums: List[int]) -> int:
        one, two = 0, 0
        for i in range(len(nums) - 1, -1, -1):
            one, two = two, max(two, nums[i] + one)

        return two
            