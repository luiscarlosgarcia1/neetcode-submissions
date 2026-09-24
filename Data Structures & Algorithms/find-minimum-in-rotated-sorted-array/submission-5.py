class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]

        while l < r:
            mid = (r + l) // 2
            if nums[l] > nums[r]:
                if nums[l] < nums[mid]:
                    l = mid
                elif nums[l] > nums[mid]:
                    r = mid
                else:
                    return min(nums[l], nums[r])

            elif nums[l] < nums[r]:
                r = mid

        return nums[l]
