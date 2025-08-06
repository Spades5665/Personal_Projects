# Problem:
#   Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

class Solution:
    def myPow(self, x: float, n: int) -> float:

        # Create a dictionary for calculating values
        pows = {1: x}

        # Generate pow recursively
        def genPow(num, exp):
            # Base cases
            if x == 0: return 0
            elif exp < 0: return 1 / genPow(num, -exp)
            elif exp == 0: return 1
            elif exp == 1: return num

            # Calculate and store
            if exp in pows: return pows[exp]
            new_val = genPow(num, exp // 2) * genPow(num, exp // 2) * (num if exp % 2 == 1 else 1) 
            pows[exp] = new_val

            # Call recursively
            return new_val

        # Call on given num
        return genPow(x, n)
