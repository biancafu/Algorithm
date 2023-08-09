# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

#didn't know how to solve it but its really simple after explanation
def copyRandomList(head):
    hashmap = { None: None } #added None becuz random pointer can point to null
    curr = head

    while curr:
        hashmap[curr] = Node(curr.val)
        curr = curr.next
    
    curr = head
    while curr:
        copy = hashmap[curr]
        copy.next = hashmap[curr.next] #pointing copy to the copy of next from original list
        copy.random = hashmap[curr.random] #pointing copy to the copy of random from original list
        curr = curr.next 
    
    return hashmap[head]