class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []

        for i, n in enumerate(nums):
            comp = target - n
            if comp in nums and nums.index(comp) != i:
                ans.append(nums.index(comp))
                ans.append(i)
                return sorted(ans)