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
        stack = [[root, 1]]
        res = 0
        while len(stack) != 0:
            node, length = stack.pop()
            if node:
                res = max(length, res)
                if root.left: stack.append([node.left, length + 1])
                if root.right: stack.append([node.right, length + 1])
        return res