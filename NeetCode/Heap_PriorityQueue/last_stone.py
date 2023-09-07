# my solution: 69% speed 72% memory O(n) from heapify + O(nlogn) from popping and pushing
# i used max heap by using min heap * -1
# which is actually what neetcode did as well

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        #heapify max heap
        for i in range(len(stones)):
            stones[i] *= -1 #use *-1 to create max heap since greatest will become smallest hence stones[0] will be -max 
        #neetcode
        #stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            y = heapq.heappop(stones) * -1 # *-1 to get original value
            x = heapq.heappop(stones) * -1
            if x != y:
                heapq.heappush(stones, -(y-x)) #logn
        
        return stones[0]*-1 if stones else 0
        #neetcode
        #stones.append(0)
        #return abs(stones[0])
            

        