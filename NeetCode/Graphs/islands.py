class Solution(object):
    #bfs solution: 20% speed 86% memory
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