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
            
    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next
    
    #prepend
    def prepend(self, data):
        #2 cases: empty list or non empty list
        if not self.head: #case 1: empty list
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_node_after(self, key, data):
        #2 cases: node.next is null (last node), node.next is not null (other nodes)
        cur = self.head
        new_node = Node(data)
        while cur:
            if cur.data == key:
                if not cur.next: #case 1: last node
                    self.append(data)
                    return
                else: #case 2: other nodes
                    next = cur.next
                    cur.next = new_node
                    new_node.prev = cur
                    new_node.next = next
                    next.prev = new_node
                    return
            cur = cur.next
        
    def add_node_before(self, key, data):
        #2 cases: add node before 1) head, 2) all other nodes
        cur = self.head
        while cur:
            if cur.data == key: 
                if cur == self.head: #case 1
                    self.prepend(data)
                    return
                else: #case 2
                    new_node = Node(data)
                    prev = cur.prev
                    new_node.prev = prev
                    new_node.next = cur
                    prev.next = new_node
                    cur.prev = new_node
                    return
            cur = cur.next

    def delete(self, key):
        #4 cases: deleteing head (only 1 node in list), deleting head (with other nodes in list), deleting middle nodes, deleting last not
        cur = self.head
        while cur:
            if cur.data == key:
                if cur == self.head:
                    #case 1: deleting head (the only node in list)
                    if not cur.next:
                        cur = None
                        self.head = None
                        return
                    #case 2: deleting head (with other nodes in list)
                    else:
                        next = cur.next
                        next.prev = None
                        cur.next = None
                        cur = None
                        self.head = next
                        return
                #case 3: deleting last node
                elif not cur.next:
                    cur.prev.next = None
                    cur.prev = None
                    cur = None
                    return
                #case 4: other nodes
                else:
                    prev = cur.prev
                    next = cur.next
                    prev.next = next
                    next.prev = prev
                    cur.next = None  #dunno if we need this
                    cur.prev = None #dunno if we need this
                    cur = None
                    return
            cur = cur.next

    #copy and paste for exercise remove dupliates (deleting node passed in function)
    def delete_node(self, node):
        cur = self.head
        while cur:
            if cur == node and cur == self.head:
                # Case 1:
                if not cur.next:
                    cur = None 
                    self.head = None
                    return

                # Case 2:
                else:
                    nxt = cur.next
                    cur.next = None 
                    nxt.prev = None
                    cur = None
                    self.head = nxt
                    return 

            elif cur == node:
                # Case 3:
                if cur.next:
                    nxt = cur.next 
                    prev = cur.prev
                    prev.next = nxt
                    nxt.prev = prev
                    cur.next = None 
                    cur.prev = None
                    cur = None
                    return

                # Case 4:
                else:
                    prev = cur.prev 
                    prev.next = None 
                    cur.prev = None 
                    cur = None 
                    return 
            cur = cur.next

    def reverse(self):
        cur = self.head
        while cur:
            next = cur.next
            prev = cur.prev
            cur.next = prev
            cur.prev = next
            cur = next
        
        if prev:
            self.head = prev.prev #its prev.prev not .next because we are looking for last node(technically first node in the reverse list) 
        
    
    def pairs_with_sum(self, sum_val):
        pairs = []
        cur = self.head

        while cur:
            target = cur.next
            target_val = sum_val - cur.data
            while target:
                if target.data == target_val:
                    break
                target = target.next
            
            if target: #only record it if we find a pair
                pairs.append(f"({cur.data},{target.data})")
            
            cur = cur.next
        
        return pairs