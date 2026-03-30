class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = set(nums)
        return len(n) < len(nums)