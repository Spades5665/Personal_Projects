# Problem: Given an integer array nums sorted in non-decreasing order, 
#          return an array of the squares of each number sorted in 
#          non-decreasing order.

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        # Stores sorted squared values
        squared = []

        # Index values to keep track of positions from left and right
        left = 0
        right = len(nums) - 1
        
        # Loops until the index values overlap, indicating all elements have been squared
        while left <= right:

            # Checks if the value on the right side is greater or equal to the element at the left side
            if abs(nums[right]) >= abs(nums[left]):
                squared.insert(0, nums[right] ** 2)
                right -= 1
            
            # Checks the opposite
            else:
                squared.insert(0, nums[left] ** 2)
                left += 1
        
        # Returns sorted, squared array
        return squared
        