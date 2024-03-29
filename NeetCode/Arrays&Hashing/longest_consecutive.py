#https://leetcode.com/problems/longest-consecutive-sequence/description/
#find the longest consecutive in the list of number given
class Solution(object):
    #go through the numbers, if we the number is the furthest to the left, see how long it can go consecutively
    def longestConsecutive(self, nums):
        numbers = set(nums)
        max_length = 0
        for n in numbers:
            if n - 1 not in numbers:
                length = 0
                while n + length in numbers:
                    length += 1
                    max_length = max(max_length, length)
        
        return max_length