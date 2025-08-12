# Problem:
#   Given an array of integers nums which is sorted in ascending order, and an integer target, 
#   write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
#   You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # Binary search
        def binarySearchArray(l, r, val):
        
            # Check if array is valid
            if l > r: return -1

            # Check midpoint
            m = (l + r) // 2
            if nums[m] == val: return m

            # Search next location
            return binarySearchArray(l, m - 1, val) if nums[m] > val else binarySearchArray(m + 1, r, val)

        # Call binary search
        return binarySearchArray(0, len(nums) - 1, target)
