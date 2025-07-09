# Problem: Given an array of positive integers nums and a positive integer target, 
#          return the minimal length of a whose sum is greater than or equal to target. 
#          If there is no such subarray, return 0 instead.

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        # Minimum subarray length
        minLen = len(nums) + 1

        # Index for moving left side of "window"
        l = 0

        # Sum of the "window"
        s = 0

        # Loop thorough each value
        for r in range(len(nums)):
            
            # Expand the right side of the "window"
            s += nums[r]

            # Move the left side of the "window" until sum < target
            while s >= target:

                # Check if new "window" size is lower than minLen
                if r - l + 1 < minLen:
                    minLen = r - l + 1
                
                # Update "window" values
                s -= nums[l]
                l += 1

        # Return minLen if a smaller "window" was found, otherwise 0
        return minLen if minLen != len(nums) + 1 else 0
