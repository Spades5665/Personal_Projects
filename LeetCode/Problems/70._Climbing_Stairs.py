# Problem:
#   You are climbing a staircase. It takes n steps to reach the top.
#   Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    def climbStairs(self, n: int) -> int:
        
        # Dictionary to keep track of steps counted so far
        steps = {-1: 0, 0: 1, 1: 1}

        # Recursively call until all steps have been counted
        def climb(num):

            # Check if n is in steps
            if num in steps: return steps[num]

            # Get the two possible steps and add to steps
            step_sum = climb(num - 1) + climb(num - 2)
            steps[num] = step_sum

            # Return sum
            return step_sum
        
        # Call on first number
        return climb(n)
