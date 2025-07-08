# Problem: Given a 0-indexed integer array nums, find the leftmost middleIndex 
#          (i.e., the smallest amongst all the possible ones).
#          A middleIndex is an index where nums[0] + nums[1] + ... + nums[middleIndex-1] == 
#          nums[middleIndex+1] + nums[middleIndex+2] + ... + nums[nums.length-1].
#          If middleIndex == 0, the left side sum is considered to be 0. Similarly, 
#          if middleIndex == nums.length - 1, the right side sum is considered to be 0.
#          Return the leftmost middleIndex that satisfies the condition, 
#          or -1 if there is no such index.

class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        
        # Get the sum first for calculating
        s = sum(nums)

        # Keep track of total so far and index
        ind, total = 0, 0

        # Loop through all nums
        while ind < len(nums):

            # Check if left side is equal to right side
            if total == s - total - nums[ind]:
                return ind
            
            # Increase total
            total += nums[ind]
            ind += 1
        
        # Answer wasn't found
        return -1
