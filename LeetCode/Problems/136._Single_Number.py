# Problem: 
#   Given a non-empty array of integers nums, every element appears twice except for one. 
#   Find that single one.
#   You must implement a solution with a linear runtime complexity and use only constant extra space.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        # Holds the value of the single number
        single = 0

        # Loop through each number using xor bitwise operation
        for num in nums: single ^= num

        # Return single number
        return single
