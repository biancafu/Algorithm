#wasn't able to get it. 
#its a bit tricky but once you understand diameter = left height + right height -2 (this is because when we count height, we count the number of nodes)
#but for diameter, we are counting edges. and therefore when we do left height + right height, we have to subtract the extra 1 node count on each side
#however in the code, we can see that because when we are at the current node, we calculate diameter BEFORE returning the new height accounted with current node
#therefore we do not need to account for the -2 mentioned above
#this is also because we chose to return 0 when node is None, if we decided to return -1, then we would actually hv to + 2 to account for them
#becuz again, the position where we are calculating for the diameter didn't account the node yet, so if we are subtracting for null nodes, we have to add them back

#this solution can beat 100%
class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.res = 0

        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.res = max(self.res, left + right) #update diameter here before returning height on next line (this will uncount the current node so its only the leftheight and right height which would be correct for diameter)
            return 1 + max(left, right) #max depth (height)
        
        def dfs_2(root): #-1 version
            if not root:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            self.res = max(self.res, left + right + 2) #update diameter here before returning height on next line (this will uncount the current node so its only the leftheight and right height which would be correct for diameter)
            return 1 + max(left, right) #max depth (height)
        
        dfs(root)
        return self.res

