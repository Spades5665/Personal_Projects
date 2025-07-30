# Problem:
#   You are given the root node of a binary search tree (BST) and a value to insert into the tree. 
#   Return the root node of the BST after the insertion. 
#   It is guaranteed that the new value does not exist in the original BST.
#   Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. 
#   You can return any of them.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        # Create new node
        new_node = TreeNode(val)

        # Check if root exists
        if not root: return new_node

        # Loop until spot is found for new node
        curr = root
        while curr:

            # Find next spot to look
            if curr.val > new_node.val: 
                
                # Check if the left child exists
                if curr.left: curr = curr.left
                
                # Add node and return
                else:
                    curr.left = new_node
                    return root

            # Find next spot to look
            else: 
                
                # Check if the right child exists
                if curr.right: curr = curr.right
                
                # Add node and return
                else:
                    curr.right = new_node
                    return root
