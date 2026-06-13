class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        subset = []
        def dfs(cur):
            if cur > target:
                return
            
            if cur == target:
                tmp = tuple(sorted(subset))
                if tmp not in res:
                    res.append(tmp)
                return

            for n in nums:
                subset.append(n)
                dfs(cur + n)
                subset.pop()

        dfs(0)
        return [list(x) for x in res]