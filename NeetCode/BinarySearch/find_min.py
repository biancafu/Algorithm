#wasn't able to solve it, already done it before as well, didn't understand concept fully
#https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

class Solution(object):
    def findMin(self, nums):
        low = 0
        high = len(nums) - 1
        while low < high: #exclusive becuase when low == high, our increment will be high = mid which means it will become infinite loop since we are not incrementing
            mid = (low + high) // 2
            if nums[mid] > nums[high]: #the right half contains the lower number (restarted somewhere)
                low = mid + 1
            else: #if mid <= high means we are ascending, so go left half for smaller values, but we have to include mid because it could be the lowest number, therefore high = mid
                high = mid 
        return nums[low]