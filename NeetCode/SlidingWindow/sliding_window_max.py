def maxSlidingWindow(nums, k):
    #needcode uses deque which I am not familiar with
    
    #time limited exceeded
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