#25 min all by myself!! O(n)
#the same solution as neetcode!

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