# Problem: 
#   Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
#   The distance between two cells sharing a common edge is 1.

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        # Dimensions of original matrix
        m, n = len(mat), len(mat[0])

        # Set up a matrix to store distance values
        dist_mat = [[0 for _ in range(n)] for _ in range(m)]

        # Loop through each cell in mat
        for r in range(m):
            for c in range(n):

                # Check if current element is a 1 and calculate its distance
                if mat[r][c] == 1:
                    north = dist_mat[r - 1][c] if r > 0 else math.inf
                    east = dist_mat[r][c - 1] if c > 0 else math.inf

                    # Find the minimum distance between the cell above and the cell to the right
                    dist_mat[r][c] = min(north + 1, east + 1)
        
        # Loop through each cell in mat in reverse
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):

                # Check if current element is a 1 and calculate its distance
                if mat[r][c] == 1:
                    south = dist_mat[r + 1][c] if r < m - 1 else math.inf
                    west = dist_mat[r][c + 1] if c < n - 1 else math.inf
                
                    # Find the minimum distance between the cell above and the cell to the right
                    dist_mat[r][c] = min(dist_mat[r][c], south + 1, west + 1)

        # Return result matrix
        return dist_mat
