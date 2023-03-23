#identify if the linkedlist is palindrome
#3 ways to solve
from singly_linkedlist import LinkedList
#string: comparing string and its reverse to see if it is palindrome
def is_palindrome1(self):
    s = ""
    cur = self.head
    while cur:
        s += cur.data
        cur = cur.next
    return s == s[::-1]

#stack: using stack to store linkedlist, and compare one by one
def is_palindrome2(self):
    s = []
    cur = self.head
    while cur:
        s.append(cur.data) #remember if we are storing data or node
        cur = cur.next

    cur = self.head
    while cur:
        if cur.data != s.pop(): #comparing first element with last element (stack: LIFO)
            return False
        cur = cur.next
    return True

#2 pointer: store data in list, then compare using list[-1](kinda similar to stack)
def is_palindrome3(self):
    if self.head:
        p = self.head
        prev = [] #to store data
        i = 0 #to get len of linkedlist
        while p:
            i += 1
            prev.append(p.data) #remember if we are storing data or node
            p = p.next
        
        p = self.head
        count = 1 #since prev[-1] start with -1 not 0
        while p and count <= i//2 + 1:
            if prev[-count] != p.data:
                return False
            p = p.next
            count += 1
        return True 
    else:
        return True


llist = LinkedList()


llist_2 = LinkedList()
llist_2.append("A")
llist_2.append("B")
llist_2.append("C")

print(is_palindrome1(llist))
print(is_palindrome2(llist))
print(is_palindrome3(llist))
print(is_palindrome1(llist_2))
print(is_palindrome2(llist_2))
print(is_palindrome3(llist_2))