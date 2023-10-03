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


# Bubble sort in Python

def bubbleSort(array):
    
  # loop to access each array element
  for i in range(len(array)):

    # loop to compare array elements
    for j in range(0, len(array) - i - 1):

      # compare two adjacent elements
      # change > to < to sort in descending order
      if array[j] > array[j + 1]:

        # swapping elements if elements
        # are not in the intended order
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp


data = [-2, 45, 0, 11, -9]

bubbleSort(data)

print('Sorted Array in Ascending Order:')
print(data)