# Problem:
#   Given the root of a binary tree, determine if it is a valid binary search tree (BST).
#   A valid BST is defined as follows:
#   The left subtree of a node contains only nodes with keys strictly less than the node's key.
#   The right subtree of a node contains only nodes with keys strictly greater than the node's key.
#   Both the left and right subtrees must also be binary search trees.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # Validate each node
        def validate(node, min_val, max_val):

            # Check if node exists
            if not node: return True

            # Check nodes value
            if not (min_val < node.val < max_val): return False

            # Check the children
            return validate(node.left, min_val, node.val) and validate(node.right, node.val, max_val)
        
        # Call on root
        return validate(root, -math.inf, math.inf)
