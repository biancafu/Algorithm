#took 12 min and got it wrong. very bad
#while reversing the list, i made a mistake of adding on extra step next.next = curr, this is unnecessary since we can update this in the next loop 
#(when next becomes curr, so curr.next is updated)
#also forgot to update head at the very end (we need to point head towards the end aka the top of reversed list) 
#this would be prev because when the while loop breaks, curr = None and prev = last node of list

def reverseList(self, head):
    curr = head
    prev = None

    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    head = prev
    return head