# Problem: 
#   Write a function that reverses a string. The input string is given as an array of characters s.
#   You must do this by modifying the input array in-place with O(1) extra memory.

class Solution:
    def reverseString(self, s: List[str]) -> None:
        
        # Swap values at l and r
        def swap(l, r):

            # Swap only if the indices are valid
            if l < r:
                 s[l], s[r] = s[r], s[l]
                 swap(l + 1, r - 1)

        # Call on s
        swap(0, len(s) - 1)
