class Solution(object):
    def rob(self, nums):
        """
        backtracking: we rob curr house or we don't rob curr house
        dfs to go through these options
        memotization for dp solution

        backtrack:
        def dfs(amount, i):
            if i >= len(nums):
                return
            
            return max(dfs(amount + nums[i], i+2), #rob curr house
            dfs(amount, i+1)) #don't rob curr house
        """

        #iterative + memo (bottom up)
        if len(nums) == 1:
            return nums[0]
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])#do we start from zero index or index 1, find which one is max
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], #added num from n-2
            dp[i-1]) #added num from n-1, can't add curr
        
        return dp[-1]





s = Solution()
a = s.rob([2,1,1,2])
        