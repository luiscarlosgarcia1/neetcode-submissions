class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def dfs(i, cur):
            if i >= len(nums):
                return 1 if cur == target else 0

            if (i, cur) in dp:
                return dp[(i, cur)]

            sub, add = cur - nums[i], cur + nums[i]
            res = dfs(i + 1, sub) + dfs(i + 1, add)

            dp[(i, cur)] = res
            return res

        return dfs(0, 0)