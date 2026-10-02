import heapq

class MedianFinder:

    def __init__(self):
        self.leftMX, self.rightMN = [], []

    def addNum(self, num: int) -> None:
        if self.rightMN and num > self.rightMN[0]:
            heapq.heappush(self.rightMN, num)
        else:
            heapq.heappush(self.leftMX, -1 * num)

        if len(self.leftMX) > len(self.rightMN) + 1: # leftMX is too large
            val = -1 * heapq.heappop(self.leftMX)
            heapq.heappush(self.rightMN, val)
        if len(self.rightMN) > len(self.leftMX) + 1: # rightMN is too large
            val = heapq.heappop(self.rightMN)
            heapq.heappush(self.leftMX, -1 * val)

    def findMedian(self) -> float:
        if len(self.leftMX) > len(self.rightMN): # median is top left
            return -1 * self.leftMX[0]
        elif len(self.rightMN) > len(self.leftMX): # median is top right
            return self.rightMN[0]

        return (-1 * self.leftMX[0] + self.rightMN[0]) / 2.0
