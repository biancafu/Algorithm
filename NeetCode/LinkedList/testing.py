class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


e = ListNode(4)
d = ListNode(3, e)
c = ListNode(2, d)
b = ListNode(1, c)

head = b
head = head.next
head.next = None

while b:
    print(b.val)
    b = b.next

#this shows that essentially the linkedlist is being modified even tho the pointer is at different spot
