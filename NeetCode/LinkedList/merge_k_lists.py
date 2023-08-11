#wasn't able to solve it, becuz of messy logic but basically its just sorting
#instead of wanting to sort 1 by 1, if we group by 2 and do it that way, the time complexity would be nlogk (n being len of linkedlist and logk is from dividing list into 2 each time)
#initially what i was doing would be O(nk) the solution below from neetcode would be O(nlogk)
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            mergelists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergelists.append(self.merge(l1, l2))
            lists = mergelists
        
        return lists[0]

    
    def merge(self, l1, l2):
        dummy = ListNode(0)
        curr = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
            
        if l1:
            curr.next = l1
        elif l2:
            curr.next = l2
        
        return dummy.next

                    

a = ListNode(1)
b = ListNode(4)
c = ListNode(5)
a.next = b
b.next = c

d = ListNode(1)
e = ListNode(3)
f = ListNode(4)
d.next = e
e.next = f

g = ListNode(2)
h = ListNode(6)
g.next = h

n = Solution()
r = n.mergeKLists([a, d ,g])
while r:
    print(r.val)
    r = r.next