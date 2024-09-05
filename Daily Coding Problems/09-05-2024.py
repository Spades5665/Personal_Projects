"""
Problem: Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
Example: With a list of [10, 15, 3, 7] and a k value of 17, the program should return true with 10 and 7.
"""

s = [10, 15, 3, 7]
k = 17

def hasSum(s, k):
    val = False
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] + s[j] > k:
            j -= 1
        elif s[i] + s[j] < k:
            i += 1
        else:
            val = True
            break
    return val
        
print(hasSum(s, k))