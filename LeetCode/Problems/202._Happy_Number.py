# Problem:
#   Write an algorithm to determine if a number n is happy.
#   A happy number is a number defined by the following process:
#   Starting with any positive integer, replace the number by the sum of the squares of its digits.
#   Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
#   Those numbers for which this process ends in 1 are happy.
#   Return true if n is a happy number, and false if not.

class Solution:
    def isHappy(self, n: int) -> bool:

        # Create a set to keep track of numbers tried
        tried_nums = {n}

        # Loop until n is 1
        while n != 1:

            # Reset n 
            num = 0

            # Square and sum up all of n's digits
            for digit in str(n): num += int(digit) ** 2

            # Check if n has been tried before, if not, add n to set
            if num in tried_nums: return False
            else: 
                tried_nums.add(num)
                n = num 
        
        # An n value of 1 was found
        return True
