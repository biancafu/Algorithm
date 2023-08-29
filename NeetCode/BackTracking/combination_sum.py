#had the correct logic but was writing the code wrong, had to check previous question to code it correctly
#solved it in 27 min (with help)
#I think backtracking is using recursion to get all possibilities but we are modifying one array
#therefore all solutions are "connected" which is why we need to use copy to keep the matching solutions (since lists are mutable)
#we also use 1 array to keep track of current solution, so we should append/pop accordingly when we are navigating different paths
#eg: add num (append to array and explore the path by recursion), 
#then comes back to this loop and explore not add num (pop previous appeneded num, then recursion call)

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:   
        #we have 3 cases, we take current and move on, or take current again, or don't take current
        #our bounding condition is that when sum => target, it stops. If sum == target, record it down
        output = []
        def dfs(i, summ, nums):
            if i >= len(candidates) or summ > target:
                return 

            if summ == target:
                output.append((nums.copy()))
                return
            curr = candidates[i]
            nums.append(curr)
            #add current again
            dfs(i, summ + curr, nums)
            nums.pop()

            # dfs(i+1, summ + curr, nums)
            # ^ this will cause the solution to be slow since we are doing an extra loop
            #this will be cover by the above dfs() call since the next call it will have 2 choices: to add current or not
            #adding current means we are adding multiple current and not adding means we only add curr once, hence covering both possibilities

            
            #don't add current
            dfs(i+1, summ, nums)

 

        dfs(0, 0, [])
        return (output)