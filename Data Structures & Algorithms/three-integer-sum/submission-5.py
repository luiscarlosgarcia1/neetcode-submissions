class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()

        for i in range(len(nums)):
            j, k = i + 1, len(nums) - 1
            while j < k:
                target = -(nums[i])
                comp = nums[j] + nums[k]
                if comp == target:
                    res.add((nums[i], nums[j], nums[k]))
                    j, k = j + 1, k - 1
                elif comp < target:
                    j += 1
                elif comp > target:
                    k -= 1

        return list(list(tup) for tup in res)