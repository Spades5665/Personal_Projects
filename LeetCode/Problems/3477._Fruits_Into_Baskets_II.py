# Problem:
#   You are given two arrays of integers, fruits and baskets, each of length n, where fruits[i] 
#   represents the quantity of the ith type of fruit, and baskets[j] represents the capacity of the jth basket.
#   From left to right, place the fruits according to these rules:
#   Each fruit type must be placed in the leftmost available basket with a capacity greater than or equal to the 
#   quantity of that fruit type.
#   Each basket can hold only one type of fruit.
#   If a fruit type cannot be placed in any basket, it remains unplaced.
#   Return the number of fruit types that remain unplaced after all possible allocations are made.

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:

        # Keep track of fruits left to place
        fruits_left = len(fruits)

        # Place fruits
        for fruit in fruits:
            for i in range(len(baskets)):

                # Check if current basket can hold fruit
                if baskets[i] >= fruit:

                    # Reduce basket and decrement fruits left
                    baskets[i] = 0
                    fruits_left -= 1
                    break
                
        # Return count
        return fruits_left
