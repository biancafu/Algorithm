#25 min all by myself!! O(n)
#the same solution as neetcode!
'''
we initialize the result array with zeros, so we only edit the ones we find a match (higher than the temperature recorded)
this would work if we store in the stack both the temperature and the index 
because we would need the index to modify data at the same location for the result array and 
'''
def dailyTemperatures(temperatures):
        stack = []
        result = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                    result[stack[-1][1]] = (i - stack[-1][1])
                    stack.pop()
            stack.append([temp, i])
        
        return result


a = dailyTemperatures([73,74,75,71,69,72,76,73])
print(a)