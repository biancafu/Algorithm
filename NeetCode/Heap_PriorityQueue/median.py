#we will keep track of the numbers with 2 heaps
#the two heaps will have every element in left heap <= every element in right heap
#and the length of heap would be always same or differ in 1 becuz we can have odd length

#faster solution using same logic as neetcode: 97%~87% speed 51% memory (stable)
from heapq import *
class MedianFinder(object):

    def __init__(self):
        self.maxheap = [] #left
        self.minheap = [] #right

    def addNum(self, num):
        #we will add new number to maxheap (smaller array) regardless, and we will always push to the right array unless it already has a greater length
        #check if we have same length or not
        if len(self.maxheap) == len(self.minheap):
            heappush(self.minheap, -heappushpop(self.maxheap, -num)) #this will take max value from left arr and push into right arr so we can achieve always having more on right or equal
        else: #when we have more at right array so we need to push to left array 
            heappush(self.maxheap, -heappushpop(self.minheap, num)) 
        

    def findMedian(self):
        if len(self.maxheap) == len(self.minheap): 
            return float(-self.maxheap[0] + self.minheap[0]) / 2.0 
        else: #we always have the extra number on right array (set by how we constructed our addNum), so if its odd, its gonna be at minheap
            return self.minheap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


#neetcode solution: 54% speed 83 % memory
class MedianFinder(object):

    def __init__(self):
        self.maxheap = [] #left
        self.minheap = [] #right    

    def addNum(self, num):
        heapq.heappush(self.maxheap, -num)
        
        #making sure length is similar
        if len(self.maxheap) - len(self.minheap) > 1: #left has more value
            left = -heapq.heappop(self.maxheap) #largest from left
            heapq.heappush(self.minheap, left)
        elif len(self.minheap) - len(self.maxheap) > 1: #right has more value
            right = heapq.heappop(self.minheap) #smallest from right
            heapq.heappush(self.maxheap, right)
        
        #check if smallest element in right >= largest element in left
        #maxheap[0] = largest element in left, minheap[0] = smallest element in right
        while self.maxheap and self.minheap and -self.maxheap[0] > self.minheap[0]: #not inclusive because they can be equal
            left = -heapq.heappop(self.maxheap)
            right = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -right)
            heapq.heappush(self.minheap, left)

        

    def findMedian(self):

        maxlen = len(self.maxheap)
        minlen = len(self.minheap)
        #mistake: don't pop, just take the vlaue
        if ( maxlen + minlen ) % 2 == 0: 
            return float(-self.maxheap[0] + self.minheap[0]) / 2
        else:
            return -self.maxheap[0] if maxlen > minlen else self.minheap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()