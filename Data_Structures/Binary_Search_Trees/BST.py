class Node(object):
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

#recursion on itself
#this works only because we check if the left/right is none and insert value
#meaning that there is a condition for next of leaf nodes (None)
#if we don't have one (like the printing, only checking what current node is)
#then every next of leaf node (None) it will go back to node = self.root
#this won't work:
# def inorder_print_tree(self, cur_node = None):
#         if cur_node is None:
#             cur_node = self.root
#         self.inorder_print_tree(cur_node.left)
#         print(str(cur_node.data))
#         self.inorder_print_tree(cur_node.right)
def insert(self, data, cur_node = None):
        if self.root is None:
            self.root = Node(data)
        else:
            if not cur_node:
                cur_node = self.root
            if data < cur_node.data:
                if cur_node.left is None:
                    cur_node.left = Node(data)
                else:
                    self.insert(data, cur_node.left)

            elif data > cur_node.data:
                if cur_node.right is None:
                    cur_node.right = Node(data)
                else:
                    self.insert(data, cur_node.right)


#recursion on inorder that would work: have to pass in root node instead of calling function without input
def inorder_print_tree(self, cur_node):
        if cur_node:
            self.inorder_print_tree(cur_node.left)
            print(str(cur_node.data))
            self.inorder_print_tree(cur_node.right)

def find(self, data, cur_node = None):
        if self.root:
            if cur_node is None:
                cur_node = self.root
            if data > cur_node.data and cur_node.right:
                return self.find(data, cur_node.right)
            elif data < cur_node.data and cur_node.left:
                return self.find(data, cur_node.left)
            elif data == cur_node.data:
                return True
            return False #need this
        else:
            return None
        
def is_bst_satisfied(self):
    def helper(node, low = float('-inf'), high = float('inf')):
        if not node: #no nodes means bst is satisfied
            return True

        val = node.data
        #has to be within the range
        if val <= low or val >= high:
            return False
        
        if not helper(node.right, val, high): #node.right has to be greater than val, so val becomes the lower bound
            return False
        if not helper(node.left, low, high): #node.left has to be smaller than val, so val becomes the upper bound
            return False
        return True
    
    return helper(self.root)
        