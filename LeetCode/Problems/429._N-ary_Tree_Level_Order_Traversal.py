# Problem:
#   Given an n-ary tree, return the level order traversal of its nodes' values.
#   Nary-Tree input serialization is represented in their level order traversal, 
#   each group of children is separated by the null value (See examples).

"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:

        # 2d array to hold levels
        levels = []
        
        # Recursively traverse in level order
        def levelOrderNary(node, level):

            # Check for node
            if node:

                # Add to level
                if level < len(levels): levels[level].append(node.val)
                else: levels.append([node.val])

                # Add children
                for child in node.children: levelOrderNary(child, level + 1)

        # Call on root
        levelOrderNary(root, 0)

        # Return list
        return levels
