class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []
        for x, y in points:
            dist = (x**2 + y**2) ** 0.5
            heapq.heappush(heap, (-dist, [x, y]))
            if len(heap) > k:
                heapq.heappop(heap)

        for i in range(len(heap)):
            _, point = heapq.heappop(heap)
            res.append(point)

        return res