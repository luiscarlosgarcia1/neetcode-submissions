class Solution:
    def trap(self, height: List[int]) -> int:
        res = [0] * len(height)
        l, r = 0, len(height) - 1
        lm, rm = -1, -1

        while l <= r:
            lm = max(lm, height[l])
            rm = max(rm, height[r])

            if height[l] <= height[r]:
                res[l] = lm - height[l]
                l += 1
            else:
                res[r] = rm - height[r]
                r -= 1

        return sum(res)
