def plus_one(arr):
    #easiest
    # s = ''.join(map(str, arr))
    # return int(s) + 1

    #logic
    #my way: works with plus more than 1
    i = len(arr) - 1
    carry = 0
    arr[i] += 1
    while i >= 0:
        sum = arr[i] + carry
        if sum >= 10:
             carry = sum // 10
             sum %= 10
        else:
            carry = 0
        arr[i] = sum
        i -= 1
    
    if carry > 0:
        arr.insert(0, carry)
    return arr

#can do it this way cuz it adds one at a time only
def plus_one_solution(arr):
    arr[-1] += 1
    for i in (range(len(arr) - 1, 0, -1)): #or reversed(range(1, len(arr)))
        if arr[i] != 10: #no need to continue loop through
            break

        arr[i-1] += 1
        arr[i] = 0
    
    if arr[0] == 10:
        arr[0] = 1
        arr.append(0)
    
    return arr

A1 = [1, 4, 9]
A2 = [9, 9, 9]
# print(plus_one(A1))
# print(plus_one(A2))
print(plus_one_solution(A1))
print(plus_one_solution(A2))