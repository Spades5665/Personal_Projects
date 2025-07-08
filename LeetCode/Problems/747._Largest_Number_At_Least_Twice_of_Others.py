# Problem: You are given an integer array nums where the largest integer is unique.
#          Determine whether the largest element in the array is at least twice as 
#          much as every other number in the array. If it is, return the index of 
#          the largest element, or return -1 otherwise.

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:

        # Keeps track of max index
        maxInd = 0

        # Holds the top 2 unique maxs
        max1, max2 = nums[0], None

        # Loop through each num
        for i in range(len(nums)):

            # Check for new max
            if nums[i] > max1:
                max2 = max1
                max1 = nums[i]
                maxInd = i
            
            # Check if num is larger than max2 and is unique
            elif nums[i] != max1 and (max2 == None or nums[i] > max2):
                max2 = nums[i]
        
        # Check if max1 is at least twice as large as max2
        if max1 >= max2 * 2:
            return maxInd

        # Failed to be larger
        return -1
