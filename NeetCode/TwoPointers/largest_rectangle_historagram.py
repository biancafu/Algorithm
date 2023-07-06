#hard question, cannot solve it
#https://leetcode.com/problems/largest-rectangle-in-histogram/description/
'''
to solve this problem, we need to understand a couple of things
first, understand that if height[i] < height[i + 1], that means we can keep extending the rectangle (keep adding on the stack)
second, if height[i] > height[i + 1] that means all the heights that are greater than height[i + 1] will have to come to a stop
meaning that for all the hights > height[i + 1], we need to pop them out of the stack and calculate their area
so for example, if i = 3 < i = 2 and i = 1, then we first calculate area using h2 * (i == 3 - i == 2 ) = h2*1 = h2
and then for i = 1, h1 * (i==3 - i==1) = 2h1. In this case the width would be 2 since it is from index 1
we will never have to worry about going left because the left one will be counting towards right
(stack wil always be scending)
'''

def largestReactangleArea_neetcode(heights):
    stack = []
    maxarea = 0

    for i, height in enumerate(heights):
        start = i
        while stack and stack[-1][1] > height: #when the curr height is smaller than previous, we need to cut off the higher rectangles since they cannot extend to the right anymore
            maxarea = max(maxarea, stack[-1][1] * (i - stack[-1][0])) #area = pop_height * (i - pop_index)
            start = stack[-1][0] #update start for the smaller height (curr height) since we pop the bigger ones, meaning the smaller one can extend to the left side
            stack.pop()
        stack.append([start, height])
    
    for [i, height] in stack: #calculate the rest of rectangles in stack (the ones that didn't get cut off half way due to having a smaller right side)
        maxarea = max(maxarea, height * (len(heights) - i))    
    return maxarea

#another faster way since we don't have to iterate through the stack again for the left overs (the right boundary ones?)
def largestRectangleArea(height):
        height.append(0) #append 0 as a dummy for the right boundary (for the rectangles that didn't hit a smaller right side, it can continue to extend, so we add a 0 to stop it)
        stack = [-1] #we need a -1 so when the stack is left with one element, the height for it would be height[-1] which is zero  ( we know that since we added the zero ) to enforce the right boundary
        area = 0
        for i in range(len(height)):
            while height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i - 1 - stack[-1]  # i-1 represents the right boundary of the considered rectangle and stack[-1] represents the left boundary
                area = max(area, h * w)
            stack.append(i)
        height.pop()
        return area

heights = [2,1,5,6,2,3]
a = largestRectangleArea(heights)
print(a)