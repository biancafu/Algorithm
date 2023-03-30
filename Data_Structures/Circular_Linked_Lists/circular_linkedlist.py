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


    #remove
    def remove(self, key):
        #2 cases: removing head or removing other nodes in list
        if self.head:
            #case 1: removing head
            if self.head.data == key:
                #subcase 1:only has 1 node in the list
                if self.head.next == self.head:
                    self.head = None
                    return
                #subcase 2:has more than 1 node in list
                cur = self.head
                while cur.next != self.head:
                    cur = cur.next
                cur.next = self.head.next #loop back to new head
                self.head = self.head.next #increment head to new head

            #case 2: removing other nodes in list
            else:
                # cur = self.head
                # prev = None
                # while cur.next != self.head:
                #     #increment right away since we already checked head
                #     prev = cur
                #     cur = cur.next

                #     if cur.data == key:
                #         prev.next = cur.next #skipping cur
                #         cur = None
                #         return
                
                #maybe this is a better way? this one will remove all the node with the key (not just one) from linkedlist
                cur = self.head.next #skip first node since we checked already
                prev = self.head
                while cur != self.head:
                    if cur.data == key:
                        prev.next = cur.next
                        cur = None
                    else:
                        prev = cur
                    cur = prev.next

    def length(self):
        count = 0
        cur = self.head
        while cur: #if empty list, count = 0, won't run while loop
            count += 1
            cur = cur.next

            if cur == self.head:
                break
        return count
    
    #split list
    def split_list(self):
        if not self.head or self.head.next == self.head:
            return
        
        cur = self.head
        prev = None
        mid = self.length() // 2
        count = 0 #self.head will be at 0

        #pass first half of the list
        while cur and count < mid:
            prev = cur
            count += 1
            cur = cur.next
        prev.next = self.head #loop back to head mid point to cut the list in half

        secondhalf = CircularLinkedList() #create an empty circular linkedlist
        while cur.next != self.head: #will break out of loop on last node
            secondhalf.append(cur.data)
            cur = cur.next
        #last node needs to be append as well
        secondhalf.append(cur.data)
        self.print_list()
        print("\n")
        secondhalf.print_list()

    #for josephus problem
    def remove_node(self, node):
        if self.head == node: #removing head of list
            if self.head.next == self.head: #if head is only node in list
                self.head = None
                return
            #more than 1 node in list
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            #cur = last node of list, point it to the new head (skip old head)
            cur.next = self.head.next
            self.head = self.head.next #appoint new head

        #removing other nodes in list (not head)
        else:
            cur = self.head.next
            prev = self.head
            while cur != self.head:
                if cur == node:
                    prev.next = cur.next
                else:
                    prev = cur
                cur = cur.next
    def josephus_circle(self, step):
        #we want to remove the node at the step until there is only one node left
        cur = self.head
        while self.head.next != self.head:
            count = 1
            while count != step:
                count += 1
                cur = cur.next
            print("KILL:" + str(cur.data))
            self.remove_node(cur)
            cur = cur.next
            

