from singly_linkedlist import LinkList
#20 min, not good solution
def sum_two_lists(self, llist):
    p = self.head
    q = llist.head
    carry = 0
    result = LinkList()
    while p or q:
        if p:
            i = p.data
        else:
            i = 0
        
        if q:
            j = q.data
        else:
            j = 0
        sum = i + j + carry

        if sum >= 10:
            carry = sum // 10 #should always be 1
            sum %= 10
        else:
            carry = 0 #resetting carry from previous run
        
        #increment to next node
        if p:
            p = p.next
        if q:
            q = q.next
        result.append(sum)
    
    return result
















    #first solution

    # p = self.head
    # q = llist.head
    # result = LinkedList()
    # #if one of the lists is empty, return the other one
    # if not p:
    #     return q
    # if not q:
    #     return p
    
    # carry = 0
    # while p or q:
    #     sum = p.data + q.data + carry
    #     if sum >= 10:
    #         carry = sum//10
    #         sum %= 10
    #     else:
    #         carry = 0
    #     result.append(sum)
    #     p = p.next
    #     q = q.next
    
    # if p:
    #     while p:
    #         if carry != 0:
    #             result.append(p.data + carry)
    #             carry = 0
    #         else:
    #             result.append(p.data)
    #         p = p.next     

    #     if q:
    #         while q:
    #             if carry != 0:
    #                 result.append(p.data + carry)
    #                 carry = 0
    #             else:
    #                 result.append(q.data)
    #             q = q.next
    
    # return result