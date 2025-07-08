# Problem: Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
#          Return any array that satisfies this condition.

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:

        # Indices to keep track of where to swap
        lInd, rInd = 0, len(nums) - 1

        # Loop through nums until enough have been scanned
        while lInd != rInd:

            # Swap if an element is odd
            if nums[lInd] % 2 == 1:
                temp = nums[lInd]
                nums[lInd] = nums[rInd]
                nums[rInd] = temp
                rInd -= 1
            
            # Move counter up if even
            else:
                lInd += 1
        
        # Return finished array
        return nums
