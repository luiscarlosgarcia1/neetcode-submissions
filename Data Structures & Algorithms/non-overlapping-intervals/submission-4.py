class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort()
        cur = intervals[0][1]

        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if cur > start:
                res += 1
                cur = min(cur, end)
            else:
                cur = end

        return res