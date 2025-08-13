# Problem:
#   You are a product manager and currently leading a team to develop a new product. 
#   Unfortunately, the latest version of your product fails the quality check. 
#   Since each version is developed based on the previous version, all the versions after a bad version are also bad.
#   Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, 
#   which causes all the following ones to be bad.
#   You are given an API bool isBadVersion(version) which returns whether version is bad. 
#   Implement a function to find the first bad version. You should minimize the number of calls to the API.

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        # Binary search n
        def binarySearchBad(l, r):

            # Check for end cases
            if l > r or (l == r and not isBadVersion(l)): return -1

            # Get mid value
            m = (l + r) // 2

            # Check if m is bad
            if isBadVersion(m) and (m == 1 or not isBadVersion(m - 1)): return m

            # Call on next part of array
            return binarySearchBad(l, m - 1) if isBadVersion(m) else binarySearchBad(m + 1, r)
        
        # Call on range of values
        return binarySearchBad(1, n)
