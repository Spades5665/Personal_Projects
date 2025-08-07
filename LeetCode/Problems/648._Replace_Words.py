# Problem:
#   In English, we have a concept called root, which can be followed by some other word to 
#   form another longer word - let's call this word derivative. For example, when the root 
#   "help" is followed by the word "ful", we can form a derivative "helpful".
#   Given a dictionary consisting of many roots and a sentence consisting of words separated 
#   by spaces, replace all the derivatives in the sentence with the root forming it. If a 
#   derivative can be replaced by more than one root, replace it with the root that has the 
#   shortest length.
#   Return the sentence after the replacement.

class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_leaf = False

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:

        # Convert dictionary to trie
        root = TrieNode()

        # Loop through each character in each word in dictionary
        for word in dictionary:

            # Get root
            curr = root

            for c in word:

                # Check if c exists yet
                if c not in curr.children: curr.children[c] = TrieNode()

                # Move to next children to check
                curr = curr.children[c]
            
            # Update leaf counter
            curr.is_leaf = True

        # Loop through each word in sentence
        words = sentence.split(" ")
        for i in range(len(words)):

            # Get root
            curr = root

            # Check characters in word
            word = ""
            for c in words[i]:

                # End if a character isn't found
                if c not in curr.children: break

                # Move counter and add to word
                curr = curr.children[c]
                word += c

                # Check if the end of a prefix is found
                if curr.is_leaf: 
                    words[i] = word
                    break

        # Return new sentence
        return " ".join(words)
