# Problem:
#   Given a root node reference of a BST and a key, delete the node with the given key in the BST. 
#   Return the root node reference (possibly updated) of the BST.
#   Basically, the deletion can be divided into two stages:
#   Search for a node to remove.
#   If the node is found, delete the node.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        # Check if root exists
        if not root: return None

        # Determine which node to check next
        if root.val > key: root.left = self.deleteNode(root.left, key)
        elif root.val < key: root.right = self.deleteNode(root.right, key)

        # Root has value key
        else:

            # Check for children
            if not root.left: return root.right
            if not root.right: return root.left

            # Find the predecessor
            node = root.left
            while node.right: node = node.right

            # Swap values and attach predecessor
            root.val = node.val
            root.left = self.deleteNode(root.left, root.val)

        # Return the root
        return root
