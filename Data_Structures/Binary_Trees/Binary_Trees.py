class Node():
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

class BinaryTree():
    def __init__(self, root) -> None:
        self.root = Node(root)
    
    #traverse algorithms
    #DFS
    #pre-order: data -> left -> 
    #picture: F B A D C E G I H
    def preorder_print(self, start, traversal):
        if start:
            traversal += (str(start.value) + "-") #updated current traversal
            traversal = self.preorder_print(start.left, traversal) #call function (recursion) with new traversal
            traversal = self.preorder_print(start.right, traversal) #call function (recursion) with new traversal (after left was traversed)
        return traversal
        
    #in-order: left -> data -> right
    def inorder_print(self, start, traversal):
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    #post-order: left -> right -> data
    def postorder_print(self, start, traversal):
        if start: 
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")   
        return traversal

    #helper function
    def print_tree(self, traversal_type):
            if traversal_type == "preorder":
                return self.preorder_print(tree.root, "")
            elif traversal_type == "inorder":
                return self.inorder_print(tree.root, "")
            elif traversal_type == "postorder":
                return self.postorder_print(tree.root, "")

            else:
                print("Traversal type " + str(traversal_type) + " is not supported.")
                return False


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

#print(tree.print_tree("preorder"))
#print(tree.print_tree("inorder"))
print(tree.print_tree("postorder"))