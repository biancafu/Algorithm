class Solution(object):
    # 91.5% speed 88.5% memory
    def pacificAtlantic(self, heights):
        """
        instead of doing backtracking and checking all the grid, start from where the ocean is and extends to whereever it can touch on the grid
        for both pacific ocean and atlantic ocean create a set that marks down where the ocean extends until
        *mistake previously: did a dfs checking for both pacific and atlantic 
        """
        def dfs(r, c, visited, prev):
            if (r,c) in visited or r < 0 or r >= m or c < 0 or c >= n or heights[r][c] < prev: 
                #if prev > curr it will not flow to curr this is becuz we are reverse checking
                #we are starting from ocean so ocean should be smallest, whatever is greater will folow to ocean, whatever is smaller will not flow
                return 
            
            #if it is within range and not visited, and height is less than prev
            visited.add((r,c))
            dfs(r+1,c,visited,heights[r][c])
            dfs(r-1,c,visited,heights[r][c])
            dfs(r,c+1,visited,heights[r][c])
            dfs(r,c-1,visited,heights[r][c])
            
        
        m = len(heights) #not square, need n
        n = len(heights[0])
        pacific = set()
        atlantic = set()
        output = []


        for i in range(m):
            dfs(i, 0, pacific, heights[i][0])
            dfs(i, n-1, atlantic, heights[i][n-1])

        
        for i in range(n):
            dfs(0, i, pacific, heights[0][i])
            dfs(m-1, i, atlantic, heights[m-1][i])
        
        for i in range(m):
            for j in range(n):
                if (i,j) in pacific and (i,j) in atlantic:
                    output.append([i,j])
        return output 
            

        