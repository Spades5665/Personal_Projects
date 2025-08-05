# Problem:
#   Given a binary tree, determine if it is height-balanced.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # Traverse each subtree
        def findDepths(node):
            
            # Leaf case
            if not (node.left or node.right): return 1

            # Get depths of children
            l_child_depth = findDepths(node.left) if node.left else 0
            r_child_depth = findDepths(node.right) if node.right else 0

            # Check if the child depths are within 1 or a previous bad pair was found
            if l_child_depth == -1 or r_child_depth == -1 or abs(l_child_depth - r_child_depth) > 1: return -1

            # Update depth
            return max(l_child_depth, r_child_depth) + 1
        
        # Run find depths on root if it exists
        return findDepths(root) > -1 if root else True
