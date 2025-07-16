# Problem: 
#   Design a HashSet without using any built-in hash table libraries

class MyHashSet:

    # Initialize hash set as an array of size n
    def __init__(self):

        # Create size n as a prime to reduce collisions
        self.n = 1000003
        self.hash_set = [None] * self.n

    # add(key) Inserts the value key into the HashSet
    def add(self, key: int) -> None:
        self.hash_set[key % self.n] = key

    # remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing
    def remove(self, key: int) -> None:
        self.hash_set[key % self.n] = None 

    # contains(key) Returns whether the value key exists in the HashSet or not
    def contains(self, key: int) -> bool:
        return self.hash_set[key % self.n] != None
