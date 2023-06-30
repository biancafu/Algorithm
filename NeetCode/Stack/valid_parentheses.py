#https://leetcode.com/problems/valid-parentheses/

#11 min (made silly mistake thought stack was FIFO)

def isValid(s):
        stack = [] #LIFO
        pair = {')': '(', '}': '{', ']':'['}

        for char in s:
            #if its open bracket, add them to stack
            if char in pair.values():
                stack.append(char)

            #if its closing bracket, pop one from stack and compare
            else:
                #check len(stack) to make sure it is within range
                if len(stack) > 0 and stack.pop(-1) == pair[char]: #only case where it can continue checking is when stack is not empty and the value matches
                    continue
                return False #all the other cases are False (case 1: stack is empty, case 2: values don't match)
        
        return len(stack) == 0 
                