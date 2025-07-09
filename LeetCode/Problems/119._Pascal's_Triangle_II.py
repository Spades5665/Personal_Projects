# Problem: Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

# Each value of a pascal triangle is equal to (row) choose (index in row)
from math import comb

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        # Generate the values from the choose function
        return [comb(rowIndex, x) for x in range(rowIndex + 1)]
