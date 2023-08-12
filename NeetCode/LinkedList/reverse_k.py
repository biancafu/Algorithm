class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        count = 0
        dummy = ListNode(0)
        dummy.next = head
        left, right = head, head

        while right:
            if count == k:
                self.reverse(left, right)
                left = left.next
                count = 0

            
            count += 1
            right = right.next
        return dummy.next
            

    def reverse(self, left, right):
        prev = right
        curr = left
        while curr != right:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next


f = ListNode(5)
e = ListNode(4,f)
d = ListNode(3, e)
c = ListNode(2, d)
b = ListNode(1, c)

a = Solution().reverseKGroup(b, 2)
while a:
    print(a.val)
    a = a.next