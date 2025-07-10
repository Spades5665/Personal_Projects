# Problem: Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
#          An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
#          You may assume all four edges of the grid are all surrounded by water.

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # Dimensions of grid
        m, n = len(grid), len(grid[0])

        # Keep track of islands found
        islands = 0

        # Loop through each value in grid
        for row in range(m):
            for col in range(n):

                # Check if current element is a land mass (1)
                if grid[row][col] == "1":

                    # Increment islands and change land to water
                    islands += 1
                    grid[row][col] = "0"

                    # Queue for holding island masses
                    queue = []
                    queue.append([row, col])
                
                    # Loop until all land connected to grid[r][c] has been accounted for
                    while len(queue) > 0:

                        # Pop the next location to check 
                        r, c = queue.pop(0)

                        # Check if the northern edge is connected
                        if r - 1 >= 0 and grid[r - 1][c] == "1":
                            grid[r - 1][c] = "0"
                            queue.append([r - 1, c])
                        
                        # Check if the eastern edge is connected
                        if c + 1 < n and grid[r][c + 1] == "1":
                            grid[r][c + 1] = "0"
                            queue.append([r, c + 1])
                        
                        # Check if the southern edge is connected
                        if r + 1 < m and grid[r + 1][c] == "1":
                            grid[r + 1][c] = "0"
                            queue.append([r + 1, c])
                        
                        # Check if the western edge is connected
                        if c - 1 >= 0 and grid[r][c - 1] == "1":
                            grid[r][c - 1] = "0"
                            queue.append([r, c - 1])

        # Return island count
        return islands
