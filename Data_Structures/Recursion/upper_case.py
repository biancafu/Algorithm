#Find the upper case in the string

def find_uppercase(input, i = 0):
    if input[i].isupper():
        return input[i]
    if i == len(input) - 1:
        return "No upper case"
    return find_uppercase(input, i + 1)

#or 
    # if i == len(input):
    #     return "No upper case"
    # if input[i].isupper():
    #     return input[i]
    # else:
    #     return find_uppercase(input, i + 1)


input_str_1 = "lucidProgramming"
input_str_2 = "LucidProgramming"
input_str_3 = "lucidprogramming"

print(find_uppercase(input_str_1))
print(find_uppercase(input_str_2))
print(find_uppercase(input_str_3))
