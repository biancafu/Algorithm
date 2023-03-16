# Exercise: Convert Decimal Integer to Binary

from stack import Stack

def int_to_binary(number):
    s = Stack()
    binary = ""
    #divide num by 2 until it reaches 0
    while number != 0:
        #for each division, store remainder in stack
        remainder = number % 2
        number //= 2
        s.push(str(remainder))
    #pop up stack to get binary result
    while not s.is_empty():
        binary += s.pop()
    
    return binary

