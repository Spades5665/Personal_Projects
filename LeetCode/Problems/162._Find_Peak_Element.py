# Problem:
#   A peak element is an element that is strictly greater than its neighbors.
#   Given a 0-indexed integer array nums, find a peak element, and return its index. 
#   If the array contains multiple peaks, return the index to any of the peaks.
#   You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always 
#   considered to be strictly greater than a neighbor that is outside the array.
#   You must write an algorithm that runs in O(log n) time.

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        # Binary search for peak
        def binarySearchPeak(l, r):

            # Check valid indeices
            if l > r: return -1

            # Get mid
            m = (l + r) // 2
            
            # Check for peak
            if (nums[m - 1] if m - 1 > -1 else -math.inf) < nums[m] > (nums[m + 1] if m + 1 < len(nums) else -math.inf): return m

            # Call recursively
            return binarySearchPeak(l, m - 1) if nums[m] < (nums[m - 1] if m - 1 > -1 else -math.inf) else binarySearchPeak(m + 1, r)

        # Call on array
        return binarySearchPeak(0, len(nums) - 1)
