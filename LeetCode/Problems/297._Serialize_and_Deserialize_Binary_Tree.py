# Problem:
#   Serialization is the process of converting a data structure or object into a sequence of bits so that 
#   it can be stored in a file or memory buffer, or transmitted across a network connection link to be 
#   reconstructed later in the same or another computer environment.
#   Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your 
#   serialization/deserialization algorithm should work. You just need to ensure that a binary tree can 
#   be serialized to a string and this string can be deserialized to the original tree structure.
#   Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do 
#   not necessarily need to follow this format, so please be creative and come up with different 
#   approaches yourself.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    # Encodes a tree to a single string.
    def serialize(self, root):
        
        # Coded string to return
        coded_string = []

        # Traverse tree in pre order
        def preOrderVisit(node):

            # Encode value of node
            coded_string.append(str(node.val) + "." if node else "N.")

            # Add children
            if node: 
                preOrderVisit(node.left)
                preOrderVisit(node.right)

        # Call on root
        preOrderVisit(root)

        # Return coded string
        return "".join(coded_string)[:-1]
        
    # Decodes your encoded data to tree.
    def deserialize(self, data):
        
        # Create queue to pull from
        queue = deque(data.split("."))

        # Deconstruct coded string
        def decode():

            # Pop new value
            new_val = queue.popleft()

            # Check for null node
            if new_val == "N": return None

            # Get next node value
            node = TreeNode(int(new_val))
        
            # Attach children
            node.left = decode()
            node.right = decode()
        
            # Return new node
            return node

        # Return root
        return decode()
