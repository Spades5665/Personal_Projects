# Problem: Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        # Find the dimensions of the matrix
        m = len(mat)
        n = len(mat[0])

        # Create counters and result array
        diag = [0] * m * n
        direc, i, r, c = 1, 0, 0, 0

        # loop until all dimensions have been read
        while i < len(diag):

            # Set result value from matrix
            diag[i] = mat[r][c]

            # Positive direction (up and to the right)
            if direc:

                # Check if the right side of the matrix was reached
                if c == n - 1:
                    direc = 0
                    r += 1
                
                # Check if the top side of the matrix was reached
                elif r == 0:
                    direc = 0
                    c += 1
                
                # Increment diagonally
                else:                
                    r -= 1
                    c += 1
            
            # Negative direction (down and to the left)
            else:

                # Check if the bottom side of the matrix was reached
                if r == m - 1:
                    direc = 1
                    c += 1
                
                # Check if the left side of the matrix was reached
                elif c == 0:
                    direc = 1
                    r += 1
                
                # Increment Diagonally
                else:                
                    r += 1
                    c -= 1
            
            # Increment index
            i += 1

        # Return diagonal values
        return diag
