# Problem:
#   Given an integer array nums, return true if any value appears at least
#   twice in the array, and return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # Creates a set or nums then checks if they have different lengths
        return len(nums) != len(set(nums))
