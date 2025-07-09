# Problem: Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        
        # Any value above len(nums) can be done in less steps, so adjust k
        k %= len(nums)
        
        # Use pythons subarray index format to move the section to the front
        nums[:] = nums[len(nums) - k:len(nums)] + nums[0:len(nums) - k]
