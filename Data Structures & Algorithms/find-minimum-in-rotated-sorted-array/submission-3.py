class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1
        res = nums[0]

        while low <= high:
            if nums[low] < nums[high]:
                return min(nums[low], res)
                
            mid = (low + high) // 2
            res = min(nums[mid], res)

            if nums[mid] >= nums[low]:
                low = mid + 1
            elif nums[mid] < nums[high]:
                high = mid - 1

        return res