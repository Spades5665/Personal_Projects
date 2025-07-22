# Problem: 
#   You are given an array of positive integers nums and want to erase a subarray 
#   containing unique elements. The score you get by erasing the subarray is equal to the sum of its elements.
#   Return the maximum score you can get by erasing exactly one subarray.
#   An array b is called to be a subarray of a if it forms a contiguous subsequence of a, 
#   that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:

        # Index tracker left side of the window
        left = 0

        # Sum trackers 
        current_sum, max_sum = 0, 0

        # Set containing current elements in subarray
        arr = set()

        # Loop through each num in nums
        for right in range(len(nums)):

            # Shrink window until duplicates are gone
            while nums[right] in arr:
                arr.remove(nums[left])
                current_sum -= nums[left]
                left += 1

            # Add the value to current sum and expand window
            current_sum += nums[right]

            # Add new value to set
            arr.add(nums[right])

            # Update max
            max_sum = max(max_sum, current_sum)

        # Return max sum found
        return max_sum
