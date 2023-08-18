#was not able to solve it
#overcomplicated it by thinking left or right subtree
#essentially, we just need to set boundaries for left and right side, it can apply to all nodes
#update the boundaries as we call node.left/node.right

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(node, low = float('-inf'), high = float('inf')):
            if not node:
                return True
            
            if node.val >= high or node.val <= low:
                return False

            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)

        return dfs(root)
