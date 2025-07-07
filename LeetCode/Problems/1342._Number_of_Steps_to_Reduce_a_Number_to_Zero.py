# Problem: Given an integer num, return the number of steps to reduce it to zero.
#          In one step, if the current number is even, you have to divide it by 2, 
#          otherwise, you have to subtract 1 from it.

class Solution:
    def numberOfSteps(self, num: int) -> int:
        
        # Keeps track of how many iterations went by
        steps = 0

        # Loops until num is 0
        while num > 0:

            # Applies the logic and increments steps
            num = num / 2 if num % 2 == 0 else num - 1
            steps += 1

        # Returns how many iterations it took
        return steps
