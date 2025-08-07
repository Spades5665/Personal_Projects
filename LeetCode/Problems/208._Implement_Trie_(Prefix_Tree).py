# Problem:
#   A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently 
#   store and retrieve keys in a dataset of strings. There are various applications of this 
#   data structure, such as autocomplete and spellchecker.

# Set up a class for trie nodes
class TrieNode:

    # Initialize
    def __init__(self):

        # Keep track of children and if leaf node
        self.children = {}
        self.is_leaf = False

class Trie:

    # Trie() Initializes the trie object.
    def __init__(self):

        # Root of trie
        self.root = TrieNode()
        
    # insert(word) Inserts the string word into the trie.
    def insert(self, word: str) -> None:

        # Loop through each character in word
        curr = self.root
        for c in word:

            # Check if c exists yet
            if c not in curr.children: curr.children[c] = TrieNode()

            # Move to next children to check
            curr = curr.children[c]
        
        # Update leaf counter
        curr.is_leaf = True

    # search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
    def search(self, word: str) -> bool:

        # Loop through each character in trie
        curr = self.root
        for c in word:

            # Check if c is in children
            if c in curr.children: curr = curr.children[c]

            # If no match, end
            else: return False
        
        # Check if the current node is a leaf
        return curr.is_leaf
        
    # startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, 
    # and false otherwise.
    def startsWith(self, prefix: str) -> bool:
        
        # Loop through each character in trie
        curr = self.root
        for c in prefix:

            # Check if c is in children
            if c in curr.children: curr = curr.children[c]

            # If no match, end
            else: return False
        
        # Prefix was found
        return True
