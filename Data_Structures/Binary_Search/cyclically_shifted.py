#normal array: [1, 2, 3, 4, 5]
#cyclically shifted array: [2,3,4,5,1], [3,4,5,1,2], [4,5,1,2,3], [5,1,2,3,4]

#find the index that gives lowest number (1 in this case)


#since 1,2,3,4,5 will be a normal array, we know that the first index will NOT be the lowest
#it is cyclically shifted meaning that we can eliminate the half that we know does not contain the lowest number
#how do we know? by comparing the high value to the mid value, if mid > high, this means that the other half started from high + 1 value, so eliminate left side
#if mid < high meaning that this will gradaully increase, so eliminate right side
#IMPORTANT: when mid < high, we look at the left side but still include mid itself because it is possible that mid is the smallest number
#when low == high, this is when we reach the lowest point of the array, therefore we cannot have while loop include the low==high

def find(A):
    low = 0
    high = len(A) - 1

    while low < high:
        mid = (low + high) // 2
        if A[mid] > A[high]:
            low = mid + 1
        else: # A[mid] <= A[high]: not sure if we need <= or just <, tested both got the same answer
            #i don't think we will ever get mid == high, because low != high, which means we will never get to a point where mid == high
            high = mid

    return low

A = [4, 5, 6, 7, 1, 2, 3]
idx = find(A)
print(A[idx])