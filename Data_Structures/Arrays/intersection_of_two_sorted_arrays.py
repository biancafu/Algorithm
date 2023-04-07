def intersection_of_two_sorted_arrays(arr1, arr2):
    #easier way, for unsorted arrays, but  higher runtime
    # return list(set(arr1).intersection(arr2))

    #faster runtime way with sorted arrays
    i, j = 0, 0
    intersection = set()
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            intersection.add(arr1[i])
            i += 1
            j += 1
        elif arr1[i] > arr2[j]:
            j += 1
        else: #arr1[i] < arr2[j]
            i += 1
    return list(intersection)

A = [2, 3, 3, 5, 7, 11]
B = [3, 3, 7, 15, 31]
print(intersection_of_two_sorted_arrays(A, B))