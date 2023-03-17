#Reversing string using stack
from stack import Stack

def reverse_string(string1):
    s = Stack()
    reverse = ""
    for char in string1:
        s.push(char)

    while not s.is_empty():
        reverse += s.pop()
    
    return reverse

input_str = "!evitacudE ot emocleW"
print(reverse_string(input_str))
