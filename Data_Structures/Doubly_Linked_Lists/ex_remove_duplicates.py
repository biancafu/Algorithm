from doubly_linkedlist import DoublyLinkedList
# 11 min
def remove_duplicates(self):
    cur = self.head
    duplicates = set()

    while cur:
        if cur.data in duplicates: #duplicate value
            next = cur.next
            self.delete_node(cur)
            cur = next
        else: #non duplicate value
            duplicates.add(cur.data)
            cur = cur.next



dllist = DoublyLinkedList()
dllist.append(8)
dllist.append(4)
dllist.append(4)
dllist.append(6)
dllist.append(4)
dllist.append(8)
dllist.append(4)
dllist.append(10)
dllist.append(12)
dllist.append(12)


remove_duplicates(dllist)
dllist.print_list()