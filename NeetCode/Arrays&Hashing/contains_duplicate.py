#https://leetcode.com/problems/contains-duplicate/description/

class Solution(object): #O(n)
    def containsDuplicate(self, nums):
        occurance = set()
        for num in nums:
            if num in occurance:
                return True
            else:
                occurance.add(num)
        
        return False
    
#set will eliminate duplicates
#simplier solution but slower in run time
#this is because we are inputting all numbers into set, instead of adding until a repeated number shows up (faster)
    def containsDuplicateslower(nums):
        return len(set(nums)) != len(nums)

#this would work because if there are duplicate, then that means the length would not be equal
