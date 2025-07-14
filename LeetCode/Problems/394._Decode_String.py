# Problem: Given an encoded string, return its decoded string.
#          The encoding rule is: k[encoded_string], where the encoded_string inside the 
#          square brackets is being repeated exactly k times. Note that k is guaranteed 
#          to be a positive integer.
#          You may assume that the input string is always valid; there are no extra white 
#          spaces, square brackets are well-formed, etc. Furthermore, you may assume that 
#          the original data does not contain any digits and that digits are only for 
#          those repeat numbers, k. For example, there will not be input like 3a or 2[4].

class Solution:
    def decodeString(self, s: str) -> str:
        
        # Holds the decoded string
        decodedString = ""

        # Stack to hold characters in wait
        stack = deque()

        # Loop through each character in s
        for c in s:

            # Check if current character is the end bracket
            if c == ']':

                # Collect all the letters between the brackets and put it in tempString
                tempString = ""
                while not stack[-1] == '[': tempString = stack.pop() + tempString

                # Pop the left bracket out
                stack.pop()

                # Collect the correct number of times the string should be produced
                num = ""
                while stack and stack[-1].isdigit(): num = stack.pop() + num

                # Put those characters back in stack the correct number of times                
                stack.append(tempString * int(num))

            # Add character to stack
            else:
                stack.append(c)    
        
        # Empty the stack into result string
        while stack:
            decodedString = stack.pop() + decodedString
    
        # Return decoded message
        return decodedString
