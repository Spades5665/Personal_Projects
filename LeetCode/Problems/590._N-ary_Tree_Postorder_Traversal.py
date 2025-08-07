# Problem:
#   Given the root of an n-ary tree, return the postorder traversal of its nodes' values.
#   Nary-Tree input serialization is represented in their level order traversal. 
#   Each group of children is separated by the null value (See examples)

"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:

        # Keep track of vals found
        vals = []

        # Recursively traverse in post order
        def postOrderNary(node):

            # Check for node
            if node:

                # Add children
                for child in node.children: postOrderNary(child)

                # Add to vals
                vals.append(node.val)

        # Call on root
        postOrderNary(root)

        # Return list
        return vals
