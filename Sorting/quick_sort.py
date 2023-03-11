#pick a pivot number (a number to compare)
#sort all numbers in 2 lists: less than pivot, more than pivot
#continue to sort in sub sequence
#recursion to continue sort the sub sequences until it breaks from having length <= 1


# def quick(list1):
#     if len(list1) <= 1:
#         return list1
#     else: 
#         pivot = list1.pop()

#     items_greater = []
#     items_lower = []

#     for item in list1:
#         if pivot < item:
#             items_greater.append(item)
#         else:
#             items_lower.append(item)
    
#     return quick(items_lower) + [pivot] + quick(items_greater)

#O(nlogn) solution
def partion(start, end, list1): #find the position of pivot
    pivot = list1[start]
    i = start + 1 # should i add 1 or not? before it gave me bug for not adding now its not anymore
    j = end

    while i < j: #when i>j, they don't swap places anymore
        while list1[i] <= pivot: #keep incrementing until list1[i] > pivot, find greater than pivot
            i += 1
    
        while list1[j] > pivot: #keep incrementing until list1[j] < pivot
            j -= 1
        
        if i < j:
            list1[i], list1[j] = list1[j], list1[i]
    
    list1[j], list1[start] = list1[start], list1[j]
    print('pivot',pivot)
    print('j',j)
    return j

def quick(start, end, list1):
    if start >= end:
        return
    j = partion(start, end, list1)
    quick(start, j-1, list1)
    quick(j+1, end, list1)




data = [7,9,10,3,6,8,2,6,33]
quick(0, len(data) - 1, data)
print(data)