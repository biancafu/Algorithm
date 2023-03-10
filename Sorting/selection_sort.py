# find min through each iteration
# 2 list: list on left will be sorted, list on right will be unsorted

def selection(list1):
    for i in range(len(list1)-1):
        min = i
        for j in range(i + 1, len(list1)):
            if list1[min] > list1[j]:
                min = j
        list1[i], list1[min] = list1[min], list1[i]
    
    return list1


print(selection([2,9,10,3,6,8,7,6]))