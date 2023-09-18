class Solution(object):

    def climbStairs(self, n):
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
        
        for i in range(4, n+1): #-1 because we started from 1, 1 not just 1
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

        
        


        

        
        

        
        