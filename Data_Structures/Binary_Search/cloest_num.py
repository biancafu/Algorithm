#given an ordered list, find the number closest to target

def closest_num(data, target):
    #edge cases
    if len(data) == 0:
        return None
    if len(data) == 1:
        return data[0]
    
    low = 0
    high = len(data) - 1
    min_gap = float('inf')
    closest_num = float('inf')
    while low <= high:
        mid = (low + high) // 2

        #calculate gaps from left and right side of mid
        if mid + 1 < len(data):
            right_gap = abs(data[mid + 1] - target)
        if mid > 0:
            left_gap = abs(target - data[mid - 1])
        
        #update min_gap and closest_num
        if min_gap > left_gap or min_gap > right_gap:
            min_gap = min(left_gap, right_gap)
            if right_gap < left_gap:
                closest_num = data[mid + 1]
            else:
                closest_num = data[mid - 1]
        
        #increment to next half
        if target > data[mid]:
            low = mid + 1
        elif target < data[mid]:
            high = mid - 1
            #if mid = 0, high will become -1, and target was less than data[0 (mid)] which means closest num is data[0]
            if high < 0:
                return data[mid]
        else: #target == data[mid]
            return data[mid] #target
        
    return closest_num

A1 = [1, 2, 4, 5, 6, 6, 8, 9]
A2 = [2, 5, 6, 7, 8, 8, 9]

print(closest_num(A1, 11))
print(closest_num(A2, 4)) 