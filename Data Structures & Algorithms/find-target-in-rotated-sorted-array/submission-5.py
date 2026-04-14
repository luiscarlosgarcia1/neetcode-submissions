class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid

            if nums[low] <= nums[mid]:
                # mid is in greater side
                if target > nums[mid] or target < nums[low]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                # mid is in smaller side
                if target < nums[mid] or target > nums[high]:
                    high = mid - 1
                else:
                    low = mid + 1

        return -1