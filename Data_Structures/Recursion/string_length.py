#calculate the length of string

def string_length(input):
    if input == '':
        return 0
    return 1 + string_length(input[1:])


input_str = "LucidProgramming"

print(string_length(input_str))
