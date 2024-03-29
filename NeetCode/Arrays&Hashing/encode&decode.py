#encode list of strings to a string and decode string into list of strings

#using just symbols can be uneffective since it could appear in the string
#therefore, we use a number indicating the length of string and after we use a symbol to indicate that this is the end of length and beginning of string

class Solution:
    def encode(self, strs):
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s
        return result

    #my solution might be more memory efficient since i didn't use j
    #he should also be able to just use i (but i didn't verify)
    def decode(self, str):
        result = []
        i = 0
        while i < len(str):
            length = ""
            while str[i] != "#":
                length += str[i]
                i += 1
            result.append(str[i + 1: i + 1 + int(length)]) # i is at # right now, remember: end is NOT inclusive!!!
            i += 1 + int(length)
        return result

    def decode_neetcode(self, str):
        res, i = [], 0

        while i< len(str):
            j = i
            while str[j] != '#':
                j += 1
            length = int(str[i:j])
            res.append(str[j+1: j+1+length])
            i = j+1+length
        
        return res


#be careful with the increment! remmeber str[start:end] end is not inclusive 
#also increment to the next character to check not the end of string!
s = Solution()
a = ["das", "ekgf", "Fdsf"]
code = s.encode(a)
print(code)
print(s.decode(code))