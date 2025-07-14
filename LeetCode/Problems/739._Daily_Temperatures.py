# Problem: Given an array of integers temperatures represents the daily temperatures, 
#          return an array answer such that answer[i] is the number of days you have 
#          to wait after the ith day to get a warmer temperature. If there is no 
#          future day for which this is possible, keep answer[i] == 0 instead.

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
         
        # Monotonic decreasing stack to hold next higher temp
        stack = deque()
        
        # Holds the index of the next highest temp
        answer = [0] * len(temperatures)
        
        # Loop through each temperature in reverse
        for i in range(len(temperatures) - 1, -1, -1):
            
            # Check if current temperature is greater or equal to stack contents
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()

            # The next greater temp is the next stack value if it exists
            answer[i] = stack[-1] - i if stack else 0

            # Append the higher temperature for the next index to check
            stack.append(i)
        
        # Return resulting array
        return answer
