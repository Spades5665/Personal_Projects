# Problem: You are given a large integer represented as an integer array digits, 
#          where each digits[i] is the ith digit of the integer. The digits are 
#          ordered from most significant to least significant in left-to-right 
#          order. The large integer does not contain any leading 0's.
#          Increment the large integer by one and return the resulting array of digits.

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        # Check if carry occurred and current index
        carry, i = 1, len(digits) - 1
        
        # Loop until carry math is done
        while carry:

            # Check if front of number was reached
            if i < 0:
                digits.insert(0, 1)
                break

            # Check if carry will occur
            if digits[i] == 9:
                digits[i] = 0

            # No carry so add 1 and reset
            else:
                digits[i] += 1
                carry = 0

            # Update index
            i -= 1

        # Return array
        return digits
