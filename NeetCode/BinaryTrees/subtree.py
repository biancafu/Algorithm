#easy question but i find it tricky, wasn't able to solve it
class Solution(object):
    def isSubtree(self, root, subRoot):
        # logically, we will think to go through the tree and when the root.val == subroot.val then we can check if it is the same tree
        # to do this, we can create 1 helper function to check if it is the same tree
        # and also make a recursive function itself to head to next starting node
        # we have edge cases for when root is null and subRoot not null, then its impossible for subroot to be subtree of root, if root and subroot are both null then it is a subtree
        #edge cases
        if not subRoot:
            return True
        if not root:
            return False
        
        # if root.val == subRoot.val: this doesn't work because we can have repeated values in the tree. If we have a tree that happens to have subroot in the later section but we have same value in the front, it will return False without going to the bottom. ex: lets say we have [1, 1] and subroot [1], once we check first time and have same value, we would already return False and not gonna check the rest.
        if self.sameTree(root, subRoot): #has to run it every time
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) #only needs 1 to be true




    def sameTree(self, r1, r2):
        if not r1 and not r2: 
            return True
        
        if not r1 or not r2 or r1.val != r2.val:
            return False
        
        return self.sameTree(r1.left, r2.left) and self.sameTree(r1.right, r2.right)
        