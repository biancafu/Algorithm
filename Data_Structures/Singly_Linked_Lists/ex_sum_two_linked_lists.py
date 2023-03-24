from singly_linkedlist import LinkList
#20 min, not good solution
def sum_two_lists(self, llist):
    p = self.head
    q = llist.head
    result = LinkedList()
    #if one of the lists is empty, return the other one
    if not p:
        return q
    if not q:
        return p
    
    carry = 0
    while p or q:
        sum = p.data + q.data + carry
        if sum >= 10:
            carry = sum//10
            sum %= 10
        else:
            carry = 0
        result.append(sum)
        p = p.next
        q = q.next
    
    if p:
        while p:
            if carry != 0:
                result.append(p.data + carry)
                carry = 0
            else:
                result.append(p.data)
            p = p.next     

        if q:
            while q:
                if carry != 0:
                    result.append(p.data + carry)
                    carry = 0
                else:
                    result.append(q.data)
                q = q.next
    
    return result