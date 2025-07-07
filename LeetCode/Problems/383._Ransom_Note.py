# Problem: Given two strings ransomNote and magazine, return true 
#          if ransomNote can be constructed by using the letters 
#          from magazine and false otherwise.
#          Each letter in magazine can only be used once in ransomNote.

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        # Loop through each letter in ransomNote
        for letter in ransomNote:

            # Check if magazine has the letter
            if letter in magazine:

                # Remove one letter from magazine
                magazine = magazine.replace(letter, "", 1)
            
            # No match in magazine
            else:
                return False

        # All letters got matched
        return True 
 