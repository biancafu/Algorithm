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
    #prepend - insert node in the beginning of linkedlist
    #insert_after_node - insert after a specific node 