# Problem:
#   Design a data structure that supports adding new words and finding if a string matches any previously added string.

# Set up a class for trie nodes
class TrieNode:

    # Initialize
    def __init__(self):

        # Keep track of children and if leaf node
        self.children = {}
        self.is_leaf = False

class WordDictionary:

    # WordDictionary() Initializes the object.
    def __init__(self):
        self.root = TrieNode()
        
    # addWord(word) Adds word to the data structure, it can be matched later.
    def addWord(self, word: str) -> None:
        
        # Loop through each character in word
        curr = self.root
        for c in word:

            # Check if c exists yet
            if c not in curr.children: curr.children[c] = TrieNode()

            # Move to next children to check
            curr = curr.children[c]
        
        # Update leaf counter
        curr.is_leaf = True
        
    # search(word) Returns true if there is any string in the data structure that matches word 
    # or false otherwise. word may contain dots '.' where dots can be matched with any letter.
    def search(self, word: str) -> bool:
        
        # Check for string in trie
        def trieSearch(root, s):
            
            # Get root
            curr = root

            # Loop through each character in s
            for i in range(len(s)):

                # Check for special cases
                if s[i] == '.':

                    # Result of children
                    res = False

                    # Recall on each child
                    for child in curr.children: res = res or trieSearch(curr.children[child], s[i + 1:])
                        
                    # Return result of children
                    return res

                if s[i] not in curr.children: return False
                
                # Advance current
                curr = curr.children[s[i]]

            # Check if word is a leaf node
            return curr.is_leaf    

        # Call on word
        return trieSearch(self.root, word)
