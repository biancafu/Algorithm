from types import List
from collections import defaultdict, deque

# couldnt do the question at all by myself
# time 71% memory 23%
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        '''
        equations[i] = [A, B], A, B are strings
        values[i] = A -> B (if B-> A: 1/values[i] = values[i]**-1 )
        queries[j] = [C, D] 

        looking for C -> D 
        if we can't find this relation, return -1.0
        return List[float]

        1. create graph (directional)
        2. traverse through the graph (BFS/DFS) -> BFS 
        3. see if relationship exists (return value if it does, else return -1.0)

        a - 2.0 -> b    b - 3.0- > c
          <-1/2.0-       <- 1/3.0 - 

        dict[a] = [[b, value], []]
        dict[b] = [[a, 1/value]] #reverse direction

        bfs better for cycle detection

        '''

        #create graph
        adj = defaultdict(list)
        for i, eq in enumerate(equations):
            src, target = eq
            value = values[i]

            adj[src].append((target, value))
            adj[target].append((src, 1/value)) #reverse direction

        def bfs(src, target):
            if src not in adj or target not in adj:
                return -1.0
            
            q = deque()
            visited = set() #prevent cycle
            q.append((src, 1))
            visited.add(src)

            while q:
                curr, curr_weight = q.popleft()

                if curr == target: #found our target
                    return curr_weight
                
                for nei, nei_weight in adj[curr]:
                    if nei not in visited:
                        q.append((nei, curr_weight * nei_weight))
                        visited.add(nei)

            return -1.0

        return [ bfs(src, target) for src,target in queries ]



        