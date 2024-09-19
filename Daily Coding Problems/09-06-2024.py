"""
Problem: Given a list of numbers, produce a new list that is the product of every element in the original array, except the one at the index
Example: With a list of [1, 2, 3, 4, 5], the new array would be [120, 60, 40, 30, 24]
"""

A = [1, 2, 3, 4, 5]
B = [1, 1, 1, 1, 1]

def findProd(A):
    for i in range(len(A)):
        for j in range (len(A)):
            if i != j:
                B[i] *= A[j]
    return B

print(findProd(A))