# Problem: 
#   A school is trying to take an annual photo of all the students. The students are asked 
#   to stand in a single file line in non-decreasing order by height. Let this ordering be 
#   represented by the integer array expected where expected[i] is the expected height of 
#   the ith student in line.
#   You are given an integer array heights representing the current order that the students 
#   are standing in. Each heights[i] is the height of the ith student in line (0-indexed).
#   Return the number of indices where heights[i] != expected[i].

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        # Get sorted version of heights
        expected = heights[:]
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(expected) - 1):
                if expected[i] > expected[i + 1]: 
                    expected[i], expected[i + 1] = expected[i + 1], expected[i]
                    swapped = True

        # Keep track of how many are in the right spot
        count = 0

        # Loop through each height
        for i in range(len(heights)):

            # Check if height is in the expected spot
            if expected[i] != heights[i]: count += 1
        
        # Return how many failed
        return count
