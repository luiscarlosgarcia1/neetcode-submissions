class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zcnt = 1, 0
        output = []
        for n in nums:
            if n != 0: prod *= n
            else: zcnt += 1
        
        if zcnt >= 2:
            return [0 for i in range(len(nums))]
        elif zcnt == 1:
            for n in nums:
                output.append(prod if n == 0 else 0)
            return output
        else:
            for n in nums:
                output.append(prod // n)
            return output