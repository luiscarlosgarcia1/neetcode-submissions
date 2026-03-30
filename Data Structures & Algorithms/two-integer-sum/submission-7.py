class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            comp = target - n
            if comp in nums and nums.index(comp) != i:
                return sorted([i, nums.index(comp)])