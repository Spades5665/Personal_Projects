# Problem: 
#   Given two integer arrays nums1 and nums2, return an array of their intersection. 
#   Each element in the result must be unique and you may return the result in any order.

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # Return the list form of the intersection of the two sets
        return list(set(nums1) & set(nums2))
