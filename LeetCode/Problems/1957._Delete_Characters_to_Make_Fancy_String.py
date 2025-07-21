# Problem: 
#   A fancy string is a string where no three consecutive characters are equal.
#   Given a string s, delete the minimum possible number of characters from s to make it fancy.
#   Return the final string after the deletion. It can be shown that the answer will always be unique.

class Solution:
    def makeFancyString(self, s: str) -> str:

        # Grab the first 2 characters
        fancy_str = s[:2]

        # Loop through th rest of the letters in s, adding to fancy_str if it is not the same as the last 2 characters
        for i in range(2, len(s)):
            if s[i] != s[i - 1] or s[i] != s[i - 2]: fancy_str += s[i]

        # Return final string
        return fancy_str
