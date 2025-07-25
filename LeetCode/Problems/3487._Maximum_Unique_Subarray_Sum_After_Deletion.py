# Problem:
#   You are given an integer array nums.
#   You are allowed to delete any number of elements from nums without making it empty. After performing the deletions, select a
#   subarray of nums such that:
#   All elements in the subarray are unique.
#   The sum of the elements in the subarray is maximized.
#   Return the maximum sum of such a subarray.

class Solution:
    def maxSum(self, nums: List[int]) -> int:

        # Check if the array is all negative or max 0
        if max(nums) <= 0: return max(nums)

        # Hash table to hold the frequencies of each number
        hash_table = defaultdict(int)

        # Gather the frequencies of each number
        for num in nums: hash_table[num] += 1

        # Get the maximum sum
        max_sum = 0
        for key in hash_table: 
            if key > 0: max_sum += key
        
        # Return max
        return max_sum
