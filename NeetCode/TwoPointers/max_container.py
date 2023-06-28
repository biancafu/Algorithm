def maxArea_twopointers(height): #O(n)
     maxarea = 0
     l = 0
     r = len(height) - 1
     while l < r:
          area = min(height[l], height[r])*(r - l)
          maxarea = max(maxarea, area)

          if height[l] > height[r]:
               r -= 1
          else:
               l += 1
     return maxarea


#brute force O(n^2), exceeded time limit
def maxArea(height):
        maxarea = 0
        for w in range(len(height)):
            for i in range(w + 1, len(height)):
                length = min(height[w], height[i])
                width = i - w
                maxarea = max(maxarea, length * width)
        
        return maxarea

a = maxArea([1,8,6,2,5,4,8,3,7])
b = maxArea_twopointers([1,8,6,2,5,4,8,3,7])

print(b)

