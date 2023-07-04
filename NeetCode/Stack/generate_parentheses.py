#very hard, couldn't solve it.
#solution invloes backstracking(recursion) and stack (optional) with the concept of DFS
#the time complexity ~O(4^n)

def generateParenthesis(n):
        #we create a backtracking solution with 2 parameters: open and close number of brackets
        #because we see that if we want a valid solution, 
        #1. our open bracket number needs to be greater than the close bracket number (open > close)
        #   (not inclusive because if we add another bracket after open == close, close > open which is invalid)
        #2. our open brackets has to be less than n (open < n)
        #3. if we have a matching number of n and open and close, we have a match (n == open == close)
        results = []
        stack = [] #using a stack to keep track of the forming solution (brackets)
        #we can also use a string and pass it as a parameter

        def dfs(open, close):
            #base case
            if open == close == n:
                results.append(''.join(stack))
                return

            #can do elif here but won't
            if open < n:
                stack.append('(') #add the new open bracket to stack
                dfs(open + 1, close)
                stack.pop() #to clean up after (since we are using 1 single stack for all answers)

            #not doing elif because this is where we separate on the tree
            #we can have both open < n and open >= close, it will generate different pattern when continuing
            if open > close:
                stack.append(')')
                dfs(open, close + 1)
                stack.pop()

        dfs(0, 0)
        return results 

a = generateParenthesis(3)
print(a)