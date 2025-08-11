# Problem:
#   Given an array nums with n objects colored red, white, or blue, sort them in-place 
#   so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
#   We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
#   You must solve this problem without using the library's sort function.

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        
        # Setup pointers for where to place 0's and 2's
        l, r = 0, len(nums) - 1

        # Loop through each number
        i = 0
        while i <= r:

            # Get value for swapping
            temp = nums[i]

            # Check for cases to swap
            if nums[i] == 2:
                nums[i] = nums[r]
                nums[r] = temp
                r -= 1
                continue
            elif nums[i] == 0:
                nums[i] = nums[l]
                nums[l] = temp
                l += 1
            
            # Increment i
            i += 1
