import heapq
class MedianFinder:

    def __init__(self):
        self.maxheap=[]
        self.minheap=[]

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxheap,-num)
        heapq.heappush(self.minheap,-heapq.heappop(self.maxheap))
        if (len(self.maxheap)<len(self.minheap)):
            heapq.heappush(self.maxheap,-heapq.heappop(self.minheap))

    def findMedian(self) -> float:
        if len(self.maxheap)==len(self.minheap):
            return(-self.maxheap[0]+self.minheap[0])/2.0
        return -self.maxheap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()