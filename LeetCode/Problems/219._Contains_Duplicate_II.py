# Problem:
#   Given an integer array nums and an integer k, return true if there are two 
#   distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        # Hash map to hold unique values and their last index
        hash_map = dict()

        # Loo pthrough each num in nums
        for i in range(len(nums)):

            # Add the value to the hash_map if it isn't in yet
            if nums[i] not in hash_map: hash_map[nums[i]] = i

            else: 

                # Get the last found index
                j = hash_map[nums[i]]

                # Check if the difference is less than k
                if i - j <= k: return True

                # Update the value for next occurance
                else: hash_map[nums[i]] = i
        
        # No indices were found
        return False
