# Problem:
#   You're given strings jewels representing the types of stones that are jewels, 
#   and stones representing the stones you have. Each character in stones is a 
#   type of stone you have. You want to know how many of the stones you have are also jewels.
#   Letters are case sensitive, so "a" is considered a different type of stone from "A".

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        # How many stones are jewels
        jewels_count = 0

        # Loop through each stone and add to count if it is a jewel
        for c in stones:
            if c in jewels: jewels_count += 1
        
        # Return count
        return jewels_count
