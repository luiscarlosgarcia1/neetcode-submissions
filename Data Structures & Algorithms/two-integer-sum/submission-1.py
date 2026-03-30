class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        col = set()
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    col.add(i)
                    col.add(j)
        return sorted(list(col))