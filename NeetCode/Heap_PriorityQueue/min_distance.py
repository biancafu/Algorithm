#logic was correct but misunderstood something about heap (should of taken about 15 min but didn't know where went wrong with the code)
#heap's largest/smallest number will be at root heap[0], however, doesn't mean the other elements in the array is sorted
#therefore we can't take a segment of the array and think it will be in sorted order (the mistake i made)
#we can only get min/max from popping it out of the heap using heapq.heappop()

#all solutions had very similar speed
#but i think the first one makes sense where it would take least time
#neetcode's should take most time because it is heapifying the whole array O(N) which is simpler in terms of coding
#but since we are using add/pop on heap, this is O(logn) so i think its faster

class Solution(object):
    #solution using max heap (i think its fastest) 77% speed 45% memory
    def kClosest(self, points, k):
        heap = [] #no need to heapify since we don't hv any values
        for x,y in points:

            d = -(pow(x,2) + pow(y,2)) #since we are calculating distance to (0,0), so we are subtracting 0 (taking x/y as it is); not doing sqrt, since its fine like this        
            if len(heap) == k and d < heap[0]:
                    heapq.heappushpop(heap, [d,x,y])
            else:
                heapq.heappush(heap, [d, x, y]) #will use first value to heap sort by default

        return [[x,y] for dist,x,y in heap]
    
    #my solution
    def kClosest(self, points, k):
        heap = [] #no need to heapify since we don't hv any values
        output = []
        for x,y in points:

            d = (pow(x,2) + pow(y,2)) #since we are calculating distance to (0,0), so we are subtracting 0 (taking x/y as it is); not doing sqrt, since its fine like this        

            heapq.heappush(heap, [d, x, y]) #will use first value to heap sort by default
        output = []
        for i in range(k):
            d,x,y = heapq.heappop(heap)
            output.append([x,y])

        return output
    
    #neetcode solution
    def kClosest(self, points, k):
        minHeap = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minHeap.append([dist, x, y])
        
        heapq.heapify(minHeap)
        res = []
        for _ in range(k):
            _, x, y = heapq.heappop(minHeap)
            res.append((x, y))
        return res
            

        