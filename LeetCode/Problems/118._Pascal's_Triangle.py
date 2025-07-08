# Problem: Given an integer numRows, return the first numRows of Pascal's triangle.
#          In Pascal's triangle, each number is the sum of the two numbers directly above it

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        # Create empty triangle or correct dimensions
        triangle = [[0] * x for x in range(1, numRows + 1)]
        
        # Loop through each element in the triangle
        for r in range(len(triangle)):
            for c in range(len(triangle[r])):

                # Check if the current element is on the edge of the triangle (always 1)
                if c == 0 or c == len(triangle[r]) - 1:
                    triangle[r][c] = 1
                
                # Make element the sum of the two "above" it
                else:
                    triangle[r][c] = triangle[r - 1][c - 1] + triangle[r - 1][c]

        # Return triangle
        return triangle
