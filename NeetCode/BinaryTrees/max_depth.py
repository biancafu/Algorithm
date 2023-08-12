# 6 min, speed 61% memory 75% not that good
# DFS solution (same as neetcode)
class Solution(object):
    def maxDepthDFS(self, root):
        if root == None:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    def maxDepthBFS(self, root):
        pass
    def maxDepth_iterative(self, root):
        pass