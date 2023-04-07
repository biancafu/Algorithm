#Assign tasks to workers so that the time it takes to complete all the tasks is minimized given a count of workers 
#and an array where each element indicates the duration of a task.
#We wish to determine the optimal way in which to assign tasks to some workers. 
#Each worker must work on exactly two tasks. Tasks are independent of each other, and each task takes a certain amount of time.

#fastest would be the average/mean of all hours
def optimal(arr):
    arr = sorted(arr)
    for i in range(0, len(arr) // 2): # //2 doesn't work on odd number, but since tasks comes in pairs so we can use it
        print(arr[i], arr[~i])


A = [6, 3, 2, 7, 5, 5]
optimal(A)