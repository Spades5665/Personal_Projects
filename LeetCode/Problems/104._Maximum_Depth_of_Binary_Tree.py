# Problem:
#   Given the root of a binary tree, return its maximum depth.
#   A binary tree's maximum depth is the number of nodes along the longest path 
#   from the root node down to the farthest leaf node.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # Search the tree from bottom up
        def bottomUp(node):

            # Return 0 if node doesn't exist
            if not node: return 0

            # Call on each child if they exist
            left_depth = bottomUp(node.left)
            right_depth = bottomUp(node.right)

            # Return the max of either depth and add 1 
            return max(left_depth, right_depth) + 1

        # Return max depth of the tree
        return bottomUp(root)
