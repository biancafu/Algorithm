#sort each number at a time
#left to the current number will be sorted, right will be unsorted
#for each iteration, compare the current with left ones and shift until its at the correct spot

def insertion(list1):
    for i in range(1,len(list1)):
        current = i

        for j in range(i - 1, 0, -1):
            if list1[j] > list1[current]:
                list1[current], list1[j] = list1[j], list1[current]
                current = j
            else: 
                continue
        
        #or
        #while list1[i-1] > list1[current] and i>0:
            #list1[current], list1[j] = list1[j], list1[current]
            #i -= 1 
    return list1

print(insertion([1,8,4,6,7,22,5]))


