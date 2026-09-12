class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            dp = 1
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    dp = max(dp, 1 + LIS[j])
            LIS[i] = dp

        return max(LIS)