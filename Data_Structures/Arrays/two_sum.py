def two_sum_hash_table(arr, target): 
    #only 2 numbers, so i could do this
    #time O(n), space O(n)
    pairs = dict()
    for i in range(0, len(arr)):
        if arr[i] in pairs:
            return True
        pairs[target - arr[i]] = arr[i]
    
    return False

def two_sum(arr, target):
    #can do this becuz its sorted and pairs
    i, j = 0, len(arr) - 1
    while i < j: #not <= becuz if i == j, they r on same number
        sum = arr[i] + arr[j]
        if sum == target:
            return True
        elif sum > target:
            j -= 1
        else: #sum < target
            i += 1
    return False


A = [-2, 1, 2, 4, 7, 11]
target = 13

print(two_sum_hash_table(A, target))
print(two_sum(A, target))