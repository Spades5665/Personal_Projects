# Problem:
#   Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

class Solution:
    def myPow(self, x: float, n: int) -> float:

        # Check base cases
        if x == 0: return 0
        if n < 0:  return 1 / self.myPow(x, -n)
        if n == 0: return 1
        if n == 1: return x
        
        # Recursively call until a base case is reached
        return (x if n % 2 else 1) * self.myPow(x * x, n // 2)
