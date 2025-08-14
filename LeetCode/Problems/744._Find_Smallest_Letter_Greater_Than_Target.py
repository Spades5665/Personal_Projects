# Problem:
#   You are given an array of characters letters that is sorted in non-decreasing order, 
#   and a character target. There are at least two different characters in letters.
#   Return the smallest character in letters that is lexicographically greater than target. 
#   If such a character does not exist, return the first character in letters.

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        # Binary search for letter
        def binarySearchLetter(l, r):

            # Base case
            if l > r: return letters[0]

            # Check mid
            m = (l + r) // 2
            if letters[m] > target and (letters[m - 1] <= target if m - 1 > -1 else True): return letters[m]

            # Check next
            return binarySearchLetter(l, m - 1) if letters[m] > target else binarySearchLetter(m + 1, r)

        # Call on array
        return binarySearchLetter(0, len(letters) - 1)
