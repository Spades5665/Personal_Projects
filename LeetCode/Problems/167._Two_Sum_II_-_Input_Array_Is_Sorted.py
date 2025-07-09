# Problem: Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
#          find two numbers such that they add up to a specific target number. Let these two numbers 
#          be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
#          Return the indices of the two numbers, index1 and index2, added by one as an integer array 
#          [index1, index2] of length 2.
#          The tests are generated such that there is exactly one solution. You may not use the same element twice.
#          Your solution must use only constant extra space.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # Index pointers
        left, right = 0, len(numbers) - 1
        
        # Loop while there are still numbers to check
        while left != right:

            # Add the two
            s = numbers[left] + numbers[right]
            
            # Check if sum is the target value
            if s == target:
                return [left + 1, right + 1]
            
            # If less than target, increment left to the next number (>= current)
            elif s < target:
                left += 1
            
            # If greater than target, decrement right to the next number (>= current)
            else:
                right -= 1
