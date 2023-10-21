from collections import deque
class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def walls_and_gates(self, rooms):
        # write your code here
        q = deque()
        seen = set()
        ROWS = len(rooms)
        COLS = len(rooms[0])

        #get all gates in the rooms
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append((r,c,0))  

                       


        #bfs
        while q:
            length = len(q)
            for gate in range(length):
                r, c, steps = q.popleft()
                if r < 0 or r >= len(rooms) or c < 0 or c >= len(rooms[0]) or rooms[r][c] == -1 or (r,c) in seen:
                    continue
                seen.add((r,c))
                rooms[r][c] = steps
                q.append((r+1, c, steps+1)) 
                q.append((r-1, c, steps+1)) 
                q.append((r, c+1, steps+1)) 
                q.append((r, c-1, steps+1)) 

        return rooms
    

s = Solution()
a = s.walls_and_gates([[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]])
print(a)