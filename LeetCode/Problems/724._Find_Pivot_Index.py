# Problem: Given an array of integers nums, calculate the pivot index of this array.
#          The pivot index is the index where the sum of all the numbers strictly to the left 
#          of the index is equal to the sum of all the numbers strictly to the index's right.
#          If the index is on the left edge of the array, then the left sum is 0 because there 
#          are no elements to the left. This also applies to the right edge of the array.
#          Return the leftmost pivot index. If no such index exists, return -1.

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
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
