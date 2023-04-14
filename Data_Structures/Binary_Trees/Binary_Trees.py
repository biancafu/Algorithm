class Node():
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

class Stack(object):
    def __init__(self):
        self.items = []

    def __len__(self):
        return self.size()
     
    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):  
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        s = ""
        for i in range(len(self.items)):
            s += str(self.items[i].value) + "-"
        return s
    
class Queue(): #FIFO (start is the end of list)
    def __init__(self) -> None:
        self.items = []
    
    def enqueue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
    
    def is_empty(self):
        return len(self.items) == 0
    
    def peek(self):
        if len(self.items) > 0:
            return self.items[-1]
        
    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)

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
    #picture: A B C D E F G H I
    def inorder_print(self, start, traversal):
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    #post-order: left -> right -> data
    #picture: A C E D B H I G F
    def postorder_print(self, start, traversal):
        if start: 
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")   
        return traversal
    
    #BFS
    #picture: 1 2 3 4 5
    def levelorder_print(self, start):
        if not start:
            return
        queue = Queue()
        queue.enqueue(start)
        traversal = ""

        while len(queue) > 0:
            node = queue.dequeue()
            traversal += str(node.value) + "-"
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return traversal
    
    #picture 4 5 2 3 1
    def reverse_levelorder_print(self, start):
        if not start:
            return
        queue = Queue()
        stack = []
        queue.enqueue(start)
        traversal = ""

        while len(queue) > 0:
            #same step as levelorder for queue but putting in stack instead of traversal
            node = queue.dequeue()
            stack.append(node)

            # have to get right then left for reverse 
            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)

        while len(stack) > 0:
            traversal += str(stack.pop().value) + "-"
        
        return traversal
            
            
    def height(self, start):
        if not start:
            return -1
        left = self.height(start.left)
        right = self.height(start.right)

        return 1 + max(left, right)

    def size_(self, node):
        if node is None:
            return 0
        return 1 + self.size_(node.left) + self.size_(node.right)

    def size(self):
        if self.root is None:
            return 0

        stack = Stack()
        stack.push(self.root)
        size = 1
        while stack:
            node = stack.pop()
            if node.left:
                size += 1
                stack.push(node.left)
            if node.right:
                size += 1
                stack.push(node.right)
        return size

    #helper function
    def print_tree(self, traversal_type):
            if traversal_type == "preorder":
                return self.preorder_print(tree.root, "")
            elif traversal_type == "inorder":
                return self.inorder_print(tree.root, "")
            elif traversal_type == "postorder":
                return self.postorder_print(tree.root, "")
            elif traversal_type == "levelorder":
                return self.levelorder_print(tree.root)
            elif traversal_type == "reverse_levelorder":
                return self.reverse_levelorder_print(tree.root)

            else:
                print("Traversal type " + str(traversal_type) + " is not supported.")
                return False
    


# Calculate size of binary tree:
#     1
#    / \
#   2  3
#  / \
# 4  5
# 
# 
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

print(tree.size())
print(tree.size_(tree.root))
