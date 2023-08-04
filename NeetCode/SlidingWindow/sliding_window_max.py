import collections


def maxSlidingWindow(nums, k):
    #needcode uses deque which I am not familiar with
    #deque: like a queue but able to pop/insert from both ends, can be used using collections.deque() in python
    #the idea is to keep q[0] with the largest number of the window, and q[-1] will have the smallest number 
    #to keep the queue in decreasing order, we will have to keep popping q[-1] until q[-1] > current number (this is because we cannot insert from the middle)
    #what about the smaller numbers? well we don't care about them because we are trying to find the max of substring, this means that if we find a greater number, we are safe to disgard the smaller ones
    #we also have to pop off the numbers that are out of the window range, this will always be checked at the furthest left since we are incrementing 1 by 1
    #meaning that we only have to check and pop 1 at each iteration (pop q[0] if it is out of range)


    res = []
    r = 0
    q = collections.deque() #using this to store index
    while r < len(nums):
        #pop smaller values
        while q and nums[q[-1]] < nums[r]:
            q.pop()
        q.append(r)

        #check if q[0] is out of range:
        if q[0] < r - k + 1:
            q.popleft() #deque method
        
        if r + 1 >= k:
            res.append(nums[q[0]])
        r += 1
    
    return res





    #time limited exceeded with this solution that I originally created where I rewrote after I tried to just use max(window) on every window
    #I rewrote this to only find max again when the original max is pushed out by index, but this is still too slow
    res = []
    l = 1
    window = nums[0:k]
    res.append(max(window))
    maximum = [res[0], window.index(res[0])]

    for r in range(k, len(nums)):
        num = nums[r]
        window = nums[r - k + 1: r + 1]
        if maximum[0] <= num:
            maximum = [num, r]
            res.append(num)
        elif maximum[0] > num and maximum[1] > r - k:
            res.append(maximum[0])
        else: #maximum out of window
            temp = max(window)
            maximum = [temp, l + window.index(temp)]
            res.append(temp)
        l += 1
    return res

a = maxSlidingWindow([1,-1], 1)
print(a)