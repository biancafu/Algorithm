class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        if not self.stack:
            self.stack.append((val, val))
        else:
            mn = min(self.stack[-1][1], val)
            self.stack.append((val, mn))

    def pop(self):
        if self.stack:
            self.stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1][0]
        return 0

    def getMin(self):
        if self.stack:
            return self.stack[-1][1]
        return 0