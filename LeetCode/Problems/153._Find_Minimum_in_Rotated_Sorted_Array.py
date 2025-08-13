# Problem: 
#   Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 
#   For example, the array nums = [0,1,2,4,5,6,7] might become:
#   [4,5,6,7,0,1,2] if it was rotated 4 times.
#   [0,1,2,4,5,6,7] if it was rotated 7 times.
#   Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array 
#   [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
#   Given the sorted rotated array nums of unique elements, return the minimum element of this array.
#   You must write an algorithm that runs in O(log n) time.

class Solution:
    def findMin(self, nums: List[int]) -> int:

        # Find min in rotated sorted array
        def binarySearchRotated(l, r):

            # End if invalid values
            if l > r: return -1

            # Find mid
            m = (l + r) // 2

            # End if minimum was found
            if nums[m] <= nums[m - 1]: return nums[m]

            # Search next area
            return binarySearchRotated(l, m - 1) if nums[m] < nums[r] else binarySearchRotated(m + 1, r)
        
        # Call Binary Search
        return binarySearchRotated(0, len(nums) - 1)
