#didn't time, but probably 40 min (second try), 97% speed 90% memory
#using my own logic (very similar to neetcode), i was able to come to this solution for the second time trying to solve it.
#i think the first time, i became very confused especially with the part where we are reversing in the middle of the linkedlist
#I did not consider the fact that we are not using None, we have to set the previous value pointing to the new head of reversed linkedlist
#as well as pointing the new last node of reversed linkedlist to the correct next node of the original linkedlist
#while incrementing/restarting every pointer we also have to take into account that the curr node is no longer the last node of the section
#it would be the head of section after reversing, and so we have to reset curr node to the last node of reversed section as well

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseKGroup(self, head, k):
        
        dummy = ListNode(0)
        dummy.next = head
        prev, curr, left = dummy, head, head
        count = 0
        def reverse(prev, end, head):
            r_prev = end
            curr = head

            while curr != end:
                next = curr.next
                curr.next = r_prev #pointing to the next node in line which is the end (for the first node of reverse which would be the last after reversing)
                r_prev = curr
                curr = next
            prev.next = r_prev #pointing previous to the new start node of reversed section

        while curr:
            count += 1

            if count == k: 
                next = curr.next #saving this for next pointer
                reverse(prev, next, left)
                count = 0
                #be careful here, curr is now head of the reversed section
                curr = prev = left #first node became last, prev for the next section will also become the current last node
                left = next #increment left to the first node of the next section, which would be the next node saved from linkedlist before reversing
            
            curr = curr.next

        return dummy.next
        

        


f = ListNode(5)
e = ListNode(4,f)
d = ListNode(3, e)
c = ListNode(2, d)
b = ListNode(1, c)

a = Solution().reverseKGroup(b, 2)
while a:
    print(a.val)
    a = a.next