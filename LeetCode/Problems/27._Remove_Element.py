# Problem: Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be 
#          changed. Then return the number of elements in nums which are not equal to val.
#          Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
#          Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining 
#          elements of nums are not important as well as the size of nums.
#          Return k.

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        # Index tracker
        k = 0
        
        # Loop until each element has been checked
        while k < len(nums):
            
            # Check if element is equal to val
            if nums[k] == val:
                nums.remove(nums[k])
            else:
                k += 1
        
        # Return resulting index count
        return k
