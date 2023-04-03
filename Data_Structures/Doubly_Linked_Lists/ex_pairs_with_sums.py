from doubly_linkedlist import DoublyLinkedList
#15 min
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

dllist = DoublyLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.append(5)

print(dllist.pairs_with_sum(5))