#50% speed 25% memory not that good
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        #root = preorder[0] this will always be true
        #if we split inorder with root, the left will always be left subtree, and right is right subtree
        #using these 2 concepts, we can recursively check each subtree
        #by splitting preorder into left and right subtree, using that length to identify where to call recursively using inorder.
        #inorder array root will always be first even in subtree
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(root.val)
        root.left = self.buildTree(preorder[1: mid + 1], inorder[0: mid])
        root.right = self.buildTree(preorder[mid + 1: ], inorder[mid+1: ])
        return root
    

    #a lot faster solution, but im too lazy to analyze it now, can read it later
    def buildTree(self, preorder, inorder):
        
        self.inorder_map={val:idx for idx, val in enumerate(inorder)}
        self.preorder_idx=0

        def treeHelper(left, right):
            if left>right:
                return None

            node_val = preorder[self.preorder_idx]
            root=TreeNode(node_val)
            self.preorder_idx+=1

            inorder_index=self.inorder_map[node_val]

            root.left = treeHelper(left, inorder_index-1 )
            root.right = treeHelper(inorder_index+1, right)

            return root

        return treeHelper(0, len(inorder)-1)
    