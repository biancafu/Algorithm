# https://www.hackerrank.com/challenges/find-the-running-median

#initiall solved it in this way
#!/bin/python3

import math
import os
import random
import re
import sys
import bisect
import heapq

'''
for loop go through the array
sorted arr      median
7               7.0 
3,7             5.0

output arr to store all medians (median 1 digit)

use bisect to insert in sorted order O(n)
if binary search then insert will be O(logn + n)
'''

    
def findMedian(arr):
    length = len(arr)
    if length % 2 == 0: #even
        mid1 = length // 2
        mid2 = mid1 - 1
        return float((arr[mid1] + arr[mid2])/2)
    else: #odd
        return float(arr[length//2])
    
    
def runningMedian(a):
    sorted_arr = []
    medians = []
    for num in a:
        bisect.insort(sorted_arr, num)
        medians.append(findMedian(sorted_arr))
    
    return medians
    

#second solution: to always push it on right side first, then check length

'''
for loop go through the array
sorted arr      median
7               7.0 
3,7             5.0

output arr to store all medians (median 1 digit)

use 2 heaps to solve this
max heap for lower half
min heap for higher half
'''
    
def runningMedian(a):
    a.append(0) #from mistake, we need to add an extra to iterate one more round to get previous median
    left, right = [], [a[0]] #max, min
    median = [] #mistake: dont put first median here, because our loop later will append median from previous, then add new number
    for i in range(1, len(a)):
        num = a[i]
        #always push to right
        if len(right) > len(left):
            median.append(float(right[0])) #odd
        else:
            median.append(float((right[0]-left[0])/2))
        
        #always push to right first, then push to left (a bit inefficient)
        heapq.heappush(left, -heapq.heappushpop(right, num))
        
        #check if length left > right (we can't have that becuase of the way we designed to grab median)
        if len(left)>len(right):
            heapq.heappush(right, -heapq.heappop(left))
    
    
    return median
       

#third solution: put it on each side according to the its value, then always ensure right side is the one with more length
     
def runningMedian(a):
    L, R = [], [a[0]]
    median = [float(a[0])]
    
    for i in range(1, len(a)):
        num = a[i]
        if num > R[0]:
            heappush(R, num)
        else:
            heappush(L, -num)
            
        
        if len(R) - len(L) > 1:
            heappush(L, -heappop(R))
        elif len(L) - len(R) > 0:
            heappush(R, -heappop(L))

        if len(L) == len(R):
            median.append((R[0]-L[0])/2)
        else:
            median.append(R[0])
    
    return median
        
            
            
