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

A1 = [1, 4, 9]
A2 = [9, 9, 9]
a = plus_one(A1)
print(a)
print(plus_one(A2))