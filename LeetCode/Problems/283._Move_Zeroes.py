# Problem: Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#          Note that you must do this in-place without making a copy of the array.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        # Keeps track of current index to place values into
        ind = 0

        # Loop through all elements in nums
        for i in range(len(nums)):

            # Check if element is not 0
            if nums[i] != 0:

                # Check if element needs to be moved 
                if i != ind:
                    nums[ind] = nums[i]
                    nums[i] = 0

                # Increment if number found 
                ind += 1
