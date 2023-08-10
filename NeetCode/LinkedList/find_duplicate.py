#circular linkedlist
#need to use floyd's algorithm: using a slow and fast pointer, do a loop until the first intersection 
#then start another slow pointer from the beginning, with the original slow pointer counting from the first intersection, 
#then the second intersection would be the beginning of the circle linkedlist
#this is because: slow = p + c - x; fast = p + nc - x where p is distance to loop, c is length of loop and x is distance to beginning of loop from intersection
#we know 2 slow = 1 fast, therefore 2(p + mc - x) = p + nc - x => p -lc - x = 0 (but c is loops) so basically we have p = x (+ l loops)

def findDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    slow, fast, p = 0, 0, 0
    #we are using n in nums as the next destination (if nums[1] = 3, next one goes to nums[3])
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    while True:
        slow = nums[slow]
        p = nums[p]
        if p == slow:
            return p
