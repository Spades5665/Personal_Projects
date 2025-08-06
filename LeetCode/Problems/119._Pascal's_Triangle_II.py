# Problem: 
#   Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        # Generate the values from the choose function
        return [comb(rowIndex, x) for x in range(rowIndex + 1)]
