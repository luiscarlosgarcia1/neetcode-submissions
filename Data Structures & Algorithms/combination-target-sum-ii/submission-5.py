class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        candidates.sort()

        def dfs(i, cur):
            if cur == target:
                res.append(subset.copy())
                return 

            if cur > target or i >= len(candidates):
                return

            subset.append(candidates[i])
            dfs(i + 1, cur + candidates[i])

            subset.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1

            dfs(i + 1, cur)

        dfs(0, 0)
        return res