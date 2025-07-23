# Problem:
#   Implement the RandomizedSet class
#   You must implement the functions of the class such that each function works in average O(1) time complexity.

import random

class RandomizedSet:

    # RandomizedSet() Initializes the RandomizedSet object.
    def __init__(self):
        self.hash_set = dict()
        self.arr = []
        self.size = 0
        
    # insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
    def insert(self, val: int) -> bool:
        if val not in self.hash_set: 
            self.hash_set[val] = self.size
            self.arr.append(val)
            self.size += 1
            return True
        
        return False
        
    # remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
    def remove(self, val: int) -> bool:
        if val in self.hash_set: 
            index = self.hash_set.pop(val)
            
            pop_val = self.arr.pop()
            if index < self.size - 1:
                self.arr[index] = pop_val
                self.hash_set[pop_val] = index
                
            self.size -= 1
            return True
        
        return False

    # getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element 
    # exists when this method is called). Each element must have the same probability of being returned.
    def getRandom(self) -> int:
        return self.arr[random.randint(0, len(self.arr) - 1)]
