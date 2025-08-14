# Problem:
#   Given a positive integer num, return true if num is a perfect square or false otherwise.
#   A perfect square is an integer that is the square of an integer. 
#   In other words, it is the product of some integer with itself.
#   You must not use any built-in library function, such as sqrt.

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        # Binary search for sqrt
        def binarySearchSqrt(l, r, n):

            # Check base cases
            if l > r: return False

            # Get mid and check for good value
            m = (l + r) // 2
            if n / m == float(m): return True

            # Recursively call
            return binarySearchSqrt(l, m - 1, n) if n / m < m else binarySearchSqrt(m + 1, r, n)

        # Return binary search 
        return binarySearchSqrt(1, num, num)
