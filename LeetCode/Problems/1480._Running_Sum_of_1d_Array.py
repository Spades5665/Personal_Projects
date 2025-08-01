# Problem: Given an array nums. We define a running sum of an array as 
#          runningSum[i] = sum(nums[0]…nums[i]). Return the running sum of nums.

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        # Loops through all indices except the first
        for i in range(1, len(nums)):
            
            # Updates the index by adding the sum of the last index
            nums[i] += nums[i-1]

        # Returns changed array
        return nums
    