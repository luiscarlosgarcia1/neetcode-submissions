from functools import cache
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2

        @cache
        def dfs(i, cur):
            if i == len(nums):
                return False
            if cur > target:
                return False
            if cur == target:
                return True

            return dfs(i + 1, cur) or \
                dfs(i + 1, cur + nums[i])

        return dfs(0, 0)