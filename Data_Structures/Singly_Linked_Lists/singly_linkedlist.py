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
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head #new node pointing to node at head of linkedlist
        self.head = new_node #change head of linkedlist to new node
    
    #insert_after_node - insert after a specific node 
    def insert_after_node(self, prev_node, data):
        #A->B->C (B = prev_node)
        #insert D after B (ABDC)

        if not prev_node: #check if node is None or doesnt exist
            print("Node does not exist")
            return
        
        new_node = Node(data) #D = new_node
        new_node.next = prev_node.next #A->B->C, D->C
        prev_node.next = new_node #A->B->D, D->C <=> A->B->D->C

        

        
