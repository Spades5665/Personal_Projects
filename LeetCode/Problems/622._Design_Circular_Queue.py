# Problem: Design your implementation of the circular queue. The circular queue is a linear data structure in 
#          which the operations are performed based on FIFO (First In First Out) principle, and the last position 
#          is connected back to the first position to make a circle. It is also called "Ring Buffer".
#          One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. 
#          In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a 
#          space in front of the queue. But using the circular queue, we can use the space to store new values.

class MyCircularQueue:

    # Keep track of current size of queue and its max size
    size, maxSize = 0, 0

    # Keep track of current head and tail positions
    head, tail = 0, 0

    # Queue
    arr = None

#   Initializes the object with the size of the queue to be k, and updates maxSize
    def __init__(self, k: int):
        self.maxSize = k
        self.arr = [None] * self.maxSize

#   enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
    def enQueue(self, value: int) -> bool:
        
        # Checks for empty space in queue
        if self.isFull():
            return False
        else:
            # Update the value at tail and tail itself
            self.arr[self.tail] = value
            self.tail += 1
            self.tail %= self.maxSize

            # Increase size and return
            self.size += 1
            return True

#   deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
    def deQueue(self) -> bool:
        
        # Checks for items in queue
        if self.isEmpty():
            return False
        else:
            # Update the value at head and head itself
            self.arr[self.head] = None
            self.head += 1
            self.head %= self.maxSize

            # Decrease size and return
            self.size -= 1
            return True

#   Int Front() Gets the front item from the queue. If the queue is empty, return -1.
    def Front(self) -> int:
        return self.arr[self.head] if self.arr[self.head] != None else -1

#   Int Rear() Gets the last item from the queue. If the queue is empty, return -1.
    def Rear(self) -> int:
        return self.arr[self.tail - 1] if self.arr[self.tail - 1] != None else -1

#   isEmpty() Checks whether the circular queue is empty or not.
    def isEmpty(self) -> bool:
        return self.size == 0

#   isFull() Checks whether the circular queue is full or not.
    def isFull(self) -> bool:
        return self.size == self.maxSize
