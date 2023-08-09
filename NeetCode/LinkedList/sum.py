#38 min but the test caases didn't all pass
#neetcode solution is so much better
#i essentially got the right idea, but the implementation is horrible
#need to think better logically


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    res = ListNode(0)
    curr = res
    #instead of creating lets modify list1
    carry = 0
    while l1 or l2 or carry: #using carry here instead of doing another if loop is super smart 
        #(this way we don't need a prev pointer since the loop will break when either l1 or l2 is none which mean we can't do l1.next becuz theres no none.next)
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        s = v1 + v2 + carry
        carry = s // 10
        curr.next = ListNode(s % 10)
        curr = curr.next

        l1 = l1.next if l1 else None #there is no next on None, so we have to condition it becuz of our while loop
        l2 = l2.next if l2 else None

    return res.next