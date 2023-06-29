def trap( height):
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
        