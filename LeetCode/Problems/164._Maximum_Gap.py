# Problem:
#   Given an integer array nums, return the maximum difference between two successive elements 
#   in its sorted form. If the array contains less than two elements, return 0.
#   You must write an algorithm that runs in linear time and uses linear extra space.

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        
        # Counting sort for default numbers
        def countingSort(nums_list, place):

            # Intitialize count array
            counts = [0] * 10

            # Get frequency of each value
            for num in nums_list: counts[(num // place) % 10] += 1

            # Get the starting places of each num
            for i in range(1, len(counts)): counts[i] += counts[i - 1]

            # Add nums to their correct spot
            sorted_list = [0] * len(nums_list)
            for i in range(len(nums_list) - 1, -1, -1):
                sorted_list[counts[(nums_list[i] // place) % 10] - 1] = nums_list[i]
                counts[(nums_list[i] // place) % 10] -= 1

            # Return sorted list
            nums_list[:] = sorted_list[:]

        # Radix sort in place
        def radixSort(nums_list):

            # Call counting sort on all digits
            place = 1
            max_num = max(nums_list)
            while place <= max_num:
                countingSort(nums_list, place)
                place *= 10

        # Radix sort the array
        radixSort(nums)
        
        # Find max diff between nums 
        max_diff = 0
        for i in range(len(nums) - 1): max_diff = max(max_diff, nums[i + 1] - nums[i])
    
        # Return max diff
        return max_diff
