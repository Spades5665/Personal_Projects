# Problem:
#   Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#   You may assume that each input would have exactly one solution, and you may not use the same element twice.
#   You can return the answer in any order.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Create a hashmap to hold values found so far
        hash_map = dict()

        # Loop through each num in nums
        for i in range(len(nums)):

            # Check if the pair of values has been found
            if target - nums[i] in hash_map: return (i, hash_map[target - nums[i]])

            # Add element to hash map
            hash_map[nums[i]] = i
        
        # No pair was found
        return []
