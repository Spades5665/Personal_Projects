# Problem: You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
#          Evaluate the expression. Return an integer that represents the value of the expression.
# Note that:
#          The valid operators are '+', '-', '*', and '/'.
#          Each operand may be an integer or another expression.
#          The division between two integers always truncates toward zero.
#          There will not be any division by zero.
#          The input represents a valid arithmetic expression in a reverse polish notation.
#          The answer and all the intermediate calculations can be represented in a 32-bit integer.

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        # Holds numbers in wait to be operated on and the final result
        stack = deque()

        # Loop through each token
        for token in tokens:

            # Add the last two numbers in the stack
            if token == '+':
                stack.append(stack.pop() + stack.pop())
            
            # Subtract the last two numbers in the stack
            elif token == '-':

                # Grab the last two elements
                right, left = stack.pop(), stack.pop()
                
                # Difference the two
                stack.append(left - right)

            # Multiply the last two numbers in the stack
            elif token == '*':
                stack.append(stack.pop() * stack.pop())

            # Divide the last two numbers in the stack
            elif token == '/':

                # Grab the last two elements
                right, left = stack.pop(), stack.pop()

                # Divide the two
                stack.append(int(left / right))

            # Append the next number
            else:
                stack.append(int(token))

        # Return the remaining value
        return stack.pop()
