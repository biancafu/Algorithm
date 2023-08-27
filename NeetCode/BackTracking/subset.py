#using python3 because python does not have copy function
#speed 75-98% (10ms difference) memory 10-76% (with 1 mb difference)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #basically a tree with 2 nodes: 1) take current number 2) don't take current number
        #with this tree expanding more and more, this becomes our back tracking solution
        #backtracking usually means we are brute forcing and we want ALL solutions
        output = []
        current = []
        def dfs(i):
            #breaking condition
            if i >= len(nums):
                output.append(current.copy()) #because lists are mutable, it will change if we dont use a new copy
                return

            #append with current
            current.append(nums[i])
            dfs(i+1) #recursively incrementing

            #dont append with current
            current.pop() #we pop the current off for the decision of not appending
            dfs(i+1) #then increment for that decision
        
        dfs(0)
        return output