class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        res = []
        perms = self.permute(nums[1:])

        for perm in perms:
            perm.insert(0, nums[0])
            res.append(perm.copy())

            for i in range(1, len(perm)):
                perm[i - 1], perm[i] = perm[i], perm[i - 1]
                res.append(perm.copy())

        return res