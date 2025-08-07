# Problem:
#   Design a map that allows you to do the following:
#   Maps a string key to a given value.
#   Returns the sum of the values that have a key with a prefix equal to a given string.

class TrieNode():
    def __init__(self):
        self.children = {}
        self.score = 0

class MapSum:

    # MapSum() Initializes the MapSum object.
    def __init__(self):

        # Set root and dictionary to hold word values
        self.root = TrieNode()
        self.word_vals = defaultdict(int)
        
    # insert(String key, int val) Inserts the key-val pair into the map. 
    # If the key already existed, the original key-value pair will be overridden to the new one.
    def insert(self, key: str, val: int) -> None:

        # Calculate how much to add to each prefix
        pre_sum = val - self.word_vals[key]

        # Loop through each prefix character in key
        curr = self.root
        for c in key:
            
            # Check if next char exists in tree
            if c not in curr.children: curr.children[c] = TrieNode()

            # Update value
            curr = curr.children[c]
            curr.score += pre_sum
        
        # Update value
        self.word_vals[key] = val

    # sum(String prefix) Returns the sum of all the pairs' value whose key starts with the prefix.
    def sum(self, prefix: str) -> int:
        
        # Search for prefix
        curr = self.root
        for c in prefix:

            # Check for character
            if c in curr.children: curr = curr.children[c]
            
            # Prefix not found
            else: return 0
        
        # Return score at prefix
        return curr.score
