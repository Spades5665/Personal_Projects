# Problem:
#   You are given an integer array nums and two integers indexDiff and valueDiff.
#   Find a pair of indices (i, j) such that:
#   i != j,
#   abs(i - j) <= indexDiff.
#   abs(nums[i] - nums[j]) <= valueDiff, and
#   Return true if such pair exists or false otherwise.

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:

        # Check if value diff is 0
        if valueDiff == 0:

            # Create a dictionary to hold values found and their index
            val_ind = dict()
            
            # Collect each number
            for i in range(len(nums)):

                # Check if value has been found
                if nums[i] in val_ind and i - val_ind[nums[i]] <= indexDiff: return True

                # Add to dictionary
                val_ind[nums[i]] = i
            
            # No value pair was found
            return False
        
        # Value diff is > 0
        else:

            # Sort list into a window of size index diff
            window = SortedList(nums[: indexDiff + 1])

            # Index trackers
            l, r = 0, indexDiff + 1

            # Loop through each number
            for i in range(len(nums)):

                # Get differences from each side
                l_diff = nums[i] - valueDiff
                r_diff = nums[i] + valueDiff

                # Get the index of the left side
                ind = window.bisect_right(l_diff)

                # Check for good values
                if ind < len(window) and window[ind] == l_diff: return True
                elif ind < len(window) - 1 and window[ind + 1] <= r_diff: return True
                elif ind > 0 and window[ind - 1] == l_diff: return True

                # Update pointers
                if i >= indexDiff:
                    window.discard(nums[l])
                    l += 1
                if r < len(nums): window.add(nums[r])
                r += 1
            
            # No good pair was found
            return False
