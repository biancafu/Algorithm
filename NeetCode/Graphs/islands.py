class Solution(object):
    #dfs 95% speed 86% memory
    def numIslands(self, grid):
        m = len(grid)
        n = len(grid[0])
        islands = 0

        def dfs(r,c):
            if r < 0 or c < 0 or r >= m or c >= n or grid[r][c] != "1":
                return
            
            grid[r][c] = "2"
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    dfs(r,c)
                    islands += 1

        return islands

    #bfs solution: 20% speed 86% memory O(m*n) becuz we are skipping the ones we checked already essentially it will be around O(m*n)
    #instead of using a set to keep track of visited coords, just change the grid value to something else to keep track

    def numIslands(self, grid):
        
        m = len(grid)
        n = len(grid[0])
        islands = 0

        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            grid[r][c] = "2"

            while q:
                row, column = q.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]

                for dr, dc in directions:
                    r, c = row + dr, column + dc
                    if r in range(m) and c in range(n) and grid[r][c] == "1":
                        q.append((r,c))
                        grid[r][c] = "2"
        
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    bfs(r,c)
                    islands += 1
        

        return islands