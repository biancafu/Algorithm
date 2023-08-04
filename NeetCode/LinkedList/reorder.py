#unable to solve the first time
#but the second time solved with 26 min 88% speed 26%memory
import math
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#my solution is similar to neetcode, but the way i reorder the two list at the very end is different
#for me, I switched up leftpointer and rightpointer every iteration so that each iteration we are reordering 1 node at a time
#for neetcode, he did 2 nodes at a time, he created two temp variable (i created 1)
#this means that he reorders it faster (even better memory maybe becuz i used count for length and he did fast&slow pointer)

#for the while loop condition, for me since Im switching the left right pointer every iteration, I said while leftpointer and it eventually went to None
#but for neetcode, if i do while leftpointer, it goes out of range for right pointer and if i do while rightpointer, it becomes a circle linkedlisit 
#since the left pointer is not pointing to None
#this is why he had his left pointer pointing to None (I didn't do this becuz i used counter for length)
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

#this is faster: 94%, the memory is around the same: 22%
def reorderList_neetcode(head):
    fast, slow = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    #this will stop when slow is pointing to the middle

    #separating the list into two portion left and right
    right = slow.next
    slow.next = None

    #reverse right side
    prev = None
    while right:
        next = right.next
        right.next = prev
        prev = right
        right = next
    
    left, right = head, prev
    while right:
        next1, next2 = left.next, right.next
        left.next = right
        right.next = next1
        left = next1
        right = next2
    
    return head
    


        
        

e = ListNode(4)
d = ListNode(3, e)
c = ListNode(2, d)
b = ListNode(1, c)

a = reorderList(b)
while a:
    print(a.val)
    a = a.next