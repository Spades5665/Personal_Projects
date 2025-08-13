# Problem:
#   There is an integer array nums sorted in ascending order (with distinct values).
#   Prior to being passed to your function, nums is possibly left rotated at an unknown 
#   index k (1 <= k < nums.length) such that the resulting array is 
#   [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
#   For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].
#   Given the array nums after the possible rotation and an integer target, return the index 
#   of target if it is in nums, or -1 if it is not in nums.
#   You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # Find target in rotated sorted array
        def binarySearchRotated(l, r, val):

            # End if invalid values
            if l > r: return -1

            # Find mid
            m = (l + r) // 2

            # End if value was found
            if nums[m] == val: return m

            # Search next area
            return binarySearchRotated(l, m - 1, val) \
            if (nums[m] < nums[l] and (nums[m] > val or val >= nums[l])) or (nums[m] > nums[l] and nums[l] <= val < nums[m]) \
            else binarySearchRotated(m + 1, r, val) 
        
        # Call Binary Search
        return binarySearchRotated(0, len(nums) - 1, target)
