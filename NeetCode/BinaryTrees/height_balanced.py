#got it right around 10 min but didn't call the function so it wasn't working
# 94% speed 54% memory

#leetcode has similar but instead of doing self.ans, he did a array to store it when we do the recursive call
#so return [balanced (boolean), height], so every recursive call he checks if balanced is true from left and right side
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        self.ans = True
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            if abs(left - right) > 1: self.ans = False
            return 1 + max(left, right)
        
        dfs(root)
        return self.ans



