# Problem: 
#   A word is considered valid if:
#   It contains a minimum of 3 characters.
#   It contains only digits (0-9), and English letters (uppercase and lowercase).
#   It includes at least one vowel.
#   It includes at least one consonant.
#   You are given a string word.
#   Return true if word is valid, otherwise, return false.
# Notes:
#   'a', 'e', 'i', 'o', 'u', and their uppercases are vowels.
#   A consonant is an English letter that is not a vowel.

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
