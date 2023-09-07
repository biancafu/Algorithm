# using min heap is the fastest way since it keeps the array sorted and add/pop is O(logn) which is better than normal array operations O(n)
# fastest: 97% speed 86% memory

class KthLargest(object):

    def __init__(self, k, nums):

        self.k, self.nums = k, nums
        heapq.heapify(self.nums) #min heap O(n)
        #keep heap in size k (using min heap to pop the min values out until we hv the k largest values left)
        while len(self.nums) > k:
            heapq.heappop(self.nums) #pops min value


    def add(self, val):
        if len(self.nums) == self.k:
            if val > self.nums[0]: #self.nums[0] has the smallest value since this is a min heap
                heapq.heappushpop(self.nums, val) #more effificent than pushing and popping separately
        else: #has less than k numbers in heap
            heapq.heappush(self.nums, val)
        
        #neetcode (similar speed)
        # heapq.heappush(self.minHeap, val)
        # if len(self.minHeap) > self.k:
        #     heapq.heappop(self.minHeap)
        # return self.minHeap[0]

        
        # return self.nums[0]


        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

#this is slow because inserting in an array takes O(N)
class KthLargest_binarySearch(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.nums = sorted(nums)

        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        l, r = 0, len(self.nums)-1
        while l <= r:
            mid = (l+r) // 2 
            if self.nums[mid] == val:
                l = mid
                break
            elif self.nums[mid] > val:
                r = mid - 1
            else:
                l = mid + 1
        
        self.nums.insert(l, val) #O(N)
        return self.nums[-self.k]



s = KthLargest(3,[4,5,8,2])
print(s.add(3))
print(s.add(5))
print(s.add(10))
print(s.add(9))
print(s.add(4))