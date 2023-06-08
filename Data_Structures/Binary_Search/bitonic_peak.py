def find_bitonic_peak(A):

    #need at least 3 element to form bitonic peak
    if len(A) < 3:
        return None
    
    low = 0
    high = len(A) - 1
    
    while low <= high:
        mid = (low + high) // 2
        #check range of mid (make sure it doesn't go out of range)
        left = A[mid - 1] if mid > 0 else float('-inf') #make it -inf so if first element is peak, it can satisfy the condition by being larger than -inf (mid > left)
        right = A[mid + 1] if mid < len(A) - 1 else float('-inf') #make it -inf so if last element is peak, it can satisfy mid > right

        if A[mid] > left and A[mid] > right: #peak
            return A[mid]
        elif A[mid] > left and A[mid] < right: #eliminate left half
            low = mid + 1
        elif A[mid] < left and A[mid] > right: #eliminate right half
            high = mid - 1
    return None

def find_peak(A): #https://leetcode.com/problems/find-peak-element/description/
    #unordered list, with repeatable numbers, find any peak (could have more than 1): a number greater than its left and right side
    #this works with binary search since eventually we will find one peak when we keep eliminating the side where it satisfies the condition (mid > right side/left side) 
    #since then it means it is the current peak from that side, and we need a bigger peak from the other side
    #when only 1 element
    if len(A) == 1: return 0
    #if first element/last element is peak: (since there can be multiple peaks)
    if A[0] > A[1]: return A[1]
    if A[len(A) - 1] > A[len(A) - 2]: return A[len(A) - 1]

    #we can eliminate top and end since we checked it already
    low = 1
    high = len(A) - 2

    while low <= high:
        mid = (low + high) // 2
        if A[mid] > A[mid - 1] and A[mid] > A[mid + 1]:
            return A[mid]
        elif A[mid] < A[mid - 1]: # we are only checking one side, since there can be multiple peaks and we do not need  worry if the other side also has peak
            high = mid - 1
        elif A[mid] < A[mid + 1]:
            low = mid + 1
    return None 

            
            



      

# Peak element is "5".
A = [1, 2, 3, 4, 5, 4, 3, 2, 1]
print(find_bitonic_peak(A))
A = [1, 6, 5, 4, 3, 2, 1]
print(find_bitonic_peak(A))
A = [1, 2, 3, 4, 5]
print(find_bitonic_peak(A))
A = [5, 4, 3, 2, 1]
print(find_bitonic_peak(A))