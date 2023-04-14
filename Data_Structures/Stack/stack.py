class Stack():
    #stack is LIFO
    #end of list will be the top of stack
    def __init__(self):
        self.items = [] #create an empty list as our stack
    
    def push(self, item):
        self.items.append(item) #append item to the end of list which is top of stack
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop() #pop the last item of list which is first item of stack
    
    def is_empty(self): 
        return len(self.items) == 0
    
    def peek(self): #returns the first item of stack
        if not self.is_empty():
            return self.items[-1]
    
    def get_stack(self):
        return self.items