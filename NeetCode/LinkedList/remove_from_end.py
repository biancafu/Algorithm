
#30 min becuz i redid it in the middle, took a while to figure out becuz i wasn't able to figure out what to do for the edge case when length == n
#needed to remove the first node but my while loop doesn't do that
#my solution speed is 85% and 69% memory
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    length = 0
    curr = head
    while curr:
        curr = curr.next
        length += 1

    count = 1
    curr = head

    if length == n:
        return curr.next
    while curr and curr.next:
        if count == length - n:
            next = curr.next.next
            curr.next = next
            break
        curr = curr.next
        count += 1
    return head

f = ListNode(5)
e = ListNode(4,f)
d = ListNode(3, e)
c = ListNode(2, d)
b = ListNode(1, c)

a = removeNthFromEnd(b, 2)
while a:
    print(a.val)
    a = a.next