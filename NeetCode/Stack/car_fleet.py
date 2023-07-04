def carFleet(target, position, speed):
        dv = [[p, s] for p, s in zip(position, speed)]
        stack = []
        # dv.sort()
        # dv.reverse()
        for [p ,s] in sorted(dv)[::-1]:
            stack.append(float(target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)

def carFleet(self, target, pos, speed):
        time = [float(target - p) / s for p, s in sorted(zip(pos, speed))]
        res = cur = 0
        #cur is the largest time
        for t in time[::-1]:
            if t > cur: #when there is a bigger time from behind, that means theres gonna be another fleet (since all the car behind this car will follow its speed and it will never catch up to the one in front)
                res += 1
                cur = t
        return res

#the solution on the upper half appends all time and pops off when we find one that catches up to the stack ahead (we only compare the last two because the third car will never catch up to first)
#this is because they are all in one lane, even if the end car catches up, it will only catch up to the car in front of it
#the solution on the lower half only increment its count when a bigger time occurs because a bigger time means that this is a new fleet and it won't catch up to the previous one
#both solution start by sorting the position and looping in reverse order, this is because we know that the car in front can never be surpass, so we check from the first car to the last 
#(first car is the car starting at largest position), in this case, we only have to see if the cars behind would catch up and become a fleet or not

a = carFleet(10, [6,8], [3,2])
print(a)