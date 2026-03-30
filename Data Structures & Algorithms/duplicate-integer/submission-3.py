class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        collection = set()
        for i in nums:
            collection.add(i)
        if len(collection) < len(nums):
            return True
        return False