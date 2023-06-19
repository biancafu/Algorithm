#will only be able to use binary way if it is sorted, can't use this here since we need the original index (can't sort list)
#first time failed (saw solution), second time 7 min 

class Solution(object):
    def twoSum(self, nums, target):
        occurence = dict()
        for i, num in enumerate(nums):
            if target - num in occurence:
                return [i, occurence[target - num]]
            else:
                occurence[num] = i