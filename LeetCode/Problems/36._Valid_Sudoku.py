# Problem:
#   Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated
#   Note:
#      A Sudoku board (partially filled) could be valid but is not necessarily solvable.
#      Only the filled cells need to be validated according to the mentioned rules.

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Hash table to hold placements of values 
        hash_table = dict()

        # Loop through each value in the board
        for row in range(len(board)):
            for col in range(len(board[0])):

                # Get the current value
                val = board[row][col]

                # Check if the value is a number
                if val != ".":

                    # Calculate the sub box this number is in
                    sub_box = ((row // 3) * 3) + (col // 3) + 1

                    # Add the value to the table if it hasnt been seen yet
                    if val not in hash_table: hash_table[val] = [[row, col, sub_box]]
                    else: 

                        # Loop through all values of val seen so far
                        for r, c, sub in hash_table[val]:

                            # Check if the new value breaks the rules
                            if row == r or col == c or sub_box == sub: return False
                        
                        # Add it to the table if it passes
                        hash_table[val].append([row, col, sub_box])
        
        # All numbers passed
        return True
