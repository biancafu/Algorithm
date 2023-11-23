#beat 9.12 % only :c

class Solution:
    def valid_tree(self, n, edges):
        '''
        to be a tree, there can be no loops AND every node has to be conneced
        do union find:
            - make sure only one parent exist in the end (only 1 negative element from parent array)
            - no loops occur (no union with same parent)
        '''
        negative = n
        parent = [-1] * n
        def find(node):
            if parent[node] < 0:
                return [node, abs(parent[node])] #return node and its weight
            return find(parent[node]) #continue to find until we find the parent
        
        def union(node1, node2):
            p1, w1 = find(node1)
            p2, w2 = find(node2)

            if p1 == p2: #found loop
                return False
            
            if w1 >= w2:
                parent[p2] = p1
                parent[p1] -= w2
            else:
                parent[p1] = p2
                parent[p2] -= w1

            return True #if union successfully

        for node1, node2 in edges:
            if not union(node1, node2):
                return False
            negative -= 1
            
    
        return True if negative == 1 else False






s = Solution()
a = s.valid_tree(5, [[0,1],[0,2],[0,3],[1,4]])
print(a)