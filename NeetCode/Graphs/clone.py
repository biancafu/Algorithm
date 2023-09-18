"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    # 77% speed 69 % memory
    #time complexity = O(n) where n = e+v  v = number of verticies(nodes) and e = number of edges
    def cloneGraph(self, node):
        #hashmap
        clones = {}
        """
        clones = {
            val1, neighbors = [clone2, clone4]
            val2, neighbors = [clone1, clone3]
            val3, neighbors = [clone2, clone4]
            val4, neighbors = [clone1, clone3]
        }
        """

        def dfs(curr):
            if curr in clones:
                return clones[curr] #return clone node

            clone = Node(curr.val)
            clones[curr] = clone

            for neighbor in curr.neighbors:
                output = dfs(neighbor)
                #if output: #output will always have something since we need to return itself after we created a clone for it to be appeneded to the neighbor from the node before
                clone.neighbors.append(output)
            
            return clone

        
        return dfs(node) if node else None