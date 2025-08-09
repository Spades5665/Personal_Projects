# Problem:
#   Given an integer n, return true if it is a power of two. Otherwise, return false.
#   An integer n is a power of two, if there exists an integer x such that n == 2x.

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        # Count only if there is a single bit in n or make positive
        return n > 0 and n.bit_count() == 1
        