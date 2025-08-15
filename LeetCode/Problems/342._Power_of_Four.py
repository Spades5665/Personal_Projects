# Problem:
#   Given an integer n, return true if it is a power of four. Otherwise, return false.
#   An integer n is a power of four, if there exists an integer x such that n == 4x.

class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        # Check if number is divisible by 4
        return False if n < 1 else True if n == 1 else self.isPowerOfFour(n / 4)
