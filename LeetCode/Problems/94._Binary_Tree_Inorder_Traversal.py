# Problem: 
#   Given the root of a binary tree, return the inorder traversal of its nodes' values.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        # Hold in order sequence
        in_order = []

        # Recursively traverse tree
        def inOrderTraversal(node):

            # Check for left child
            if node.left: inOrderTraversal(node.left)

            # Collect node's value
            in_order.append(node.val)

            # Check for right child
            if node.right: inOrderTraversal(node.right)

        # Call on root if root exists
        if root: inOrderTraversal(root)

        # Return list
        return in_order
