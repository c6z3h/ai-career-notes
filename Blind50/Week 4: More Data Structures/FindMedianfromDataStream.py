class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small, self.large = [], []
        
    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """ 
        heapq.heappush(self.small, -1 * num)
        
        # if largest of small > smallest of large >> swap
        if self.large and self.small and (-1 * self.small[0] > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        # if len(diff)>1, push over
        if len(self.small)-len(self.large)>1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large)-len(self.small)>1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)
            
    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.small)>len(self.large):
            return -1 * self.small[0]
        if len(self.large)>len(self.small):
            return self.large[0]
        return float(self.large[0] + -1 * self.small[0])/2
    
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
