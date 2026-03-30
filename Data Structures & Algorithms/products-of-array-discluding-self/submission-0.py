class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(len(nums)):
            output.append(self.findProd(nums, i))
        return output


    def findProd(self, nums: List[int], indx: int) -> int:
        prod = 1
        for j in range(len(nums)):
            if j == indx: continue
            else: prod *= nums[j]
        return prod