"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        res = 0
        minheap = [float('inf')]
        intervals.sort(key=lambda x: x.start)

        for i in intervals:
            print(i.start, i.end)

        for i in intervals:
            # does it conflict
            if i.start < minheap[0]:
                res += 1
            else:
                heapq.heappop(minheap)

            heapq.heappush(minheap, i.end)

        return res