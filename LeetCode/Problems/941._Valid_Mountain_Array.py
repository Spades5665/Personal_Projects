# Problem: Given an array of integers arr, return true if and only if it is a valid mountain array.
#          Recall that arr is a mountain array if and only if:
#          arr.length >= 3
#          There exists some i with 0 < i < arr.length - 1 such that:
#          arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
#          arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        # Check base cases first, not long enough, no peak
        if len(arr) < 3 or arr[0] >= arr[1] or arr[len(arr) - 2] <= arr[len(arr) - 1]:
            return False
        
        # Check for peak and index counter
        ind = 0
        peak = False

        # Loop through each element
        while ind < len(arr) - 1:

            # Check for equal elements
            if arr[ind] == arr[ind + 1]:
                return False

            # Check for increasing values until the peak
            if not peak and not arr[ind] < arr[ind + 1]:
                peak = True
            
            # Check for decreasing values after the peak
            if peak and not arr[ind] > arr[ind + 1]:
                return False
            
            # Increase counter
            ind += 1

        # Mountain was found
        return True
