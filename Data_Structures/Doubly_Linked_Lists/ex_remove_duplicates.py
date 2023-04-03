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
