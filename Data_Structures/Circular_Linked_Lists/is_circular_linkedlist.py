from circular_linkedlist import CircularLinkedList

def is_circular_linked_list(self, input_list):
    if input_list.head: #not empty list
        cur = input_list.head
        while cur: #break out loop if cur = None (not circular)
            cur = cur.next #increment to next node right away since there is nothing to check for self.head
            if cur == input_list.head:
                return True
    return False