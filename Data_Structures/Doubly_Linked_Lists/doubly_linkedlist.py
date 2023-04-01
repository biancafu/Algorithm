class Node():
    def __init__(self, data) -> None:
        self.prev = None
        self.next = None
        self.data = data

class DoublyLinkedList():
    def __init__(self) -> None:
        self.head = None
    
    #append
    def append(self, data):
        #2 cases: if list is empty, if list is not
        #case 1: list is empty
        if not self.head: 
            self.head = Node(data)

        #case 2: list not empty
        else:
            cur = self.head
            while cur.next: #stop on last node
                cur = cur.next
            new_node = Node(data)
            cur.next = new_node
            new_node.prev = cur
            

