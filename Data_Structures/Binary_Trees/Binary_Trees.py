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
    if not start:
        return
    traversal += str(start) + "-" #updated current traversal
    traversal = self.preorder_print(start.left, traversal) #call function (recursion) with new traversal
    traversal = self.preorder_print(start.right, traversal) #call function (recursion) with new traversal (after left was traversed)
    return traversal
    
#in-order: left -> data -> right

#post-order