class Solution(object):
    def findRedundantConnection(self, edges):
        """
        kinda got a similar idea to union find when i thought the 2 nodes cannot be visited but slightly diff because idk how to structure all the nodes

        union the nodes base on their weights, and form a tree structure whenever we union the 2 nodes 
        """

        #union find
        #parent array to keep track of weight (the value) and if this is the parent itself, it will be negative (otherwise it will be positive and the index of the parent will be the value)
        parent = [-1] * (len(edges) + 1) #len og edges == num of nodes, but we want to start from 1
        def find(a):
            if parent[a] < 0: #negative == parent itself
                return [a, abs(parent[a])] #[curr node(itself), weight]
            #else it is a children of some parent at parent[a], continue finding parent
            return find(parent[a]) #forgot to put return so it returned none at first


        def union(a, b):
            parenta, weighta = find(a)
            parentb, weightb = find(b)

            if parenta == parentb: #find cycle
                return False #to indicate cycle

            if weighta > weightb:
                parent[parentb] = a #mistake: has to use parentb to get the toppest parent so we update the whole tree (multiple nodes)
                parent[parenta] -= weightb
            else:
                parent[parenta] = b
                parent[parentb] -= weighta
            
            return True #to indicate merge successful
        
        for a,b in edges:
            if not union(a,b):
                return [a,b]


            

s = Solution()
a = s.findRedundantConnection([[1,5],[3,4],[3,5],[4,5],[2,4]])
print(a)