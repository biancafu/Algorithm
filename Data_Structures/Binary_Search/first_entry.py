#given a sorted list and key, return the index of the first occurence of the key value 
def first_occurence(A, target):
    low = 0
    high = len(A) - 1

    while low <= high:
        mid = (low + high) // 2
        if A[mid] == target:
            if mid - 1 < 0: #make sure its within range
                return mid
            if A[mid - 1] != target: #if this is first occurence
                return mid
            high = mid - 1 #if this is not first occurence, continue to find
        elif A[mid] > target:
            high = mid - 1
        elif A[mid] < target:
            low = mid + 1
    
    return None

A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
target = 108
x = first_occurence(A, target)
print(x)