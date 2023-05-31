#binary search: cut in half (eliminate the half that does not have the target)

def linear_search(data, target): #look through everything
    for index, x in enumerate(data):
        if x == target:
            return True
    return False

def binary_search(data, target): 
    low = 0
    high = len(data)
    
    while low <= high:
        mid = (low + high) // 2 #cutting in half every loop
        if data[mid] == target:
            return True
        elif data[mid] > target: #take the larger half, eliminate smaller half
            low = mid + 1 #increment one to exclude mid since we already checked
        else:
            high = mid - 1 #decrease one to exclude mid since we already checked
    
    return False # no match


