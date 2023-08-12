#my initial solution but its slow
class Solution(object):
    def invertTree(self, root):
        self.traverse(root)
        return root
    
    def traverse(self, root):
        if root == None:
            return None
        root.left, root.right = root.right, root.left
        self.traverse(root.left)
        self.traverse(root.right)


#this is a lot faster, it seems like instead of doing if root: , doing if root == None: is faster
class Solution1(object):
    def invertTree(self, root):
        if root == None:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root