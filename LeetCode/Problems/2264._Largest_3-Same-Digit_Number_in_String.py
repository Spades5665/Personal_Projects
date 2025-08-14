# Problem:
#   You are given a string num representing a large integer. An integer is good if it meets the following conditions:
#   It is a substring of num with length 3.
#   It consists of only one unique digit.
#   Return the maximum good integer as a string or an empty string "" if no such integer exists.
#   Note:
#   A substring is a contiguous sequence of characters within a string.
#   There may be leading zeroes in num or a good integer.

class Solution:
    def largestGoodInteger(self, num: str) -> str:

        # Find max sub num
        max_num = ""
        for i in range(len(num) - 2):

            # Get the next 3 values
            next_num = num[i : i + 3]

            # Check the next 3 values
            if num[i] == num[i + 1] == num[i + 2]: 
                if (int(max_num) if max_num else -1) < int(next_num): max_num = next_num
        
        # Return max num
        return max_num
