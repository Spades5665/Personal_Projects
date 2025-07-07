# Problem: Given an array nums of integers, return how many of them contain an even number of digits.

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        # Loops through each number in nums
        for i in range(len(nums)):

            # Checks if nums[i] has even digits and makes it 1 if true
            nums[i] = 1 if len(str(nums[i])) % 2 == 0 else 0
        
        # Returns the sum of all the numbers with even digits
        return sum(nums)
       