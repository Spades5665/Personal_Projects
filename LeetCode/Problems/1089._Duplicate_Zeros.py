# Problem: Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:

        # Keeps track of current index
        ind = 0

        # Loops until each element has been read
        while ind < len(arr):

            # Checks if the element is 0
            if arr[ind] == 0:

                # Inserts a new 0, then pops the last and increments to avoid reading the new 0
                arr.insert(ind, 0)
                arr.pop()
                ind += 1

            ind += 1    
