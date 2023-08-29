class Solution:
    #neetcode solution is better on average
    #didn't understand the question properly
    #we need to remove duplicates, becuz if we do the same as subset1, we will get repeated values like [1,2] [1,2] since we hv 2 2s.
    #very important point, we NEED TO SORT the array so its easier for us to check and remove duplicates
    #when we see duplicates, we skip that one, since we will take care of the repeated values from just 1 of them
    
    #my solution works ranging from speed 54-95% memory 56-84%
    #15 min, i only solved it using tricks, I don't understand how to solve it logically
    #basically did subset.py and then I sorted solutions and use set to eliminate duplicates

    # speed 66-99% memory 56%
    def subsetsWithDup_neetcode(self, nums):
        
        output = []
        nums.sort() #or nums = sorted(nums)
        def dfs(i, curr):
            if i >= len(nums):
                output.append((curr[:]))
                return

            #adding current num (just like subset1)
            curr.append(nums[i])
            dfs(i+1, curr)            

            #check for duplicates
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1 #increment until no repeated values
            # i = last repeated value after loop
            
            #not adding current num
            curr.pop()
            dfs(i+1, curr) #i+1 to get next value (not repeated one)
        

        dfs(0, [])
        return output
    
    def subsetsWithDup(self, nums):
        output = set()
        curr = []
        def dfs(i):
            if i >= len(nums):
                output.add(tuple(sorted(curr[:])))
                return

            curr.append(nums[i])
            #adding current num
            dfs(i+1)

            curr.pop()
            #not adding current num
            dfs(i+1)
        

        dfs(0)
        return list(output)