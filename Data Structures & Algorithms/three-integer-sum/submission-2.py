class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = set()

        nums.sort()
        for i in range(len(nums)):
            l, r = i+1, len(nums)-1
            while l < r:
                target = -nums[i]
                comp = nums[l] + nums[r]
                if comp < target:
                    l += 1
                elif comp > target:
                    r -= 1
                else:
                    triplet = (nums[i], nums[l], nums[r])
                    if triplet not in seen:
                        seen.add(triplet)
                        res.append(list(triplet))
                    else:
                        l, r = l+1, r-1
        return res