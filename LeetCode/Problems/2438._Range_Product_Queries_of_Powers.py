# Problem: 
#   Given a positive integer n, there exists a 0-indexed array called powers, 
#   composed of the minimum number of powers of 2 that sum to n. 
#   The array is sorted in non-decreasing order, and there is only one way to form the array.
#   You are also given a 0-indexed 2D integer array queries, where queries[i] = [lefti, righti]. 
#   Each queries[i] represents a query where you have to find the product of all powers[j] with lefti <= j <= righti.
#   Return an array answers, equal in length to queries, where answers[i] is the answer to the ith query. 
#   Since the answer to the ith query may be too large, each answers[i] should be returned modulo 109 + 7.

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        
        # Gather the powers that could add up to n
        possible_powers = []
        num = 1
        while num <= n:
            possible_powers.append(num)
            num *= 2

        # Find the lowest number of powers to add to n
        powers = []
        for power in possible_powers[:: -1]:
            if power <= n: 
                powers.append(power)
                n -= power
        
        # Reverse powers
        powers.reverse()
  
        # Find the product of each query
        answer = []
        for query in queries:
            prod = 1
            for i in range(query[0], query[1] + 1): prod *= powers[i]
            answer.append(prod % ((10 ** 9) + 7))
        
        # Return the resulting query products
        return answer
