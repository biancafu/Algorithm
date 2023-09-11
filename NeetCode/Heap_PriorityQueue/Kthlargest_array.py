class Solution(object):
    #leetcode solution, same as neetcode using quick select, but was able to run successfully
    #neetcode (better solution)
    #using Quick Select , O(n) (similar to quick sort but quick sort is O(nlogn) since after division, it has to quicksort each division as well)
    #but quick select here, we are eliminating one side and picking the side we need to do another quick select
    #would run into time limit exceeded even tho it is in O(n)



    #my solution, 3 min
    #25% speed 25% memory
    #O(n + klogn) better than sorting O(nlogn)
    def findKthLargest(self, nums, k):
        new_nums = [ -n for n in nums ]
        heapq.heapify(new_nums)

        for i in range(k):
            output = heapq.heappop(new_nums)
        
        return -output



#mistake of trying to decrease the size of nums, with the same k, we will not be able to find the right value in some cases, we can fix it by decreasing the k when we decrease size of nums
#give l and r pointers to indicate where we are searching in the array (instead of decreasing the actual size - my mistake)

