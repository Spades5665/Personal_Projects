# Problem: 
#   You are given an image represented by an m x n grid of integers image, where image[i][j] 
#   represents the pixel value of the image. You are also given three integers sr, sc, and 
#   color. Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].
# To perform a flood fill:
#   Begin with the starting pixel and change its color to color.
#   Perform the same process for each pixel that is directly adjacent (pixels that share a side with 
#   the original pixel, either horizontally or vertically) and shares the same color as the starting pixel.
#   Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their 
#   color if it matches the original color of the starting pixel.
#   The process stops when there are no more adjacent pixels of the original color to update.
#   Return the modified image after performing the flood fill.

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        # Check if image exists or if it is already the correct color
        if not image or image[sr][sc] == color:
            return image

        # Set the origin color and start queue
        originColor = image[sr][sc]
        queue = deque([[sr, sc]])

        # Loop until queue is empty
        while queue:

            # Get the next row and column and set its new color
            r, c = queue.popleft()
            image[r][c] = color

            # Loop through each adjacent tile
            for dr, dc in [[-1, 0], [0, 1], [1, 0], [0, -1]]:

                # If the new row and column produce the same origin color, add it to queue
                if 0 <= r + dr < len(image) and 0 <= c + dc < len(image[0]) and image[r + dr][c + dc] == originColor:
                    queue.append([r + dr, c + dc])
        
        # Return changed image
        return image
