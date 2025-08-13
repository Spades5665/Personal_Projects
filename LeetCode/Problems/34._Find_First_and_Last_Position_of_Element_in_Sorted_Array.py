# Problem:
#   Given an array of integers nums sorted in non-decreasing order, find the starting and 
#   ending position of a given target value.
#   If target is not found in the array, return [-1, -1].
#   You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        # Search for the left index
        def binarySearchL(l, r, val):

            # Check base case
            if l > r: return -1

            # Get mid
            m = (l + r) // 2
            
            # Check if val is the left most
            if nums[m] == val and (nums[m - 1] != val if m - 1 > -1 else True): return m

            # Call on next
            return binarySearchL(m + 1, r, val) if nums[m - 1 if m - 1 > -1 else m] < val else binarySearchL(l, m - 1, val)
        
        # Search for the right index
        def binarySearchR(l, r, val):

            # Check base case
            if l > r: return -1

            # Get mid
            m = (l + r) // 2
            
            # Check if val is the left most
            if nums[m] == val and (nums[m + 1] != val if m + 1 < len(nums) else True): return m

            # Call on next
            return binarySearchR(l, m - 1, val) if nums[m + 1 if m + 1 < len(nums) else m] > val else binarySearchR(m + 1, r, val)
        
        # Call on left and right
        return [binarySearchL(0, len(nums) - 1, target), binarySearchR(0, len(nums) - 1, target)]
