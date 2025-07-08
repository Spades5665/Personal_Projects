# Problem: You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
#          and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
#          Merge nums1 and nums2 into a single array sorted in non-decreasing order.
#          The final sorted array should not be returned by the function, but instead be stored inside 
#          the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements 
#          denote the elements that should be merged, and the last n elements are set to 0 and should be 
#          ignored. nums2 has a length of n.

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    
        # Keeps track of indicies in each array, and number of m values checked in nums1
        ind1, ind2, mCount = 0, 0, m

        # Loops until all elements in num2 have merged
        while ind2 < n:

            # Checks if nums1 still has values to check
            if ind1 < mCount:

                # Checks if nums2 element < nums1 element
                if nums1[ind1] > nums2[ind2]:

                    # Adds element from nums2 then removes a zero
                    nums1.insert(ind1, nums2[ind2])
                    nums1.pop()

                    # Increment counters
                    ind2 += 1
                    mCount += 1
            
            # Merge the rest of nums2
            else:
                nums1[ind1] = nums2[ind2]
                ind2 += 1

            # Advance counter
            ind1 += 1
