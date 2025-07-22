# Problem:
#   Given a string s, find the length of the longest without duplicate characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # Hold the max length of a substring found
        max_len = 0

        # Set to hold current substring characters
        arr = set()

        # Left side of window
        left = 0

        # Loop through each character in s
        for right in range(len(s)):
 
            # Remove elements from the array until it is unique
            while s[right] in arr: 
                arr.remove(s[left])
                left += 1

            # Add current element
            arr.add(s[right])

            # Update max length
            max_len = max(max_len, len(arr))

        # Return max length found
        return max_len
