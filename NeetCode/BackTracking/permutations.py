#my original solution/logic (had to look at neetcode's explanation to get inspiration)
#but my solution is differennt than his and very slow and bad memory
#speed 6% memory 10%

#neetcode's solution is best: 92% speed 98% memory
#but logically, its a bit more confusing becuz we are appending to the end of permutations so result output is in a diff order than expected
#to understand better, we can change perm.append(curr) to perm.insert(0,curr), i think this makes more sense
#however this causes the solution to decrease in speed for ~30%

class Solution:
    def permute_neetcode(self, nums: List[int]) -> List[List[int]]:

        output = []
        # initially i set that so that we pass in nums and curr, where curr is the recorded array
        # but we don't need this since we will always have same length (we are basically rotating all posibilities of permutation, so we just need to copy nums since we are switching the number positions)
            #base case
        #if len(nums) == 0: # not 0 but 1, becuz when we hv 1, then we only hv 1 permutation
        if len(nums) == 1:
            return [nums[:]] #faster than copy

        for i in range(len(nums)):
            curr = nums.pop(0)
            perms = self.permute_neetcode(nums)#this returns all permutation excluding the first element of nums (curr)
            
            # append curr_num to end of array to all permutations to get all permutations from this level
            for perm in perms:
                perm.append(curr)
            #need to add it back to the end of previous array to rotate nums array, this way we can rotate every element to be the first element to get all permutations
            nums.append(curr)
            output.extend(perms)

        return output

    #my solution's logic but faster 99% still memory 10%. memory is same as mine cuz we are saving path
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, path): 
            if not nums: 
                result.append(path) 
                return 
            for i in range(len(nums)): 
                #nums[:0] = [], don't need to worry about nums[i+1] out of range becuz we are not decreasing size, and its given that len(nums) >= 1
                backtrack(nums[:i] + nums[i+1:], path + [nums[i]]) #rotating nums (forgot we can do [:i] to not include 0)
                #arr1 + arr2 = [arr1 ..., arr2 ...]
        result = [] 
        backtrack(nums, []) 
        return result 

    def permute_mysolution(self, nums: List[int]) -> List[List[int]]:
        output = []


        #[1,2,3], []
        def dfs(nums, curr):
            #base case
            if len(nums) == 0:
                output.append(curr.copy())
                return

            for i in range(len(nums)):
                curr_num = nums[0]
                curr.append(nums.pop(0))
                dfs(nums, curr)
                #clean up
                curr.pop()
                #append curr_num to end of array to get all permutations
                nums.append(curr_num)
        
        dfs(nums, [])
        return output
