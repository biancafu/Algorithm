from collections import deque

'''
my solution logic works, but its showing memory exceed limit
it is becuz of the while loop where we are appending every single neighbor even when its out. (since our logic will eliminate it after)
but it is still adding onto the q at first, which takes up more memory.

an improved solution would be to check the coordinates first and validate it before adding it to the q, 
we can do that by making a addRoom function and put the if statement to check in it, if its a valid coordinate, then we add it to the queue and seen

another improvement we can make is, we don't need to pass in step parameter to keep track of the distance
we can simply have a distance variable where it increases every end of for loop, this will ensure that all the same level coordinates will get the correct distance

'''

#improved solution
from collections import deque
class Solution:

    def walls_and_gates(self, rooms):
        # write your code here
        q = deque()
        seen = set()
        ROWS = len(rooms)
        COLS = len(rooms[0])
        dist = 0

        #check if room is in range, if so, then add
        def addRooms(r,c):
            if r < 0 or r >= len(rooms) or c < 0 or c >= len(rooms[0]) or rooms[r][c] == -1 or (r,c) in seen:
                return
            seen.add((r,c))
            q.append((r,c))
            
            

        #get all gates in the rooms
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append((r,c))  
                    seen.add((r,c))
                    

        #bfs
        while q:
            length = len(q)
            for gate in range(length):
                r, c = q.popleft()
                rooms[r][c] = dist
                addRooms(r+1, c)
                addRooms(r-1, c)
                addRooms(r, c+1)
                addRooms(r, c-1)
            dist += 1

        return rooms

#first solution
class Solution:
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