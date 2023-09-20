class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        similar to finding how many islands there are
        when we traverse through the lands, we keep track of how many of them there are
        mark areas we traversed already
        """
        m = len(grid)
        n = len(grid[0])
        max_area = 0

        def dfs(r,c): 
            if r < 0 or c < 0 or r >= m or c >= n or grid[r][c] == 0:
                return 0 #water
            grid[r][c] = 0 #mark the checked lands #made a mistake here, put 2 equal sign lol
            
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    max_area = max(dfs(r,c), max_area) #return area 
        
        return max_area
                    


        