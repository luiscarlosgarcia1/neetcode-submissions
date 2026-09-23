class Solution:
    def sortColors(self, nums: List[int]) -> None:
        one = two = 0

        for n in nums:
            if n == 0:
                one += 1
                two += 1
            elif n == 1:
                two += 1

        for i in range(0, one):
            nums[i] = 0
        for i in range(one, two):
            nums[i] = 1
        for i in range(two, len(nums)):
            nums[i] = 2