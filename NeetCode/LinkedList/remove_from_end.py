
#30 min becuz i redid it in the middle, took a while to figure out becuz i wasn't able to figure out what to do for the edge case when length == n
#needed to remove the first node but my while loop doesn't do that
#my solution speed is 85% and 69% memory
#the speed varies between different submission, some neetcode is faster, so its not
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd_neetcode(head, n):
    #using 2 pointers to find the nth position instead of counting like mine
    #the idea is to have left and right counter to have a gap of n
    #this will ensure that we get to the nth position from end with left pointer when the right pointer reachese the end
    #since we need 1 before n to replace, lets add n + 1 gap
    #i can't just do n + 1 becuz n+1 could be out of range (maybe can do if i add edge cases) needs to add a dummy node instead
    dummy = ListNode(0, head)
    left, right = dummy, head
    right = None
    while n > 0 and right:
        right = right.next
        n -= 1
    
    while right:
        left = left.next
        right = right.next

    
    left.next = left.next.next
    # #we are returning dummy.next becuz for edge cases when we are removing the first node, right pointer goes all the way to None
    # #and left pointer will be left at dummy
    # #so left.next = left.next.next => dummy.next = None
    # #but head stays untouched
    return dummy.next

    # we can't return head, for some reason even if the pointer points to head and then we set pointer = None, head will not become None
    # next = left.next
    # next.val = 3
    # next = None
    # left.next = left.next.next
    # return head


        


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

a = removeNthFromEnd_neetcode(ListNode(1), 1)
while a:
    print(a.val)
    a = a.next