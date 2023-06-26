class Solution(object):
    #this solution is better because it does everything in 1 single loop:
    #we can check if the character is alnum, if not, increment.
    #if both are alnum, then we can compare. and remember to INCREMENT if it passes the comparison
    
    def isPalindrome_better(self, s): #O(n)
        #check if palidrome
        start = 0
        end = len(s) - 1
        while start <= end:
            if not s[start].isalnum():
                start += 1
            elif not s[end].isalnum():
                end -= 1
            elif s[start].lower() != s[end].lower():
                return False
            else:
                start += 1
                end -= 1
        return True
    
    def isPalindrome(self, s): #O(2n) = O(n)
        string = ""
        for char in s:
            if char.isalnum(): #is alphanumeric
                string += char.lower() #add the lower case to the string

        #check if palidrome
        start = 0
        end = len(string) - 1
        while start <= end:
            if string[start] != string[end]:
                return False
            start += 1
            end -= 1
        
        return True
