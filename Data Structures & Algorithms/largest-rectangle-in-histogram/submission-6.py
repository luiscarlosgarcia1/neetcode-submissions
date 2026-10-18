class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []

        for i in range(len(heights)):
            start = i
            while stack and heights[i] < stack[-1][1]:
                idx, h = stack.pop()
                res = max(res, (i - idx) * h)
                start = idx
            stack.append((start, heights[i]))

        while stack:
            idx, h = stack.pop()
            res = max(res, (len(heights) - idx) * h)

        return res
