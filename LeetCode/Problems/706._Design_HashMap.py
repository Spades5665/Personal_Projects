# Problem:
#   Design a HashMap without using any built-in hash table libraries    

class MyHashMap:

    # MyHashMap() initializes the object with an empty map
    def __init__(self):
        self.n = 1000003
        self.hash_map = [None] * self.n
        
    # put(int key, int value) inserts a (key, value) pair into the HashMap. 
    # If the key already exists in the map, update the corresponding value
    def put(self, key: int, value: int) -> None:
        self.hash_map[key % self.n] = [key, value]
        
    # get(int key) returns the value to which the specified key is mapped, 
    # or -1 if this map contains no mapping for the key
    def get(self, key: int) -> int:
        return self.hash_map[key % self.n][1] if self.hash_map[key % self.n] != None else -1
        
    # remove(key) removes the key and its corresponding value if the map 
    # contains the mapping for the key
    def remove(self, key: int) -> None:
        self.hash_map[key % self.n] = None
