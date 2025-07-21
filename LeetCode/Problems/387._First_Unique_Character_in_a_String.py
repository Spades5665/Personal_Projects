# Problem:
#   Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

class Solution:
    def firstUniqChar(self, s: str) -> int:

        # Create hash_table to hold characters and their indices
        hash_table = dict()
        
        # Loop through each character in s
        for i in range(len(s)):

            # Check if current character has been added yet, if not set its value to its index
            if s[i] not in hash_table:
                hash_table[s[i]] = i
            
            # If the character is found again, set its value to len(s)
            else:
                hash_table[s[i]] = len(s)
        
        # Loop through each key in hash table until a value within the length of s is found
        for c in hash_table:
            if hash_table[c] < len(s): return hash_table[c]
        
        # No such character was found
        return -1
