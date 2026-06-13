class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        subset = []
        def dfs(i, cur):
            if i == len(nums) or cur > target:
                return
            
            if cur == target:
                res.append(subset.copy())
                return

            subset.append(nums[i])
            dfs(i, cur + nums[i])

            subset.pop()
            dfs(i + 1, cur)

        dfs(0, 0)
        return res