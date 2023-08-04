#unable to solve the first time
#but the second time solved with 26 min 88% speed 26%memory
import math
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head):
    """
    :type head: ListNode
    :rtype: None Do not return anything, modify head in-place instead.
    """
    #count length of linkedlist
    curr = head
    length = 0
    while curr:
        curr = curr.next
        length += 1

    lefthalf = head
    pointer = lefthalf
    count = 0
    #count until half of linkedlist
    while count <= math.ceil(length / 2): #used inclusive condition before, but it was wrong
                #this is because we didn't split the half correctly (counted one more since inclusive) which led to the righthalf ending 1 value early, 
                #and so when we do left.next = right (right becomes None) ending the leftpointer
        pointer = pointer.next
        count += 1

    #reverse the rest of the half
    righthalf = pointer 
    prev = None
    while righthalf:
        next = righthalf.next
        righthalf.next = prev
        prev = righthalf
        righthalf = next
    
    righthalf = prev
    while lefthalf:
        next = lefthalf.next
        lefthalf.next = righthalf
        lefthalf = lefthalf.next  #lefthalf = righthalf
        righthalf = next
    
    return head

    

e = ListNode(4)
d = ListNode(3, e)
c = ListNode(2, d)
b = ListNode(1, c)

a = reorderList(b)
while a:
    print(a.val)
    a = a.next