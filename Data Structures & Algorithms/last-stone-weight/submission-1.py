class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            x, y = -heapq.heappop(heap), -heapq.heappop(heap)
            print(x, y)
            if x == y:
                continue
            
            heapq.heappush(heap, -(x - y))

        return -heap[0] if heap else 0