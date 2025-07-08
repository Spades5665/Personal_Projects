# Problem: Given an array arr, replace every element in that array with the greatest element among 
#          the elements to its right, and replace the last element with -1.
#          After doing so, return the array.

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        # Keeps track of the current max found
        maxNum = -1

        # Loop in reverse all elements in arr
        for i in range(len(arr) - 1, -1, -1):
            
            # Save element for later
            temp = arr[i]
            arr[i] = maxNum
            
            # Checks if element is the new max
            if temp > maxNum:
                maxNum = temp

        # Finished array
        return arr
