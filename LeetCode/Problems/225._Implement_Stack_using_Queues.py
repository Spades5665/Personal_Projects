# Problem: Implement a last-in-first-out (LIFO) stack using only two queues. The implemented 
#          stack should support all the functions of a normal stack (push, top, pop, and empty).
# Challenge: Can you do it with only one queue?

class MyStack:

    # Initializes the queue
    def __init__(self):
        self.queue = deque()

    # push(int x) Pushes element x to the top of the stack.
    def push(self, x: int) -> None:
        self.queue.append(x)
        
    # pop() Removes the element on the top of the stack and returns it.
    def pop(self) -> int:

        # Shifts the elements in queue one to the right, putting the "top" at the front
        for _ in range(len(self.queue) - 1): self.queue.append(self.queue.popleft())

        return self.queue.popleft()
        
    # top() Returns the element on the top of the stack.
    def top(self) -> int:
        
        # Shifts the elements in queue one to the right, putting the "top" at the front
        for _ in range(len(self.queue) - 1): self.queue.append(self.queue.popleft())

        # Save value at the top, then shift it back to correct order
        val = self.queue.popleft()
        self.queue.append(val)
        return val
        
    # empty() Returns true if the stack is empty, false otherwise.
    def empty(self) -> bool:
        return not self.queue
