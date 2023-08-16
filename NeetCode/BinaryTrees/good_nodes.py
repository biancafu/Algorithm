#finished about 23 min i think, but the code wasn't working because I used the wrong variable
#(i named maxval but put max for the variable) need to name the variable a bit better in the future
#not the best speed ~70% and 58% memory
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(node, maxval):
            if not node:
                return 0
            
            count = 1 if node.val >= maxval else 0
            maxval = max(maxval, node.val)
            res = count + dfs(node.left, max) + dfs(node.right, max)
            print(res)
            return res

        return dfs(root, root.val)

            
            



