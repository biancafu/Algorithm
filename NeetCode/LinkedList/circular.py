#neetcode uses slow, fast pointer (Floyd's tortoise and hare)
#Floyd's tortoise and hare is O(n) since the slow pointer will go n times until it meets with the fast one
#slow goes 1 step, and fast goes 2 steps at a time making the slow at half when fast finishes a loop and slow will meet fast at starting point after


#around same speed and less memory
def hasCycle_neetcode(self, head):

        slow, fast = head, head

        while fast and fast.next: 
            #need fast.next since we are moving 2 steps at a time        
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
            
        return False

#2 min 40 sec
#this works but memory is bad since im storing it in a dict
def hasCycle(self, head):
        seen = {}
        curr = head
        while curr:
            if curr in seen:
                return True
            seen[curr] = curr
            curr = curr.next
        
        return False

