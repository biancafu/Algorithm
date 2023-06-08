#find the fixed number: the number where index  == arr[index] using binary search
A1 = [-10, -5, -3, 0, 1, 2, 3, 7]


def find_fixed_num_linear(A):
    for index, item in enumerate(A):
        if index == item:
            return index
    return None

def find 