class Solution(object):

    #Neetcode 99% speed 80% memory
    def climbStairs(self, n):
        #when it comes to decision tree (recursion/backtracking?) we can usually find a way to make it more effificent. we will be using memoization/cache for this question (store the repeated process in a cache)
        #when we draw the decision tree, we can see that whenever we will have repeated where n = 2, n = 3 ... and we already know the answers if we run them once (since we will only be able to add 1 or add 2 every time)
       
        #using the understanding of a decision tree, we see that a lot of the steps/decisions are repeated. how do we optimize a case like this? here we are going to use memoization where we keep track of the repeated parts
        #so we see that n = (n-1) + (n-2) when we start from the back of the cases
        #0 case 5: 1
        #1 case 4: 1
        #2 case 3 = case4+case5 = 1+1 = 2
        #3 case 2 = case3+case4 = 2+1 = 3
        #4 case 1 = case2+case3 = 3+2 = 5
        #5 case 0 = case1+case2 = 5+3 = 8
        #1 1 2 3 5 8
        if n <= 3:
            return n
        one = 3
        two = 2
        
        for i in range(4, n+1): #this is because when n = 5, we will have 012345 (total of 6) operations, since range does not include n, we have to do n + 1
            temp = one + two
            two = one
            one = temp

        return one
    
    #original solution: time limited exceeded
    #this is the right track, but how to simplify more from here?
    #if we draw the decision tree, we can see that we are repeating some of the steps, where if we can store the result of it (memoization)
    #it will speed up the whole process to O(n) instead of O(2^n)
    def climbStairs(self, n):
        #take 1 or 2 steps
        self.output = 0
        def dfs(total):
            if total >= n:
                if total == n:
                    self.output += 1
                return

            
            dfs(total + 1)
            dfs(total + 2)
    

        dfs(0)
        return self.output

#solution on leetcode discusiion
#also memoization but another approach
#91% speed 48% memory
class Solution2(object):
    def climbStairs(self, n):
        memo = {}
        return self.helper(n, memo)
    
    def helper(self, n, memo):
        if n == 0 or n == 1:
            return 1
        if n not in memo:
            memo[n] = self.helper(n-1, memo) + self.helper(n-2, memo)
        return memo[n]
    

        
        


        

        
        

        
        