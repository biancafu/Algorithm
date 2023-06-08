#find the fixed number: the number where index  == arr[index] using binary search
#########################################################################################################
#if index > item: left of the index will not satisfy 
#(since even if you subtract the least number it will still -1 and it will be same as index which means we are travelling parallelly)
#same applies to the right side when index < item
#THIS ONLY APPLIES BECAUSE IT IS AN ORDERED LIST WITH NO REPEATED NUMBERS
#only when mid == A[mid] would make the rest of the sides possible to satisfy the condition as well

def find_fixed_num_linear(A):
    for index, item in enumerate(A):
        if index == item:
            return index
    return None

def find_fixed_num(A):
    low = 0
    high = len(A) - 1

    while low <= high:
        mid = (low + high) // 2
        if A[mid] > mid: 
            high = mid - 1
        elif A[mid] < mid:
            low = mid + 1
        elif A[mid] == mid: #else:
            return mid
    return None

# Fixed point is 7:
A1 = [-10, -5, -3, 0, 1, 2, 3, 7]

# Fixed point is 0:
A2 = [0, 2, 5, 8, 17]

# No fixed point. Return "None":
A3 = [-10, -5, 3, 4, 7, 9]
print(A1)
print(find_fixed_num(A1))
print(A2)
print(find_fixed_num(A2))
print(A3)
print(find_fixed_num(A3))