# Problem: Given an array of integers nums and an integer target, 
#          return indices of the two numbers such that they add 
#          up to target.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Loops through all numbers in nums, except the last index to avoid out of bounds errors
        for i in range(len(nums) - 1):

            # Loop through numbers ahead of i to the end
            for j in range(i + 1, len(nums)):

                # Check if the two numbers equal target
                if nums[i] + nums[j] == target:
                    return [i, j]

        # No two indices equaled the target
        return []
    