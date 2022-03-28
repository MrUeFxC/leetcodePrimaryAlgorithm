import math


class MinStack(object):

    def __init__(self):
        self.stack = list()
        self.minStack = [math.inf]

    def push(self, val: int) -> None:
        """
        :type val: int
        :rtype: None
        """
        if self.minStack is not None:
            self.minStack.append(min(self.minStack[-1],val))
        else:
            self.minStack.append(val)
        self.stack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.minStack.pop()
    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]




val1 = 1
val2 = 2
val3 = 3
obj = MinStack()
obj.push(val1)
obj.push(val2)
obj.push(val3)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()