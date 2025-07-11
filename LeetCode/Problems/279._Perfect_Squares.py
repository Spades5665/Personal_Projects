# Problem: Given an integer n, return the least number of perfect square numbers that sum to n.
#          A perfect square is an integer that is the square of an integer; in other words, it 
#          is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect 
#          squares while 3 and 11 are not.

import math

class Solution:
    def numSquares(self, n: int) -> int:
        
        # Generate all squares that could sum to n
        squares = [x ** 2 for x in range(1, int(math.sqrt(n)) + 1)]

        # Create a queue to hold difference values and squares used so far
        sumSquares = deque()
        sumSquares.append([n, 0])

        # Holds values that have been tried before so no repeat math
        tried = {n}

        # Loop while there are still numbers to check
        while len(sumSquares):

            # Get current value and number of squares used to get to it
            num, squaresUsed = sumSquares.popleft()

            # Check if number has made it to 0
            if num == 0:
                return squaresUsed
        
            # Loop through each square 
            for square in squares:

                # Check if the difference stays above 0 and the difference hasn't been tried before
                if num - square not in tried and num - square >= 0:
                    tried.add(num - square)
                    sumSquares.append([num - square, squaresUsed + 1])

        # No number of squares was found
        return -1
