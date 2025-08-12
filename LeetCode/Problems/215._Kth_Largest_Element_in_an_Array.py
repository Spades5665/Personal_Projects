# Problem:
#   Given an integer array nums and an integer k, return the kth largest element in the array.
#   Note that it is the kth largest element in the sorted order, not the kth distinct element.
#   Can you solve it without sorting?

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # Heapify the list
        heapq.heapify(nums)

        # Return the kth largest value
        return heapq.nlargest(k, nums)[-1] if nums else None
