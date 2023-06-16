#count the consonants in the string

def count_consonants(input):
    vowels = "aeiou"
    if len(input) == 0: # or if input == '':
        return 0
    if input[0].lower() not in vowels and input[0].isalpha():
        return 1 + count_consonants(input[1:])
    else:
        return count_consonants(input[1:])
    


input_str = "abc de"
print(input_str)
print(count_consonants(input_str))
input_str = "LuCiDPrograMMiNG"
print(input_str)
print(count_consonants(input_str))