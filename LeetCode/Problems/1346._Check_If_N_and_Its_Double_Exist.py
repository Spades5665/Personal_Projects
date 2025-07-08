# Problem: Given an array arr of integers, check if there exist two indices i and j such that:
#          i != j
#          0 <= i, j < arr.length
#          arr[i] == 2 * arr[j]

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        
        # Loop through each element in arr
        for i in range(len(arr)):
            
            # Try to find the index of the double, if none exist, move to next element
            try:
                j = arr.index(arr[i] * 2)
                if i != j:
                    return True
            except:
                continue
        
        # No element and its double was found
        return False
