# Problem: Given two binary strings a and b, return their sum as a binary string.

class Solution:
    def addBinary(self, a: str, b: str) -> str:

        # Convert strings to binary nums, add in int math, convert to binary, convert back to string, then return without "0b" prefix ([2:])
        return str(bin(int(a, 2) + int(b, 2)))[2:]
