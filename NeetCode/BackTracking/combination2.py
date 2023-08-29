class Solution:
    #97% speed 96% memory
    #even better with neetcode solution (with optimization)
    #we are splitting our recursion into having duplicate candidate values and not having
    #if the array is [1,1,2], one of the recursion will hv all the 1s and other has none
    #the one with 1s will cover all variations with 1s
    #to do this, we use a prev to indicate if value is repeated, we updated prev once we call recursion already (the call with all 1s)
    #so when we increment to the next for loop, where we see another 1, our candidates[i] == prev condition will run and skip this loop
    

    def combinationSum2_neet(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        curr = []
        candidates.sort()
        def backtrack(pos, target):
            if target == 0:
                output.append(curr[:])
                return
            if target < 0:
                return

            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev: 
                    continue
                #optimize
                if candidates[i] > target:
                    break

                #check combination with next num
                curr.append(candidates[i])
                backtrack(i+1, target - candidates[i])
                curr.pop()
                prev = candidates[i]

        backtrack(0, target)
        return output
    #better solution than mine 98% 17%
    def combinationSum2_better(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        curr = []
        candidates.sort()
        def backtrack(pos, target):
            if target == 0:
                output.append(curr[:])
                return
            if target < 0:
                return 

            for i in range(pos, len(candidates)):
                if i > pos and candidates[i] == candidates[i-1]: #i > pos so can't skip the case where we are checking duplicate candidate values as well 
                #then when we call backtrack(i+1) after, it will skip this duplicated candidate value
                    continue
                if candidates[i] > target: #if the current > target, since array is sorted, all the ones after would be sorted as well, so we can stop here
                    break
                #check combination with next num
                curr.append(candidates[i])
                backtrack(i+1, target - candidates[i])
                curr.pop()

        backtrack(0, target)
        return output
        
    #my solution is very slow 25% 16% not sure why
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #instead of having to add possibily more than 1 time, we can only add once
        
        #start from beginning of list and increment i toget diff candidates
        #sort the candidates
        output = []
        candidates.sort()


        def dfs(i, summ, curr):
            if summ == target:
                output.append(curr[:])
                return 
            
            if summ > target or i >= len(candidates):
                return
            
            curr.append(candidates[i])

            #we are splitting into containing duplicates and not, because when we include the value with duplicate, we will get all combinations with the duplicates, and the other one should always not include the duplicate value AT ALL (all decisions without the duplicated number)
            #decision to add curr (not i becuz can't repeat itself)
            dfs(i+1, summ+candidates[i], curr)
            #skip duplicates
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]: #stops when i == last duplicate
                i+=1 

            #decision to not add curr (skip all duplicates)
            curr.pop() 
            dfs(i+1, summ, curr)
        
        dfs(0, 0, [])
        return output