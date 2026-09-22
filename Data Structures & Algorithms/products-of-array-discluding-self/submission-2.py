class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zcount, total = 0, 1

        for n in nums:
            if n == 0:
                zcount += 1
                continue

            total *= n

        print(zcount, total)
        if zcount == 0:
            return [total // n for n in nums]
        elif zcount == 1:
            return [total if n == 0 else 0 for n in nums]
        elif zcount >= 2:
            return [0 for n in nums]

