# Problem: You are given an m x n integer grid accounts where accounts[i][j]
#          is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. 
#          Return the wealth that the richest customer has.
#          A customer's wealth is the amount of money they have in all their 
#          bank accounts. The richest customer is the customer that has the 
#          maximum wealth.

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        # Keeps track of max wealth seen so far
        wealth = 0

        # Loops through all customers
        for customer in accounts:

            # Totals the customers wealth and checks if its more than current max
            wealth = sum(customer) if sum(customer) > wealth else wealth
        
        # Return max wealth
        return wealth
    