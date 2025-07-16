# Problem:
#   You are given an integer array nums.
#   A subsequence sub of nums with length x is called valid if it satisfies:
#   (sub[0] + sub[1]) % 2 == (sub[1] + sub[2]) % 2 == ... == (sub[x - 2] + sub[x - 1]) % 2.
#   Return the length of the longest valid subsequence of nums.
#   A subsequence is an array that can be derived from another array by deleting some or 
#   no elements without changing the order of the remaining elements.

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        
        # Count how many of each parity type there are
        all_even, all_odd, alter = 0, 0, 1

        # Loop through each pair of nums
        for i in range(len(nums) - 1):

            # Current element is odd
            if nums[i] % 2:
                all_odd += 1

                # Next element is even
                if not nums[i + 1] % 2: alter += 1

            # Current element is even
            else:
                all_even += 1

                # Next element is odd
                if nums[i + 1] % 2: alter += 1

        # Check last element in nums if even or odd
        if nums[-1] % 2: all_odd += 1
        else: all_even += 1

        # Return which had a greater number
        return max(all_even, all_odd, alter)
