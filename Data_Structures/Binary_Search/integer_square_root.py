#given a number, find the largest integer where its square is less than or equal than the given number
import math

#my way
def find_largest_square(num):
    return int(math.sqrt(num))

def find_largest_square_binarysearch(num):
    low = 0
    high = num

    while low <= high:
        mid = (low + high) // 2
        square = mid * mid
        if square > num:
            high = mid - 1
        elif square < num: #solution has square <= num: because even if square == num, 
            #we can get same answer if we keep eliminating the smaller half until low > high (and high will have largest integer) 
            low = mid + 1
        else: #square == num
            return mid
    return high
        

#solution
# def integer_square_root(k):
    
#     low = 0
#     high = k 

#     while low <= high:
#         mid = (low + high) // 2
#         mid_squared = mid * mid

#         if mid_squared <= k:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return high

k = 300
print(find_largest_square(k))
print(find_largest_square_binarysearch(k))