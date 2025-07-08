# Problem: Given an integer array nums, return the third distinct maximum number in this array. 
#          If the third maximum does not exist, return the maximum number.

class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        # Set the three maxes        
        max1, max2, max3 = nums[0], None, None
        
        # Loop through all nums
        for num in nums:

            # Check if num is larger than max1, update lower maxs if true
            if num > max1:
                max3 = max2
                max2 = max1
                max1 = num
            
            # Check if num is larger than max2, update lower maxs if true
            elif num != max1 and (max2 == None or num > max2):
                max3 = max2
                max2 = num
            
            # Check if num is larger than max3 and update
            elif num != max1 and num != max2 and (max3 == None or num > max3):
                max3 = num
        
        # Return max1 if max3 doesnt exist
        return max1 if max3 == None else max3
