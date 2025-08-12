# Problem:
#   Given an array of integers nums, sort the array in ascending order and return it.
#   You must solve the problem without using any built-in functions in O(nlog(n)) time 
#   complexity and with the smallest space complexity possible.

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        # Create a function to sort array using heapsort
        def maxHeapSort(arr):

            # Heapify the array into a binary tree
            def maxHeapify(ind, size):

                # Get the children indices
                l_child, r_child = 2 * ind + 1, 2 * ind + 2

                # Find max value index
                max_ind = ind
                if l_child < size and arr[l_child] > arr[max_ind]: max_ind = l_child
                if r_child < size and arr[r_child] > arr[max_ind]: max_ind = r_child
                
                # Swap values if max index was a child index
                if max_ind != ind:
                    arr[ind], arr[max_ind] = arr[max_ind], arr[ind]
                    maxHeapify(max_ind, size)
            
            # Call heapify on original list
            for i in range(len(arr) // 2 - 1, -1, -1): maxHeapify(i, len(arr))
        
            # Use heapify to sort
            for i in range(len(arr) - 1, 0, -1):

                # Swap values and call on next
                arr[0], arr[i] = arr[i], arr[0]
                maxHeapify(0, i)
            
            # Return sorted array
            return arr

        # Call heap sort on the array
        return maxHeapSort(nums)
