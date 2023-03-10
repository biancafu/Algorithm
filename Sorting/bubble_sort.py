#sorting 2 at a time until everything is sorted

def bubble(list_a):
    index_length = len(list_a) - 1  # -1 because we can't group 2 for the last index
    sorted = False
    while not sorted:
        sorted = True #stay true if everything is sorted
        for i in range(index_length):
            if list_a[i] > list_a[i + 1]:
                sorted = False
                list_a[i], list_a[i + 1] = list_a[i + 1], list_a[i] #swap number places in list
        
    return list_a

print(bubble([2,3,7,5,8,0,1]))
