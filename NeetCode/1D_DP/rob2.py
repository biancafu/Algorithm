class Solution(object):
    #correct idea, i wanted to find a more efficient way to store the middles and just see which is max addinf nums[0] or nums[1] 
    # but it wouldn't work becuz it will change the whole comparison in the middle part
    #so using this logic, we will use the previous way to solve but with diff nums array
    #we are also comparing to nums[0] in case we only have 1 value
    def rob(self, nums):
        """
        split into 2
        dfs(i, len(nums)-2) excluding last element
        dfs(i+1, len(nums)-1) starting from second element
        return max
        """

        def helper(nums):
            rob1, rob2 = 0, 0
            for n in nums:
                temp = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = temp
            
            return rob2
        
        return max(nums[0],helper(nums[:-1]), helper(nums[1:]))
    #if we only hv one value, our helpers function are passed in with empty arrays which would return 0, so we need to compare first element of nums for this edge case
    


        