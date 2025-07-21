# Problem:
#   Given two integer arrays nums1 and nums2, return an array of their intersection. 
#   Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # Keep track of currents index
        ind = 0

        # Loop through smaller list
        if len(nums1) <= len(nums2):

            while ind < len(nums1):

                # If current value is in both, remove from the second list
                if nums1[ind] in nums2:
                    nums2.remove(nums1[ind])
                    ind += 1

                # Otherwise remove it from the first list
                else:
                    nums1.remove(nums1[ind])
            
            # Return result array
            return nums1
        
        else:

            while ind < len(nums2):

                # If current value is in both, remove from the second list
                if nums2[ind] in nums1:
                    nums1.remove(nums2[ind])
                    ind += 1
                
                # Otherwise remove it from the first list
                else:
                    nums2.remove(nums2[ind])
            
            # Return result array
            return nums2
