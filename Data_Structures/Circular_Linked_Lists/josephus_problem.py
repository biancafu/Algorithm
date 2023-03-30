from circular_linkedlist import CircularLinkedList


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
            

     
cllist = CircularLinkedList()
cllist.append(1)
cllist.append(2)
cllist.append(3)
cllist.append(4)


cllist.josephus_circle(2)
cllist.print_list()