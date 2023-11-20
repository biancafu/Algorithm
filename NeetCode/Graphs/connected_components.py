class Solution:
    def count_components(self, n, edges):
        """
        undirected graph: n nodes, edges array
        edges[i] = [node a, nodeb]
        return number of connected components

        use union find, with a parent array
        count how many parents there are in the end (or use a set and remove)
        """

        parent = [-1] * n
        
        #find parent
        def find(node):
            if parent[node] < 0:
                return [node, abs(parent[node])] #return itself, and its weight
            
            return find(parent[node]) #recursively find the parent

        #union
        def union(node1, node2):
            p1, w1 = find(node1)
            p2, w2 = find(node2)

            if w1 >= w2:
                parent[p2] = p1
                parent[p1] -= w2
            else:
                parent[p1] = p2
                parent[p2] -= w1
            
        for node1, node2 in edges:
            union(node1, node2)
        
        counter = 0
        print(parent)
        for p in parent:
            if p < 0:
                counter += 1
        
        return counter

            

            

s = Solution()
a = s.count_components(1000, [[0, 99], [1, 100], [2, 101], [3, 102], [4, 103], [5, 104], [6, 0], [7, 0], [8, 7], [9, 8]])
print(a)