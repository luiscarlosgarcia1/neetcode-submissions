class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()

        n = len(intervals)
        i = 0

        while i < n:
            cur = intervals[i]
            i += 1
            while i < n and cur[1] >= intervals[i][0]:
                cur[0] = min(cur[0], intervals[i][0])
                cur[1] = max(cur[1], intervals[i][1])
                i += 1
            res.append(cur)

        return res