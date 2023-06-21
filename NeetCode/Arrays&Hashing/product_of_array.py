#https://leetcode.com/problems/product-of-array-except-self/description/
#calculate the product of the array
#we are separating the index to left and right of the current index and multiplying them together to get the product
#left [1,1,2,6]
#right [24, 12, 4, 1]

class Solution(object):
    #O(n) optimized solution using O(1) memory since result does not count towards
   
    def productExceptSelf_best(self, nums):
        result = [1 for i in range(len(nums))]
        prefix = 1
        for i in range(len(nums)):
            result[i] *= prefix
            prefix *= nums[i]

        # or
        # for i in range(1,len(nums)):
        #     result[i] = result[i-1] * nums[i-1]
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        
        return result

    def productExceptSelf_better(self, nums):
        result = [1]
        #prefix
        product = 1
        for i in range(len(nums) - 1):
            product *= nums[i]
            result.append(product)

        #postfix
        product = 1
        j = 0
        for i in range(len(nums) - 2, -1, -1):
            product *= nums[i + 1]
            result[i] *= product
        return result
     
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        #left side
        left = [1]
        right = [1]
        #prefix
        product = 1
        for i in range(len(nums) - 1):
            product *= nums[i]
            left.append(product)
        #postfix
        product = 1
        for i in range(len(nums) - 1, 0, -1):
            product *= nums[i]
            right.insert(0, product)
        result = []
        for i in range(len(nums)):
            result.append(left[i] * right[i])
        
        return result
