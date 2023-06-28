def maxArea(height):
        #brute force O(n^2), exceeded time limit
        """
        :type height: List[int]
        :rtype: int
        """
        maxarea = 0
        for w in range(len(height)):
            for i in range(w + 1, len(height)):
                length = min(height[w], height[i])
                width = i - w
                maxarea = max(maxarea, length * width)
        
        return maxarea

a = maxArea([1,8,6,2,5,4,8,3,7])
print(a)

