# Problem:
#   Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:
#   0 <= i, j, k, l < n
#   nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:

        # Hold all possible sums of the first two arrays
        hash_table = defaultdict(int)

        # How many sums of 0 were found
        zero_sums = 0

        # Add every combination of sums from the first two arrays
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                hash_table[nums1[i] + nums2[j]] += 1

        # Check every possible combination of the second two arrays for a result of 0
        for i in range(len(nums3)):
            for j in range(len(nums4)):
                zero_sums += hash_table[-(nums3[i] + nums4[j])]

        # Return all sums that equaled 0
        return zero_sums
