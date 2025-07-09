# Problem: Given two strings needle and haystack, return the index of the first occurrence of 
#          needle in haystack, or -1 if needle is not part of haystack.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        # Loop through substrings of length equal to needle in haystack
        for i in range(len(haystack) - len(needle) + 1):

            # Check if current substring is needle
            if haystack[i:i + len(needle)] == needle:
                return i
        
        # Substring not found
        return -1
