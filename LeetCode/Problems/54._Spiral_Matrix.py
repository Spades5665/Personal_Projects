# Problem: Given an m x n matrix, return all elements of the matrix in spiral order.

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        # Dimensions of the matrix, and row and column counters
        m, n, r, c = len(matrix), len(matrix[0]), 0, 0

        # Direction, index, and result array
        direc, i, spir = 1, 0, [0] * m * n
        
        # Loop through all dimensions
        while i < len(spir):

            # Grab next value from matrix
            spir[i] = matrix[r][c]

            # Check if direction is going east
            if direc % 4 == 1:

                # Check if the end was reached
                if c == n - (direc // 4) - 1:
                    direc += 1
                    r += 1
                
                # Expand more east
                else:
                    c += 1
            
            # Check if direction is going south
            elif direc % 4 == 2:

                # Check if the end was reached
                if r == m - (direc // 4) - 1:
                    direc += 1
                    c -= 1
                
                # Expand more south
                else:
                    r += 1

            # Check if direction is going west
            elif direc % 4 == 3:

                # Check if the end was reached
                if c == 0 + (direc // 4):
                    direc += 1
                    r -= 1
                
                # Expand more west
                else:
                    c -= 1

            # Check if direction is going north
            else:

                # Check if the end was reached
                if r == 0 + (direc // 4):
                    direc += 1
                    c += 1
                
                # Expand more north
                else:
                    r -= 1

            # Increment index
            i += 1
        
        return spir
