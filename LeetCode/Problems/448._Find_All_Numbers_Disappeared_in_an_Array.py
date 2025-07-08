# Problem: Given an array nums of n integers where nums[i] is in the range [1, n], 
#          return an array of all the integers in the range [1, n] that do not appear in nums.

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        # Generate all the possible numbers as placeholders
        allNums = [0] * len(nums)

        # Loop through all nums and record which ones are found
        for num in nums:
            allNums[num - 1] += 1
        
        # Loop through all placeholders in allNums
        for i in range(len(nums) - 1, -1, -1):

            # Check if the placeholder was found and remove if so
            if allNums[i] > 0:
                allNums.pop(i)
            
            # Change the value from 0 to the right value
            else:
                allNums[i] = i + 1
        
        # Now only contains the numbers not found in nums
        return allNums
