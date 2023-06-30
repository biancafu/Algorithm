def trap_neetcode(height):
    #different incrementation
    l, r = 0, len(height) - 1 
    lmax, rmax = height[l], height[r]
    total = 0
    while l < r:
        if lmax < rmax: 
            l += 1 #increment to the next value first since we have our lmax and rmax set as the start and end value already
            #if we update the max first, our area will never be negatvie
            #this works because even if max is updated (to the current height), we will get 0 from subtraction
            #meaning that no area will be added
            lmax = max(lmax, height[l])
            total += lmax - height[l]
        else: #rmax < lmax
            r -= 1
            rmax = max(rmax, height[r])
            total += rmax - height[r]
            

    return total

def trap_faster(height):
    #to calculate the trapped rain area use logic:
    #min(left max height, right max height) - current height
    #shift the lower max height side
    #we only know one side max of the current position, so how come this works?
    #because we want the min of the max, so we just need the smaller side

    #concern that how do we know if the side will close off if we only know one side of max height?
    #we move the side with smaller max height, so we know for sure, the other side max >= this side 
    

    l, r = 1, len(height) - 2 #skipping the first and last value since end point cannot contain water
    lmax, rmax = height[0], height[len(height) - 1]
    total = 0
    while l < r: 
        if lmax <= rmax: 
            if lmax - height[l] > 0:
                total += lmax - height[l] #lmax is the smaller side
            lmax = max(lmax, height[l])
            l += 1
        else: #rmax < lmax
            if rmax - height[r] > 0:
                total += rmax - height[r]
            rmax = max(rmax, height[r])
            r -= 1

    return total


def trap(height):
    #slower solution
    #O(n) = O(3n)
    leftmax = []
    rightmax = []
    rain = 0

    maxnum = 0
    for i in range(0, len(height)):
        leftmax.append(maxnum)
        maxnum = max(maxnum, height[i])
    
    maxnum = 0
    for i in range(len(height) - 1, -1, -1):
        rightmax.insert(0, maxnum)
        maxnum = max(maxnum, height[i])

    for i in range(1, len(height) - 1):
        area = min(leftmax[i], rightmax[i]) - height[i]
        if area > 0:
            rain += area
    
    return rain
        