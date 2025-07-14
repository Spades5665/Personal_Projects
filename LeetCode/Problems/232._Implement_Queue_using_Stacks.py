# Problem: Implement a first in first out (FIFO) queue using only two stacks. The implemented queue 
#          should support all the functions of a normal queue (push, peek, pop, and empty).

class MyQueue:

    # Initializes two stacks
    def __init__(self):
        self.inStack = deque()
        self.outStack = deque()
        
    # push(int x) Pushes element x to the back of the queue.
    def push(self, x: int) -> None:
        self.inStack.append(x) 
        
    # pop() Removes the element from the front of the queue and returns it.
    def pop(self) -> int:

        # Stores the reverse of inStack into outStack if outStack is empty
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        
        return self.outStack.pop()

    # peek() Returns the element at the front of the queue.
    def peek(self) -> int:

        # Stores the reverse of inStack into outStack if outStack is empty
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        
        return self.outStack[-1]
        
    # empty() Returns true if the queue is empty, false otherwise.
    def empty(self) -> bool:
        return not self.inStack and not self.outStack
