class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        ref = defaultdict(int)
        nums.sort()

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                comp = -(nums[i] + nums[j])
                if comp not in ref:
                    continue
                
                k = ref[comp]
                res.add((nums[k], nums[i], nums[j]))

            ref[nums[i]] = i

        return list(list(tup) for tup in res)