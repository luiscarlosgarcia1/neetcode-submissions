class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        collect = set(nums)
        return len(collect) != len(nums)