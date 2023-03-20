#singly linked list 
#linkedlist basic structure: node, linkedlist class

class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None #empty linkedlist

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

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
    
    #delete node by data
    def delete_node(self, key): 
        cur_node = self.head
        # need to identify 2 cases: 
        #   1. deleting head node
        #   2. deleting some node in the linkedlist

        #case 1: deleting head node
        if cur_node and cur_node.data == key: 
            self.head = cur_node.next
            cur_node = None
            return
        
        prev_node = None #prev node at head node
        #case 2: deleting some node in the linkedlist
        while cur_node and cur_node.data != key: #when cur_node is not None, find the node according to key 
            prev_node = cur_node
            cur_node = cur_node.next
        
        if cur_node is None: #if we can't find a matching node in list
            return
        
        prev_node.next = cur_node.next #prev_node -> cur_node.next (skipping the cur_node) meaning we removed the cur_node from linkedlist
        cur_node = None #deleting the cur_node

    #delete node by position
    def delete_by_position(self, pos):
        #needs linkedlist to not be empty to find positions:
        if self.head: #cur_node is not None <=> linkedlist is not empty 
            cur_node = self.head
            #position is 0 (deleting head node)
            if pos == 0:  
                self.head = cur_node.next
                cur_node = None
                return
            
            prev_node = None #prev node of head is None
            cur_pos = 0 #current position is 0

            #when cur_node is not None, find the node at pos
            while cur_node and cur_pos != pos: 
                prev_node = cur_node
                cur_node = cur_node.next
                cur_pos += 1
            
            if cur_node is None: #if we can't find a matching node in list
                return
            
            prev_node.next = cur_node.next
            cur_node = None

    #get length by iteration
    def len_iteration(self):
        cur_node = self.head
        count = 0

        while cur_node:
            count += 1
            cur_node = cur_node.next
        
        return count

    #get length by recursion
    def len_recursion(self, node): #pass in the node you want to start counting from
        if node is None: #breaking condition (end of linkedlist)
            return 0
        return 1 + len_recursion(node.next) #counting next node

    #swap node
    def swap_nodes(self, key1, key2):
        if key1 == key2: #cannot swap same element
            return
        
        #find the node matching the key and its previous node
        cur1 = self.head
        prev1 = None
        while cur1 and cur1.data != key1:
            prev1 = cur1
            cur1 = cur1.next

        cur2 = self.head
        prev2 = None
        while cur2 and cur2.data != key2:
            prev2 = cur2
            cur2 = cur2.next

        #check if we can find a matching values (nodes) in the list
        if not cur1 or not cur2:
            return

        #check if previous node is None
        if prev1: #if previous node exists
            prev1.next = cur2 #swap direction pointing to new value
        else:  #cur node is head if previous is None
            self.head = cur2 #swap head

        if prev2:
            prev2.next = cur1
        else:
            self.head = cur1
        
        cur1.next, cur2.next = cur2.next, cur1.next
        


        

        
