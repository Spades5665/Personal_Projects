# Problem:
#   Given a non-negative integer x, return the square root of x rounded down to the nearest integer. 
#   The returned integer should be non-negative as well.
#   You must not use any built-in exponent function or operator.

class Solution:
    def mySqrt(self, x: int) -> int:

        # Binary search
        def binarySearchSQRT(l, r, val):
        
            # Check if array is valid
            if l > r: return r

            # Check midpoint
            m = (l + r) // 2
            if val // m == m: return m

            # Search next location
            return binarySearchSQRT(l, m - 1, val) if val // m < m else binarySearchSQRT(m + 1, r, val)

        # Call binary search
        return binarySearchSQRT(1, x, x)
