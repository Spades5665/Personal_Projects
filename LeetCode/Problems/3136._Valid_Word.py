class Solution:
    def isValid(self, word: str) -> bool:
        
        # Word wasn't long enough or contained not allowed characters
        if len(word) < 3 or not word.isalnum(): return False
        
        # All the vowels for checking
        vowels = ['a', 'e', 'i', 'o', 'u']

        # Flag variables to determine if at least one of each is in word
        vCheck, cCheck = False, False

        # Loop through each character in word
        for c in word:

            # Check for vowels and consonants
            if c.lower() in vowels: vCheck = True
            if not c.lower() in vowels and c.isalpha(): cCheck = True

            # Check if one of each has been found
            if vCheck and cCheck: return True


        # One of each letter type was not found
        return False
