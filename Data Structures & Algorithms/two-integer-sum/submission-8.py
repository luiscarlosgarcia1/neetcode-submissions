class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = set(nums)
        for i, n in enumerate(nums):
            if target - n in s:
                j = nums.index(target - n)
                if i != j:
                    return [min(i, j), max(i, j)]