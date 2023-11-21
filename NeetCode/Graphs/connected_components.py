#beat 98% submission


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

            if p1 == p2: #need to consider this or else we will be merging the node with itself and mess up the weight
                return
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
a = s.count_components(80,
[[1, 67], [2, 14], [3, 20], [4, 49], [5, 44], [6, 38], [7, 78], [8, 2], [9, 64], [10, 25], [11, 65], [12, 1], [13, 27], [14, 41], [15, 11], [16, 35], [17, 22], [18, 27], [19, 76], [20, 71], [21, 44], [22, 62], [23, 73], [24, 52], [25, 62], [26, 61], [27, 76], [28, 38], [29, 55], [30, 7], [31, 46], [32, 51], [33, 18], [34, 29], [35, 72], [36, 67], [37, 59], [38, 75], [39, 54], [40, 63], [41, 51], [42, 42], [43, 13], [44, 73], [45, 24], [46, 21], [47, 31], [48, 13], [49, 68], [50, 27], [51, 44], [52, 22], [53, 37], [54, 37], [55, 59], [56, 3], [57, 61], [58, 9], [59, 58], [60, 76], [61, 75], [62, 30], [63, 2], [64, 48], [65, 26], [67, 62], [68, 64], [69, 8], [70, 6], [71, 45], [72, 50], [73, 9], [74, 50], [75, 70], [76, 46], [77, 61], [78, 73], [79, 28]])
print(a)