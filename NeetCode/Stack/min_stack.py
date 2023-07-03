class MinStack:
    #14 min but couldn't get min stack in constant time
    #in the right direction of thought but didn't implement it properly

    
    def __init__(self):
        self.stack = []

    def push(self, val):
        #PREVIOUS MISTAKE: I i made a variable currmin and check curr min instead of the stack for the if condition
        #this didn't work because when currmin = 0 it passes the not condition (since 1 is true and 0 is false)
        #the example underneath shows that I can still work with a currmin, but i would have to state the condition as currmin is None
        if not self.stack: 
            self.stack.append([val, val])
        else:
            currmin = min(self.stack[-1][1], val)
            self.stack.append([val, currmin])
        #this works because we are stacking up values and the min number at that current stack
        #when the stack changes, it can have a different min or not. they will all be saved
        
    #if we want to do it the way with curr min
    # def push_withcurrmin(self, val):
    #     if self.currmin is None or not self.stack: #need to check the stack is not empty or else it will go out of range when using min operation under
    #         self.currmin = val
    #     else:
    #         self.currmin = min(self.stack[-1][1], val)
    #     #stack stores the value pushed in, and its current min from all current numbers in stack
    #     self.stack.append([val, self.currmin])

    def pop(self):
        """
        :rtype: None
        """
        if self.stack: #not None
            return self.stack.pop()[0] #first value is the number pushed into the stack
        



