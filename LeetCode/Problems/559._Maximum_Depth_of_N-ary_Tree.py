# Problem:
#   Given a n-ary tree, find its maximum depth.
#   The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        # Recursively call on children
        def bottomUpNary(node, max_depth):

            # Base cases
            if not node: return 0
            if not node.children: return 1

            # Call on each child
            depth = max_depth
            for child in node.children: max_depth = max(max_depth, bottomUpNary(child, depth))

            # Update max
            return max_depth + 1

        # Call on root
        return bottomUpNary(root, 0)
