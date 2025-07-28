# Problem:
#   Given the root of a binary tree, return the postorder traversal of its nodes' values.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        # Hold post order sequence
        post_order = []

        # Recursively traverse tree
        def postOrderTraversal(node):

            # Check for left child
            if node.left: postOrderTraversal(node.left)

            # Check for right child
            if node.right: postOrderTraversal(node.right)

            # Collect node's value
            post_order.append(node.val)

        # Call on root if root exists
        if root: postOrderTraversal(root)

        # Return list
        return post_order
