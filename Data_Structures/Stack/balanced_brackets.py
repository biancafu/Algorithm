from stack import Stack

#input: list of brackets []
#output true or false
#function to check if brackets match
#iterate through the list
#check bracket
    #if opening brackets, put in a stack
    #if closing brackets, pop the stack and check if it matches

def is_matched(element1, element2):
    if (element1 == "[" and element2 == "]") or (element1 == "(" and element2 == ")") or (element1 == "{" and element2 == "}"):
        return True
    return False
        

def is_balanced(list1):
    #create a stack
    s = Stack()

    #iterate through the list
    for item in list1:
        #if opening brackets, put in a stack
        if item in "[{(":
            s.push(item)

        #if closing brackets
        elif s.is_empty(): #if list is empty but there is a closing bracket
            print(s.items)
            return False
        
        elif not s.is_empty(): #when stack not empty, pop from stack to check if the closing bracket matches
            if not is_matched(s.pop(), item): #if bracket does not match, return False
                return False
                
    
    if s.is_empty():
        return True
    else: 
        return False



print("String : (((({})))) Balanced or not?")
print(is_balanced("(((({}))))"))

print("String : [][]]] Balanced or not?")
print(is_balanced("[][]]]"))

print("String : [][] Balanced or not?")
print(is_balanced("[][]"))



