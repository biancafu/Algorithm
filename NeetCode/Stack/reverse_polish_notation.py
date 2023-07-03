def evalRPN(tokens):
        ''' 13 min to come up with the logic solution but had mistakes: 
            - used .isnumeric but it didn't work because (i guess) the tokens were a string object, and isnumeric only works with unicode 
            - forgot to convert the strings to integers when storing
            - didn't read the requirement carefully: not knowing we are rounding towards zero and also didn't how to do that
        '''
        
        #from understanding the question, we have a pattern of one operant and then 2 numbers
        #so we can stack up the numbers and pop 2 when we find an operand
        stack = []
        for c in tokens:
            if c in ['/', '*', '+', '-']:
                num2 = (stack.pop()) #reading from left to right, so first number out is the second one
                num1 = (stack.pop())
                if c == '/':
                    result = int(float(num1) / num2) #VERY IMPORTANT!! we truncates toward zero.
                    #in python 3 we can simply do int(a/b)
                    #but in python 2, we need to do int(float(a)/b)
                elif c == '*':
                    result = num1 * num2
                elif c == '+':
                    result = num1 + num2
                elif c == '-':
                    result = num1 - num2
                stack.append(result)
            else:
                stack.append(int(c))
        
        return stack[-1] #in the end there should only be 1 number left which is the final result

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
a = evalRPN(tokens)
print(a)