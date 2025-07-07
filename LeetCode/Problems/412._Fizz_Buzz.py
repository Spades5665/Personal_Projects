# Problem: Given an integer n, return a string array answer (1-indexed) where:
#          answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
#          answer[i] == "Fizz" if i is divisible by 3.
#          answer[i] == "Buzz" if i is divisible by 5.
#          answer[i] == i (as a string) if none of the above conditions are true.

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        # Stores resulting list of values
        answer = []

        # Loop through all numbers from 1 to n
        for i in range(1, n + 1):

            # Check if num is divisible by 3 AND 5
            if i % 3 == 0 and i % 5 == 0:
                answer.append("FizzBuzz")
            
            # Check if num is divisible by just 3
            elif i % 3 == 0:
                answer.append("Fizz")

            # Check if num is divisible by just 5
            elif i % 5 == 0:
                answer.append("Buzz")

            # Num was not divisible by either
            else:
                answer.append(str(i))
        
        # Returns final list
        return answer
