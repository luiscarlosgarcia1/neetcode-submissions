class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(start, cur):
            if cur > target:
                return

            if cur == target:
                res.append(path.copy())
                return

            for i in range(start, len(nums)):
                path.append(nums[i])
                dfs(i, cur + nums[i])
                path.pop()

        dfs(0, 0)
        return res