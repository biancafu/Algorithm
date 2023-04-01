class Node():
    def __init__(self, data) -> None:
        self.prev = None
        self.next = None
        self.data = data

class DoublyLinkedList():
    def __init__(self) -> None:
        self.head = None
    
    