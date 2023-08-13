#lowest common anscestor: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
#couldn't solve it. im not sure if it was because i didn't get it right or because i didn't know q and p was a fricking node
#i thought they were integers.... my logic was in the right direction 
#however at first i did try to use a if for when returning root, but i think that was wrong becuz its too hard to specify which condition
#we need to return the root node, instead, we should just specify when to go to the right or left, and else for returning

#recursive is faster than iterative here!

class Solution(object):
    def iterative_lowestCommonAncestor(self, root, p, q):
        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root
            
    
    def recursive_lowestCommonAncestor(self, root, p, q):
        l = min(p.val, q.val)
        r = max(p.val, q.val)

        if l > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif r < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root