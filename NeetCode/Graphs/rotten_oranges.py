from collections import deque
#51% speed 85% memory
class Solution(object):
    def orangesRotting(self, grid):
        """
        0 -> empty cel
        1 -> fresh orange
        2 -> rotten orange

        every minute, any fresh orange beside a rotten orange becomes rotten
        return min minutes for all fresh oranges to turn rotten
        if impossible return -1

        set of rotten
        set of fresh
        BFS!! the rotten one and change fresh ones into rotten
        if number of fresh curr == number of fresh prev, and is not empty, then its impossible

        its impossible to use DFS becuz it goes all the way to bottom at once
        instead we should do BFS where it can search each level (rotten oragne) at the same tmie
        """
        m = len(grid)
        n = len(grid[0])
        moves = 0
        fresh = 0

        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i,j))
        
        directions = ((1,0),(0,1),(-1,0),(0,-1))
        while q and fresh > 0:
            length = len(q)
            moves += 1
            for p in range(length):
                i,j = q.popleft()
                for dr,dc in directions:
                    r, c = i+dr, j+dc
                    if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != 1:
                        continue
                    grid[r][c] = 2
                    q.append((r,c))
                    fresh -= 1

        return moves if fresh == 0 else -1





