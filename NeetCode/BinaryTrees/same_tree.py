# 6 min
class Solution(object):
    def isSameTree(self, p, q):
        if not q and not p:
            return True
        if not q or not p or p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
        
