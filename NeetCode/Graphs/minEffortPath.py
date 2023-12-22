class Solution:
    #I'm looking for max(height[x1][y1] - height[x2][y2]) from the min path i selected
    #I'll store min(height[x1][y1] - height[x2][y2]) for the current block and its neighbors
    #from all the paths i took, i want to keep track of the max of the distance
    
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        heap = [[0,0,0]]
        visited = set()
        cost = 0
        while heap:
            wei, i, j = heapq.heappop(heap)
            cost = max(cost, wei)
            if (i,j) in visited:
                continue
    
            if i == len(heights)-1 and j == len(heights[0])-1:
                return cost
            visited.add((i,j))
            for x,y in ((i+1,j), (i-1,j), (i, j+1), (i, j-1)):
                if 0 <= x < len(heights) and 0 <= y < len(heights[0]) and (x,y) not in visited:
                    d = abs(heights[i][j] - heights[x][y])
                    heapq.heappush(heap, (d, x, y))

        return cost