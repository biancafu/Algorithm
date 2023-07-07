#4 min with careless mistake (mixed up the high low increment)
#https://leetcode.com/problems/binary-search/description/

class Solution(object):
    def search(self, nums, target):
        #cut in half
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1

            else: #nums[mid] < target
                low = mid + 1
    
        return -1