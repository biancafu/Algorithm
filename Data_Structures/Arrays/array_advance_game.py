def array_advance(arr):
    i = 0
    max_reach = 0
    last_index = len(arr) - 1
    while i <= max_reach and max_reach < last_index: #if i > max reach, we can't go further; if max reach >= last_index, we also reached goal
        max_reach = max(max_reach, arr[i] + i)
        i += 1
    
    return max_reach >= last_index


# True: Possible to navigate to last index in A:
# Moves: 1,3,2
A = [3, 3, 1, 0, 2, 0, 1]
print(array_advance(A))

# False: Not possible to navigate to last index in A:
A = [3, 2, 0, 0, 2, 0, 1]
print(array_advance(A))