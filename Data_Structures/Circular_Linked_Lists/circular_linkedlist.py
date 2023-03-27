class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList():
    def __init__(self):
        self.head = None
    
    #append
    def append(self, data):
        #2 cases: list is empty, list is not empty
        #case 1: list is empty
        if not self.head: 
            self.head = Node(data)
            self.head.next = self.head
        
        #case 2: list is not empty, append new node to last node
        else: 
            new_node = Node(data)
            cur = self.head
            #find last node (cur = last node when break out of loop)
            while cur.next != self.head:
                cur = cur.next
            #change last node pointing to new node 
            cur.next = new_node
            #update new node.next pointing to head (new node becomes the last node)
            new_node.next = self.head
        
    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                break

    #prepend: add new node to the top of linkedlist
    def prepend(self, data):
        #2 cases: linkedlist empty or not empty
        new_node = Node(data)
        new_node.next = self.head
        cur = self.head
        #case1: linkedlist empty
        if not cur:
            new_node.next = new_node
            
        #case 2:
        else:
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
        self.head = new_node






        



cllist = CircularLinkedList()
cllist.append("C")
cllist.append("D")
# cllist.prepend("B")
# cllist.prepend("A")
cllist.print_list()