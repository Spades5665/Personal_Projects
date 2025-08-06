# Problem:
#   The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, 
#   such that each number is the sum of the two preceding ones, starting from 0 and 1. 
#   Given n, calculate F(n).

class Solution:
    def fib(self, n: int) -> int:

        # Create a dictionary to hold past values
        past = {0: 0, 1: 1}

        # Generate the fibonacci numbers up to n
        def genFib(n):

            # Check for value in dictionary
            if n in past: return past[n]

            # Add to dictionary
            val = genFib(n - 1) + genFib(n - 2)
            past[n] = val

            # Return calculated value
            return val
        
        # Call on n
        return genFib(n)       
