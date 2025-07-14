# Problem: Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

class MinStack:

    # MinStack() initializes the stack object.
    def __init__(self):

        # Holds pairs of values, [int value, min value so far]
        self.stack = []

        # Holds minimum value seen so far
        self.min = None
        
    # push(int val) pushes the element val onto the stack.
    def push(self, val: int) -> None:

        # Figure out current minimum value
        if self.min == None or val < self.min:
            self.min = val

        # Add new value pair to stack
        self.stack.append([val, self.min])

    # pop() removes the element on the top of the stack.
    def pop(self) -> None:

        # Pop element out of stack
        self.stack.pop()

        # Update min value
        self.min = self.stack[len(self.stack) - 1][1] if len(self.stack) else None

    # top() gets the top element of the stack.
    def top(self) -> int:

        # Return value from left side of pair
        return self.stack[len(self.stack) - 1][0]
        
    # getMin() retrieves the minimum element in the stack.
    def getMin(self) -> int:

        # Return minimum from right side of pair
        return self.stack[len(self.stack) - 1][1]
