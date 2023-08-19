#solved it without checking solution on second try, ~ 7 min
#this first time i wasn't able to solve it because i didn't use a external counter
#i have to use one with this solution because the way i am adding 1 to counter is determined by when a node is not null
#in that case, on evey leaf node, it will start from value 1, but thats not what we want
#1 should be the furthest left leaf node and it will add up, no number should repeat, this is why we use external counter

#both answers from iterative to recursive varies for speed and memory so hard to tell
#ranges from 20-42ms (99% - 36%) and memory about 20.9-21.2 mb (40%-95%)

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def kthSmallest(self, root, k): #my recursive solution
        #do in order dfs (left -> root -> right)
        self.count = 0
        def dfs(node):
            if not node:
                self.count += 0
                return

            if self.count > k: #don't need to waste time and memory, return once solution is found
                return
            
            dfs(node.left)
            self.count += 1
            if self.count == k:
                self.res = node.val
                #return     #i think this doesn't change much
            
            dfs(node.right)

        dfs(root)
        return self.res