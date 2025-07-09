# Problem: Given a string s, reverse the order of characters in each word within a 
#          sentence while still preserving whitespace and initial word order.

class Solution:
    def reverseWords(self, s: str) -> str:

        # Split s up into words
        s = s.split(" ")

        # Stores reversed strings
        s2 = []

        # Loop through each word
        for i in range(len(s)):

            # Add reversed string to s2
            s2.append(s[i][::-1])
        
        # Rejoin words with spaces
        return " ".join(s2)
