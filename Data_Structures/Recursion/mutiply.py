#mutiply the given numbers using recursion

def mutiply(x, y):
    if y > x: #to minimize total number of recursive looping
        return mutiply(y, x)
    if y == 0:
        return 0
    return x + mutiply(x, y - 1)


print(mutiply(3,2))