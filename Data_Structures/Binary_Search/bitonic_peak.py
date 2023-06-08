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
      

# Peak element is "5".
A = [1, 2, 3, 4, 5, 4, 3, 2, 1]
print(find_bitonic_peak(A))
A = [1, 6, 5, 4, 3, 2, 1]
print(find_bitonic_peak(A))
A = [1, 2, 3, 4, 5]
print(find_bitonic_peak(A))
A = [5, 4, 3, 2, 1]
print(find_bitonic_peak(A))