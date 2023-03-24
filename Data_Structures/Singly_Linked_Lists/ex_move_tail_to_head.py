from singly_linkedlist import LinkedList
#14 min to solve
def move_tail_to_head(self):
    if self.head and self.head.next: #need at least 2 elements to rotate
        length = self.len_iteration()
        p = self.head
        count = 0
        while p:
            count += 1
            if count == length - 1: #second last node
                second_last = p
            if count == length: #last node
                last = p
            p = p.next
        last.next = self.head #last node point to head
        self.head = last #change first node to last node
        second_last.next = None #make second last node to tail


#solution: basically the same
def move_tail_to_head_solution(self):
    if self.head and self.head.next:
        p = self.head
        second_last = None #basically same as prev
        while p.next: #this stops the loop on the last node
            second_last = p
            p = p.next
        
        p.next = self.head
        self.head = p
        second_last.next = None


llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

llist.print_list()
move_tail_to_head_solution (llist)
print("\n")
llist.print_list()