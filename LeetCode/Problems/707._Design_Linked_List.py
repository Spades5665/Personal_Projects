# Problem: 
#   Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
#   A node in a singly linked list should have two attributes: val and next. val is the value of the 
#   current node, and next is a pointer/reference to the next node.
#   If you want to use the doubly linked list, you will need one more attribute prev to indicate the
#   previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

class Node:
   def __init__(self, val = None):
      self.val = val
      self.next = None
      self.prev = None

class MyLinkedList:

    # MyLinkedList() Initializes the MyLinkedList object.
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    # get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
    def get(self, index: int) -> int: 

        # Check for valid index
        if not 0 <= index < self.size: return -1
        
        # Index is closer to head
        if index <= self.size - index - 1:

            # Loop until index is found
            curr = self.head
            for i in range(index): curr = curr.next

            # Return value at index
            return curr.val
        
        # Index is closer to tail
        else:

            # Loop until index is found
            curr = self.tail
            for i in range(self.size - index - 1): curr = curr.prev

            # Return value at index
            return curr.val
        
    # addAtHead(int val) Add a node of value val before the first element of the linked list. 
    # After the insertion, the new node will be the first node of the linked list.
    def addAtHead(self, val: int) -> None:

        # Create new head node
        new_head = Node(val)
        new_head.next = self.head
        
        # Update current head node and size
        if self.size > 0: self.head.prev = new_head
        self.head = new_head
        self.size += 1

        # Update tail if this is the first node
        if self.size == 1: self.tail = self.head
        
    # addAtTail(int val) Append a node of value val as the last element of the linked list.
    def addAtTail(self, val: int) -> None:

        # Create new tail node
        new_tail = Node(val)
        new_tail.prev = self.tail
        
        # Update current tail node and size
        if self.size > 0: self.tail.next = new_tail
        self.tail = new_tail
        self.size += 1

        # Update head if this is the first node
        if self.size == 1: self.head = self.tail
        
    # addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals 
    # the length of the linked list, the node will be appended to the end of the linked list. If index is greater than 
    # the length, the node will not be inserted.
    def addAtIndex(self, index: int, val: int) -> None:

        # Check if index is valid
        if 0 <= index <= self.size: 
        
            # Add new node at the head
            if index == 0: self.addAtHead(val)

            # Add new node at the tail
            elif index == self.size: self.addAtTail(val)

            # Add new node in the middle:
            else:
                # Start a current node
                curr = None

                # Index is closer to head
                if index <= self.size - index - 1:

                    # Loop until index is found
                    curr = self.head
                    for i in range(index): curr = curr.next
                
                # Index is closer to tail
                else:

                    # Loop until index is found
                    curr = self.tail
                    for i in range(self.size - index - 1): curr = curr.prev
                
                # Create a new node and update its pointers
                new_node = Node(val)
                new_node.next = curr
                new_node.prev = curr.prev

                # Update the node at index and size
                curr.prev.next = new_node
                curr.prev = new_node
                self.size += 1
   
    # deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.
    def deleteAtIndex(self, index: int) -> None:

        # Check if index is valid
        if 0 <= index < self.size: 
        
            # Delete node at the head
            if index == 0: 
                
                # Update head node and size
                self.head = self.head.next
                if self.size > 1: self.head.prev = None
                self.size -= 1

            # Delete node at the tail
            elif index == self.size - 1: 
                
                # Update head node and size
                self.tail = self.tail.prev
                if self.size > 1: self.tail.next = None
                self.size -= 1

            # Delete node in the middle
            else: 
            
                # Start a current node
                curr = None

                # Index is closer to head
                if index <= self.size - index - 1:

                    # Loop until index is found
                    curr = self.head
                    for i in range(index): curr = curr.next
                
                # Index is closer to tail
                else:

                    # Loop until index is found
                    curr = self.tail
                    for i in range(self.size - index - 1): curr = curr.prev

                print(index, self.size, curr.next)
                
                # Delete current node and update its neighbors pointers and size
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
                self.size -= 1
