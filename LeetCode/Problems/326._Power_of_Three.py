# Problem:
#   Given an integer n, return true if it is a power of three. Otherwise, return false.
#   An integer n is a power of three, if there exists an integer x such that n == 3x.

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        # Check if n has reached 1
        if n == 1: return True

        # Recursively call until 3 is 1
        return self.isPowerOfThree(n / 3) if n > 0 and not n % 3 else False
