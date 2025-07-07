# Problem: Given a binary array nums, return the maximum number of consecutive 1's in the array.

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        # Holds max length of 1's found so far
        maxLength = 0

        # Counts current string of 1's
        count = 0

        # Loops through all numbers in nums
        for num in nums:

            # Checks if num is a 0, if not, increase count and update max
            if num == 0:
                count = 0
            else:
                count += 1
                maxLength = count if count > maxLength else maxLength
            
        # Returns max string of 1's
        return maxLength
