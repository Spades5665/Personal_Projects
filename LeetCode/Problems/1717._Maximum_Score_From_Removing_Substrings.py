# Problem:
#   You are given a string s and two integers x and y. You can perform two types of operations any number of times.
#   Remove substring "ab" and gain x points.
#   For example, when removing "ab" from "cabxbae" it becomes "cxbae".
#   Remove substring "ba" and gain y points.
#   For example, when removing "ba" from "cabxbae" it becomes "cabxe".
#   Return the maximum points you can gain after applying the above operations on s.

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:

        # Get the max string and value
        max_str = "ab" if x >= y else "ba"
        min_str = "ba" if x >= y else "ab"
        max_pts = max(x, y)
        min_pts = min(x, y)

        # Keeps track of the points gathered
        points = 0

        # Loop through each pair of characters in s
        ind = 0
        while ind + 1 < len(s):

            # If max string is found, add to points and remove from s
            if s[ind : ind + 2] == max_str: 
                points += max_pts
                s = s[0 : ind] + s[ind + 2 : len(s)]
                ind -= 1
            
            # String wasn't found, so move to next pair
            else: ind += 1 
        
        # Loop through each pair of characters in s
        ind = 0
        while ind + 1 < len(s):

            # If min string is found, add to points and remove from s
            if s[ind : ind + 2] == min_str: 
                points += min_pts
                s = s[0 : ind] + s[ind + 2 : len(s)]
                ind -= 1

            # String wasn't found, so move to next pair
            else: ind += 1 

        # Return points found
        return points
