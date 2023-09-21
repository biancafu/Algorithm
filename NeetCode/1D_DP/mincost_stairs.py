class Solution(object):
    #dp: doesn't have to be with recursion!
    #60-92% speed 65-98%memory

    #start from front
    def minCostClimbingStairs(self, cost):

        #we can either do from start or from back to accumulate
        cost.append(0)

        for i in range(2,len(cost)):
            cost[i] += min(cost[i-1],cost[i-2])
        
        return min(cost[-1], cost[-2])

    #start from back
    def minCostClimbingStairs(self, cost):
        '''
        using the logic of fibonacci sequence: we start from the back since the front one depends on the back one 
        because n - 1 = 1
                n - 2 = 2
                n - 3 = 3
                n - 4 = 5
        so we start from n - 1 accumulate to n - n = 0
        cost = [10, 15, 20, 0]
        '''

        cost.append(0)
        
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1],cost[i + 2])
        
        return min(cost[0], cost[1])



    #backtracking (without dynamic)
    def minCostClimbingStairs(self, cost):
        """
        -reach top of stairs
        -min cost

        can start from index 0 or 1


            0           1
        1       2      1    2
        
        """

        cost.append(0) #this will be the top
        def dfs(i):
            
            if i >= len(cost) - 1:
                return 0
            
            return cost[i] + min(dfs(i + 1), dfs(i + 2))

        return min(dfs(0), dfs(1))
