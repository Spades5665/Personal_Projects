# Problem: Given an input string s, reverse the order of the words.
#          A word is defined as a sequence of non-space characters. The words in s will 
#          be separated by at least one space.
#          Return a string of the words in reverse order concatenated by a single space.
#          Note that s may contain leading or trailing spaces or multiple spaces between
#          two words. The returned string should only have a single space separating the 
#          words. Do not include any extra spaces.

class Solution:
    def reverseWords(self, s: str) -> str:
        
        # Prepare string by removing extra spaces and splitting
        s = s.strip()
        s = s.split(" ")

        # Holds reversed string
        rev = ""

        # Loop through each word in s
        for i in range(len(s) - 1, -1, -1):

            # Check if the current word isn't empty
            if s[i] != "":
                rev += s[i]

                # Adds a space between words
                if i != 0:
                    rev += " "

        # Return reversed string
        return rev
