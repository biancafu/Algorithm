#72% speed, 57% memory

class Solution(object):
    def maxPathSum(self, root):
        # think about it with two cases: 1) we are splitting, taking left->root->right #2) we are only taking one path (either right or left)
        # we want to update the max everytime with case 1, and we want to return the max path without splitting, this could be left, right, or just the node itself
        self.maxpath = root.val

        def dfs(root):

            if root:
                left = max(dfs(root.left), 0)
                right = max(dfs(root.right), 0)
                self.maxpath = max(self.maxpath, root.val + left + right)
                return root.val + max(left, right)
        
        dfs(root)
        return self.maxpath