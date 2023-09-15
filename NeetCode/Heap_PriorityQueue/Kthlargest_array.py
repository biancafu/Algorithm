import random
#leetcode solution, same as neetcode using quick select, but was able to run successfully
#difference between leetcode and neetcode's solution is that leetcode partitions it into 3 diff arrays and uses length of the parts to determine where kth element would be
#then continue calling with the corresponding arrays
#where as neetcode divides it into 2 parts, using a pointer (p) to determine if we will swap elements in the array to different position (by comparing to pivot)
#then comepare p to k and see if we are going to continue search which part of the array
class Solution(object):
    def findKthLargest(self, nums, k):
        #quick select

        def quickselect(nums, k):
            left, mid, right = [], [], []
            partition = random.choice(nums)
            
            #split into 3 sections: left = smaller numbers, mid = same numbers, right = bigger numbers
            for num in nums:
                if partition == num:
                    mid.append(num)
                elif partition > num:
                    left.append(num)
                else:
                    right.append(num)
            #we need to know where is k, is it in right side? is it in the middle? or is it in left side?
            #first case, k is in right, we continue quick select the right section
            #we continue this until we sort everything on the right
            if len(right) >= k:
                return quickselect(right, k)
            
            #k is in left, we subtract k by what we already went through and continue searching
            elif len(right) + len(mid) < k: 
                return quickselect(left, k - len(right) - len(mid))
            
            #third case, k is in mid. we will get here when we sort to the last element and k = 1 and the last element will be in mid, then it wont satisfy either of the recursive call condition resulting us to return 
            return partition
        
        return quickselect(nums, k)
    



    
#neetcode
    #using Quick Select , O(n) (similar to quick sort but quick sort is O(nlogn) since after division, it has to quicksort each division as well)
    #but quick select here, we are eliminating one side and picking the side we need to do another quick select
    #would run into time limit exceeded even tho it is in O(n)

class Solution_neetcode(object):
    def partition(self, nums, left, right):
        pivot, fill = nums[right], left

        for i in range(left, right):
            if nums[i] <= pivot:
                nums[fill], nums[i] = nums[i], nums[fill]
                fill += 1

        nums[fill], nums[right] = nums[right], nums[fill]

        return fill
    def findKthLargest(self, nums, k):
        k = len(nums) - k
        left, right = 0, len(nums) - 1

        while left < right:
            pivot = self.partition(nums, left, right)

            if pivot < k:
                left = pivot + 1
            elif pivot > k:
                right = pivot - 1
            else:
                break

        return nums[k]

        
class Solution2(object):
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


s = Solution()
a = s.findKthLargest([3,2,3,1,2,4,5,5,6], 4)
print(a)