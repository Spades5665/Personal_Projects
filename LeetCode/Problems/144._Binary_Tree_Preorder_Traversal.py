# Problem:
#   Given the root of a binary tree, return the preorder traversal of its nodes' values.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        # Hold pre order sequence
        pre_order = []

        # Recursively traverse tree
        def preOrderTraversal(node):

            # Collect node's value
            pre_order.append(node.val)

            # Check for left child
            if node.left: preOrderTraversal(node.left)

            # Check for right child
            if node.right: preOrderTraversal(node.right)
        
        # Call on root if it exists
        if root: preOrderTraversal(root)

        # Return list
        return pre_order
