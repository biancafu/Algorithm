#i understood the question wrong, but i still probably wouldnt get it, need to strengthen my linkedlist knowledge/fundamentals

#recursion approach: i probably can't come up with it, i don't understnad that well, but leave it here as reference

def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return mergeTwoLists(l1, l2)
        
def mergeTwoLists(self, l1, l2):
        if l1 == None: return l2
        if l2 == None: return l1
        if l1.val <= l2.val:
            l1.next = mergeTwoLists(l1.next, l2)
            return l1
        if l1.val >= l2.val:
            l2.next = mergeTwoLists(l1, l2.next)
            return l2

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists_neetcode(list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode() #the linkedlist pointing at head
        res = dummy #the same pointer pointing at head but will be updating through the linkedlist later
        if not list1:
            return list2
        elif not list2:
            return list1
    

        while list1 and list2:
            if list1.val <= list2.val:
                res.next = list1
                list1 = list1.next
            else:
                res.next = list2
                list2 = list2.next
            res = res.next
        
        if list1:
            res.next = list1
        elif list2:
            res.next = list2
        
        return dummy.next

#this is my solution that I originally thought of, I thought the question wanted us to merge without creating a new linkedlist (has to modified one of the given ones)
#I wasn't able to do it at first because I was kinda confused, after reviewing solution video, I was able to come up with the solution
#that is modifying the list itself instead of creating a dummy
#the speed seems to be around the same (good cases it takes a bit faster than neetcode)
#for the memory I assume it is better than neetcode because I am not using dummy but sometimes it varies depending on the cases so i think theyre very similar

def merge_my_solution(list1, list2):
     
        if not list1:
            return list2
        elif not list2:
            return list1

        if list1.val <= list2.val:
            l1 = list1
            l2 = list2

        else:
            l1 = list2
            l2 = list1



        while l1.next and l2:
            next = l1.next #2
            if next.val >= l2.val: #2 > 1
                l1.next = l2 #1 -> 1
                l2 = next   #l2 = 2 -> 4
                
            l1 = l1.next #l1 = 1 (second 1)
        if l2:
            l1.next = l2
        return list1 if list1.val <= list2.val else list2
                
        
