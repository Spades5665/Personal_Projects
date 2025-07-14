# Problem: Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
#          determine if the input string is valid.
#          An input string is valid if:
#          Open brackets must be closed by the same type of brackets.
#          Open brackets must be closed in the correct order.
#          Every close bracket has a corresponding open bracket of the same type.

class Solution:
    def isValid(self, s: str) -> bool:

        # Hold a stack of the left side of each bracket
        stack = deque()

        # Loop through each character in s
        for c in s:

            # If a right bracket is found, the top of the stack should match
            if c == ')':
                if not stack or stack.pop() != '(':
                    return False
            elif c == ']':
                if not stack or stack.pop() != '[':
                    return False
            elif c == '}':
                if not stack or stack.pop() != '{':
                    return False
            
            # Append each left side
            else:
                stack.append(c)
                
        # Check if there were unmatched left sides
        return False if stack else True
