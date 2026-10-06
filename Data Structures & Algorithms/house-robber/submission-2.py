class Solution:
    def rob(self, nums: List[int]) -> int:
        res = 0
        dp = [-1] * len(nums)

        def dfs(i):
            if i >= len(nums):
                return 0

            if dp[i] != -1:
                return dp[i]
            
            take = nums[i] + dfs(i + 2)
            skip = dfs(i + 1)

            dp[i] = max(take, skip)
            return dp[i]

        one, two = 0, 0
        for i in range(len(nums) - 1, -1, -1):
            one, two = two, max(two, nums[i] + one)

        return two
            