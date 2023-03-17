#singly linked list 
#linkedlist basic structure: node, linkedlist class

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None #empty linkedlist

    #insertion, O(n)
    #append - append node at the end of linkedlist
    def append(self, data):
        new_node = Node(data) 
        if self.head == None: #linkedlist is empty
            self.head = new_node
            return
        
        curr_node = self.head
        while curr_node.next: #go to end of linkedlist
            curr_node = curr_node.next
        
        curr_node.next = new_node #append node to end of linkedlist
        
    #prepend - insert node in the beginning of linkedlist
    #insert_after_node - insert after a specific node 